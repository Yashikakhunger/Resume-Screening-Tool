import spacy
from pdfminer.high_level import extract_text

nlp = spacy.load("en_core_web_md")

def parse_resume(file_bytes):
    with open("temp_resume.pdf", "wb") as f:
        f.write(file_bytes)
    text = extract_text("temp_resume.pdf")
    doc = nlp(text)
    entities = {ent.label_: ent.text for ent in doc.ents}
    return text
