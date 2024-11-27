import unittest
from graph_db.graph_queries import GraphDatabaseHandler
from rasa_bot.actions.action_query_articles import ActionQueryArticles

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.db = GraphDatabaseHandler("bolt://localhost:7687", "neo4j", "password")

    def tearDown(self):
        self.db.close()

    def test_rasa_neo4j_integration(self):
        articles = self.db.query_articles()
        self.assertGreater(len(articles), 0, "No articles retrieved from Neo4j")

if __name__ == "__main__":
    unittest.main()
