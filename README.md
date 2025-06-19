# 💻 Gemini Linux Command Executor

Welcome to **Gemini Linux Command Executor**, a smart web app that transforms your natural language instructions into safe, executable Linux terminal commands using Google Gemini AI! 🚀

---

## ✨ Features

- **AI-powered Command Generation:** Enter your Linux task in plain English and receive a ready-to-run terminal command.
- **One-click Execution:** Seamlessly generate and execute commands with a single click.
- **Safe and Transparent:** See the generated command before it runs.
- **Error Handling:** Clear output and error display for every execution.
- **Modern UI:** Built with [Gradio](https://gradio.app/) for an interactive experience.

---

## 🖥️ Demo

![Gemini Linux Command Executor Screenshot](https://raw.githubusercontent.com/hardik0501/Linux_AI/main/assets/demo-screenshot.png)  
<sup><i>(Replace this with an actual screenshot of your app!)</i></sup>

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/hardik0501/Linux_AI.git
cd Linux_AI
```

### 2. Install dependencies

```bash
pip install gradio google-generativeai
```

### 3. Get your Gemini API key

Sign up and get your [Google Gemini API key](https://ai.google.dev/).

### 4. Set your API key

Open `Genaioops.py` and replace:
```python
GEMINI_API_KEY = "Your api key"
```
with your actual API key.

### 5. Run the app

```bash
python Genaioops.py
```

The app will launch in your browser!

---

## 🛡️ Security Note

- **Always review the generated command before execution.**
- The AI strives for safety, but you should verify any sensitive or potentially destructive operations.

---

## 📝 Example Usage

1. **Input:**  
   *What do you want to do?*  
   `List all files in the current directory`

2. **Generated Command:**  
   ```bash
   ls -l
   ```

3. **Command Output:**  
   (Displays the file list)

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to check the [issues page](https://github.com/hardik0501/Linux_AI/issues).

---

## 📄 License

This project is [MIT Licensed](LICENSE).

---

## 🙏 Acknowledgements

- [Gradio](https://gradio.app/)
- [Google Gemini AI](https://ai.google.dev/)
- Inspired by the need to simplify Linux for everyone.

---

> Created with ❤️ by [hardik0501](https://github.com/hardik0501)
