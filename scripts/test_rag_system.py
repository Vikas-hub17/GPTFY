import time
from rasa_sdk.executor import CollectingDispatcher
from graph_db.graph_queries import GraphDatabaseHandler

db = GraphDatabaseHandler("bolt://localhost:7687", "neo4j", "password")

def test_query():
    start_time = time.time()
    results = db.query_articles()
    end_time = time.time()
    print("Results:", results)
    print(f"Query Time: {end_time - start_time:.4f} seconds")

test_query()
