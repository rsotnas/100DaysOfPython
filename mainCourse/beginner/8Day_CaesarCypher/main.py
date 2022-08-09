import art

print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


# TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
# e.g.
# plain_text = "hello"
# shift = 5
# cipher_text = "mjqqt"
# print output: "The encoded text is mjqqt"
def encrypt(plain_text, shift):
    cipher_text = ''
    for l in plain_text:
        position = alphabet.index(l)
        new_position = position + shift
        while new_position >= len(alphabet):
            alphabet.extend(alphabet)
        cipher_text += alphabet[new_position]
    print(f'The encoded text is {cipher_text}')


# TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

# TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
# e.g.
#cipher_text = "mjqqt"
#shift = 5
#plain_text = "hello"
# print output: "The decoded text is hello"
def decrypt(cipher_text, shift):
    plain_text = ''
    for l in cipher_text:
        position = alphabet.index(l) - shift
        new_position = position
        if new_position < 0:
            new_position *= -1
        while new_position >= len(alphabet):
            alphabet.extend(alphabet)
        plain_text += alphabet[position]
    print(f'The decoded text is {plain_text}')


# TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'direction' variable. You should be able to test the code to encrypt *AND* decrypt a message.

if direction == 'encode':
    encrypt(plain_text=text, shift=shift)
else:
    decrypt(cipher_text=text, shift=shift)
