# Parser used to extract the automaton definition from file
# Used in both DFA.py and NFA.py to parse language definitions

def load_automaton(filename):
    alphabet = []
    states = []
    final_states = []
    initial_state = ""
    transitions = {}

    reading = False

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()

            if line == "!start!":
                reading = True
                continue
            if line == "!stop!":
                reading = False
                break  # Stop reading after !stop!

            if not reading or not line or line.startswith("!"):
                continue

            if "=" in line and "=>" not in line:
                key, value = line.split("=")
                key, value = key.strip(), value.strip()

                if key == "A":
                    alphabet = [x.strip() for x in value.split(",")]
                elif key == "Q":
                    states = [x.strip() for x in value.split(",")]
                elif key == "F":
                    final_states = [x.strip() for x in value.split(",")]
                elif key == "S":
                    initial_state = value.strip()
            
            elif "=>" in line:
                left, right = line.strip().split("=>")
                new_state = right.strip()
                
                params = left.replace("(", "").replace(")", "").split()
                if len(params) == 2:
                    source_state, symbol = params

                    key = (source_state, symbol)
                    if key not in transitions:
                        transitions[key] = []
                    
                    if new_state not in transitions[key]:
                        transitions[key].append(new_state)

    return alphabet, states, final_states, initial_state, transitions

# Alias for backwards compatibility
incarca_automat = load_automaton
