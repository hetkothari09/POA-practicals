def add(ac, x, qrn):
	c = 0
	for i in range(qrn): 
		
		# updating accumulator with A = A + BR
		ac[i] = ac[i] + x[i] + c;
		
		if (ac[i] > 1):
			ac[i] = ac[i] % 2
			c = 1
		
		else:
			c = 0

def complement(a, n):
	x = [0] * 8
	x[0] = 1
	
	for i in range(n):
		a[i] = (a[i] + 1) % 2
	add(a, x, n)


def rightShift(ac, qr, qn, qrn):

	temp = ac[0]
	qn = qr[0]
	
	print("\t\trightShift\t", end = "");
	
	for i in range(qrn - 1):
		ac[i] = ac[i + 1]
		qr[i] = qr[i + 1]

	
	qr[qrn - 1] = temp


def display(ac, qr, qrn):

	# accumulator display
	for i in range(qrn - 1, -1, -1):
		print(ac[i], end = '')
	print("\t", end = '')

	# multiplier display
	for i in range(qrn - 1, -1, -1):
		print(qr[i], end = "")


def boothAlgorithm(br, qr, mt, qrn, sc):

	qn = 0
	ac = [0] * 10
	temp = 0
	print("qn\tq[n+1]\t\tBR\t\tAC\tQR\t\tsc")
	print("\t\t\tinitial\t\t", end = "")
	
	display(ac, qr, qrn)
	print("\t\t", sc, sep = "")
	
	while (sc != 0):
		print(qr[0], "\t", qn, sep = "", end = "")
		
		if ((qn + qr[0]) == 1):
		
			if (temp == 0):
				
				add(ac, mt, qrn)
				print("\t\tA = A - BR\t", end = "")
				
				for i in range(qrn - 1, -1, -1):
					print(ac[i], end = "")

				temp = 1
			
			
			elif (temp == 1):
			
				add(ac, br, qrn)
				print("\t\tA = A + BR\t", end = "")
				
				for i in range(qrn - 1, -1, -1):
					print(ac[i], end = "")
				temp = 0
			
			print("\n\t", end = "")
			rightShift(ac, qr, qn, qrn)
		
		elif (qn - qr[0] == 0):
			rightShift(ac, qr, qn, qrn)
		
		display(ac, qr, qrn)
		
		print("\t", end = "")
		
		sc -= 1
		print("\t", sc, sep = "")


def main():

	mt = [0] * 10
	brn = 4
	br = [ 0, 1, 1, 0 ]
	for i in range(brn - 1, -1, -1):
		mt[i] = br[i]
	
	br.reverse()

	complement(mt, brn)
	qrn = 4
	sc = qrn
	
	qr = [ 1, 0, 1, 0 ]
	qr.reverse()

	boothAlgorithm(br, qr, mt, qrn, sc)
	
	print("\nResult = ", end = "")

	for i in range(qrn - 1, -1, -1):
		print(qr[i], end = "")
	print()
		
main()
