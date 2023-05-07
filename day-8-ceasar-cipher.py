alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
array = []
count = 0
cipher_array = []
cipher_text = ""
#ODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, n_shift):
    for letter in plain_text:
        array.append(alphabet.index(letter) + n_shift)
    for n in range(0,len(array)):
            if array[n] > 25:
                array[n] = array[n] % 26
    for n in array:
        cipher_array.append(alphabet[n])
    cipher_text = "".join(cipher_array)
    print(f"The encoded text is {cipher_text}")

if direction == "encode":
    encrypt(text, shift)
    #ODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#ODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.