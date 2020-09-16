import pyttsx3

engine = pyttsx3.init()


engine.setProperty("volume",5.0)
engine.setProperty("rate",125)

question_list = [
	"How many continents are there?",  			
	"What is the capital of India?",			
	"NG mei kaun se course padhaya jaata hai?"
]
options_list = [
	["Four", "Nine", "Seven", "Eight"],
	["Chandigarh", "Bhopal", "Chennai", "Delhi"],
	["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]
solution_list = [['3','seven'], ['4','delhi'], ['1','software engineering']]
_50_50=[
	["3 . Seven","4 . Eight"],
	["1 . Chandigarh","4 . Delhi"],
	["1 . Software Engineering","4 . Agriculture"]
]
use_5050=0
print ("-------------------Welcome to my KBC game-----------------")
engine.say("Welcome to my KBC game")
engine.runAndWait()
print ("        ---------------Badal Doshanjh-------------        ")
engine.say("Badal Doshanjh")
engine.runAndWait()
for i in range(len(question_list)):
	counter=0
	print ("aapke question hain:-", question_list[i])
	engine.say("aapka question hain", question_list[i])
	engine.runAndWait()
	print ("aapka options hain:-")
	engine.say("aapka options hain")
	engine.runAndWait()
	for j in range(len(options_list[i])):
		print (j+1,".",options_list[i][j])
		engine.say(j+1, options_list[i][j])
		engine.runAndWait()
	if use_5050==2:
		print ("you have all ready use 5050 chance!")
		engine.say("you have all ready use 50 50 chance")
		engine.runAndWait()
		print ("you don't have 5050 chance!")
		engine.say("you don't have 50 50 chance")
		engine.runAndWait()
		pass
	else:
		engine.say("you want to 50 50 yes or not")
		engine.runAndWait()
		user1=input("you want to 5050 yes or not : ")
		for c in range(len(_50_50[i])):	
			if user1 in "yes":
				print (_50_50[i][c])
				engine.say(_50_50[i][c])
				engine.runAndWait()
				use_5050+=1
			elif user1 in "not":
				print ("okay! No problem as your wish.")
				engine.say("okay! No problem as your wish")
				engine.runAndWait()
				break
	engine.say("choose your options")
	engine.runAndWait()
	user=input("choose your options:").lower()
	for k in range(len(solution_list)):
		if user in solution_list[i]:
			print ("aapka answer shi hain")
			engine.say("aapka answer shi hain")
			engine.runAndWait()
			break
		else:
			print ("aapka answer galat hain")
			engine.say("aapka answer galat hain")
			engine.runAndWait()
			print ("aap game se bahar kr diy gy hain")
			engine.say("aap game se bahar kr diy gy hain")
			engine.runAndWait()
			counter+=1
			break
	if counter==1:
		break
else:
	print ("congratulation! you won this game.")
	engine.say("congratulation you won this game")
	engine.runAndWait()
