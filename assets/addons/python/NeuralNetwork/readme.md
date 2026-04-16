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
