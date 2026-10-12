# Parser for regular expression configuration files

def load_regex(filename):
    regex_pattern = ""
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

            # The first valid line after !start! is considered the regex pattern
            regex_pattern = line
            break 
            
    return regex_pattern

# Alias for backwards compatibility
incarca_regex = load_regex
