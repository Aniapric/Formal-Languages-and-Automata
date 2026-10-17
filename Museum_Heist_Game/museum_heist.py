import time
import os

# Clear the terminal screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Interactive enter prompt for user experience
def wait_for_enter(message="[ Press ENTER to continue... ]"):
    input(f"\n  {message}")

# Typewriter text effect with delay
def print_slow(text, delay=0.04):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# ascii art drawings

# Draw museum facade
def draw_museum_front():
    print(r"""
   🕵️  <-- you

         -----------------------------
        |     NATIONAL ART MUSEUM     |
        |   -----   -----   -----     |
        |   |   |   |   |   | 🖼️ |     |
        |   -----   -----   -----     |
        |                             |
        -----------[ door ]------------
    """)

# Draw character at entrance
def draw_entrance():
    print(r"""
         -----------------------------
        |     NATIONAL ART MUSEUM     |
        |   -----   -----   -----     |
        |   |   |   |   |   | 🖼️ |     |
        |   -----   -----   -----     |
        |         --> 🕵️ <--           |
        -----------[ door ]------------
    """)

# Draw room progression towards the painting
def draw_room(room_number, total_rooms):
    displayed_rooms = ""
    for i in range(1, total_rooms + 1):
        if i < room_number:
            displayed_rooms += " [✓]    "
        elif i == room_number:
            displayed_rooms += " [🕵️]   "
        else:
            displayed_rooms += " [ ]    "

    print(f"""
        -----------------------------
        |     NATIONAL ART MUSEUM     |
        |   -----   -----   -----     |
        |   |   |   |   |   | 🖼️ |     |
        |   -----   -----   -----     |
        |   {displayed_rooms:<40}
        -----------[ door ]------------
    """)

# Draw stolen painting
def draw_stolen_painting():
    print(r"""
         -----------------------------
        |     NATIONAL ART MUSEUM     |
        |   -----   -----   -------   |
        |   |   |   |   |   | 🖼️ 🕵️ |   |
        |   -----   -----   -------   |
        |                             |
        -----------[ door ]------------
    """)

# Draw reverse room traversal for escape
def draw_escape(remaining_rooms, total_rooms):
    displayed_rooms = ""
    for i in range(1, total_rooms + 1):
        if i < remaining_rooms:
            displayed_rooms += " [🔒]   "   # Rooms not yet cleared
        elif i == remaining_rooms:
            displayed_rooms += "[🕵️]   "   # You are here
        else:
            displayed_rooms += " [✓]    "   # Rooms already cleared

    print(f"""
        -----------------------------
        |     NATIONAL ART MUSEUM     |
        |   -----   -----   -----     |
        |   |   |   |   |   | ❌ |     |
        |   -----   -----   -----     |
        |   {displayed_rooms:<40}
        -----------[ door ]------------
    """)

def draw_escaped():
    print(r"""
   🕵️💨 <-- you escaped!

        +------------------------------------------+
        |           NATIONAL ART MUSEUM            |
        |   🚔🚔 police arriving... too late!      |
        +------------------------------------------+
    """)

# game phases

# Introductory story
def intro():
    clear()
    print("=" * 50)
    print("       🏛️  MUSEUM HEIST  🏛️")
    print("=" * 50)
    wait_for_enter()

    clear()
    print_slow("\n  It's midnight. The city is asleep.")
    time.sleep(0.3)
    print_slow("  For months you have studied the museum's blueprints.")
    time.sleep(0.3)
    print_slow("  Today is the big day.\n")
    wait_for_enter()

    clear()
    print_slow("  You are standing in front of the museum...")
    time.sleep(0.4)
    draw_museum_front()
    print_slow("  You must make your way through three doors 🚪.")
    print_slow("  To escape, you will have to retrace your steps in reverse.")
    wait_for_enter("[ Press ENTER to begin infiltration... ]")

# Infiltration phase (PUSH)
# The automaton sequentially pushes symbols from the stack alphabet into its LIFO memory.
def infiltration_phase(stack, museum_rooms):
    clear()
    print("\n🏛️  --- PHASE 1: INFILTRATION  --- 🏛️\n")
    time.sleep(0.5)

    print_slow("  Sneaking through the back door...")
    wait_for_enter()

    clear()
    print_slow("  You reached the main entrance...")
    draw_entrance()
    wait_for_enter()

    for i, room in enumerate(museum_rooms):
        stack.append(room)  # Push transition: add symbol to PDA stack
        clear()
        print_slow(f"  Sneaking into room 👣 {i + 1}...")
        time.sleep(0.3)
        print_slow(" Security bypassed! The door locks behind you. [🔓]")
        draw_room(i + 1, len(museum_rooms))
        wait_for_enter()

    clear()
    print_slow("  You found the painting. 🖼️ ")
    time.sleep(0.5)
    print_slow("  Taking it off the wall...")
    time.sleep(0.6)
    draw_stolen_painting()
    print_slow("  You must escape through the EXACT route you came in!")
    wait_for_enter("[ Press ENTER to begin escape... ]")

# Escape phase (POP)
def escape_phase(stack, security):
    clear()
    print("\n🏃  --- PHASE 2: ESCAPE  --- 🏃\n")
    time.sleep(0.4)
    print_slow("  Each door has a security keypad.")
    print_slow("  Read the clue and enter the correct password.\n")
    time.sleep(0.3)

    total_rooms = len(stack)

    while stack:
        # Read the top of the stack without removing it yet
        current_room = stack[-1]
        clue = security.get(current_room, "No clue available.")

        draw_escape(len(stack), total_rooms)

        print(f"  Keypad locked! 🔐")
        print(f"  Clue 💡: {clue}")
        # Read word from input tape (Input alphabet Sigma)
        answer = input("  Password ⌨️: ")

        # Transition function: verify if input matches the top of the stack
        if answer.strip().lower() == current_room.lower():
            # Accepted transition -> execute POP
            stack.pop()
            clear()
            print(" Correct! The door unlocked. ✅ \n")
            time.sleep(0.6)
        else:
            clear()
            print("\n WRONG! ")
            time.sleep(0.3)
            print_slow(" The police caught you. Game over. 🚓 ")
            return False

    clear()
    draw_escaped()
    time.sleep(0.3)
    # Acceptance by empty stack
    print_slow("  Mission accomplished! 🏆 \n")
    return True

# Aliases for backwards compatibility
asteapta_enter = wait_for_enter
tipareste_incet = print_slow
deseneaza_fata_muzeu = draw_museum_front
deseneaza_intrare = draw_entrance
deseneaza_sala = draw_room
deseneaza_tablou_furat = draw_stolen_painting
deseneaza_evadare = draw_escape
deseneaza_evadat = draw_escaped
faza_infiltrare = infiltration_phase
faza_evadare = escape_phase

# main entry point
if __name__ == "__main__":
    security = {
        "Claude Monet": "He was obsessed with how light changes throughout the day and painted hundreds of variations of the same subject, the famous 'Water Lilies' in his Giverny garden.",
        "Marie Curie": "Discovered two new chemical elements that glowed in the dark. She is the only person in history with Nobel Prizes in two distinct sciences.",
        "Mozart": "Composed over 600 works before passing away suddenly at just 35 years old. His final masterpiece, the famous 'Requiem', was left unfinished on his deathbed."
    }

    pda_stack = []
    rooms = ["Claude Monet", "Marie Curie", "Mozart"]  # Input alphabet of the PDA

    intro()
    infiltration_phase(pda_stack, rooms)
    escape_phase(pda_stack, security)
