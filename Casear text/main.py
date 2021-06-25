import string

plain_text = "jgnnq yqtnf"
shift = 26-7
shift %=26

alphabet = string.ascii_lowercase

shifted = alphabet[shift:] + alphabet[:shift]

table = str.maketrans(alphabet, shifted)
encripted = plain_text.translate(table)

print(encripted)