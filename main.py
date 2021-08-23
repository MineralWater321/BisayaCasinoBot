import random
def swertres(wager, number):
	result = random.randint(1,999)
	number_list = list(str(number))
	result_list = list(str(result))
	print("The result is " + str(result))
	while len(number_list) < 3:
		number_list.insert(0, 0)
	while len(result_list) < 3:
		result_list(0, 0)
	if number == result:
		return wager * 80
	elif number_list == result_list:
		return (wager/6) * 80
	else:
		print("No win")
		return 0
	
swertres(321, 8)