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
    return ''.join(output)


text_input = input("Texte à chiffrer : ")
result = encrypt(text_input)
pyperclip.copy(result)
print ("Résultat : ", result)
print("Résultat copié dans le presse papier :+1: :aga:")