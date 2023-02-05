# Dictionary to find Morse equivalent of given characters
morse_dict = {'a': '._', 'b': '_...', 'c': '_._.', 'd': '_..', 'e': '.', 'f': '.._.', 'g': '__.', 'h': '....',
              'i': '..', 'j': '.___', 'k': '_._', 'l': '._..', 'm': '__', 'n': '_.', 'o': '___', 'p': '.__.',
              'q': '__._', 'r': '._.', 's': '...', 't': '_', 'u': '.._', 'v': '..._', 'w': '.__', 'x': '_.._',
              'y': '_.__', 'z': '__..', '0': '_____', '1': '.____', '2': '..___', '3': '...__', '4': '...._',
              '5': '.....', '6': '_....', '7': '__...', '8': '___..', '9': '____.', ' ': ' ', '.': '._._._',
              ',': '__..__', '?': '..__..', "'": '.____.', ':': '___...', '/': '_.._.'}


# Functions to convert a given text to morse code and vice-versa


def text_to_morse(text: str = None):
    morse_list = [morse_dict[char] for char in text]
    morse_code = '   '.join(morse_list)
    return morse_code


def morse_to_text(code: str = None):
    morse_list = code.split('   ')
    morse_list = [m.strip() for m in morse_list]
    while '' in morse_list:
        morse_list[morse_list.index('')] = ' '
    text_list = [list(morse_dict.keys())[list(morse_dict.values()).index(morse)] for morse in morse_list]
    text_list[0] = text_list[0].upper()
    text = ''.join(text_list)
    return text


# The program loop for user interaction
running = True
print('Welcome to "Text to Morse" program.')
print("You can enter your text or Morse code to get it's parallel counterpart.")
print('To quit, please type "!quit" in the prompt.')
print("This program accepts only alphanumeric, space and standard punctuation(.,?':/) characters for text, "
      "and . and _ with 3 spaces inbetween characters for morse code!")

while running:
    content = input('Enter your text here: ').lower()

    # Checks for empty strings
    if content == '':
        pass

    # Checks for user's request to quit program
    elif content == '!quit':
        running = False
        print('Thank you for using my program.')
        print('Goodbye!!')

    # Checks the given Morse code according to program's standards
    elif all(char in ('.', '_', ' ') for char in content):
        try:
            print(morse_to_text(content))
        except ValueError:
            print('Please provide 3 spaces in between character codes!')

    # Checks the given text according to program's standards
    elif all(char.isalnum() or char.isspace() or char in ['.', ',', '?', "'", ':', '/'] for char in content):
        print(text_to_morse(content))

    # Reminds the program's syntax and standards
    else:
        print("This program accepts alphanumeric, space and standard punctuation(.,?':/) characters for text, "
              "and . and _ for morse code ONLY!!!")
        print('Please try again.')
