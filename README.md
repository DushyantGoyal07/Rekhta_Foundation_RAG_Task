### How to use:

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 2. Create .env

Create a file named .env in the project root:

```GOOGLE_API_KEY=Your_Key```

### 3. Run
```python pipeline.py```

### 4. Outputs

**output.txt**  
Cleaned OCR text produced by the LLM

**analysis.md**  
Automated hallucination checks (line count deviation, length comparison)

**before_after.md**  
Manual examples showing OCR cleanup.

**design_note.md**  
Explanation of scaling, RAG usage, fine-tuning, and quality measurement
