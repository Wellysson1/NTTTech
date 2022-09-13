def caesar(data, key, encrypted=True):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_data = ''
    for c in data:
        index = alphabet.find(c)
        if index == -1:
            new_data += c
        else:
            new_index = index + key if encrypted else index - key
            new_index = new_index % len(alphabet)
            new_data += alphabet[new_index]
    return new_data


key = int(input("Digite a sua chave: "))
original = input("Digite a sua frase: ")
ciphered = caesar(original, key)
print('Encriptada:', ciphered)

decriptar = input("Você deseja decriptar a mensagem? (1)Yes (2)No")

if decriptar == "1":
    plain = caesar(ciphered, key, False)
    print('Decriptada:', plain)
