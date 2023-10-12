#Python program for substitution cipher
key =  2
senderText = input("Enter the message:- ")
ciphertext = ''
for i in senderText:
	ciphertext += chr(ord(i)+2)
print(f"Cipher Text = {ciphertext}")

'''
OUTPUT:
Enter the message:- ac35
Cipher Text = ce57
'''