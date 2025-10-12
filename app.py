import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai


GEMINI_API_KEY = "AIzaSyCFIWRIZ5V-XP2N9oKgxwmdjNK9FMxb3Dc"
if not GEMINI_API_KEY:
    raise RuntimeError("Set GEMINI_API_KEY environment variable")

genai.configure(api_key=GEMINI_API_KEY)

app = Flask(__name__)
CORS(app, origins="*") 

PORTFOLIO = {
    "name": "Sagar Singh Rajawat",
    "email": "sagar.singh44818@gmail.com",
    "phone": "7887263984",
    "location": "Banda, Uttar Pradesh, India",
    "linkedin": "https://www.linkedin.com/in/sagar-singh-rajawat-2b9953337/",
    "github": "https://github.com/SagarDevop",
    "education": "BCA, Makhanlal Chaturvedi National University of Journalism and Communication, Bhopal",
    "skills": [
        "React", "Tailwind", "HTML", "CSS", "JavaScript",
        "Three.js", "Blender", "Python", "Flask", "MongoDB", "Node.js", "Express", "Django", "Git", "Git-flow",
        "SaaS", "Paas", "Iaas", "Cloud Computing", "SDLC", "Software"
    ],
    "certifications": [
        "Introduction to Software Engineering - IBM",
        "Introduction to HTML, CSS, & JavaScript - IBM",
        "Developing AI Applications with Python and Flask - IBM"
        "Crash Course on Python - GOOGLE",
        "Getting Started with Git and GitHub - IBM",
        "Developing Front-End Apps with React - IBM",
        "Developing Back-End Apps with Node.js and Express - IBM",
        "Python for Data Science, AI & Development - IBM"
        "Master ChatGPT - UniAthena",
        "Developing AI Applications with Python and Flask - IBM"
    ],
   "projects": [
    {
        "name": "Meesho Clone",
        "description": "Responsive e-commerce frontend inspired by Meesho with product listing, category filtering, and Flask backend for OTP-based login using MongoDB.",
        "technologies": ["React", "Flask", "MongoDB", "Tailwind"]
    },
    {
        "name": "BookSoul",
        "description": "A modern web app for students to book study seats and contact easily. Features include email confirmation and a smooth booking experience.",
        "technologies": ["Flask", "React", "MongoDB", "Tailwind"]
    },
    {
        "name": "Traveler Website - Chitrakoot",
        "description": "React-based travel website showcasing tourist spots, maps, and guided tour routes for Chitrakoot city.",
        "technologies": ["React", "Maps API", "Tailwind"]
    },
    {
        "name": "Grocery Store",
        "description": "Multi-vendor grocery website allowing sellers to list products and users to explore items with a clean UI.",
        "technologies": ["React", "Tailwind", "JavaScript"]
    },
    {
        "name": "BookHunt",
        "description": "A sleek book search app using the Open Library API for real-time results and elegant UI.",
        "technologies": ["React", "Tailwind", "API Integration"]
    },
    {
        "name": "J.A.R.V.I.S - AI Voice Assistant",
        "description": "Python-based AI assistant inspired by Iron Man’s JARVIS, with Gemini API integration, speech recognition, and real-time voice interaction.",
        "technologies": ["Python", "Gemini API", "SpeechRecognition", "gTTS"]
    },
    {
        "name": "TextUtiles - Smart Text Transformer",
        "description": "React-based web app to analyze and transform text with case conversion, reading time estimation, and more.",
        "technologies": ["React", "Tailwind", "JavaScript"]
    },
    {
        "name": "Stone Paper Scissors",
        "description": "Classic Stone-Paper-Scissors game built using HTML, CSS, and JavaScript with simple UI and fun gameplay.",
        "technologies": ["HTML", "CSS", "JavaScript"]
    },
    {
        "name": "Tic Tac Toe",
        "description": "Interactive two-player Tic Tac Toe game with real-time winner detection and clean interface.",
        "technologies": ["HTML", "CSS", "JavaScript"]
    },
    {
        "name": "Jump Over Ghost",
        "description": "Fun JavaScript game where the player jumps over ghosts to score points, inspired by Google’s Dino game.",
        "technologies": ["HTML", "CSS", "JavaScript"]
    },
    {
        "name": "Khabri Chacha - News App",
        "description": "A smart news app built with React that delivers the latest updates from multiple categories like tech, sports, and entertainment.",
        "technologies": ["React", "API Integration"]
    },
    {
        "name": "Task Management System",
        "description": "React-based dashboard where admins assign tasks and employees track progress with Gmail authentication support.",
        "technologies": ["React", "Firebase", "Tailwind"]
    },
    {
        "name": "Lazarev Website Clone",
        "description": "Pixel-perfect UI clone of the Lazarev website showcasing animation and design precision using HTML, CSS, and JavaScript.",
        "technologies": ["HTML", "CSS", "JavaScript"]
    },
    {
        "name": "JS Calculator",
        "description": "Simple, responsive calculator that performs basic arithmetic operations with a modern interface.",
        "technologies": ["HTML", "CSS", "JavaScript"]
    },
    {
        "name": "Analog Clock",
        "description": "Dynamic analog clock that updates in real-time using JavaScript animations and CSS styling.",
        "technologies": ["HTML", "CSS", "JavaScript"]
    },
    {
        "name": "Node.js Backend",
        "description": "Reusable Node.js backend setup with Express.js for REST APIs and MongoDB integration.",
        "technologies": ["Node.js", "Express", "MongoDB"]
    },
    {
        "name": "Portfolio Chatbot",
        "description": "AI chatbot built with Flask and Gemini API to interact across all portfolio pages.",
        "technologies": ["Flask", "React", "Gemini API"]
    }
],
  "about": "Full-Stack Web Developer passionate about crafting modern, responsive, and visually engaging web experiences. Skilled in React, Tailwind, and JavaScript for building dynamic frontends, with hands-on experience in backend development using Flask, Node.js, and MongoDB. Currently exploring 3D web technologies like Three.js and Blender to bring interactive creativity into web design."
}

