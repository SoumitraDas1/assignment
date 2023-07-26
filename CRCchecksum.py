'''
Python program for CRC checksum
Code written by Soumitra Das
'''

def GeneratorPolyToBits(polynomial,power): #function for convert polynomial to bits
  divisor = ''
  x1=['x','1']
  for i in range(power,1,-1): #this for loop append bits to divisor string upto x2
    i=str(i)
    if i in polynomial: # '1' bit appended if x^i present in the polynomial
      divisor+='1'
    else:
      divisor+='0' #'0' bit appended if x^i not present 
  for i in x1: #this for loop check x and 1 in the polynomial 
    if i in polynomial:
      divisor+='1'
    else:
      divisor+='0'
  return divisor
def _0bits(power): #function for creating string of 0 bits 
  bits=''
  for i in range(power):
    bits+='0'
  return bits

def crcChecksum(dividend,divisor,bits0): # function for calculate checksum
  remainder=''
  dividendLength=len(dividend) # total number of bits in dividend
  divisorLength=len(divisor) #total number of bits in divisor
  def subtractUsingXor(Dividend,Divisor): #function for subtracting using XOR operator
    result = bin(int(Dividend,2)^int(Divisor,2)) #converting binary string to integer and perform XOR operation. Then again convert the result to binray string
    result=_0bits(divisorLength-(len(result)-2)-1)+result[2:] # adding '0' bits to match divisor length
    return result
  Divd=dividend[0 : divisorLength-1] # declare and initialize Divd variable to get bits dividend. Total no of bits is 1 less than divisor length 
  for i in range(0,dividendLength -  divisorLength + 1):
    Divd += dividend[i+divisorLength-1] #appending 1 bits per iteration to matchup divisorLength
    if Divd[0]=='1': #if 1st bit of Divd is 1 then perform XOR with divisor * 1
      remainder = subtractUsingXor(Divd,divisor) #calling the function 
    else:
      remainder = subtractUsingXor(Divd,bits0) # if 1st bit is 0 then perform XOR with divisor * 0
    Divd = remainder #assing remainder value to Divd variable 

  return remainder #funtion returns CRC checksum bits string


if __name__ == '__main__':
  GeneratorPolynomial = input('Enter the polynomial ... (ex.. x5 + x4 + x3 ..... + 1 --> ') # getting polynomial user input 
  power=int(input('Enter the max power of the polynomial --> ')) # polynomial maximum power user input in integer 
  divisor = GeneratorPolyToBits(GeneratorPolynomial,power) #calling function 
  FrameBits=input('Enter Frame bits--> ') #frame Bits user input 
  bits0= _0bits(power) #calling function for creating '0' bits string
  dividend=FrameBits + bits0 # appending '0' bits with Framebits 
  CRCchecksum=crcChecksum(dividend,divisor,bits0) #calling function 
  print('CRC checksum is --> ', CRCchecksum)
