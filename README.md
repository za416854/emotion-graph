# emotion-graph
 Python + Neo4j + Hugging Face minimum viable project



# Before starts project
pip install transformers neo4j
or 
pip install -r requirements.txt

create a neo4j database 

run python backend/app.py
then go to postman

choose POST => http://127.0.0.1:8080/analyze 
data: baby => raw =>
{
  "text": "she is a good person!",
  "user_id": "tester01"
}

the result we can see the how confident the feedback is positive or negative then we can analyse the data!