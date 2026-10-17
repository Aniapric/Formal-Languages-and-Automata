# load parser
from automaton_parser import load_automaton

# simulate dfa execution
def run_dfa(word, start, final_states, delta):
    current_state = start
    
    # process each symbol
    for symbol in word:
        key = (current_state, symbol)

        # transition to next state
        if key in delta:
            current_state = delta[key][0]
        else:
            return False
            
    # check acceptance
    return current_state in final_states

# backwards compatibility alias
ruleaza_dfa = run_dfa

if __name__ == "__main__":
    # load dfa definition
    alphabet, states, final_states, start, delta = load_automaton("language.dfa")
    
    # read input string
    word = input("Enter a string to test with DFA: ")
    result = run_dfa(word, start, final_states, delta)
    
    # print validation result
    if result:
        print(f"The string '{word}' was ACCEPTED.")
    else:
        print(f"The string '{word}' was REJECTED.")