from pyairtable import Table

api_key = "your_airtable_api_key"
base_id = "your_base_id"
table_name = "RAG Results"

table = Table(api_key, base_id, table_name)

def log_test_result(query, response_time, system_type):
    table.create({
        "Query": query,
        "Response Time": response_time,
        "System": system_type
    })

log_test_result("Retrieve AI Basics", "0.45s", "Graph-RAG")
