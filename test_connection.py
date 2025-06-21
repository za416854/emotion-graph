from neo4j import GraphDatabase

driver = GraphDatabase.driver("bolt://127.0.0.1:7687", auth=("neo4j", "11111111"))

try:
    driver.verify_connectivity()
    print("✅ 成功連上 Neo4j")
except Exception as e:
    print("❌ 錯誤：", e)

