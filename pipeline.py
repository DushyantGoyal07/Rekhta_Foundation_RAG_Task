import os
import warnings
import google.generativeai as genai
from dotenv import load_dotenv

# Code starts from here --------------------
warnings.filterwarnings("ignore")
load_dotenv()

INPUT_FILE = "input.txt"
PROMPT_FILE = "prompt.txt"
OUTPUT_FILE = "output.txt"
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

# Validation Check
def validate(original:str, corrected:str) -> str:
    original_length = len(original)
    corrected_length = len(corrected)
    original_lines = len([l for l in original.splitlines() if l.strip()])
    corrected_lines = len([l for l in corrected.splitlines() if l.strip()])
    line_deviation = abs(corrected_lines - original_lines) / max(1, original_lines)

    with open("analysis.md", "w", encoding="utf-8") as f:
        f.write("# Hallucination Detection\n\n")
        f.write("## Line Count Deviation Check\n")
        f.write(f"- Original lines: {original_lines}\n")
        f.write(f"- Corrected lines: {corrected_lines}\n")
        f.write(f"- Line Deviation: {line_deviation}\n\n")

        f.write("## Length Comparison Check\n")
        f.write(f"- Original length: {original_length}\n")
        f.write(f"- Corrected length: {corrected_length}\n")
        f.write(f"- Length Comparison: {"Original Length is Higher" if corrected_length<=original_length else "Corrected Length is Higher"}\n")

def main():
    ocr_text = load_file(INPUT_FILE)
    prompt_template = load_file(PROMPT_FILE)

    # Cleaning
    cleaned_text = clean_ocr_with_llm(prompt_template, ocr_text)

    # Validation Check
    validate(ocr_text, cleaned_text)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(cleaned_text)


if __name__ == "__main__":
    main()