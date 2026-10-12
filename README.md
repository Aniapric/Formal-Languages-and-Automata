# Formal Languages and Automata

This repository contains the lab implementations for the Formal Languages and Automata course.

## Repository structure

The files are organized by topic:

- **`DFA_NFA/`**: Implementations of deterministic (DFA) and nondeterministic (NFA) finite automata.
- **`Grammar_Generator/`**: A language generator based on formal context-free grammars (CFG).
- **`Museum_Heist_Game/`**: An interactive terminal game based on pushdown automata logic ("Museum Heist").
- **`PDA/`**: Implementations of pushdown automata (PDA) for recognizing context-free languages.
- **`Regex/`**: A regular expression matching engine implemented manually using backtracking.
- **`Erdos_Gyarfas_Conjecture/`**: Verification script and academic paper on the Erdős–Gyárfás conjecture.

---

## 🏛️ Game Description: "Museum Heist" (PDA Game)

This game is a practical implementation of a Pushdown Automaton (PDA).

### How to Play 🎮

You are an art thief who must infiltrate a museum and escape with the stolen painting.
The game has two logical phases that follow the LIFO (Last-In, First-Out) principle:

- **Infiltration phase (PUSH)**: As you pass through the museum rooms, each room is "pushed" onto the PDA's stack. The stack keeps track of the path you have taken.
- **Escape phase (POP)**: To get out, you must go back through the same path in reverse. Leaving each room requires entering the correct password to "pop" that room off the stack. If the stack becomes empty, you have escaped successfully.

### Theoretical Concepts Implemented 📖

- **Input alphabet ($\Sigma$)**: The names of the rooms (`Claude Monet`, `Marie Curie`, `Mozart`).
- **LIFO memory**: The PDA uses a stack to force the player to follow the reverse order of the rooms visited.
- **Transition function ($\delta$)**: Each escape attempt checks whether the user's input matches the top of the stack.
- **Acceptance**: The mission is considered complete (string accepted) if and only if the stack ends up empty.
