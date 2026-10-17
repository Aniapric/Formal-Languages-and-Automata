# load parser
from automaton_parser import load_automaton

# compute epsilon closure for states
def epsilon_closure(initial_states, delta):
    closure = set(initial_states)
    
    while True:
        new_states = set()
        for state in closure:
            if (state, '.') in delta:
                for neighbor in delta[(state, '.')]:
                    if neighbor not in closure:
                        new_states.add(neighbor)
       
        # stop when no new states are reached
        if not new_states:
            break
       
        closure.update(new_states)
        
    return closure

# simulate nfa execution
def run_nfa(word, start, final_states, delta):
    # initial states including epsilon closure
    current_states = epsilon_closure({start}, delta)
    
    # process input symbols
    for symbol in word:
        next_states = set()
        
        for s in current_states:
            if (s, symbol) in delta:
                for dest in delta[(s, symbol)]:
                    next_states.add(dest)
       
        current_states = epsilon_closure(next_states, delta)
        
        # reject early if no active states remain
        if not current_states:
            return False
    
    # check if any current state is accepting
    for s in current_states:
        if s in final_states:
            return True
            
    return False

# backwards compatibility alias
ruleaza_nfa = run_nfa

if __name__ == "__main__":
    # load nfa definition
    alphabet, states, final_states, start, delta = load_automaton("language.nfa")
    word = input("Enter a string for NFA: ")
    
    # test acceptance
    result = run_nfa(word, start, final_states, delta)
    if result:
        print(f"The string '{word}' was ACCEPTED.")
    else:
        print(f"The string '{word}' was REJECTED.")