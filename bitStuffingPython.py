signal='101011111111'
l=len(signal)   #counting the total bits in signal
i=0
while i<(l-5):
    if signal[i:i+5]=='11111':                  #if we get continuous five 1's 
        signal=signal[:i+5]+'0'+signal[i+5:]    # then we append a '0' after that
        i+=5                                    #and increase the i pointer to 5
    else: i+=1      #else increase the i pointer to 1
print(signal)
#output 1010111110111
