import streamlit as st
from backend import extract_text_from_file, ask_question, parse_question

st.set_page_config(page_title="📊 Financial Document Q&A", layout="wide")

st.markdown("""
    <h1 style='text-align: center; color: #502380;'>📊 Financial Document Q&A Assistant</h1>
    <p style='text-align: center; font-size: 16px;'>Upload your financial PDFs or Excel files and ask questions</p>
""", unsafe_allow_html=True)



# Upload section
uploaded_file = st.file_uploader(
    "Upload a financial document", 
    type=["pdf", "csv", "txt", "xls", "xlsx"]
)

document_text = ""


# Extract text
if uploaded_file is not None:
    with st.spinner("Processing document..."):
        document_text = extract_text_from_file(uploaded_file)
    st.success("✅ Document loaded successfully!")

# Q&A section
if document_text:
    st.subheader("Ask Questions About Your Document")
    query = st.text_input("Enter your question:")
    
    if query:
        with st.spinner("Thinking..."):
            parsed= parse_question(query)
            answer = ask_question(document_text, query)
        st.write("Answer:", f"{float(answer):.2f}" if isinstance(answer, (int, float)) else str(answer))

        st.info(f"🔎 Detected Metrics: {parsed['metrics']} | Detected Periods: {parsed['years']}")


        with st.expander("📄 Extracted Document Content", expanded=False):
            st.text_area("Extracted Content", document_text, height=300)

