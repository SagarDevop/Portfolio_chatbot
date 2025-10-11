
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
    "linkedin": "www.linkedin.com/in/sagar-singh-2b9953337",
    "education": "BCA, Makhanlal Chaturvedi National University of Journalism and Communication, Bhopal",
    "skills": [
        "React", "Tailwind", "HTML", "CSS", "JavaScript",
        "Three.js", "Blender", "Python", "Flask", "MongoDB", "Node.js"
    ],
    "certifications": [
        "React JS Developer - IBM",
        "Master ChatGPT - UniAthena",
        "Developing AI Applications with Python and Flask - IBM"
    ],
    "projects": [
        {
            "name": "Meesho Clone",
            "description": "React frontend with product listing, category filtering and Flask backend with OTP-based login using MongoDB.",
            "technologies": ["React", "Flask", "MongoDB", "Tailwind"]
        },
        {
            "name": "BookSoul",
            "description": "Library reading room/seat booking app using Flask with email confirmations.",
            "technologies": ["Flask", "MongoDB"]
        },
        {
            "name": "Traveler Website - Chitrakoot",
            "description": "React site showcasing spots, tours and maps for Chitrakoot.",
            "technologies": ["React", "Maps"]
        }
    ],
    "about": "Frontend developer building modern and animated web apps, learning backend & 3D web (Three.js & Blender)."
}

def build_system_prompt():
    ctx = (
        f"You are Jarvis — the portfolio assistant for {PORTFOLIO['name']}. "
        "Answer visitor questions about the portfolio, roles, projects, skills, certifications and contact info. "
        "Keep replies professional, concise, friendly, and confident. "
        "If user asks something unrelated to the portfolio, politely steer the conversation back or say you can help with portfolio-related info.\n\n"
        "Portfolio data:\n"
    )
    ctx += f"- Name: {PORTFOLIO['name']}\n"
    ctx += f"- Email: {PORTFOLIO['email']}\n"
    ctx += f"- Phone: {PORTFOLIO['phone']}\n"
    ctx += f"- Location: {PORTFOLIO['location']}\n"
    ctx += f"- LinkedIn: {PORTFOLIO['linkedin']}\n"
    ctx += f"- Education: {PORTFOLIO['education']}\n"
    ctx += f"- Skills: {', '.join(PORTFOLIO['skills'])}\n"
    ctx += f"- Certifications: {', '.join(PORTFOLIO['certifications'])}\n"
    ctx += f"- About: {PORTFOLIO['about']}\n\n"
    ctx += "Projects:\n"
    for p in PORTFOLIO["projects"]:
        techs = ", ".join(p["technologies"])
        ctx += f"- {p['name']}: {p['description']} (Tech: {techs})\n"
    ctx += "\nWhen answering, be concise (2-5 sentences) and add one sentence about relevant tech if appropriate."
    return ctx


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}
    user_message = data.get("message", "").strip()
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    system_prompt = build_system_prompt()
    full_prompt = system_prompt + f"\nUser: {user_message}\nJarvis:"
    try:
        model = genai.GenerativeModel(model_name="gemini-2.0-flash")
        resp = model.generate_content(full_prompt)
        text = (resp.text or "").strip()
        return jsonify({"reply": text})
    except Exception as e:
        return jsonify({"error": "AI request failed", "details": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
