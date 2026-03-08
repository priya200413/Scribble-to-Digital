import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def process_notes(text):
    prompt = f"""
You are an AI that fixes messy OCR text from handwritten notes.

The OCR text may contain:
- spelling mistakes
- missing letters
- broken words
- random symbols

Your tasks:

1. Correct spelling mistakes
2. Reconstruct incomplete words
3. Fix grammar
4. Convert into clear readable paragraphs
5. Extract To-Do tasks separately

Return output in this format:

CLEAN NOTES:
<corrected notes>

TODO TASKS:
- task 1
- task 2

OCR TEXT:
{text}
"""
    response = model.generate_content(prompt)

    return response.text