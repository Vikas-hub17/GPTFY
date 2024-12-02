from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher
from graph_db.rag_schema import RAGSchema
from graph_db.neo4j_connection import Neo4jConnection

class ActionQueryRAGDocuments(Action):
    def name(self):
        return "action_query_rag_documents"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain):
        connection = Neo4jConnection(uri="bolt://localhost:7687", user="neo4j", password="password")
        schema = RAGSchema(connection)
        documents = schema.query_documents()
        dispatcher.utter_message(text=f"Available documents: {', '.join(documents)}")
        connection.close()
        return []