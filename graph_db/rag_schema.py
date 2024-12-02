from .neo4j_connection import Neo4jConnection

class RAGSchema:
    def __init__(self, connection):
        self.connection = connection

    def create_schema(self):
        query = """
        CREATE (:Document {id: '1', title: 'Deep Learning', content: 'Details on deep learning'})
        CREATE (:Document {id: '2', title: 'Data Science', content: 'Basics of data science'})
        """
        self.connection.query(query)

    def query_documents(self):
        query = "MATCH (d:Document) RETURN d.title AS title"
        return [record["title"] for record in self.connection.query(query)]