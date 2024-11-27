CREATE (:Article {id: '1', title: 'AI Basics', content: 'Introduction to AI...'});
CREATE (:Article {id: '2', title: 'Deep Learning', content: 'Deep learning techniques...'});
CREATE (:Article {id: '3', title: 'Graph Databases', content: 'How graph databases work...'});

CREATE (:Relationship {type: 'related_to'})
  -[:CONNECTS]->(:Article {id: '1'})
  <-[:CONNECTS]-(Article {id: '2'});
