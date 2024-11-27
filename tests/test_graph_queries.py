import unittest
from graph_db.graph_queries import GraphDatabaseHandler

class TestGraphQueries(unittest.TestCase):
    def setUp(self):
        self.db = GraphDatabaseHandler("bolt://localhost:7687", "neo4j", "password")

    def tearDown(self):
        self.db.close()

    def test_query_articles(self):
        articles = self.db.query_articles()
        self.assertGreater(len(articles), 0, "No articles returned!")

if __name__ == "__main__":
    unittest.main()
