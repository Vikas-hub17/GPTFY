import unittest
from rasa_sdk.executor import CollectingDispatcher
from rasa_bot.actions.action_query_articles import ActionQueryArticles

class TestRasaActions(unittest.TestCase):
    def setUp(self):
        self.dispatcher = CollectingDispatcher()
        self.tracker = {
            "get_slot": lambda slot_name: "AI Basics" if slot_name == "article_title" else None
        }
        self.domain = {}

    def test_action_query_articles(self):
        action = ActionQueryArticles()
        response = action.run(self.dispatcher, self.tracker, self.domain)
        self.assertIsInstance(response, list)
        self.assertIn("utter_article_found", str(self.dispatcher.messages))

if __name__ == "__main__":
    unittest.main()
