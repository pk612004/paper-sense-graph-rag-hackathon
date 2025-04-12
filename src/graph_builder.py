
import spacy
import networkx as nx
import matplotlib.pyplot as plt
from pdf_loader import load_all_pdfs

nlp = spacy.load("en_core_web_sm")

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


import os
def draw_graph(G, output_path=None):
    if output_path is None:
        output_path = os.path.join("output", "graph.png")

    import matplotlib.pyplot as plt
    plt.figure(figsize=(20, 12)) 
    pos = nx.spring_layout(G, k=0.45, iterations=50)

    degrees = dict(G.degree())
    node_sizes = [v * 100 for v in degrees.values()]
    node_colors = [v for v in degrees.values()]

    nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors,
                           cmap=plt.cm.coolwarm, alpha=0.9)
    nx.draw_networkx_edges(G, pos, alpha=0.3)
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")

    plt.title("Co-occurrence Graph", fontsize=18)
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.show()


draw_graph(G)

