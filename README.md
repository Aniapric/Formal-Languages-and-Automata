# Formal Languages and Automata

A collection of Python implementations for formal language theory, automata models, grammars, and regular expressions, developed for the Formal Languages and Automata course at the Faculty of Mathematics and Computer Science, University of Bucharest.

## Features

- **Deterministic & Non-Deterministic Finite Automata (DFA / NFA)**: Word validation, transition parsing, and epsilon-closure reachability.
- **Context-Free Grammar Generator (CFG)**: Random recursive derivation of valid language strings from production rules.
- **Pushdown Automata (PDA)**: Stack-based automaton simulating non-deterministic context-free language acceptance.
- **Regex Matcher**: Manual regular expression engine using recursive backtracking with concatenation, alternation (`|`), and Kleene star (`*`).
- **Museum Heist (Interactive PDA Game)**: Terminal game applying LIFO stack mechanics (push on infiltration, pop with clues on escape).
- **Erdos-Gyarfas Conjecture Verification**: Empirical verification of power-of-two cycle lengths on cubic (3-regular) graphs using `networkx`.

## Repository Structure

```text
├── DFA_NFA/
│   ├── DFA.py                    # Deterministic finite automaton runner
│   ├── NFA.py                    # Non-deterministic finite automaton with epsilon closure
│   ├── automaton_parser.py       # Configuration parser for .dfa and .nfa files
│   ├── language.dfa              # Sample DFA language definition
│   └── language.nfa              # Sample NFA language definition
├── Grammar_Generator/
│   ├── generator.py              # Recursive CFG string generator
│   ├── grammar_parser.py         # Parser for .cfg grammar definitions
│   └── language.cfg              # Sample context-free grammar rules
├── PDA/
│   ├── PDA.py                    # Pushdown automaton simulator
│   ├── pda_parser.py             # Parser for .pda files
│   └── language.pda              # Sample PDA language definition
├── Regex/
│   ├── regex.py                  # Backtracking regex matching engine
│   ├── regex_parser.py           # Parser for .regex pattern files
│   └── language.regex            # Sample regular expression pattern
├── Museum_Heist_Game/
│   └── museum_heist.py           # Interactive PDA terminal game
├── Erdos_Gyarfas_Conjecture/
│   ├── experiment.py             # Empirical graph cycle verification script
│   └── Erdos_Gyarfas_Conjecture.pdf # Academic report on the conjecture
├── README.md
└── .gitignore
```

## Game Spotlight: "Museum Heist" (PDA Game)

A practical terminal game demonstrating Pushdown Automaton (PDA) mechanics.

### How to Play

You are an art thief infiltrating a museum to steal a painting and escape:
- **Infiltration phase (PUSH)**: Passing through rooms pushes each room symbol onto the PDA stack, tracking your forward route.
- **Escape phase (POP)**: Leaving requires retracing steps in exact reverse order (LIFO). Answering the trivia clue pops that room from the stack.
- **Acceptance**: Escaping with an empty stack means the input was accepted and the heist succeeded.

### Automata Concepts

- **Input alphabet ($\Sigma$)**: Room symbols (`Claude Monet`, `Marie Curie`, `Mozart`).
- **LIFO Stack Memory**: Restricts path traversal to exact reverse order.
- **Transition Function ($\delta$)**: Validates keypad input against the current stack top.
- **Acceptance Criterion**: Mission completes if and only if the stack is empty.

## Requirements

- Python 3.8+
- `networkx` (required only for `Erdos_Gyarfas_Conjecture/experiment.py`):
  ```bash
  pip install networkx
  ```

## How to Run

Execute any script directly from the repository root:

```bash
# DFA & NFA
python3 DFA_NFA/DFA.py
python3 DFA_NFA/NFA.py

# Grammar Generator
python3 Grammar_Generator/generator.py

# Pushdown Automaton
python3 PDA/PDA.py

# Regex Engine
python3 Regex/regex.py

# Museum Heist Game
python3 Museum_Heist_Game/museum_heist.py

# Erdos-Gyarfas Conjecture Verification
python3 Erdos_Gyarfas_Conjecture/experiment.py
```

## Author

- **Ania Pricop** — [@Aniapric](https://github.com/Aniapric)
- **Course**: Formal Languages and Automata
- **Faculty**: Faculty of Mathematics and Computer Science, University of Bucharest
