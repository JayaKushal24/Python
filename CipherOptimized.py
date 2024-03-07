letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
text=input("Enter your message\n").lower()
shift=int(input("enter the shift number\n"))
direction=input("type'e' to encrypt or 'd' to deccrypt\n").lower() 
def decrypt_encrypt(text,shift,direction):
    cypher_text=''
    for i in text:
        old_position=letters.index(i)
        if direction=="e":
            new_position=old_position+shift
            if new_position>len(letters):
                new_position-=len(letters)
        elif direction=="d":
            new_position=old_position-shift
        new_letter=letters[new_position]
        cypher_text+=new_letter
    print(f"the new Message is :\t{cypher_text}")
if (direction !="d") and (direction!="e"):
    print("INVALID ENTRY")
else:
    decrypt_encrypt(text,shift,direction)