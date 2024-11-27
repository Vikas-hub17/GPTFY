import matplotlib.pyplot as plt

def visualize_results(data):
    queries = [entry["Query"] for entry in data]
    times = [float(entry["Response Time"].replace("s", "")) for entry in data]
    systems = [entry["System"] for entry in data]

    for system in set(systems):
        system_data = [(q, t) for q, t, s in zip(queries, times, systems) if s == system]
        plt.bar(
            [q for q, _ in system_data],
            [t for _, t in system_data],
            label=system
        )

    plt.xlabel("Queries")
    plt.ylabel("Response Time (seconds)")
    plt.title("RAG Systems Performance Comparison")
    plt.legend()
    plt.show()

# Example Data
test_data = [
    {"Query": "Retrieve AI Basics", "Response Time": "0.45s", "System": "Graph-RAG"},
    {"Query": "Retrieve AI Basics", "Response Time": "0.60s", "System": "Traditional RAG"}
]
visualize_results(test_data)
