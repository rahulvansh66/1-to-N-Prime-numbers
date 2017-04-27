#prime number from 1 to N

a = raw_input("How many prime number you want? : ")
a=int(a)
count=0
num =1

for num in range(1, 1000):
	if (count > a-1):
		break
	if num>1:
		for i in range(2, num):
			if(num%i)==0:
				break
		else:
			print(num)
			count += 1
