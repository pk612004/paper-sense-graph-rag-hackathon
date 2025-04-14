# 📚 Paper Sense: GraphRAG Hackathon Project

A smart research assistant that allows users to **upload academic papers** and then **ask questions** to receive **graph-enhanced, context-aware responses**. It utilizes **LangChain**, **Streamlit**, **cuGraph**, and **ArangoDB** to summarize, store, and retrieve knowledge in a meaningful and interactive way.

---

## 🚀 Features

- 📄 Upload academic PDFs and parse them efficiently.
- 🧠 Extract embeddings and build a knowledge graph.
- 🕵️ Ask natural language questions and get structured, graph-enriched answers.
- 📊 Visualize related concepts and connections.
- ⚡ Fast and easy-to-use Streamlit UI.

---
## 📹 Demo Video

Watch the full demo here: [Click to Watch](https://youtu.be/7Pmdk3cPTR8)


## 🛠️ Tech Stack

| Component | Tech Used |
|----------|------------|
| Frontend | Streamlit |
| Backend  | Python, LangChain |
| LLM      | OpenAI GPT-4 (or compatible LLM) |
| Graph DB | ArangoDB, cuGraph |
| Embeddings | FAISS, Sentence Transformers |
| Parsing PDFs | PyMuPDF / pdfminer |
| Others | Git, VSCode, HuggingFace, dotenv |

---

## 📂 Project Structure

```bash
paper_sense_graph_rag/
├── data/                 # Uploaded PDFs
├── output/               # Output summaries, results
├── src/
│   ├── graph_builder.py  # Builds knowledge graph
│   ├── pdf_loader.py     # Parses and chunks PDFs
│   ├── search_app.py     # Main app logic for QA
│   ├── summarizer.py     # Summarizes content
│   └── test_pdf_loader.py# Test cases for loaders
├── .gitignore
├── requirements.txt
├── README.md


