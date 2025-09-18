import PyPDF2
import pandas as pd
import ollama
import spacy

nlp = spacy.load("en_core_web_sm")
#Extraction of text from various file types
def extract_text_from_file(uploaded_file):
    
    text = ""
    if uploaded_file.type == "application/pdf":
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        for page in pdf_reader.pages:
            text += page.extract_text()

    elif uploaded_file.type == "text/csv":
        df = pd.read_csv(uploaded_file)
        text = df.to_string()

    elif uploaded_file.type == "text/plain":
        text = uploaded_file.read().decode("utf-8")

    elif uploaded_file.type in [
        "application/vnd.ms-excel",
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    ]:
        df = pd.read_excel(uploaded_file)
        text = df.to_string()    

    return text


def parse_question(query):
    
    doc = nlp(query.lower())
    metrics = ["revenue", "sales", "profit", "loss", "expenses", "income", "cash", "assets", "liabilities", "equity"]
    found_metrics = [m for m in metrics if m in query.lower()]
    years = [ent.text for ent in doc.ents if ent.label_ == "DATE"]

    return {
        "metrics": found_metrics,
        "years": years
    }

def ask_question(document_text, query):
   
    parsed = parse_question(query)
    structured_hint = ""
    if parsed["metrics"]:
        structured_hint += f"Metrics asked: {', '.join(parsed['metrics'])}. "
    if parsed["years"]:
        structured_hint += f"Years/periods asked: {', '.join(parsed['years'])}. "

    response = ollama.chat(
        model="llama3:latest",   
        messages=[
            {"role": "system", "content": "You are a financial assistant. Answer based on the provided document."},
            {"role": "user", "content": f"Document: {document_text}\n\nQuestion: {query}"}
        ]
    )
    return response['message']['content']