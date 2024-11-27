from neo4j import GraphDatabase

def load_data(uri, user, password):
    driver = GraphDatabase.driver(uri, auth=(user, password))

    def add_articles(tx):
        tx.run(
            """
            CREATE (:Article {id: '1', title: 'AI Basics', content: 'Introduction to AI.'});
            CREATE (:Article {id: '2', title: 'Deep Learning', content: 'Deep learning concepts.'});
            CREATE (:Article {id: '3', title: 'Graph Databases', content: 'Graph databases explained.'});
            CREATE (:Relationship {type: 'related_to'})
              -[:CONNECTS]->(:Article {id: '1'})<-[:CONNECTS]-(Article {id: '2'});
            """
        )

    with driver.session() as session:
        session.write_transaction(add_articles)

    driver.close()

load_data("bolt://localhost:7687", "neo4j", "password")
