# 📊 Financial Data Q&A with LLaMA 2

This project is a simple **Question-Answering system** for financial data.

It allows users to  **upload Excel files** , ask  **natural language questions** , and get answers with the help of **LLaMA 2** (via ollama).

---

## 🚀 Project Features

* Upload files (.xlsx,.csv,.pdf).
* Extract and display data below the upload section.
* Ask financial questions in plain English.
* Uses **NLP + LLaMA 2** to interpret queries.
* Handles both **numerical answers** (formatted to 2 decimals) and **categorical answers** (text values).
* Clean **frontend with Streamlit**.

---

## 🛠️ Tech Stack

* **Frontend** → [Streamlit]()
* **AI Model** → LLaMA 2 (SLM)
* **Data Handling** → Pandas, PyPDF2
* **Deployment Ready** → Can be deployed on Vercel (frontend) + Render/Heroku (backend).

---

## ⚡ Installation & Setup

1. Clone Repository `` git clone https://github.com/ManishinGithub1/FinQuery-Assistant.git``
   `cd FinQuery-Assistant`
2. Create Virtual Environment
   `python -m venv venv`
3. Activate venv
   `venv\Scripts\activate (for Windows users) source venv/bin/activate (for Mac users)`
4. Install Dependencies
   `pip install -r requirements.txt`
5. Run the App
   `streamlit run app.py`
6. Upload Documents & Ask Questions

* Upload Excel/PDF files in the Streamlit UI.
* Extracted content will appear below the question bar.
* Ask questions like:
  “What is the total revenue in 2024?”
  “Which category had the highest expenses?”

---

## 📝 Conclusion

The **FinQuery-Assistant** project demonstrates how financial documents can be transformed into interactive, queryable data using  **NLP and LLaMA 2** . By integrating **Streamlit (frontend)** this system provides a seamless way to upload, process, and analyze  **PDF/Excel-based financial statements** .

This assignment showcases:

* Practical skills in **document parsing (PyPDF2, Pandas)**
* Implementing **natural language processing** and **llama model** for financial insights
* Clean and interactive **user interface** with Streamlit

Overall, this project highlights how AI-driven systems can simplify financial analysis, making data more **accessible, understandable, and actionable** for users.

---

## 🔗 Connect with Me

* **GitHub** : [ManishinGithub1](https://github.com/ManishinGithub1)
* **LinkedIn** : [Y. Manish Kumar Reddy | LinkedIn](https://www.linkedin.com/in/yellaiah-gari-manish-kumar-reddy/)
