print("How much was your total purchase in cents?")
purchase = int(raw_input())
purchase_discount = purchase * 10 - purchase 

if purchase > 1000: 
	print("You spent over $10! Your final price is" + str ( purchase_discount))
