import os
os. environ [" TOKENIZERS_PARALLELISM "] = " false "
from fastapi import FastAPI
from fastapi . middleware . cors import CORSMiddleware

from langserve import add_routes
from src. base . llm_model import get_hf_llm
from src. rag. main import build_rag_chain , InputQA , OutputQA

llm = get_hf_llm ( temperature =0.9)
genai_docs = "./data_source/generative_ai"

genai_chain = build_rag_chain (llm , data_dir = genai_docs , data_type ="pdf")

app = FastAPI (
    title="LangChain Server",
    version="1.0",
    description="A simple API server for LangChain"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# --------- Routes - FastAPI ----------------

@app.get("/check")
async def check():
    return {"status": "ok"}

@app.post("/generative_ai", response_model=OutputQA)

async def generative_ai(input: InputQA):
    answer = genai_chain.invoke(input.question)
    return {"answer": answer}
# --------- LangServe ----------------
add_routes(app, genai_chain, playground_type="default", path="/generative_ai")