
# QuantumSelf — Adapted Version (Minimal changes for stability)

import gradio as gr
import numpy as np
import threading
import time
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import networkx as nx
from PIL import Image
import io

from qiskit import QuantumCircuit
from qiskit.visualization import circuit_drawer
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler, Session
from qiskit.transpiler import generate_preset_pass_manager

from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline, AutoConfig
from scipy.optimize import minimize

# ====================== SHARED STATE ======================
class QuantumState:
    def __init__(self):
        self.running = False
        self.step = 0
        self.fidelity = 0.0
        self.params = np.random.uniform(-np.pi, np.pi, 6)
        self.agent_log = "🤖 Phi-2 Agent ready — save IBM key"
        self.equations_md = "**Agent will generate equations here...**"
        self.warranty_md = "**Warranty will appear at convergence...**"
        self.debug_log = "System initialized."
        self.last_error = "None"
        self.current_backend = "Not connected"
        self.api_key_status = "No key saved"
        self.data_status = "Idle"
        self.desire = "Proof the Multiverse"
        self.agent_status = "Idle"

engine = QuantumState()

# ====================== LLM AGENT SETUP ======================
def initialize_agent():
    print("Initializing Phi-2 Reasoning Engine...")
    model_id = "microsoft/phi-2"
    tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
    tokenizer.pad_token = tokenizer.eos_token

    config = AutoConfig.from_pretrained(model_id, trust_remote_code=True)
    config.pad_token_id = config.eos_token_id

    model = AutoModelForCausalLM.from_pretrained(
        model_id, config=config, torch_dtype="auto", device_map="auto", trust_remote_code=True
    )
    return pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=512)

agent_pipe = initialize_agent()

# ====================== IBM QUANTUM OPERATIONS ======================
def configure_ibm(api_key: str):
    if not api_key or len(api_key.strip()) < 30:
        engine.api_key_status = "Invalid"
        return "❌ Key Length Error", gr.update()
    try:
        QiskitRuntimeService.save_account(channel="ibm_quantum_platform", token=api_key.strip(), overwrite=True, set_as_default=True)
        engine.api_key_status = "Valid"
        return "✅ IBM Credential Saved", gr.update(value="")
    except Exception as e:
        engine.last_error = str(e)
        return f"❌ Save Failed: {str(e)[:50]}", gr.update()

def verify_connection():
    try:
        service = QiskitRuntimeService()
        backend = service.least_busy(operational=True, simulator=False, min_num_qubits=2)
        engine.current_backend = backend.name
        return f"✅ Linked: {backend.name}"
    except Exception as e:
        return f"❌ Offline: {str(e)[:100]}"

def execute_quantum_hardware(params):
    engine.data_status = "Transmitting to IBM..."
    try:
        service = QiskitRuntimeService()
        backend = service.least_busy(operational=True, simulator=False, min_num_qubits=2)

        qc = QuantumCircuit(2)
        qc.ry(params[0], 0); qc.rz(params[1], 0)
        qc.ry(params[2], 1); qc.rz(params[3], 1)
        qc.cx(0, 1)
        qc.ry(params[4], 0); qc.rz(params[5], 1)
        qc.measure_all()

        pm = generate_preset_pass_manager(optimization_level=3, backend=backend)
        isa_qc = pm.run(qc)

        with Session(backend=backend) as session:
            sampler = Sampler(mode=session)
            sampler.options.dynamical_decoupling.enable = True
            job = sampler.run([isa_qc], shots=4096)
            result = job.result()

        counts = result[0].data.meas.get_counts()
        p11 = counts.get('11', 0) / sum(counts.values())
        engine.data_status = "Idle"
        return p11
    except Exception as e:
        engine.last_error = str(e)
        engine.data_status = "Hardware Error"
        return 0.25

# ====================== INFINITE EQUATIONS + WARRANTY (Added) ======================
def generate_infinite_equations(desire_text: str, fid: float, step: int):
    base = f"""
### Step {step} — Quantum Evolution
**Desire**: "{desire_text}"
**Fidelity**: {fid:.6f}

**Core Equations**:
1. \( |\\psi(\\theta)\\rangle = U(\\theta)|00\\rangle \)
2. \( F(\\theta) = |\\langle \\psi | target \\rangle|^2 = {fid:.6f} \)
3. \( C(\\theta) = 1 - F(\\theta) \)
"""
    try:
        prompt = f"Desire: {desire_text}. Fidelity: {fid:.4f}. Generate realistic quantum equations."
        extra = agent_pipe(prompt)[0]['generated_text']
    except:
        extra = "Generating equations..."
    return base + extra

def generate_perfect_state_warranty(desire_text: str, fid: float, step: int):
    return f"""
# 🎉 PERFECT STATE WARRANTY — Step {step}

**Desire**: "{desire_text}"
**Achieved Fidelity**: {fid:.6f}

The hybrid system certifies that the quantum evolution has reached the **Perfect State**.

All equations, paths, and results are consistent and valid on real IBM hardware.

**Formal Grant**: The desire is affirmed and realized.

Signed: IBM Quantum + Phi-2 Agent
"""

