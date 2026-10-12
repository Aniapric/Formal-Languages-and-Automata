from regex_parser import load_regex

def match_regex_manual(pattern, word):
    # Base case for empty strings (Acceptance)
    if not pattern:
        return not word
        
    # Base case for a single character in regex
    if len(pattern) == 1:
        return len(word) == 1 and (pattern == '.' or pattern == word)

    # Isolate alternation '|' only at the top level (not inside parentheses)
    parts = []
    level = 0
    current = ""
    for c in pattern:
        if c == '(':
            level += 1
        elif c == ')':
            level -= 1
        
        if c == '|' and level == 0:
            parts.append(current)
            current = ""
        else:
            current += c
    parts.append(current)
    
    if len(parts) > 1:
        return any(match_regex_manual(p, word) for p in parts)

    # Extract the first token (single character or parenthesized block)
    if pattern[0] == '(':
        level = 0
        for i, c in enumerate(pattern):
            if c == '(':
                level += 1
            elif c == ')':
                level -= 1
            if level == 0:
                break
        
        # If parentheses are not properly balanced
        if level != 0:
            i = len(pattern) - 1
            
        element = pattern[1:i]  # Exclude outer parentheses
        rest_pattern = pattern[i+1:]
    else:
        element = pattern[0]
        rest_pattern = pattern[1:]

    # Check if the token is followed by Kleene star (*)
    has_star = False
    if rest_pattern and rest_pattern[0] == '*':
        has_star = True
        rest_pattern = rest_pattern[1:]

    # Apply matching logic and advance recursively
    if has_star:
        # Branch A: Ignore star element (0 occurrences)
        if match_regex_manual(rest_pattern, word):
            return True
            
        # Branch B: Consume one match of the element and keep the star (+1 occurrences)
        for i in range(1, len(word) + 1):
            if match_regex_manual(element, word[:i]) and match_regex_manual(pattern, word[i:]):
                return True
        return False
        
    else:
        # Without star: look for a single match (Concatenation)
        for i in range(1, len(word) + 1):
            if match_regex_manual(element, word[:i]) and match_regex_manual(rest_pattern, word[i:]):
                return True
        return False

if __name__ == "__main__":
    try:
        regex = load_regex("language.regex")  # Read regex from file
        test_str = input(f"Test regex [{regex}]: ")
        
        if match_regex_manual(regex, test_str):
            print("YES - Accepted")
        else:
            print("NO - Rejected")
    except FileNotFoundError:
        print("Error: Missing language.regex file!")