"""
DESCRIPTION:
Implement a pseudo-encryption algorithm which given a string S and an integer N concatenates all the odd-indexed characters of S with all the even-indexed characters of S, this process should be repeated N times.

Examples:

encrypt("012345", 1)  =>  "135024"
encrypt("012345", 2)  =>  "135024"  ->  "304152"
encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"

encrypt("01234", 1)  =>  "13024"
encrypt("01234", 2)  =>  "13024"  ->  "32104"
encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"
Together with the encryption function, you should also implement a decryption function which reverses the process.

If the string S is an empty value or the integer N is not positive, return the first argument without changes.
"""
def decrypt(encrypted_text, n):
    text=encrypted_text
    t1=encrypted_text
    len_en=0 if encrypted_text==None else len(encrypted_text)
    a=n
    while n>0:
        i=0
        text=""
        while i < len(encrypted_text)//2:
            text+=encrypted_text[i+(len(encrypted_text)//2)]
            text+=encrypted_text[i]
            i+=1
        n-=1
        encrypted_text=text
    return encrypted_text+t1[-1] if (len_en%2!=0 and a >0) else encrypted_text      

def encrypt(text, n):
    while n > 0:
        even=''.join([text[i] for i in range(len(text)) if i%2==0])
        odd=''.join([text[i] for i in range(len(text)) if i%2!=0])
        text=odd+even
        n-=1
    return text 