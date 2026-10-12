from automaton_parser import load_automaton

def run_dfa(word, start, final_states, delta):
    current_state = start
    
    for symbol in word:
        key = (current_state, symbol)

        if key in delta:
            current_state = delta[key][0]
        else:
            return False
            
    return current_state in final_states

# Alias for backwards compatibility
ruleaza_dfa = run_dfa

if __name__ == "__main__":
    alphabet, states, final_states, start, delta = load_automaton("language.dfa")
    
    word = input("Enter a string to test with DFA: ")
    result = run_dfa(word, start, final_states, delta)
    
    if result:
        print(f"The string '{word}' was ACCEPTED.")
    else:
        print(f"The string '{word}' was REJECTED.")