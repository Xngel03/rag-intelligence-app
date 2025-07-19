# gemini.py
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()  # Load .env file
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-1.5-flash")  # ✅ Correct model

def generate_response(document_text, query):
    prompt = f"""
You are an AI assistant. Use the following document to answer the question.

Document:
{document_text[:12000]}

Question:
{query}

Only answer using information found in the document.
"""
    response = model.generate_content(prompt)
    return response.text
