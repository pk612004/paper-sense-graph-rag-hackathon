import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import os
import spacy
from pdf_loader import load_all_pdfs
from io import BytesIO

nlp = spacy.load("en_core_web_sm")

st.title("📚 PaperSense Graph RAG")
st.markdown("Explore entity relationships extracted from your research papers.")

pdf_texts = load_all_pdfs("data")
combined_text = " ".join(pdf_texts.values())
doc = nlp(combined_text)

G = nx.Graph()
for sent in doc.sents:
    ents = [ent.text.strip() for ent in sent.ents if ent.label_ in {"PERSON", "ORG", "GPE", "LOC"}]
    for i in range(len(ents)):
        for j in range(i + 1, len(ents)):
            G.add_node(ents[i], label=ents[i])
            G.add_node(ents[j], label=ents[j])
            G.add_edge(ents[i], ents[j])

st.sidebar.header("🔍 Search Entities")
search_term = st.sidebar.text_input("Enter entity name")

if search_term:
    sub_nodes = [n for n in G.nodes if search_term.lower() in n.lower()]
    subgraph = G.subgraph(sub_nodes)
    st.subheader(f"Results for: `{search_term}`")
else:
    subgraph = G

fig, ax = plt.subplots(figsize=(12, 8))
pos = nx.spring_layout(subgraph, k=0.45)

degrees = dict(subgraph.degree())
node_sizes = [v * 100 for v in degrees.values()]
node_colors = [v for v in degrees.values()]

nx.draw_networkx_nodes(subgraph, pos, node_size=node_sizes, node_color=node_colors, cmap=plt.cm.viridis, alpha=0.8, ax=ax)
nx.draw_networkx_edges(subgraph, pos, alpha=0.4, ax=ax)
nx.draw_networkx_labels(subgraph, pos, font_size=9, ax=ax)

plt.title("Named Entity Co-occurrence Graph", fontsize=15)
plt.axis("off")

st.pyplot(fig)

with st.expander("📥 Export Graph Image"):
    buf = BytesIO()
    fig.savefig(buf, format="png", dpi=300)
    st.download_button("Download PNG", buf.getvalue(), file_name="graph.png", mime="image/png")
