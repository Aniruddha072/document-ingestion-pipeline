from langchain_community.vectorstores import FAISS


def create_vectorstore(
    chunks,
    embedding_model,
    doc_id
):

    vectorstore = FAISS.from_documents(
        chunks,
        embedding_model
    )

    vectorstore.save_local(
        f"vectorstore/{doc_id}"
    )

    return vectorstore