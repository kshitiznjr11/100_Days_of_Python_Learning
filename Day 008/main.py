alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceasar(plain_text, shift_amount, cipher_direction):
    cipher_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += letter
    print(f"The {cipher_direction} text is {cipher_text}.")

from ceaser_cipher import logo, goodbye
print(logo)

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    ceasar(plain_text=text, shift_amount=shift, cipher_direction=direction)
    result = input("Type 'yes' if you want to continue. Otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print(goodbye)