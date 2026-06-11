import argparse
import sys
import json
from SPARQLWrapper import SPARQLWrapper, JSON, TURTLE

from queries import q1, q2, q3, q4, q5, q6, q7, q8

DISPATCHER = {
    "list-authors": q1,
    "papers-per-topic": q2,
    "top-5-cited": q7,
    "hinton-matches": q8,
    "check-data": q5,  
    "construct-2023": q6 
}

def execute_query(intent):
    query_func = DISPATCHER.get(intent)
    if not query_func:
        print(f"Error: Unknown intent '{intent}'.")
        print(f"Supported intents: {', '.join(DISPATCHER.keys())}")
        sys.exit(1)
    
    sparql = SPARQLWrapper("http://localhost:3030/publications/sparql")
    sparql.setQuery(query_func())
    
    if "CONSTRUCT" in query_func().upper():
        sparql.setReturnFormat(TURTLE)
    else:
        sparql.setReturnFormat(JSON)
        
    return sparql.query().convert()

def main():
    parser = argparse.ArgumentParser(description="SPARQL CLI Dispatcher")
    parser.add_argument("intent", help="Natural language intent to dispatch")
    args = parser.parse_args()
    
    result = execute_query(args.intent)
    print(result)

if __name__ == "__main__":
    main()
