def criar_pipeline_rag(vectordb):
    from langchain.chains import RetrievalQA
    from langchain.llms import Ollama

    if vectordb is None:
        return None

    llm = Ollama(model="llama3.2:1b")  
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectordb.as_retriever()
    )
    return qa_chain