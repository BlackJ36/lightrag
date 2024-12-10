import os
from lightrag import LightRAG, QueryParam
from lightrag.llm import gpt_4o_mini_complete


#########
# Uncomment the below two lines if running in a jupyter notebook to handle the async nature of rag.insert()
# import nest_asyncio
# nest_asyncio.apply()
#########

WORKING_DIR = "scene_database/data_default_scene"
os.environ["OPENAI_BASE_URL"] = "https://api.xty.app/v1"  # for embedder
os.environ["OPENAI_API_KEY"] = "sk-TyJ6SBEs7piviK3y9c5161A761D446819b6b475cBe492056"

os.environ["NEO4J_URI"] = "bolt://localhost:7687"
os.environ["NEO4J_USERNAME"] = "neo4j"
os.environ["NEO4J_PASSWORD"] = "caonima123123"

if not os.path.exists(WORKING_DIR):
    os.mkdir(WORKING_DIR)

# refresh and clean neo4j dataset
# from neo4j import GraphDatabase
# uri = "bolt://localhost:7687"
# driver = GraphDatabase.driver(uri, auth=("neo4j", "caonima123123"))
# with driver.session() as session:
#     session.run("MATCH (n) DETACH DELETE n")

rag = LightRAG(
    working_dir=WORKING_DIR,
    llm_model_func=gpt_4o_mini_complete,  # Use gpt_4o_mini_complete LLM model
    graph_storage="Neo4JStorage",
    log_level="INFO",
    # llm_model_func=gpt_4o_complete  # Optionally, use a stronger model
)
#
# with open("/home/zjj/git/LEGENT/scripts/data.json") as f:
#     rag.insert(f.read())

# rag.insert("user changed his reference to avoid shiny sunlight.The method he would like to do is close the curtains")
# Perform naive search
# print(
#     rag.query("The sunlight is too shiny,can you find something to interact with to help me?give me the object's id ,give me the relationship of {in what} or {on what}", param=QueryParam(mode="naive"))
# )

# Perform local search
# print(
#     rag.query("where is my clothes?give me the clothes's id ,give me the relationship of {in what} or {on what}", param=QueryParam(mode="local"))
# )
# print(
#     rag.query("what user would like to do when the sunlight is too shiny according to the user preference??", param=QueryParam(mode="local"))
# )
# Perform global search
# print(
#     rag.query("where is my clothes??give me the clothes's id ,give me the relationship of {in what} or {on what}", param=QueryParam(mode="global"))
# )
# print(
#     rag.query("what user would like to do when the sunlight is too shiny according to the user preference?", param=QueryParam(mode="global"))
# )
# print(
#     rag.query("what user would like to do when the sunlight is too shiny according to the user preference?", param=QueryParam(mode="local"))
# )
print(
    rag.query("what object can prevent the sunlight when the sunlight is shiny?give me its object id and the relationship of {on_what} and {in_what}", param=QueryParam(mode="hybrid"))
)
# Perform hybrid search
# print(
#     rag.query("where is my clothes??give me the clothes's id ,give me the relationship of {in what} or {on what}", param=QueryParam(mode="hybrid"))
# )
# print(
#     rag.query("what user would like to do when the sunlight is too shiny according to the user preference??", param=QueryParam(mode="hybrid"))
# )