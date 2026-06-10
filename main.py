import os
from rdflib import Graph
from queries import q1, q2, q3, q4, q5, q6, q7, q8

def run_main():

    base_dir = os.path.dirname(os.path.abspath(__file__))
    ttl_file = os.path.join(base_dir, "data", "publications.ttl")
    
    g = Graph()
    
    if not os.path.exists(ttl_file):
        print(f"Error: Could not find '{ttl_file}'.")
        return

    print(f"Loading {ttl_file}...")
    g.parse(ttl_file, format="turtle")
    
    queries = [
        ("Q1", q1()), ("Q2", q2()), ("Q3", q3()), ("Q4", q4()),
        ("Q5", q5()), ("Q6", q6()), ("Q7", q7()), ("Q8", q8())
    ]
    
    for name, query in queries:
        print(f"\n--- {name} Results ---")
        try:
            results = g.query(query)
            
            if name == "Q5": # ASK query
                for row in results:
                    print(f"Result: {row}")
            elif name == "Q6": # CONSTRUCT query
                print(f"Total triples in result: {len(results)}")
            else: # SELECT queries
                count = 0
                for row in results:
                    print(row)
                    count += 1
                    if count >= 5: 
                        break
                if count == 0:
                    print("No results found.")
        except Exception as e:
            print(f"Error executing {name}: {e}")

if __name__ == "__main__":
    run_main()