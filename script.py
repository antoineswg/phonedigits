import pyperclip
import sys

def encrypt(input):
    mapping = {
        'a': '2', 'à': '2', 'â': '2', 'ä': '2', 'b': '22', 'c': '222', 'ç': '222',
        'd': '3', 'e': '33', 'é': '33', 'è': '33', 'ê': '33', 'ë': '33', 'f': '333',
        'g': '4', 'h': '44', 'i': '444', 'î': '444', 'ï': '444',
        'j': '5', 'k': '55', 'l': '555',
        'm': '6', 'n': '66', 'o': '666', 'ô': '666', 'ö': '666',
        'p': '7', 'q': '77', 'r': '777', 's': '7777',
        't': '8', 'u': '88', 'ù': '88', 'û': '88', 'ü': '88', 'v': '888',
        'w': '9', 'x': '99', 'y': '999', 'z': '9999',
        ' ': '0', 'œ': '666 33',
        '0': '00', '1': '01', '2': '02', '3': '03', '4': '04', '5': '05', '6': '06', '7': '07', '8': '08', '9': '09'
    }
    output = []
    lines = input.split('\n')
    for line in lines:
        line_output = []
        for index, char in enumerate(line):
            if char.lower() in mapping:
                line_output.append(mapping[char.lower()] + ' ')
            else:
                next_char = index + 1
                if next_char < len(line) and line[next_char].lower() in mapping:
                    line_output.append(char + ' ')
                else:
                    line_output.append(char)
        output.append("".join(line_output).rstrip())
    return "\n".join(output)


def decrypt(input):
    mapping = {
        '2': 'a', '22': 'b', '222': 'c',
        '3': 'd', '33': 'e', '333': 'f',
        '4': 'g', '44': 'h', '444': 'i',
        '5': 'j', '55': 'k', '555': 'l',
        '6': 'm', '66': 'n', '666': 'o',
        '7': 'p', '77': 'q', '777': 'r', '7777': 's',
        '8': 't', '88': 'u', '888': 'v',
        '9': 'w', '99': 'x', '999': 'y', '9999': 'z',
        '0': ' ',
        '00': '0', '01': '1', '02': '2', '03': '3', '04': '4', '05': '5', '06': '6', '07': '7', '08': '8', '09': '9'
    }
    output = []
    lines = input.split('\n')
    for line in lines:
        tokens = line.split()
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token in mapping:
                output.append(mapping[token])
            else:
                output.append(token)
            i += 1
        output.append('\n')
    if output and output[-1] == '\n':
        output.pop()
    return "".join(output)

def multiple_lines_support(invite):
    print("Une fois le texte prêt, retournez à la ligne, puis appuyez sur Ctrl+D (MacOS) ou Ctrl+Z (Windows) et appuyez sur Entrée.")
    print(invite)
    return sys.stdin.read().strip()


mode = input("Déchiffrer (D) ou Chiffrer (C) ? ").lower()
if mode == "d":
    text_input = multiple_lines_support("Texte à déchiffrer : ")
    result = decrypt(text_input)
    state = "tudo bem"
elif mode == "c":
    text_input = multiple_lines_support("Texte à chiffrer : ")
    result = encrypt(text_input)
    state = "tudo bem"
else:
    error = "Nuh uh, faut choisir D ou C :zaga:"
    state = "L reader"


if state == "tudo bem":
    print ("Résultat : ", result)
    if input("Copier le résultat (Y/N) ? ").lower() == "y":
        pyperclip.copy(result)
        print("Résultat copié dans le presse papier :+1: :aga:")
elif state == "L reader":
    print(error)