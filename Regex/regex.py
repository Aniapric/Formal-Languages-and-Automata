# load parser
from regex_parser import load_regex

# manual regex matching using recursive backtracking
def match_regex_manual(pattern, word):
    # base case: empty regex accepts empty word
    if not pattern:
        return not word
        
    # base case: single character or wildcard dot
    if len(pattern) == 1:
        return len(word) == 1 and (pattern == '.' or pattern == word)

    # top-level alternation split on '|'
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

    # extract first token: group in parentheses or single character
    if pattern[0] == '(':
        level = 0
        for i, c in enumerate(pattern):
            if c == '(':
                level += 1
            elif c == ')':
                level -= 1
            if level == 0:
                break
        
        if level != 0:
            i = len(pattern) - 1
            
        element = pattern[1:i]
        rest_pattern = pattern[i+1:]
    else:
        element = pattern[0]
        rest_pattern = pattern[1:]

    # check kleene star on token
    has_star = False
    if rest_pattern and rest_pattern[0] == '*':
        has_star = True
        rest_pattern = rest_pattern[1:]

    # matching logic with recursion
    if has_star:
        # zero occurrences of star element
        if match_regex_manual(rest_pattern, word):
            return True
            
        # one or more occurrences
        for i in range(1, len(word) + 1):
            if match_regex_manual(element, word[:i]) and match_regex_manual(pattern, word[i:]):
                return True
        return False
        
    else:
        # single match concatenation
        for i in range(1, len(word) + 1):
            if match_regex_manual(element, word[:i]) and match_regex_manual(rest_pattern, word[i:]):
                return True
        return False

if __name__ == "__main__":
    try:
        # load regex from file
        regex = load_regex("language.regex")
        test_str = input(f"Test regex [{regex}]: ")
        
        # print match result
        if match_regex_manual(regex, test_str):
            print("YES - Accepted")
        else:
            print("NO - Rejected")
    except FileNotFoundError:
        print("Error: Missing language.regex file!")