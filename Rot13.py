"""
DESCRIPTION:
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
"""
def rot13(message):
    char={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}
    final=""
    for i in message:
        if i.lower() not in "abcdefghijklmnopqrstuvwxyz":
            final+=i
        else:
            if 26-char[i.lower()] < 13:
                value=13-(26-char[i.lower()])
            else:
                value=char[i.lower()]+13
            if i.islower():
                final+=list(char.keys())[list(char.values()).index(value)]
            else:
                final+=list(char.keys())[list(char.values()).index(value)].upper()
    return final