# Parser for Pushdown Automaton (PDA) configuration files

def load_pda(filename):
    alphabet, states, final_states, start = [], [], [], ""
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
                break
            if not reading or not line or line.startswith("!"):
                continue

            if "=" in line and "=>" not in line:
                key, val = line.split("=")
                key, val = key.strip(), val.strip()
                if key == "A":
                    alphabet = [x.strip() for x in val.split(",")]
                elif key == "Q":
                    states = [x.strip() for x in val.split(",")]
                elif key == "F":
                    final_states = [x.strip() for x in val.split(",")]
                elif key == "S":
                    start = val
            
            elif "=>" in line:
                left, right = line.split("=>")
                # Clean parentheses: (q1 0 .) -> ["q1", "0", "."]
                p_in = left.replace("(", "").replace(")", "").split()
                p_out = right.replace("(", "").replace(")", "").split()
                
                if len(p_in) == 3 and len(p_out) == 2:
                    key = (p_in[0], p_in[1], p_in[2])  # (state, char, pop)
                    value = (p_out[0], p_out[1])        # (new_state, push)
                    
                    if key not in transitions:
                        transitions[key] = []
                    transitions[key].append(value)

    return alphabet, states, final_states, start, transitions

# Alias for backwards compatibility
incarca_pda = load_pda
