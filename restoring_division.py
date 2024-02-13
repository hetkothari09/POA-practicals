def twosComplement(num):
    onesComp="" 
    for i in num:
        if i == "0":
            onesComp += "1"
        else:
            onesComp +="0"
  
    return bin(int(onesComp,2) + int("1",2)).replace('0b',"")

n1 = int(input('Enter Dividend: '))



n2 = int(input('Enter Divisor: '))

binNum1 = bin(abs(n1)).replace("0b",'')
binNum2 = bin(abs(n2)).replace("0b",'')

maxlen = len(binNum1)

binNum1 = binNum1.zfill(maxlen)
binNum2 = binNum2.zfill(maxlen + 1)

binCompNum2 = twosComplement(binNum2)
binCompNum2 = binCompNum2.zfill(maxlen)


count = maxlen
m = binNum2
minusm = binCompNum2
q = binNum1
a = "0"
a = a.zfill(maxlen+1)

leftshift=""
print("The table for the restoring algorithm is as follow:")
while count > 0:
    print("n \t M \t A \t Q ")

    print(count,"\t",m,"\t",a,"\t",q)

    merged = a+q
    leftshift = merged[1:]



    a = leftshift[:maxlen+1]

    a = bin(int(a,2)+int(minusm,2)).replace("0b","")
    if len(a) > maxlen+1:
        
        a=a[1:]
    a = a.zfill(maxlen+1)

    if a[0] == "0":
        leftshift = a+q[1:]
        leftshift += "1"
    else:
        a = bin(int(a,2)+int(m,2)).replace("0b","")
        if len(a) > maxlen+1:
            a=a[1:]
        a = a.zfill(maxlen+1)
        leftshift = a+q[1:]
        leftshift += "0"

    a = leftshift[:maxlen+1]
    q = leftshift[maxlen+1:]
    count -=1
    
print("n \t M \t A \t Q ")


print(count,"\t",m,"\t",a,"\t",q)


print("Remainder",int(a,2))
print("Quotient",int(q,2))