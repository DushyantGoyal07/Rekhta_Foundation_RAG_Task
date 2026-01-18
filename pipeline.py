import os
import json
import warnings
import google.generativeai as genai
from dotenv import load_dotenv

# Code starts from here --------------------
warnings.filterwarnings("ignore")
load_dotenv()

INPUT_FILE = "input.txt"
PROMPT_FILE = "prompt.txt"
OUTPUT_FILE = "output.txt"
REPORT_FILE = "report.json"
MODEL_NAME = "gemini-2.5-flash-lite"

GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(MODEL_NAME)


# Load Files
def load_file(path: str) -> str:
    with open(path, 'r', encoding="utf-8") as f:
        return f.read()
    
# Clean OCR
def clean_ocr_with_llm(prompt_template: str, ocr_text: str) -> str:
    prompt = prompt_template.replace("{{OCR_TEXT}}", ocr_text)
    response = model.generate_content(prompt)

    return response.text.strip()

def main():
    ocr_text = load_file(INPUT_FILE)
    prompt_template = load_file(PROMPT_FILE)

    # Cleaning
    cleaned_text = clean_ocr_with_llm(prompt_template, ocr_text)

    # Halluncinaton Check
    report = validate(ocr_text, cleaned_text)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(cleaned_text)

    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()