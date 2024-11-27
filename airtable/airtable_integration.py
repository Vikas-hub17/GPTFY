from pyairtable import Table

class AirtableHandler:
    def __init__(self, api_key, base_id, table_name):
        self.table = Table(api_key, base_id, table_name)

    def log_result(self, query, response_time, system_type):
        self.table.create({
            "Query": query,
            "Response Time": response_time,
            "System": system_type
        })

# Usage
airtable = AirtableHandler("your_api_key", "your_base_id", "RAG Results")
airtable.log_result("Retrieve AI Basics", "0.45s", "Graph-RAG")