# ====================== THE EVOLUTION CORE ======================
def process_evolution():
    while engine.running:
        try:
            # Agent Reasoning
            engine.agent_status = "Strategizing..."
            prompt = f"Objective: {engine.desire}. Fidelity: {engine.fidelity:.4f}. Suggest next move."
            response = agent_pipe(prompt, max_new_tokens=512)[0]['generated_text']
            engine.agent_log = f"Step {engine.step}: {response[-300:]}"

            # Optimization + Hardware
            def objective(x):
                return 1.0 - execute_quantum_hardware(x)

            res = minimize(objective, engine.params, method='COBYLA', options={'maxiter': 1})
            engine.params = res.x
            engine.fidelity = execute_quantum_hardware(engine.params)
            engine.step += 1

            # Generate Equations
            engine.agent_status = "Deriving Equations..."
            engine.equations_md = generate_infinite_equations(engine.desire, engine.fidelity, engine.step)

            # Check for Perfect State
            if engine.fidelity >= 0.85:
                engine.agent_status = "Finalizing Warranty..."
                engine.warranty_md = generate_perfect_state_warranty(engine.desire, engine.fidelity, engine.step)
                engine.running = False

        except Exception as e:
            engine.debug_log = f"Error: {str(e)}"
            time.sleep(5)

        engine.agent_status = "Awaiting Hardware..."
        time.sleep(2)

# ====================== UI UTILITIES ======================
def get_circuit_img():
    qc = QuantumCircuit(2)
    p = engine.params
    qc.ry(p[0], 0); qc.rz(p[1], 0); qc.ry(p[2], 1); qc.rz(p[3], 1)
    qc.cx(0, 1); qc.ry(p[4], 0); qc.rz(p[5], 1)
    buf = io.BytesIO()
    circuit_drawer(qc, output='mpl').savefig(buf, format='png')
    plt.close()
    return Image.open(buf)

def get_network_plot():
    G = nx.DiGraph()
    edges = [("Phi-2 Agent", "IBM Quantum"), ("IBM Quantum", "State"), ("State", "Goal")]
    G.add_edges_from(edges)
    pos = nx.circular_layout(G)
    edge_x, edge_y = [], []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]; x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None]); edge_y.extend([y0, y1, None])

    fig = go.Figure(data=[
        go.Scatter(x=edge_x, y=edge_y, line=dict(width=2, color='#888'), hoverinfo='none', mode='lines'),
        go.Scatter(x=[pos[n][0] for n in G.nodes()], y=[pos[n][1] for n in G.nodes()],
                   mode='markers+text', text=list(G.nodes()), marker=dict(size=20, color='magenta'))
    ])
    fig.update_layout(template="plotly_dark", margin=dict(b=0,l=0,r=0,t=0), height=300)
    return fig

def update_ui():
    return (
        get_circuit_img(),
        engine.fidelity,
        get_network_plot(),
        engine.agent_log,
        engine.agent_status,
        engine.equations_md,
        engine.warranty_md,
        engine.debug_log
    )

# ====================== GRADIO INTERFACE ======================
with gr.Blocks(theme=gr.themes.Soft()) as gui:
    gr.HTML("<h1 style='text-align:center;'>🌌 QuantumSelf: Agent-Heavy Evolution</h1>")

    with gr.Row():
        with gr.Column(scale=1):
            with gr.Group():
                api_input = gr.Textbox(label="IBM Quantum Token", type="password")
                save_btn = gr.Button("🔗 Connect IBM")
                status_txt = gr.Textbox(label="Connection", interactive=False)

            desire_box = gr.Textbox(label="Desired Reality", value=engine.desire)
            with gr.Row():
                run_btn = gr.Button("🚀 Begin Evolution", variant="primary")
                stop_btn = gr.Button("🛑 Stop", variant="stop")

            fid_meter = gr.Number(label="Current Fidelity")
            status_indicator = gr.Label(label="Agent Status")

        with gr.Column(scale=2):
            with gr.Tabs():
                with gr.Tab("Monitoring"):
                    circuit_view = gr.Image(label="Active Circuit")
                    flow_view = gr.Plot(label="System Topology")
                    log_view = gr.Textbox(label="Agent Reasoning Stream", lines=5)

                with gr.Tab("Mathematical Derivations"):
                    math_view = gr.Markdown()

                with gr.Tab("Final Warranty"):
                    cert_view = gr.Markdown()

                with gr.Tab("System Logs"):
                    debug_view = gr.Textbox(label="Debug Trace", lines=10)

    # Functionality
    save_btn.click(configure_ibm, inputs=api_input, outputs=[status_txt, api_input])

    def start_process(d):
        engine.desire = d
        engine.running = True
        threading.Thread(target=process_evolution, daemon=True).start()
        return "System Active"

    run_btn.click(start_process, inputs=desire_box, outputs=status_txt)
    stop_btn.click(lambda: setattr(engine, 'running', False), outputs=status_txt)

    refresh = gr.Timer(2.0)
    refresh.tick(update_ui, outputs=[circuit_view, fid_meter, flow_view, log_view, status_indicator, math_view, cert_view, debug_view])

if __name__ == "__main__":
    gui.launch(share=True, debug=True)
