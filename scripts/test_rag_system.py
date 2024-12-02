from graph_db.neo4j_connection import Neo4jConnection
from graph_db.rag_schema import RAGSchema

def test_rag_system():
    connection = Neo4jConnection(uri="bolt://localhost:7687", user="neo4j", password="password")
    schema = RAGSchema(connection)
    schema.create_schema()
    documents = schema.query_documents()
    print(f"Documents in Traditional RAG: {documents}")
    connection.close()

if __name__ == "__main__":
    test_rag_system()