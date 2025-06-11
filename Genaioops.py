import os
import gradio as gr
import google.generativeai as genai
import subprocess

GEMINI_API_KEY = "Your api key"
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_command(user_prompt):
    prompt = f"""You are a Linux expert. Convert the following user instruction into a safe Linux terminal command:
    "{user_prompt}"
    Only output the command, no explanation, no backticks."""
    
    try:
        response = model.generate_content(prompt)
        if hasattr(response, 'text'):
            return response.text.strip()
        else:
            return "echo 'Error: No response from model.'"
    except Exception as e:
        return f"echo 'Error generating command: {str(e)}'"

def run_command(user_prompt):
    command = generate_command(user_prompt)
    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        output = result.stdout if result.stdout else "No output"
        error = result.stderr
    except Exception as e:
        output = ""
        error = str(e)
    return command, output, error

with gr.Blocks(title="Linux Command AI with Gemini") as demo:
    gr.Markdown("## 💻 Gemini Linux Command Executor")

    user_input = gr.Textbox(label="What do you want to do?", placeholder="e.g., list all files in the current directory")
    run_button = gr.Button("Generate and Run Command")

    command_display = gr.Textbox(label="Generated Command")
    output_display = gr.Textbox(label="Command Output")
    error_display = gr.Textbox(label="Errors (if any)")

    run_button.click(fn=run_command, inputs=[user_input], outputs=[command_display, output_display, error_display])

demo.launch()
