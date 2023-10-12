#python program for tranposition Cipher

def printarr2d(arr): #function to print 2D array
	for i in arr:
		print(i)

								
SenderText = input("Enter the message-> ")	#get input from sender
n  = len(SenderText)					#store the length of the SenderMessage to variable n
Aij =  []								
c = 0
while c<n:							#covert messsing string to 2D list
     m = []
     for i in range(8):
     		if c<n:
     			m.append(SenderText[c])
     			c += 1
     		else:
     			break
     Aij.append(m)
print("Message converted to 2D Array \n")
printarr2d(Aij)
print("\n")
TransposeAji = [] 

l = len(Aij)
for i in range(8):					#transposition of 2d list
	m = []
	for j in range(l):
		if i<len(Aij[j]):
			m.append(Aij[j][i])
	TransposeAji.append(m)
print("2D Array after transposition \n")
printarr2d(TransposeAji)
print("\n")
TransposeAji.sort()					#sorting the list according 0th index of each column
print("sorted 2D array \n")
printarr2d(TransposeAji)
print("\n")
cipher = ''
for i in range (len(TransposeAji)):		#covert the transposed list to string
	for j in range(len(TransposeAji[0])):
		cipher += TransposeAji[i][j]
print(f"Cipher text -> {cipher}")

'''
OUTPUT:

Enter the message-> MEGABUCKTRansFERrupees50ofromAtoB
Message converted to 2D Array

['M', 'E', 'G', 'A', 'B', 'U', 'C', 'K']
['T', 'R', 'a', 'n', 's', 'F', 'E', 'R']
['r', 'u', 'p', 'e', 'e', 's', '5', '0']
['o', 'f', 'r', 'o', 'm', 'A', 't', 'o']
['B']


2D Array after transposition

['M', 'T', 'r', 'o', 'B']
['E', 'R', 'u', 'f']
['G', 'a', 'p', 'r']
['A', 'n', 'e', 'o']
['B', 's', 'e', 'm']
['U', 'F', 's', 'A']
['C', 'E', '5', 't']
['K', 'R', '0', 'o']


sorted 2D array

['A', 'n', 'e', 'o']
['B', 's', 'e', 'm']
['C', 'E', '5', 't']
['E', 'R', 'u', 'f']
['G', 'a', 'p', 'r']
['K', 'R', '0', 'o']
['M', 'T', 'r', 'o', 'B']
['U', 'F', 's', 'A']


Cipher text -> AneoBsemCE5tERufGaprKR0oMTroUFsA
'''