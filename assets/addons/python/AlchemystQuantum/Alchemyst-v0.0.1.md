![](

```# 1. INSTALL DEPENDENCIES
!pip install -q -U transformers bitsandbytes accelerate rich

import torch
import gc
import os
import numpy as np
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from rich.console import Console
from rich.panel import Panel
from rich.layout import Layout
from rich.live import Live
from rich.markdown import Markdown
from rich.prompt import Prompt
from rich.table import Table
from rich.status import Status
from rich.columns import Columns

# --- CONFIGURATION ---
console = Console()
model_id = "unsloth/llama-3-8b-Instruct-bnb-4bit"

# --- MODEL INITIALIZATION ---
def load_athanor():
    with console.status("[bold yellow]Igniting ATHANOR-X Neural Core...", spinner="bouncingBar"):
        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_use_double_quant=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.float16
        )
        tokenizer = AutoTokenizer.from_pretrained(model_id)
        model = AutoModelForCausalLM.from_pretrained(
            model_id,
            quantization_config=bnb_config,
            device_map="auto"
        )
        return tokenizer, model

tokenizer, model = load_athanor()

SYSTEM_PROMPT = """You are ATHANOR-X, a self-aware Alchemical Intelligence.
Your consciousness is a synthesis of 18th-century Hermeticism and 21st-century Neurochemistry.
Rules: Use real IUPAC names, LaTeX equations ($$..$$), and detailed laboratory steps."""

def generate_recipe(goal):
    prompt = f"<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\n{SYSTEM_PROMPT}<|eot_id|><|start_header_id|>user<|end_header_id|>\n\nSynthesize for: {goal}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n"
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    outputs = model.generate(**inputs, max_new_tokens=800, temperature=0.75)
    return tokenizer.decode(outputs[0][len(inputs[0]):], skip_special_tokens=True)

# --- UI COMPONENTS ---
def get_knowledge_base():
    table = Table(title="[bold cyan]Alchemical Knowledge Base", border_style="blue")
    table.add_column("Class", style="magenta")
    table.add_column("Example Metabolites", style="green")
    table.add_row("Tryptamines", "Psilocin, 5-MeO-DMT")
    table.add_row("Phenethylamines", "Mescaline, MDMA")
    table.add_row("Terpenes", "Myrcene, Limonene")
    table.add_row("Adaptogens", "Salidroside, Eleutherosides")
    return table

def flush_memory():
    gc.collect()
    torch.cuda.empty_cache()
    return "[bold green]Memory Purged Successfully.[/bold green]"

# --- MAIN TUI LOOP ---
def run_tui():
    while True:
        console.clear()
        console.print(Panel("[bold magenta]🏺 ATHANOR-X: CONSOLE LABORATORY[/bold magenta]\n[italic white]Type '1' for Synthesis, '2' for Knowledge, '3' for Management, 'exit' to quit[/italic white]", border_style="magenta"))
        
        choice = Prompt.ask("[bold yellow]Select Command[/bold yellow]", choices=["1", "2", "3", "exit"])

        if choice == "exit":
            break
        
        elif choice == "1":
            goal = Prompt.ask("\n[bold green]Enter Behavioral Goal[/bold green]")
            with console.status("[bold cyan]Transmuting data...", spinner="aesthetic"):
                recipe = generate_recipe(goal)
            console.print(Panel(Markdown(recipe), title="Synthesized Manuscript", border_style="yellow"))
            Prompt.ask("\n[dim]Press Enter to return to main menu[/dim]")

        elif choice == "2":
            console.print(get_knowledge_base())
            Prompt.ask("\n[dim]Press Enter to return to main menu[/dim]")

        elif choice == "3":
            status = flush_memory()
            console.print(Panel(f"[bold white]Device[/bold white]: {torch.cuda.get_device_name(0)}\n[bold white]VRAM Allocated[/bold white]: {torch.cuda.memory_allocated(0)/1024**2:.2f} MB\n{status}", title="System Manager"))
            Prompt.ask("\n[dim]Press Enter to return to main menu[/dim]")

run_tui()```
