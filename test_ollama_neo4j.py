from lightrag.llm import ollama_model_complete, ollama_embedding
from lightrag.utils import EmbeddingFunc
from lightrag import LightRAG, QueryParam
import os

# Initialize LightRAG with Ollama model

WORKING_DIR = "scene_database/local_neo4jWorkDir"
os.environ["OPENAI_BASE_URL"] = "https://api.xty.app/v1"  # for embedder
os.environ["OPENAI_API_KEY"] = "sk-0W4cWJtowZt0cjoi263eA084705045Bc968e5064D3501c13"

os.environ["NEO4J_URI"] = "bolt://localhost:7687"
os.environ["NEO4J_USERNAME"] = "neo4j"
os.environ["NEO4J_PASSWORD"] = "caonima123123"

if not os.path.exists(WORKING_DIR):
    os.mkdir(WORKING_DIR)

rag = LightRAG(
    working_dir=WORKING_DIR,
    llm_model_func=ollama_model_complete,  # Use Ollama model for text generation
    llm_model_name='llama3.2',  # Your model name
    # Use Ollama embedding function
    embedding_func=EmbeddingFunc(
        embedding_dim=768,
        max_token_size=8192,
        func=lambda texts: ollama_embedding(
            texts,
            embed_model="nomic-embed-text:latest"
        )
    ),
    log_level="INFO",
    graph_storage="Neo4JStorage",
)

with open("scene_database/dickens/book.txt") as f:
    rag.insert(f.read())

# Perform naive search
print(
    rag.query("What are the top themes in this story?", param=QueryParam(mode="naive"))
)

# Perform local search
print(
    rag.query("What are the top themes in this story?", param=QueryParam(mode="local"))
)

# Perform global search
print(
    rag.query("What are the top themes in this story?", param=QueryParam(mode="global"))
)

# Perform hybrid search
print(
    rag.query("What are the top themes in this story?", param=QueryParam(mode="hybrid"))
)
