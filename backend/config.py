import os
import google.generativeai as genai

# Pulls the secret key you save in your Vercel dashboard
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# This creates the 'model' variable your agents are looking for
model = genai.GenerativeModel('models/gemini-1.5-flash')