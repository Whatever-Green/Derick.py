# Say hello to derrick the worlds lamest man on earth
import sys
import random

def script():
	print("let derrick help you with life:")
	print("")
	print("Just Keep Running The Script Again And Again Till You Get Bored Or Your Mum Calles You Down For Dinner.")
	
	
	x = "           "
	print("\n")

	print(str(x) + "------------------------------")

	items = [
	"Can I be a human?",
	"“I figured something out. The future is unpredictable. \n" "― John Green, An Abundance of Katherines",
	"I pooped on my dog in line at the bank because I'm NOT crazy.",
	"Don't you need a license to be that ugly?",
	"You've a face like a million dollars - all green and wrinkled.",
	"If you're talking about me behind my back, that just means my life is obviously more interesting than yours. ",
	"Do ants poop?",
	"Craig is a weird name",
	"every stick comes with 2 balls",
	"I am feeling sad today cause its raining in some part of the world",
	"So people think that the world is round which is a stupid judgement",
	"I yelled at a snowman in my car because my family thinks I'm stupid anyway.",
	"I didn't attend the funeral, but I sent a nice letter saying I approved of it. - mark twain",
	"The wheel is turning but the hamster is definitely dead.",
	"I'm new in town. Can I have the directions to your house please?",
	"I sang to a stuffed animal in an elevator because I had a vision from God.",
	"if rocks could speak what would they say?"

	]
	random_item = random.choice(items)
	print(str(x) + random_item)
	# print (random.choice([q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11]))
	derrick1 = str(x) + """ -----------------------------	
				0
			0
		0
	cCcCcCcCcCc
	|0	0|
	|    7	 |
	| -----|
	--   ^  --- """
	derrick2 = str(x) + """ -----------------------------	
				0
			0
		0
	cCcCcCcCcCc
	|^	^|
	|    7	 |
	| -----|
	--   ^  --- """
	derrick3 = str(x) + """ -----------------------------	
				0
			0
		0
	cCcCcCcCcCc
	|D	D|
	|    7	 |
	| xxxxx|
	--   ^  --- """
	print (random.choice([derrick1, derrick2, derrick3]))

	print("\n")
	
script()

def judgement():
	answer = input("Want More? y/n: " ) 
	if answer == "y": 
		script()
	elif answer == "n": 
		print("Derick Wishes You A Good Day @_@")
		exit()
	else: 
		print("Answer the bloody question!!!!!: ") 

q = 1
while q < 6:
	judgement()

# Enjoy playing around with this script like i did so with it. 
# By Whatever Green (WG) http://whatevergreen.cf
