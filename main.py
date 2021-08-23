# import random
# def swertres(wager, number):
# 	result = random.randint(1,999)
	
# 	res_str = str(result)
# 	bet_str = str(number)
# 	print(res_str)
# 	if number == result:
# 		return wager * 80
# 	elif res_str == bet_str:
# 		return (wager/6) * 80
# 	else:
# 		print("No win")
# 		return 0
	
# swertres(321, 8)

s1 = str(123)
s2 = str(12)
set1 = s1.split(" ")
set2 = s2.split(" ")
# while len(set2) < 3:
# 	set2.insert(0, 0)
print(set1)
print(set2)
print(set1 == set2)