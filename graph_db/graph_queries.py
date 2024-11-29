from neo4j import GraphDatabase

class GraphDatabaseHandler:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def query_articles(self):
        with self.driver.session() as session:
            return session.read_transaction(self._query_articles)

    @staticmethod
    def _query_articles(tx):
        query = "MATCH (a:Article) RETURN a.title AS title"
        result = tx.run(query)
        return [record["title"] for record in result]

# Usage
db = GraphDatabaseHandler("bolt://localhost:7687", "neo4j", "12345678")
articles = db.query_articles()
print("Articles:", articles)
db.close()
