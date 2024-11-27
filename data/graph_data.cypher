CREATE (:Article {id: '1', title: 'AI Basics', content: 'Introduction to Artificial Intelligence and its applications.'});
CREATE (:Article {id: '2', title: 'Deep Learning', content: 'Exploring neural networks and deep learning concepts.'});
CREATE (:Article {id: '3', title: 'Graph Databases', content: 'Understanding how graph databases like Neo4j work.'});

CREATE (:Relationship {type: 'related_to'})-[:CONNECTS]->(:Article {id: '1'})<-[:CONNECTS]-(Article {id: '2'});
