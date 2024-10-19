# emoji.py


from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Define color codes
COLORS = {
    "Red": Fore.RED,
    "Green": Fore.GREEN,
    "Yellow": Fore.YELLOW,
    "Blue": Fore.BLUE,
    "Magenta": Fore.MAGENTA,
    "Cyan": Fore.CYAN,
    "White": Fore.WHITE,
}

def print_colored(text, color):
    print(f"{COLORS.get(color, '')}{text}{Style.RESET_ALL}")

# Preset eye and mouth styles
eye_options = ['o', 'O', '^', '@', '-', '*', 'x', 'X']
mouth_options = ['_', '~', 'v', 'U', 'w', 'n', '口']

def main():
    print("Welcome to the Colorful Emoticon Generator!")

    while True:
        print("\nPlease choose an eye style:")
        for idx, eye in enumerate(eye_options, 1):
            print(f"{idx}. {eye}")

        eye_choice = input("Enter the number for the eye style, or input any character: ")
        if eye_choice.isdigit() and 1 <= int(eye_choice) <= len(eye_options):
            eye = eye_options[int(eye_choice) - 1]
        else:
            eye = eye_choice

        print("\nPlease choose a mouth style:")
        for idx, mouth in enumerate(mouth_options, 1):
            print(f"{idx}. {mouth}")

        mouth_choice = input("Enter the number for the mouth style, or input any character: ")
        if mouth_choice.isdigit() and 1 <= int(mouth_choice) <= len(mouth_options):
            mouth = mouth_options[int(mouth_choice) - 1]
        else:
            mouth = mouth_choice

        print("\nPlease choose a color for your emoticon:")
        for color in COLORS.keys():
            print(f"- {color}")

        color_choice = input("Enter the color name (e.g., Red), or press Enter to use the default color: ")
        color = color_choice.capitalize() if color_choice.capitalize() in COLORS else ""

        # Generate the emoticon
        face = f"""
      {eye}   {eye}
        {mouth}
"""

        # Display the emoticon
        print("\nYour emoticon is:")
        if color:
            print_colored(face, color)
        else:
            print(face)

        # Continue or exit
        cont = input("Would you like to generate another emoticon? (y/n): ")
        if cont.lower() != 'y':
            print("Thank you for using the Emoticon Generator! Goodbye!")
            sys.exit()

if __name__ == "__main__":
    main()