# Design Notes:

## Scaling the Pipeline

The pipeline can be scaled by processing OCR documents asynchronously and page-wise.
Each stage—rule-based cleanup, LLM correction, and validation—can run independently. Frequently observed OCR errors can be
moved into the rule-based layer to reduce LLM usage and cost.

---

## Where RAG Fits

I used RAG here by treating the **original Urdu OCR** input itself as
**external knowledge**. The LLM is instructed using **prompt.txt** to rely only on the provided
Urdu text and not introduce any new information. T

---

## When Fine-tuning Would Help

Fine-tuning becomes useful when OCR errors are repetitive and domain-specific, such as
consistent Urdu font. A fine-tuned model can reduce prompt size, improve consistency, and lower inference cost. Until sufficient labeled data exists,
prompt-based correction is safer.

---

## Quality Measurement Over Time

Quality is measured using automated structural checks such as line count deviation and
length comparison.
These metrics ensure the corrected output remains faithful to the
original OCR text.

---