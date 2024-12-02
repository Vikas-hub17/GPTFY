from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher
from graph_db.spanner_schema import SpannerSchema
from graph_db.neo4j_connection import Neo4jConnection

class ActionQuerySpannerArticles(Action):
    def name(self):
        return "action_query_spanner_articles"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain):
        connection = Neo4jConnection(uri="bolt://localhost:7687", user="neo4j", password="password")
        schema = SpannerSchema(connection)
        articles = schema.query_articles()
        dispatcher.utter_message(text=f"Available articles: {', '.join(articles)}")
        connection.close()
        return []
