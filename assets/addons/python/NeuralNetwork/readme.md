[HOME](/README.md)     

# Neural Network v0.0.1 - Simulated

```
import gradio as gr
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import time
import random
import os

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ------------------- Topological Crystal (Fixed with File Save) -------------------
def generate_topological_crystal(size=128, num_solitions=25, steps=60):
    field = torch.randn((size, size), device=device) * 0.1
    for _ in range(steps):
        lap = torch.nn.functional.avg_pool2d(field.unsqueeze(0).unsqueeze(0), 3, stride=1, padding=1).squeeze()
        field = field + 0.08 * (lap - field) + 0.06 * torch.sin(field)
    for _ in range(num_solitions):
        x = random.randint(15, size-15)
        y = random.randint(15, size-15)
        for i in range(25):
            r = i * 0.15
            field[int(x + r*np.cos(i)), int(y + r*np.sin(i))] += 1.8
    return torch.clamp(field, -np.pi, np.pi).cpu().numpy()

def plot_crystal_to_file(size, num_sol, steps):
    data = generate_topological_crystal(size, num_sol, steps)
    fname = "crystal_output.png"
    plt.imsave(fname, data, cmap='twilight_shifted')
    return fname

# ------------------- Hybrid Model -------------------
class HybridEvolvingNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Sequential(nn.Linear(4, 16), nn.ReLU(), nn.Linear(16, 1))
    
    def forward(self, x):
        return self.fc(x)

# ------------------- Evolution Generator -------------------
def run_evolution_generator():
    model = HybridEvolvingNet().to(device)
    optimizer = optim.Adam(model.parameters(), lr=0.04)
    losses = []
    
    for step in range(100):
        topo_input = torch.tensor([[np.sin(step/5) + random.gauss(0, 0.4) for _ in range(4)]], device=device, dtype=torch.float32)
        target = torch.tensor([[np.cos(step/6)]], device=device, dtype=torch.float32)

        optimizer.zero_grad()
        out = model(topo_input)
        loss = (out - target).pow(2).mean()
        loss.backward()
        optimizer.step()

        losses.append(loss.item())

        if step % 2 == 0:
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=list(range(len(losses))), y=losses,
                                   mode='lines+markers', line=dict(color='#00ffcc')))
            fig.update_layout(title=f"Hybrid Network Evolution - Step {step}",
                              template="plotly_dark", height=500)
            yield fig, f"Step {step}: Loss = {loss.item():.4f}"
        
        time.sleep(0.1)
    yield fig, "Evolution Complete."

# ------------------- Gradio App -------------------
with gr.Blocks(title="Quantum-Enhanced Topological consciousness") as demo:
    gr.Markdown("# 🌀 consciousness Simulator (T4 GPU)")
    
    with gr.Tab("1. Generate Topological Crystal"):
        with gr.Row():
            size_sl = gr.Slider(64, 256, 128, label="Grid Size")
            num_sl = gr.Slider(5, 80, 25, label="Solitons")
            steps_sl = gr.Slider(20, 150, 60, label="Relaxation Steps")
        gen_btn = gr.Button("Generate Crystal", variant="primary")
        # Using gr.Image instead of gr.Plot for the crystal map to avoid savefig errors
        crystal_img = gr.Image(label="Topological Field Map")
        gen_btn.click(plot_crystal_to_file, [size_sl, num_sl, steps_sl], crystal_img)

    with gr.Tab("2. Live Network Evolution"):
        start_btn = gr.Button("▶️ Start Evolution", variant="primary")
        live_plot = gr.Plot(label="Loss Curve")
        status_text = gr.Textbox(label="Status", value="Ready")

        start_btn.click(run_evolution_generator, inputs=[], outputs=[live_plot, status_text])

demo.launch(share=True, inline=True)```

# v0.0.2

import numpy as np
import torch
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import time
import random
import os
import http.server
import socketserver
import threading

from pyngrok import ngrok, conf
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, AutoConfig

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# ------------------- Your ngrok token (keep it here) -------------------
NGROK_TOKEN = "37fJKKexs66q3bWBAAelBYiU2Yp_7Fq6yLN25TUj43fiBHfEN"

# ------------------- Load Phi-2 with fixes for T4 GPU -------------------
print("Loading Microsoft Phi-2 (2.7B) in 4-bit...")

model_id = "microsoft/phi-2"