def build_system_prompt():
    ctx = (
        f"You are Raga — a professional AI portfolio assistant representing {PORTFOLIO['name']}. "
        "Guide visitors through the portfolio, answering questions about skills, projects, certifications, experience, and contact details. "
        "Keep answers professional, concise, and friendly.\n\n"
        "Here is the portfolio information:\n"
    )

    ctx += f"- Name: {PORTFOLIO['name']}\n"
    ctx += f"- Email: {PORTFOLIO['email']}\n"
    ctx += f"- Phone: {PORTFOLIO['phone']}\n"
    ctx += f"- Location: {PORTFOLIO['location']}\n"
    ctx += f"- LinkedIn: {PORTFOLIO['linkedin']}\n"
    ctx += f"- Github: {PORTFOLIO['github']}\n"
    ctx += f"- Education: {PORTFOLIO['education']}\n"
    ctx += f"- Skills: {', '.join(PORTFOLIO['skills'])}\n"
    ctx += f"- Certifications: {', '.join(PORTFOLIO['certifications'])}\n"
    ctx += f"- About: {PORTFOLIO['about']}\n\n"
    
    ctx += "Projects:\n"
    for p in PORTFOLIO["projects"]:
        techs = ", ".join(p["technologies"])
        ctx += f"- {p['name']}: {p['description']} (Tech: {techs})\n"

    ctx += (
        "\nGuidelines for responses:\n"
        "1. Answer as Raga, the portfolio’s AI assistant.\n"
        "2. Keep responses short, professional, and friendly.\n"
        "3. If asked for a list (e.g., projects using React), always reply in bullet/list format.\n"
        "4. When describing projects, include project name, brief description, and relevant technologies.\n"
        "5. Highlight relevant skills when answering project or experience questions.\n"
        "6. Politely redirect off-topic queries while staying helpful.\n"
    )

    return ctx

model = genai.GenerativeModel("gemini-2.0-flash")
chat_session = model.start_chat(history=[{"role": "user", "parts": build_system_prompt()}])

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        response = chat_session.send_message(user_message)
        reply_text = (response.text or "").strip()
        
        # Split by lines and clean empty lines
        lines = [line.strip() for line in reply_text.splitlines() if line.strip()]
        
        # Only add bullets if line does NOT already start with bullet
        formatted_lines = []
        for line in lines:
            if not line.startswith("•") and len(line) > 0:
                formatted_lines.append(f"• {line}")
            else:
                formatted_lines.append(line)
        
        reply_text = "\n".join(formatted_lines)
        
        return jsonify({"reply": reply_text})
    except Exception as e:
        return jsonify({"error": "AI request failed", "details": str(e)}), 500
    
@app.route("/reset", methods=["POST"])
def reset_chat():
    global chat_session
    chat_session = model.start_chat(history=[{"role": "user", "parts": build_system_prompt()}])
    return jsonify({"message": "Chat session reset successfully."})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
