Raga Chatbot – AI Portfolio Assistant

Raga is a professional AI chatbot built with Flask and Google Gemini API that serves as an interactive portfolio assistant. It can guide visitors through your portfolio, answer questions about skills, projects, certifications, and provide contact details. The chatbot is fully customizable—you can replace the example portfolio data with your own to make it yours.

🔹 Features

💬 Interactive AI Assistant: Answers visitor queries in a friendly, professional, and concise manner.

📝 Customizable Portfolio: Easily update the PORTFOLIO dictionary with your personal details, projects, and skills.

⚡ Real-time Responses: Uses Gemini API for fast AI-driven replies.

🌐 Cross-Origin Support: Works with any frontend via CORS configuration.

🔄 Session Reset: Reset the chat session with a simple API call.

🧩 Project Highlights: Automatically includes project name, description, and technologies when answering queries.

🤖 Professional AI Persona: Always answers as "Raga" and is polite, informative, and concise.

🔹 Tech Stack

Backend: Python, Flask

AI Integration: Google Gemini API

Frontend Support: Any frontend framework (React recommended)

Other: Flask-CORS


🔹 Getting Started


1. Clone the repository
git clone https://github.com/SagarDevop/raga-chatbot.git
cd raga-chatbot

2. Install dependencies

Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows


Install required packages:

pip install -r requirements.txt


Dependencies include: Flask, flask-cors, google-generativeai

3. Configure API Key

Set your Google Gemini API Key as an environment variable:

export GEMINI_API_KEY="YOUR_API_KEY"   # Linux/Mac
set GEMINI_API_KEY="YOUR_API_KEY"      # Windows


Replace "YOUR_API_KEY" with your actual Gemini API key.

4. Update Portfolio Data

Open the server.py (or main file) and modify the PORTFOLIO dictionary:

PORTFOLIO = {
    "name": "Your Name",
    "email": "your.email@example.com",
    "phone": "1234567890",
    "location": "City, Country",
    "linkedin": "https://linkedin.com/in/yourprofile",
    "github": "https://github.com/yourusername",
    "education": "Your Education",
    "skills": ["Skill1", "Skill2", "Skill3"],
    "certifications": ["Certification1", "Certification2"],
    "projects": [
        {
            "name": "Project1",
            "description": "Description of your project",
            "technologies": ["Tech1", "Tech2"]
        }
    ],
    "about": "Write something about yourself."
}


This will make the chatbot your personalized portfolio assistant.


5. Run the Flask Server
python server.py


The API will be available at http://localhost:5000.

Endpoints:

POST /chat → Send a message and get a response.

POST /reset → Reset the chat session.

🔹 Example Chat Request

Request:

POST /chat
{
  "message": "Tell me about your projects using React"
}


Response:

{
  "reply": "- Meesho Clone: Responsive e-commerce frontend inspired by Meesho with product listing, category filtering, and Flask backend (Tech: React, Flask, MongoDB, Tailwind)\n- Traveler Website - Chitrakoot: React-based travel website showcasing tourist spots and guided tours (Tech: React, Maps API, Tailwind)\n..."
}


🔹 Usage

Replace PORTFOLIO data with your own details.

Connect your frontend (React, Vue, Angular, or plain HTML/JS) via the /chat endpoint.

Interact with Raga, your AI portfolio assistant.

You can embed it on any portfolio page to answer visitor questions dynamically.

🔹 Contributing

Contributions, feedback, and suggestions are welcome!

Fork the repository

Create a new branch (git checkout -b feature-name)

Commit your changes (git commit -m "Add feature")

Push to the branch (git push origin feature-name)

Open a Pull Request

🔹 License

MIT License © 2025 Sagar Singh Rajawat

🔹 Live Demo

You can integrate it into your portfolio website to test it live. Replace the sample data with your own portfolio info.

🔹 Contact

Sagar Singh Rajawat

Email: sagar.singh44818@gmail.com

LinkedIn: linkedin.com/in/sagar-singh-rajawat-2b9953337

GitHub: github.com/SagarDevop

✅ Make this chatbot your personalized AI portfolio assistant in minutes!
