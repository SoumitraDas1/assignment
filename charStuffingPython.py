sf='p'	#start flag
ed='$'	#end delimiter
signal='abc$efg#$mno'
i=0
n=len(signal)
while i<n:
	if signal[i]==ed or signal[i]=='#':		#if any char is eqal to end delimiter then append '#'
		signal=signal[:i]+'#'+signal[i:]	#and if char is equal to '#' then append one more '#'
		i+=1
	i+=1
signal=sf+signal							#adding the start flag to signal 
print(signal)
#output:  pabc#$efg###$mno
