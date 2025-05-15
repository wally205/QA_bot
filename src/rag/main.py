from pydantic import BaseModel, Field

from src.rag.file_loader import Loader
from src.rag.vectorstore import VectorDB
from src.rag.offline_rag import Offline_RAG

class InputQA(BaseModel):
    question: str = Field(..., description="Question to ask the model")

class OutputQA(BaseModel):
    answer: str = Field(..., description="Answer from the model")

def build_rag_chain(llm,data_dir,data_type):
    doc_loaded = Loader ( file_type = data_type ) . load_dir ( data_dir , workers =2)
    retriver=VectorDB(documents=doc_loaded).get_retriever()
    rag_langchain=Offline_RAG(llm=llm).get_chain(retriever=retriver)
    return rag_langchain
