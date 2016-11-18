print("What number would you like to multiply?")
num = int(raw_input())

multiple = 0
count = 0
while count < 1000:
	count = multiple * num
	print(str(multiple) + " times " + str(num) + " equals " + str(count))
	multiple = multiple + 1
print("Those are all of the multiples up to 1000! Have a nice day.")
