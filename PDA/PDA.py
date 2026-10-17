# load parser
from pda_parser import load_pda

# simulate pushdown automaton execution
def run_pda(word, start, final_states, delta):
    # current configuration: (word_index, current_state, stack_tuple)
    current_configurations = {(0, start, ())}
    
    # include initial epsilon transitions
    current_configurations = explore_epsilon(current_configurations, delta)

    while current_configurations:
        next_configurations = set()
        
        for idx, state, stack in current_configurations:
            # check word end and accepting state
            if idx == len(word) and state in final_states:
                return True
            
            symbol = word[idx] if idx < len(word) else None
            
            # transitions consuming an input symbol
            if symbol:
                next_configurations.update(
                    transition(state, symbol, stack, idx + 1, delta)
                )
            
            # epsilon transitions
            next_configurations.update(
                transition(state, '.', stack, idx, delta)
            )
        
        # termination condition to avoid loops
        if next_configurations == current_configurations:
            break
        current_configurations = next_configurations

    return False

# execute single pda transition step
def transition(state, symbol, stack, next_idx, delta):
    new_configs = set()
    top = stack[-1] if stack else '.'
    
    # check pop cases: top stack symbol or wildcard '.'
    for pop_symbol in [top, '.']:
        if (state, symbol, pop_symbol) in delta:
            for new_state, push_symbol in delta[(state, symbol, pop_symbol)]:
                new_stack = list(stack)
                # pop from stack
                if pop_symbol != '.':
                    new_stack.pop()
                # push to stack
                if push_symbol != '.':
                    new_stack.append(push_symbol)
                
                new_configs.add((next_idx, new_state, tuple(new_stack)))
    return new_configs

# explore epsilon reachability closure
def explore_epsilon(configurations, delta):
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

# backwards compatibility alias
ruleaza_pda = run_pda
tranzitie = transition
exploreaza_epsilon = explore_epsilon

if __name__ == "__main__":
    # load pda configuration
    _, _, final_states, start, delta = load_pda("language.pda")
    word = input("Enter a string for PDA (e.g. 0011): ")
    result = run_pda(word, start, final_states, delta)
    
    # print validation result
    if result:
        print(f"The string '{word}' was ACCEPTED.")
    else:
        print(f"The string '{word}' was REJECTED.")