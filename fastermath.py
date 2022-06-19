import sys, random

def numgen(x):
	urut = 0
	numlist = []
	while urut < int(x):
		a = random.randint(0,9)
		numlist.append(str(a))
		urut = urut + 1
	return ''.join(numlist)

def operator(x):
	a = x.replace("-m","*").replace("-a","+").replace("-s","-").replace("-d","/")
	return str(a)
try:
	if sys.argv[1] == "-d":
		print("Coming soon!")
		quit()

	if (sys.argv[2]).isdigit():
		num1 = numgen(sys.argv[2])
		num2 = numgen(sys.argv[2])
		myans = input(f"{num1} {operator(sys.argv[1])} {num2} = ")
		if len(myans) == 0:
			myans = "0"
		ans = int(eval(str(int(num1))+operator(sys.argv[1])+str(int(num2))))
		if int(myans) == ans:
			print("Jawaban benar!")
		else:
			print(f"Jawaban salah! Hasilnya {ans}")
			 
except Exception as e:
	print(e)
	print("Error")
