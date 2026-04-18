
# =========================
# INSTALL
# =========================
#!pip install gradio qiskit qiskit-aer transformers accelerate --quiet

# =========================
# IMPORTS
# =========================
import gradio as gr
import random
import torch

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

from transformers import AutoTokenizer, AutoModelForCausalLM

# =========================
# LOAD LIGHTWEIGHT AGENT (CPU)
# =========================
MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float32,
    device_map="cpu"
)

sim = AerSimulator()

# =========================
# CORE QUANTUM FUNCTIONS
# =========================
def base_circuit():
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0,1],[0,1])
    return qc

def mutate(qc):
    new = qc.copy()
    gate = random.choice(["h", "cx"])

    if gate == "h":
        new.h(random.choice([0,1]))
    else:
        new.cx(0,1)

    return new

def simulate(qc):
    result = sim.run(transpile(qc, sim), shots=100).result()
    return result.get_counts()

def loss(counts):
    target = {"11": 1.0}
    return abs(target["11"] - counts.get("11",0)/100)

# =========================
# SERENDIPITY OPTIMIZER (STREAMING)
# =========================
def run_lab_stream(steps):
    qc = base_circuit()

    circuits_log = ""
    results_log = ""
    mutation_log = ""
    network_log = ""

    yield (
        "⚛️ Initializing quantum event...",
        "", "", "", "", "", "", ""
    )

    population = [qc]

    for step in range(steps):

        new_pop = []
        for c in population:
            new_pop.append(mutate(c))
            new_pop.append(c)

        scored = []
        for c in new_pop:
            counts = simulate(c)
            l = loss(counts)
            scored.append((c, l, counts))

        scored = sorted(scored, key=lambda x: x[1])
        population = [x[0] for x in scored[:3]]

        best = scored[0]

        # Infinite scroll logs
        circuits_log += f"\n\n--- Step {step} ---\n{best[0]}"
        results_log += f"\nStep {step}: {best[2]}"
        mutation_log += f"\nStep {step}: loss={best[1]:.4f}"
        network_log += f"\nNode {step} → loss {best[1]:.4f}"

        explanation = explain(best[2])
        chemistry = chemical_placeholder(best[2])

        yield (
            f"Step {step}: Qubit evolving...",
            circuits_log,
            results_log,
            mutation_log,
            circuits_log,
            network_log,
            explanation,
            chemistry
        )

# =========================
# AGENT EXPLANATION
# =========================
def explain(counts):
    prompt = f"""
Explain this quantum measurement result:

{counts}

Explain meaning, pattern, and possible real-world analogy.
"""
    inputs = tokenizer(prompt, return_tensors="pt")

    with torch.no_grad():
        out = model.generate(**inputs, max_new_tokens=120)

    return tokenizer.decode(out[0], skip_special_tokens=True)

# =========================
# CHEMICAL PLACEHOLDER
# =========================
def chemical_placeholder(counts):
    if "11" in counts:
        return "🧪 Possible mapping: simple bonding state (H2-like approximation)"
    return "🧪 No stable molecular pattern detected"

# =========================
# GRADIO UI
# =========================
with gr.Blocks() as demo:

    gr.Markdown("# 🌐 Quantum Serendipity Lab — Infinite Evolution System")

    steps = gr.Slider(3, 15, value=6, label="Evolution Steps")
    run_btn = gr.Button("⚛️ Run Quantum Event")

    with gr.Tab("Qubit Evolution"):
        t1 = gr.Textbox(lines=5)

    with gr.Tab("Circuit Growth"):
        t2 = gr.Textbox(lines=25, max_lines=1000, autoscroll=True)

    with gr.Tab("Result / Event"):
        t3 = gr.Textbox(lines=25, max_lines=1000, autoscroll=True)

    with gr.Tab("Mutation Log"):
        t4 = gr.Textbox(lines=25, max_lines=1000, autoscroll=True)

    with gr.Tab("Circuit Changes"):
        t5 = gr.Textbox(lines=25, max_lines=1000, autoscroll=True)

    with gr.Tab("Network Expansion"):
        t6 = gr.Textbox(lines=25, max_lines=1000, autoscroll=True)

    with gr.Tab("Agent Explanation"):
        t7 = gr.Textbox(lines=20, max_lines=500)

    with gr.Tab("Chemical Interpretation"):
        t8 = gr.Textbox(lines=15, max_lines=300)

    run_btn.click(
        run_lab_stream,
        inputs=[steps],
        outputs=[t1, t2, t3, t4, t5, t6, t7, t8]
    )

demo.launch(share=True)
