import random
from grammar_parser import load_cfg

# generate string recursively from grammar rules
def generate_string(rules, current_symbol):
    # terminal symbol or epsilon
    if current_symbol not in rules:
        return "" if current_symbol == "." else current_symbol
    
    # choose production randomly
    options = rules[current_symbol]
    chosen_production = random.choice(options)
    
    # recursively build generated string
    result = ""
    for symbol in chosen_production:
        result += generate_string(rules, symbol)
    
    return result

# backwards compatibility alias
genereaza_sir = generate_string

if __name__ == "__main__":
    try:
        # load grammar rules and start symbol
        rules, start = load_cfg("language.cfg")
        
        print("--- CFG Generation Results ---")
        for i in range(5):
            final_str = generate_string(rules, start)
            print(f"Derivation {i+1}: {final_str if final_str != '' else 'ε'}")
            
    except FileNotFoundError:
        print("Error: 'language.cfg' file not found!")
