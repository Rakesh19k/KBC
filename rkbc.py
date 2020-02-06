# question_list = [
# 	"How many continents are there?",  			
# 	"What is the capital of India?",			
# 	"NG mei kaun se course padhaya jaata hai?"
# ]
# options_list = [
# 	["Four", "Nine", "Seven", "Eight"],
# 	["Chandigarh", "Bhopal", "Chennai", "Delhi"],
# 	["Software Engineering", "Counseling", "Tourism", "Agriculture"]
# ]
# solution_list = [['3','seven'], ['4','delhi'], ['1','software engineering']]
# _50_50=[
# 	["3 . Seven","4 . Eight"],
# 	["1 . Chandigarh","4 . Delhi"],
# 	["1 . Software Engineering","4 . Agriculture"]
# ]
# use_5050=0
# print ("-------------------Welcome to my KBC game-----------------")
# print ("        ---------------Badal Doshanjh-------------        ")
# for i in range(len(question_list)):
# 	counter=0
# 	print ("aapke question hai:-", question_list[i])
# 	print ("aapka options hai:-")
# 	for j in range(len(options_list[i])):
# 		print(j+1,".",options_list[i][j])
# 	if use_5050==2:
# 		print ("you have all ready use 5050 chance!")
# 		print ("you don't have 5050 chance!")
# 		pass
# 	else:
# 		user1=input("you want to 5050 yes or not/ : ")
# 		for c in range(len(_50_50[i])):	
# 			if user1 in "yes":
# 				print (_50_50[i][c])
# 				use_5050+=1
# 			if user1 in "not":
# 				print ("okay! No problem as your wish.")
# 				break	
# 	user=input("choose your options:").lower()
# 	for k in range(len(solution_list)):
# 		if user in solution_list[i]:
# 			print ("aapka answer sahi hai")
# 			break
# 		else:
# 			print ("aapka answer galat hai")
# 			print ("aap game se bahar kr diy gy hai")
# 			counter+=1
# 			break
# 	if counter==1:
# 		break
# else:
# 	print ("congratulation! you win this game.")
