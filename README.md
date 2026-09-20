# 🤖 Danish AI Agent

**Danish AI Agent** is a personal AI assistant built with Python, Flask, OpenAI API, HTML5, CSS3, and JavaScript.

It provides a simple web-based interface for interacting with an AI assistant and is designed as a foundation for building a more advanced AI agent with additional capabilities such as memory, tools, file processing, web search, and automation.

---

## ✨ Features

* 🤖 AI-powered chat
* 💬 Interactive web chat interface
* 🧠 OpenAI API integration
* 🐍 Python Flask backend
* 🎨 Responsive and modern interface
* 🔐 Environment variable support for API keys
* ⚡ Fast local development
* 💻 Windows-friendly setup
* 🧩 Easy to extend with additional AI tools and features

---

## 🛠️ Technologies Used

| Technology    | Purpose                         |
| ------------- | ------------------------------- |
| Python        | Backend programming             |
| Flask         | Web server and API              |
| OpenAI API    | AI responses                    |
| HTML5         | Web structure                   |
| CSS3          | UI styling                      |
| JavaScript    | Frontend functionality          |
| python-dotenv | Environment variable management |

---

## 📁 Project Structure

```text
AI/
│
├── app.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── .gitignore
└── README.md
```

---

# 🚀 Installation Guide

## 1. Requirements

Before installing the project, make sure you have:

* Python 3.10 or newer
* Git
* Internet connection
* An OpenAI API key

Check Python:

```powershell
python --version
```

Check Git:

```powershell
git --version
```

---

## 2. Clone the Repository

Open PowerShell or Command Prompt and run:

```powershell
git clone https://github.com/danishalipny-pixel/AI.git
```

Enter the project folder:

```powershell
cd AI
```

---

## 3. Create a Virtual Environment

Create a Python virtual environment:

```powershell
python -m venv venv
```

This creates an isolated Python environment for the project.

---

## 4. Activate Virtual Environment

### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

After activation, your terminal should look similar to:

```text
(venv) PS C:\Users\YourName\AI>
```

### If PowerShell blocks activation

Run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Then activate again:

```powershell
.\venv\Scripts\Activate.ps1
```

---

## 5. Install Required Packages

With the virtual environment activated, install the dependencies:

```powershell
pip install flask openai python-dotenv
```

You can verify the installed packages with:

```powershell
pip list
```

---

# 🔑 API Key Configuration

The application uses an environment variable for the OpenAI API key.

## 1. Create `.env`

Inside the project root, create a file named:

```text
.env
```

The structure should be:

```text
AI/
├── app.py
├── .env
├── templates/
└── static/
```

## 2. Add Your API Key

Open `.env` and add:

```env
OPENAI_API_KEY=YOUR_API_KEY_HERE
```

Replace `YOUR_API_KEY_HERE` with your own API key.

### ⚠️ Security

**Never publish your API key on GitHub.**

The `.gitignore` file should contain:

```gitignore
.env
venv/
__pycache__/
*.pyc
```

This prevents your secret API key and virtual environment from being uploaded to GitHub.

---

# ▶️ Run the Application

Make sure your virtual environment is activated:

```powershell
.\venv\Scripts\Activate.ps1
```

Then start the Flask server:

```powershell
python app.py
```

If everything is configured correctly, you should see something similar to:

```text
===================================
         DANISH AI AGENT
===================================
AI API Key: Loaded
Server: http://127.0.0.1:5000
===================================
```

---

# 🌐 Open the Application

Open your browser and visit:

```text
http://127.0.0.1:5000
```

You should see the Danish AI chat interface.

Type a message and send it to receive an AI response.

---

# 🛑 Stop the Server

To stop the Flask development server, press:

```text
Ctrl + C
```

---

# 🔄 Start the Project Again

Whenever you want to run the project again:

```powershell
cd AI
```

Activate the environment:

```powershell
.\venv\Scripts\Activate.ps1
```

Start the application:

```powershell
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

---

# 🐛 Troubleshooting

## `ModuleNotFoundError: No module named 'flask'`

Install the required packages:

```powershell
pip install flask openai python-dotenv
```

---

## `ModuleNotFoundError: No module named 'openai'`

Run:

```powershell
pip install openai
```

---

## `ModuleNotFoundError: No module named 'dotenv'`

Run:

```powershell
pip install python-dotenv
```

---

## Virtual Environment Not Found

If this command:

```powershell
.\venv\Scripts\Activate.ps1
```

does not work, create the environment:

```powershell
python -m venv venv
```

Then:

```powershell
.\venv\Scripts\Activate.ps1
```

---

## `OPENAI_API_KEY not found`

Make sure `.env` exists in the same folder as `app.py`.

Correct:

```text
AI/
├── app.py
├── .env
├── templates/
└── static/
```

And `.env` contains:

```env
OPENAI_API_KEY=YOUR_API_KEY_HERE
```

---

## `401 Invalid API Key`

Check that:

1. The API key is valid.
2. The API key is active.
3. The `.env` file contains the correct key.
4. There are no unnecessary quotes or spaces.
5. You restarted the Flask server after changing `.env`.

**Never post your API key in GitHub, screenshots, or chat.**

---

# 🔧 Development

The Flask backend is located in:

```text
app.py
```

The frontend HTML is located in:

```text
templates/index.html
```

CSS:

```text
static/style.css
```

JavaScript:

```text
static/script.js
```

You can modify these files to customize the AI assistant.

---

# 📦 Updating the Project

After making changes:

```powershell
git status
```

Add your changes:

```powershell
git add .
```

Create a commit:

```powershell
git commit -m "Update AI Agent"
```

Push to GitHub:

```powershell
git push
```

---

# 🌱 Future Improvements

Planned improvements for the AI Agent can include:

* 🧠 Conversation memory
* 📄 PDF and document processing
* 🔎 Web search
* 📁 File uploads
* 💻 Code execution
* 🎤 Voice input
* 🔊 Voice responses
* 🛠️ AI tools
* 🤖 Autonomous task execution
* 👤 User accounts
* 💾 Database integration
* 📊 AI agent dashboard

---

# 👨‍💻 Author

## Danish Rashid

**Full Stack Developer & AI Developer**

GitHub:

https://github.com/danishalipny-pixel

---

# 📌 Repository

GitHub Repository:

https://github.com/danishalipny-pixel/AI

---

# 📄 License

This project is currently intended for learning, experimentation, and development purposes.