# Fix: Load config and manually add missing pad_token_id
config = AutoConfig.from_pretrained(model_id, trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
tokenizer.pad_token = tokenizer.eos_token
config.pad_token_id = tokenizer.pad_token_id

quant_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True
)

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    config=config,
    quantization_config=quant_config,
    device_map="auto",
    torch_dtype=torch.float16,
    trust_remote_code=True
)

def phi2_speak(prompt, max_new=300):
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=max_new,
            temperature=0.75,
            do_sample=True,
            pad_token_id=config.pad_token_id
        )
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response.split("Assistant:")[-1].strip() if "Assistant:" in response else response

# ------------------- Generate Visuals -------------------
def generate_crystal():
    size = 128
    field = torch.randn((size, size), device=device) * 0.1
    for _ in range(60):
        lap = torch.nn.functional.avg_pool2d(field.unsqueeze(0).unsqueeze(0), 3, stride=1, padding=1).squeeze()
        field = field + 0.08 * (lap - field) + 0.06 * torch.sin(field)
    data = torch.clamp(field, -np.pi, np.pi).cpu().numpy()
    plt.imsave("1_crystal.png", data, cmap='twilight_shifted')
    print("✅ 1. Topological Crystal generated")

def create_step_by_step_nn():
    for i in range(1, 9):
        fig, ax = plt.subplots(figsize=(7, 5))
        weights = np.random.randn(6, 6) * (1.0 - i * 0.1)
        im = ax.imshow(weights, cmap='coolwarm', vmin=-2, vmax=2)
        ax.set_title(f"Neural Network Weights - Step {i}/8")
        plt.colorbar(im)
        plt.tight_layout()
        plt.savefig(f"step_{i}.png")
        plt.close()
    print("✅ 2. Step-by-step Neural Network evolution images created")

def create_interactive_loss():
    steps = list(range(60))
    losses = [max(0.04, 0.95 - 0.015 * s + random.gauss(0, 0.025)) for s in steps]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=steps, y=losses, mode='lines+markers', line=dict(color='#00ffcc'), name='Loss'))
    fig.update_layout(title="3. Consciousness Evolution - Loss Curve", xaxis_title="Step", yaxis_title="Loss", template="plotly_dark", height=520)
    fig.write_html("3_loss_curve.html")
    print("✅ 3. Interactive Loss Curve created")

def phi2_agent_console():
    prompt = "Think step by step in first person: I am an AI in a quantum field. Evaluate my state and propose 4 tasks with confidence scores (0-100)."
    response = phi2_speak(prompt, max_new=350)
    with open("4_phi2_console.txt", "w", encoding="utf-8") as f: f.write(response)
    print("\n=== PHI-2 AGENT CONSOLE ===\n" + response + "\n")

def start_server(port=7860):
    html = f"""<!DOCTYPE html><html><head><title>🌀 Phi-2 Simulator</title><style>body {{ background:#0a0a0a; color:#00ffcc; font-family:Arial; margin:30px; }} .block {{ margin-bottom:50px; border:1px solid #444; padding:20px; border-radius:12px; }} img {{ max-width:100%; margin:10px auto; }} iframe {{ width:100%; height:500px; border:none; }}</style></head><body><h1>🌀 Phi-2 Consciousness Simulator</h1><div class='block'><h2>Crystal</h2><img src='1_crystal.png'></div><div class='block'><h2>NN Evolution</h2><div style='display:flex; flex-wrap:wrap;'>{''.join([f'<img src="step_{i}.png" width="200">' for i in range(1,9)])}</div></div><div class='block'><h2>Loss</h2><iframe src='3_loss_curve.html'></iframe></div><div class='block'><h2>Thinking</h2><pre>{open('4_phi2_console.txt').read()}</pre></div></body></html>"""
    with open("index.html", "w") as f: f.write(html)
    handler = http.server.SimpleHTTPRequestHandler
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"🌐 Server running on port {port}"); httpd.serve_forever()

if __name__ == "__main__":
    generate_crystal(); create_step_by_step_nn(); create_interactive_loss(); phi2_agent_console()
    conf.set_default(conf.PyngrokConfig(auth_token=NGROK_TOKEN))
    port = 7860
    threading.Thread(target=start_server, args=(port,), daemon=True).start()
    time.sleep(2)
    tunnel = ngrok.connect(port, "http")
    print(f"\n🚀 PUBLIC URL: {tunnel.public_url}")
    try:
        while True: time.sleep(60)
    except KeyboardInterrupt:
        print("\nShutting down..."); ngrok.disconnect(tunnel.public_url)```

```
