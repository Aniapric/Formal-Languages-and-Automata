from automaton_parser import load_automaton

def epsilon_closure(initial_states, delta):
    closure = set(initial_states)
    
    while True:
        new_states = set()
        for state in closure:
            if (state, '.') in delta:
                for neighbor in delta[(state, '.')]:
                    if neighbor not in closure:
                        new_states.add(neighbor)
       
        if not new_states:
            break
       
        closure.update(new_states)
        
    return closure

def run_nfa(word, start, final_states, delta):
    current_states = epsilon_closure({start}, delta)
    
    for symbol in word:
        next_states = set()
        
        for s in current_states:
            if (s, symbol) in delta:
                for dest in delta[(s, symbol)]:
                    next_states.add(dest)
       
        current_states = epsilon_closure(next_states, delta)
        
        if not current_states:
            return False
    
    for s in current_states:
        if s in final_states:
            return True
            
    return False

# Aliases for backwards compatibility
ruleaza_nfa = run_nfa

if __name__ == "__main__":
    alphabet, states, final_states, start, delta = load_automaton("language.nfa")
    word = input("Enter a string for NFA: ")
    
    result = run_nfa(word, start, final_states, delta)
    if result:
        print(f"The string '{word}' was ACCEPTED.")
    else:
        print(f"The string '{word}' was REJECTED.")