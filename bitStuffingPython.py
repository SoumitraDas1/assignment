a='101011111111'
l=len(a)
i=0
while i<(l-5):
    if a[i:i+5]=='11111':
        a=a[:i+5]+'0'+a[i+5:]
        i+=5
    else: i+=1
print(a)