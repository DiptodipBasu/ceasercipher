import math
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(digit,text):
    cipher=""
    for i in text:
        pos=letters.index(i)
        new=(pos+digit)%26
        new_letter=letters[new]
        cipher+=new_letter
    print(cipher)
def decrypt(digit,text):
    cipher=""
    for i in text:
        pos=letters.index(i)
        new=(pos-digit)%26
        new_letter=letters[new]
        cipher+=new_letter
    print(cipher)
print("What do you want to do : ")
print("1.Encrypt")
print("2.Decrypt")
x=int(input("Enter choice : "))
if x==1:
    text=input("Type your message : ").lower()
    digit=int(input("Type the shift number : "))
    encrypt(digit,text)
elif x==2:
    text=input("Type your message : ").lower()
    digit=int(input("Type the shift number : "))
    decrypt(digit,text)
else:
    print("Invalid Option")