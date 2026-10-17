# parse regular expression configuration from file

def load_regex(filename):
    regex_pattern = ""
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

            # first valid line contains regex pattern
            regex_pattern = line
            break 
            
    return regex_pattern

# backwards compatibility alias
incarca_regex = load_regex
