from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os

# ==========================================
# PROJECT PATH
# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_FILE = os.path.join(BASE_DIR, ".env")

# Load .env
# override=True means .env value has priority
load_dotenv(ENV_FILE, override=True)


# ==========================================
# API KEY
# ==========================================

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError(
        "OPENAI_API_KEY not found.\n"
        "Please check your .env file."
    )


# ==========================================
# OPENAI CLIENT
# ==========================================

client = OpenAI(api_key=api_key)


# ==========================================
# FLASK APP
# ==========================================

app = Flask(__name__)


# ==========================================
# HOME PAGE
# ==========================================

@app.route("/")
def home():
    return render_template("index.html")


# ==========================================
# CHAT API
# ==========================================

@app.route("/chat", methods=["POST"])
def chat():

    try:

        # Get JSON data
        data = request.get_json(silent=True) or {}

        # Get user's message
        user_message = data.get("message", "").strip()

        # Check empty message
        if not user_message:
            return jsonify({
                "error": "Please enter a message."
            }), 400


        # ======================================
        # TERMINAL LOG
        # ======================================

        print("\n===================================")
        print("USER:", user_message)
        print("AI is thinking...")
        print("===================================")


        # ======================================
        # OPENAI RESPONSE
        # ======================================

        response = client.responses.create(

            # Current low-cost model
            model="gpt-5.6-luna",

            # AI instructions
            instructions="""
You are Danish AI, a helpful personal AI assistant.

Your responsibilities:

1. Answer questions clearly.
2. Explain difficult topics in simple language.
3. Help with programming.
4. Help debug code.
5. Write clean and working code.
6. Help with study and learning.
7. Help with research.
8. Help with AI and technology.
9. Give step-by-step instructions when useful.
10. Be friendly and professional.
11. Never pretend that you performed an action you did not perform.
12. If you are unsure about something, say so clearly.
13. Keep answers useful and easy to understand.

You are called Danish AI.
""",

            # User message
            input=user_message
        )


        # ======================================
        # GET AI ANSWER
        # ======================================

        answer = response.output_text


        # ======================================
        # TERMINAL OUTPUT
        # ======================================

        print("AI:", answer)
        print("===================================\n")


        # ======================================
        # SEND RESPONSE TO BROWSER
        # ======================================

        return jsonify({
            "reply": answer
        })


    except Exception as e:

        # ======================================
        # ERROR LOG
        # ======================================

        print("\n===================================")
        print("OPENAI ERROR:")
        print(repr(e))
        print("===================================\n")


        # ======================================
        # SEND ERROR TO BROWSER
        # ======================================

        return jsonify({
            "error": str(e)
        }), 500


# ==========================================
# START SERVER
# ==========================================

if __name__ == "__main__":

    print("")
    print("===================================")
    print("         DANISH AI AGENT")
    print("===================================")

    # Safe check only
    print("AI API Key: Loaded")

    print("Server: http://127.0.0.1:5000")

    print("===================================")
    print("")

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )