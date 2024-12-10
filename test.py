import os
from lightrag import LightRAG, QueryParam
from lightrag.llm import gpt_4o_mini_complete
#########
# Uncomment the below two lines if running in a jupyter notebook to handle the async nature of rag.insert()
# import nest_asyncio
# nest_asyncio.apply()
#########

WORKING_DIR = "scene_database/scene_data"
os.environ["OPENAI_BASE_URL"] = "https://api.xty.app/v1"  # for embedder
openai_4 = "sk-TyJ6SBEs7piviK3y9c5161A761D446819b6b475cBe492056"
openai_35 = "sk-3KYi6KL04eXHDaicAa8971C37eCa4cB186324c9cA778F71d"
os.environ["OPENAI_API_KEY"] = openai_4

if not os.path.exists(WORKING_DIR):
    os.mkdir(WORKING_DIR)

# refresh and clean neo4j dataset
from neo4j import GraphDatabase
uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "caonima123123"))
with driver.session() as session:
    session.run("MATCH (n) DETACH DELETE n")

rag = LightRAG(
    working_dir=WORKING_DIR,
    llm_model_func=gpt_4o_mini_complete,  # Use gpt_4o_mini_complete LLM model
    # llm_model_func=gpt_4o_complete  # Optionally, use a stronger model
)

with open("/home/zjj/git/LEGENT/scripts/data2.json", "r", encoding="utf-8") as f:
    rag.insert(f.read())

# with open("/home/zjj/git/LEGENT/scripts/data_default.json", "r", encoding="utf-8") as f:
#     rag.insert(f.read())

# Perform naive search
# print(
#     rag.query("What are the top themes in this story?", param=QueryParam(mode="naive"))
# )
#
# # Perform local search
# print(
#     rag.query("What are the top themes in this story?", param=QueryParam(mode="local"))
# )

# Perform global search
# print(
#     rag.query("What are the top themes in this story?", param=QueryParam(mode="global"))
# )

# Perform hybrid search
print(
    rag.query("What is the book's id ,give me the relationship of {in what} or {on what}", param=QueryParam(mode="hybrid"))
)
