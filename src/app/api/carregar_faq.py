import os
import json
from PyPDF2 import PdfReader
from langchain.vectorstores import Chroma
from langchain.embeddings import OllamaEmbeddings

VECTORSTORE_DIR = "data/chroma_faqs"
embedding_model = OllamaEmbeddings(model="nomic-embed-text")

def carregar_json(file_path: str):
    """Carrega FAQs de um JSON e retorna textos no formato 'Pergunta: ... Resposta: ...'"""
    with open(file_path, "r", encoding="utf-8") as f:
        faqs = json.load(f)
    textos = [f"Pergunta: {faq['pergunta']} Resposta: {faq['resposta']}" for faq in faqs]
    return textos

def carregar_pdf(file_path: str):
    """Extrai texto de um PDF e retorna lista de páginas"""
    reader = PdfReader(file_path)
    return [page.extract_text() for page in reader.pages]

def processar_arquivo_para_chroma(file_path: str, tipo: str = "pdf"):
    """Processa PDF ou JSON e cria/atualiza a base vetorial Chroma"""
    if tipo == "pdf":
        textos = carregar_pdf(file_path)
    elif tipo == "json":
        textos = carregar_json(file_path)
    else:
        raise ValueError("Tipo de arquivo inválido. Use 'pdf' ou 'json'.")

    vectordb = Chroma.from_texts(
        textos,
        embedding=embedding_model,
        persist_directory=VECTORSTORE_DIR
    )
    vectordb.persist()
    return vectordb