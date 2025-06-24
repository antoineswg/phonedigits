import pyperclip

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
        ' ': '0', 'œ': '666 33'
    }
    output = []
    for index, char in enumerate(input):
        if char.lower() in mapping:
            output.append(mapping[char.lower()] + ' ')
        else:
            next_char = index + 1
            if next_char < len(input) and input[next_char].lower() in mapping:
                output.append(char + ' ')
            else:
                output.append(char)
    return "".join(output)


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
        '0': ' '
    }
    output = []
    tokens = input.strip().split()
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token in mapping:
            output.append(mapping[token])
            i += 1
        else:
            output.append(token)
            i += 1
    return "".join(output)


mode = input("Déchiffrer (D) ou Chiffrer (C) ? ").lower()
if mode == "d":
    text_input = input("Texte à déchiffrer : ")
    result = decrypt(text_input)
    state = "tudo bem"
elif mode == "c":
    text_input = input("Texte à chiffrer : ")
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