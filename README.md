# 📄 RAG Intelligence App (Gemini + Multi-format Docs)

This is a Retrieval-Augmented Generation (RAG) based intelligent assistant that allows users to upload various document types and ask context-aware questions. The answers are strictly generated using the content of the uploaded document via Google Gemini's LLM.

---

## ✨ Features

- 📁 Supports multiple file formats:
  - `.pdf`, `.docx`, `.pptx`, `.txt`, `.html`
- 🤖 Ask any question about the document
- 🧠 Gemini LLM gives accurate, context-grounded answers
- 📜 Table and paragraph extraction from DOCX, PPTX, PDF
- 📄 UI built using Streamlit with a two-column layout:
  - Left: Upload and view document info
  - Right: Ask questions + see previous Q&A
- 💬 Maintains history of all questions and answers
- ✅ Accurate answers — avoids hallucinations

---

## 📂 File Structure

```
rag-intelligence-app/
│
├── ragui.py            # 🖥️ Streamlit user interface
├── extract.py          # 📄 Extracts text/tables from uploaded documents
├── gemini.py           # 🤖 Gemini API integration and prompt formatting
├── testbackend.py      # 🧪 CLI test version for backend logic
├── .env                # 🔐 Stores your Gemini API key
├── requirements.txt    # 📦 All dependencies
└── README.md           # 📘 You're here!
```

---

## 📥 Installation

### 🔧 Prerequisites
- Python 3.10 or higher
- A [Gemini API key](https://makersuite.google.com/app/apikey)

### 📦 Setup Instructions

1. **Clone this repository**
   ```bash
   git clone https://github.com/yourusername/rag-intelligence-app.git
   cd rag-intelligence-app
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file with your Gemini API key**
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

---

## 🚀 Run the App

Launch the Streamlit interface:
```bash
streamlit run ragui.py
```

It will automatically open in your browser.

---

## 🔍 How It Works

| Format     | Extraction Method             | Special Handling |
|------------|-------------------------------|------------------|
| `.pdf`     | `pdfplumber`                  | Extracts text + tables |
| `.docx`    | `python-docx`                 | Paragraphs + tables |
| `.pptx`    | `python-pptx`                 | Slide text + tables |
| `.txt`     | Built-in file reader          | Plain text        |
| `.html`    | `BeautifulSoup`               | Text content from tags |

---

## 🧠 What is RAG?

**RAG (Retrieval-Augmented Generation)** ensures responses are:
- 📚 Grounded in document data
- ✅ More accurate and factual
- 🔐 Not based on external or unknown sources

---

## 🧪 Example Use Cases

- Upload a contract and ask: “What is the termination clause?”
- Upload a report and ask: “Summarize key findings from 2023”
- Upload a table-heavy PDF and ask: “What is the data for Ernakulam?”
- Upload an HTML file and ask: “What sections are available?”

---

## 🧱 Dependencies

```
streamlit
python-docx
python-pptx
pdfplumber
pandas
beautifulsoup4
google-generativeai
python-dotenv
```

To install all at once:

```bash
pip install -r requirements.txt
```

---

## 👩‍💻 Author

**Angel Reji**  
📬 Reach out for improvements or collaboration ideas!

---

## 📜 License

MIT License – feel free to use, modify, or extend.

---

## 📌 Notes

- Currently limited to ~12,000 tokens per document (due to Gemini context window).
- Supports internal extraction only — doesn't pull answers from web.
- For production, consider chunking long docs + vector DB integration.