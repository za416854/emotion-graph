from neo4j import GraphDatabase

# 替換成你自己的本地 Neo4j 密碼
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "11111111"

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

def create_user_sentiment(user_id, text, sentiment_label):
    with driver.session() as session:
        session.write_transaction(_create_nodes_and_relationships, user_id, text, sentiment_label)

def _create_nodes_and_relationships(tx, user_id, text, sentiment_label):
    tx.run("""
        MERGE (u:User {id: $user_id})
        MERGE (s:Sentiment {label: $sentiment_label})
        MERGE (t:Text {content: $text})
        MERGE (u)-[:WROTE]->(t)
        MERGE (t)-[:HAS_SENTIMENT]->(s)
    """, user_id=user_id, text=text, sentiment_label=sentiment_label)
