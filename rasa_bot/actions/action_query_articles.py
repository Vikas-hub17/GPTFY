from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from neo4j import GraphDatabase

class ActionQueryArticles(Action):
    def name(self):
        return "action_query_articles"

    def run(self, dispatcher, tracker, domain):
        article_title = tracker.get_slot("article_title")

        if not article_title:
            dispatcher.utter_message(template="utter_ask_article_title")
            return []

        # Connect to Neo4j
        uri = "bolt://localhost:7687"
        driver = GraphDatabase.driver(uri, auth=("neo4j", "password"))

        def get_article(tx, title):
            query = f"MATCH (a:Article {{title: '{title}'}}) RETURN a.content AS content"
            result = tx.run(query)
            return [record["content"] for record in result]

        with driver.session() as session:
            articles = session.read_transaction(get_article, article_title)

        if articles:
            dispatcher.utter_message(template="utter_article_found", article_title=articles[0])
        else:
            dispatcher.utter_message(template="utter_no_article")

        return [SlotSet("article_title", None)]
