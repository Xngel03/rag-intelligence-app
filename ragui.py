import streamlit as st
from extract import extract_text
from gemini import generate_response
import os
import tempfile

st.set_page_config(page_title="RAG Intelligence App", layout="wide")
st.title("📄 RAG Intelligence App (Gemini + Multi-format Docs)")

# Session state to track history
if "history" not in st.session_state:
    st.session_state.history = []

# Divide screen into 2 columns
left, right = st.columns(2)

# LEFT SIDE: Upload and show original document
with left:
    uploaded_file = st.file_uploader("📎 Upload Document", type=["pdf", "docx", "pptx", "txt", "html"])

    if uploaded_file:
        # Save the file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[-1]) as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_path = tmp_file.name

        # Show file metadata
        st.markdown(f"**📄 File Uploaded:** `{uploaded_file.name}`")
        st.markdown(f"**🔢 Size:** {round(uploaded_file.size / 1024, 2)} KB")

        # OPTIONAL: Show raw file viewer for text/pdf (html preview coming soon)
        if uploaded_file.type.startswith("text") or uploaded_file.name.endswith(".txt"):
            st.text_area("📝 Document Preview", tmp_file.read().decode(), height=400)
        elif uploaded_file.name.endswith(".pdf"):
            st.info("📌 PDF file uploaded. Contents being processed internally.")
        elif uploaded_file.name.endswith(".docx") or uploaded_file.name.endswith(".pptx"):
            st.info("📌 Word/PPT file uploaded. Processed internally.")
        elif uploaded_file.name.endswith(".xlsx"):
            st.info("📌 Excel file uploaded. Sheet content processed internally.")

# RIGHT SIDE: Ask question, get answer, show history
with right:
    if uploaded_file:
        question = st.text_input("❓ Ask a question about the document")

        if question:
            with st.spinner("Thinking with Gemini..."):
                ext = os.path.splitext(uploaded_file.name)[-1].lower()
                content = extract_text(tmp_path, ext)
                answer = generate_response(content, question)

                # Save Q&A to session state
                st.session_state.history.append((question, answer))

                st.success("💡 Gemini's Answer:")
                st.markdown(f"**{answer}**")

    # Display history
    if st.session_state.history:
        st.markdown("### 🧠 Previous Q&A")
        for i, (q, a) in enumerate(reversed(st.session_state.history), 1):
            st.markdown(f"**{i}. Q:** {q}")
            st.markdown(f"👉 A: {a}")


