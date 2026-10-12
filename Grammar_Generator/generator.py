# Function that generates strings from grammar rules

import random
from grammar_parser import load_cfg

def generate_string(rules, current_symbol):
    # If the symbol does not appear on the LHS of any rule, it is TERMINAL
    if current_symbol not in rules:
        # '.' represents the empty string (epsilon)
        return "" if current_symbol == "." else current_symbol
    
    # Choose a production randomly
    options = rules[current_symbol]
    chosen_production = random.choice(options)
    
    # Recursively build the string
    result = ""
    for symbol in chosen_production:
        result += generate_string(rules, symbol)
    
    return result

# Alias for backwards compatibility
genereaza_sir = generate_string

if __name__ == "__main__":
    try:
        rules, start = load_cfg("language.cfg")  # Grammar rules loaded from language.cfg
        
        print("--- CFG Generation Results ---")
        for i in range(5):  # Limit to 5 derivations
            final_str = generate_string(rules, start)
            print(f"Derivation {i+1}: {final_str if final_str != '' else 'ε'}")
            
    except FileNotFoundError:
        print("Error: 'language.cfg' file not found!")
