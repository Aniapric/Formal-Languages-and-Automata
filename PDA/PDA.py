from pda_parser import load_pda

def run_pda(word, start, final_states, delta):
    # (word_index, current_state, stack)
    # The stack is represented as a tuple
    current_configurations = {(0, start, ())}
    
    # Include initial epsilon transitions
    current_configurations = explore_epsilon(current_configurations, delta)

    while current_configurations:
        next_configurations = set()
        
        for idx, state, stack in current_configurations:
            # If we reached the end of the word and we are in an accepting/final state
            if idx == len(word) and state in final_states:
                return True
            
            symbol = word[idx] if idx < len(word) else None
            
            # Try transitions consuming an input symbol
            if symbol:
                next_configurations.update(
                    transition(state, symbol, stack, idx + 1, delta)
                )
            
            # Epsilon transitions are always checked (symbol '.')
            next_configurations.update(
                transition(state, '.', stack, idx, delta)
            )
        
        # Termination condition to prevent infinite loops
        if next_configurations == current_configurations:
            break
        current_configurations = next_configurations

    return False

def transition(state, symbol, stack, next_idx, delta):
    new_configs = set()
    top = stack[-1] if stack else '.'
    
    # Check both POP cases: top symbol or ignore (.)
    for pop_symbol in [top, '.']:
        if (state, symbol, pop_symbol) in delta:
            for new_state, push_symbol in delta[(state, symbol, pop_symbol)]:
                new_stack = list(stack)
                if pop_symbol != '.':  # If popping an element, remove from stack
                    new_stack.pop()
                if push_symbol != '.':  # If pushing an element
                    new_stack.append(push_symbol)
                
                new_configs.add((next_idx, new_state, tuple(new_stack)))
    return new_configs

def explore_epsilon(configurations, delta):
    # Epsilon closure for PDA
    changed = True
    while changed:
        changed = False
        new_configs = set()
        for idx, state, stack in configurations:
            found = transition(state, '.', stack, idx, delta)
            for item in found:
                if item not in configurations:
                    new_configs.add(item)
                    changed = True
        configurations.update(new_configs)
    return configurations

# Aliases for backwards compatibility
ruleaza_pda = run_pda
tranzitie = transition
exploreaza_epsilon = explore_epsilon

if __name__ == "__main__":
    _, _, final_states, start, delta = load_pda("language.pda")
    word = input("Enter a string for PDA (e.g. 0011): ")
    result = run_pda(word, start, final_states, delta)
    
    if result:
        print(f"The string '{word}' was ACCEPTED.")
    else:
        print(f"The string '{word}' was REJECTED.")