def isprime(myNum):
	for num in range(2,myNum):
		if myNum % num == 0:
			return False
	return True

print("Welcome to primeLister.py this program will print out the prime numbers from 2 to 10,000")
list = []
for number in range(2,10001):
	p = isprime(number)
	if p == True:
		list.append(number)

my_file = open("prime.txt", "w") 
my_file.write(str(list))
my_file.close()
print(list)
 
