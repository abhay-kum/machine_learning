
import random

greeting=["hii","Hii","Hello","hey","Hey","hello"]
greeting_response=["how can i help you ?","what can I do for you?","what do you want to know?"]

question=["how is weather today?","How is the weather'?","how is the weather in ","Is it going to rain today?","it is sunshine?"]


q_answer=["i think today, it is good for roaming around the city","It seems it is cloudy today","Be careful may raining today","It's cloudy","Its clear sky","Its hot ","Bitterly cold in ","some smoke in ","hot in","no! it is not rainy today","it may be  take a umberella with you","it is a clear sky no need to worry about"," yeah it will be heavily raining today","yes it is sunshine and clear sky","no may be storm will come be aware","chill out no worry go and enjoy your day"]


some_other=["okay","fine","that's great","wow that's good to hear","okay, no problem","thank you","you are good","good to talk with you"]
some_other_response=["it's my pleasure having a great time with you","that my pleasure to help you","thank you and wish you the same","thats cool","you are amazing"]

bye=["okay bye","bye","good bye","talk to you later","talk to u later","nice to meet you"]
bye_response=["okay bye","Bye,take care","Bye, have a great time with you","okay bye, no problem","okay bye, meet u again"]

print("======== Welcome to weather Bot ======== ")
#print("======== what can I do for you?  ======== ")


while True:
	inp=input(">>")

		
	if inp in greeting:
		print( random.choice(greeting)+",  "+random.choice(greeting_response)+"\n")

	elif inp in question:
		
		for i in range(0,len(question)):
			if (question[i] == inp):
				j=3*i
				print("\n"+random.choice(q_answer[j:j+3])+"\n")
				break
	elif inp in some_other:
		print("\n"+random.choice(some_other_response) +"\n")

	elif " in " in inp:
		data=inp.split("in")
		for i in range(0,len(question)):
			if "in" in question[i]:
				j=3*i
				print("\n"+random.choice(q_answer[j:j+3])+" "+data[1]+"\n")
				break
	elif inp in bye:
		print("\n"+random.choice(bye_response)+"\n")
		break
		
	else:
	    print("\nsorry i can't understand please connect later")
	    break

				


