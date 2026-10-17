# parse context-free grammar from file

def load_cfg(filename):
    rules = {}
    start_symbol = ""
    reading = False

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            # toggle section reading
            if line == "!start!":
                reading = True
                continue
            if line == "!stop!":
                reading = False
                break
            
            # skip comments and empty lines
            if not reading or not line or line.startswith("!"):
                continue

            # parse production rule
            if "->" in line:
                left, right = line.split("->")
                variable = left.strip()
                production = right.strip().split()
                
                if variable not in rules:
                    rules[variable] = []
                rules[variable].append(production)
                
            # parse start symbol
            elif "=" in line:
                key, val = line.split("=")
                if key.strip() == "S":
                    start_symbol = val.strip()
    
    return rules, start_symbol

# backwards compatibility alias
incarca_cfg = load_cfg
