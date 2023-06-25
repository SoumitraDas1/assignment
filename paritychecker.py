def paritychecker(pkt):		
	print(pkt[:-1].count('1'),pkt[-1])
	if ((pkt[:-1].count('1'))%2==0 and pkt[-1]!='0') or ((pkt[:-1].count('1'))%2!=0 and pkt[-1]=='0'):
		print("ERROR")	#if the number of 1's is even in data bits and parity bit is not 0 then False
		return False	#or if the number of 1's is odd in data bits and parity bit is 0 then also False
	else:
		print("ACCEPTED")	#if data bits have even no of 1's and parity bit is 0 then return True
		return True			#of if data bits have odd no of 1's and parity bit is 1 then also Ture
if __name__ == "__main__":
	message = '11001100'	# 0th index bit is parity bit 
	paritychecker(message)