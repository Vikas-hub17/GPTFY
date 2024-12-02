from graph_db.neo4j_connection import Neo4jConnection
from graph_db.spanner_schema import SpannerSchema

def test_spanner_system():
    connection = Neo4jConnection(uri="bolt://localhost:7687", user="neo4j", password="password")
    schema = SpannerSchema(connection)
    schema.create_schema()
    articles = schema.query_articles()
    print(f"Articles in Spanner-like graph: {articles}")
    connection.close()

if __name__ == "__main__":
    test_spanner_system()