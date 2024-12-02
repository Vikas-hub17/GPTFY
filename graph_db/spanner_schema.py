from .neo4j_connection import Neo4jConnection

class SpannerSchema:
    def __init__(self, connection):
        self.connection = connection

    def create_schema(self):
        query = """
        CREATE (:Article {id: '1', title: 'AI Basics', content: 'Introduction to AI'})
        CREATE (:Article {id: '2', title: 'Graph Databases', content: 'Introduction to Neo4j'})
        """
        self.connection.query(query)

    def query_articles(self):
        query = "MATCH (a:Article) RETURN a.title AS title"
        return [record["title"] for record in self.connection.query(query)]
