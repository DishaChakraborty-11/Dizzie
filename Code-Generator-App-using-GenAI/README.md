# Gemini-Powered Code Generator

A Streamlit web app powered by **Google Gemini (Generative AI)** that can generate **code in multiple programming languages** from plain English descriptions — with explanations included.


##  What It Does

This tool takes your natural language input (e.g., “Sort a list in Python”), sends it to Gemini 1.5 Pro, and displays:

✅ Generated code  
✅ Syntax-highlighted output  
✅ Plain-English explanation


##  Supported Languages

- 🐍 Python  
- 🦬 JavaScript  
- 🦣 Java  
- 🦍 C#  
- 🦏 C++  
- 🕸 C  
- 🐦‍🔥 SQL  
- 🦩 R  
- 🐎 Go  


 Installation
Follow the steps below to set up and run the app locally:

1. Clone the Repository

git clone https://github.com/YOUR_USERNAME/code-generator-gemini.git
cd code-generator-gemini
🔁 Replace YOUR_USERNAME with your actual GitHub username or organization.

2. Install Python dependencies
Ensure Python 3.9 or higher is installed.

pip install -r requirements.txt


3. Set Your Gemini API Key
Open the main script (e.g., code_generator_app.py) and replace:

api_key = "YOUR_API_KEY"
with your actual Google Gemini API key.

 Tip: You can store the key securely in a .env file if needed (ask me and I’ll show you how).

4. Run the App

streamlit run code_generator_app.py
The app will open in your default browser at:

http://localhost:8501
 Optional: Create a virtual environment (recommended)

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
