def twosComplement(num):
    onesComp="" 
    for i in num:
        if i == "0":
            onesComp += "1"
        else:
            onesComp +="0"
  
    return bin(int(onesComp,2) + int("1",2)).replace('0b',"")

n1 = int(input('Enter 1st number: '))
n2 = int(input('Enter 2nd number: '))

binaryNum1 = bin(abs(n1)).replace("0b",'')
binaryNum2 = bin(abs(n2)).replace("0b",'')

maxlen = len(binaryNum1)

binaryNum1 = binaryNum1.zfill(maxlen)
binaryNum2 = binaryNum2.zfill(maxlen + 1)

binCompn2 = twosComplement(binaryNum2)
binCompn2 = binCompn2.zfill(maxlen)

count = maxlen
m = binaryNum2
minusm = binCompn2
q = binaryNum1
a = "0"
a = a.zfill(maxlen+1)
leftshift=""

while count > 0:
    merged = a+q
    leftshift = merged[1:]
    a = leftshift[:maxlen+1]

    if a[0] == "1":
        a = bin(int(a,2)+int(m,2)).replace("0b","")
        if len(a) > maxlen+1:
            a=a[1:]
        a = a.zfill(maxlen+1)
    else:
        a = bin(int(a,2)+int(minusm,2)).replace("0b","")
        if len(a) > maxlen+1:
            a=a[1:]
        a = a.zfill(maxlen+1)
 

    leftshift = a+q[1:]

    if a[0] == "1":
        leftshift += "0"
    else:
        leftshift +="1"

    a = leftshift[:maxlen+1]
    q = leftshift[maxlen+1:]
    count -=1


if a[0] == "1":

    a = bin(int(a,2)+int(m,2)).replace("0b","")
    if len(a) > maxlen+1:
        a = a[1:]

print("remainder: " ,int(a,2))
print("quotient: ", int(q,2))

        