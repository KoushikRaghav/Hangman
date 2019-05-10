import random
def switch():
	option = int(input("\t\t\tTo start the game, press 1 \n\t\t\t\t"))
	if option == 1:
		game()
	else:
		print "\t\t\t\tBYE"
		

def main():
	print("\t\t\t----HANGMAN----\n")
	print("\t\t\t--WELCOME USER--\n")
	switch()

def game():
	no_of_turns = 5
 	with open("text.txt") as f:
    		answer = f.read().split()
 	print answer
 	null = ''
 		
 	while no_of_turns > 0:
 		i = 0
 		negative = 0
 		
 		for letter in answer[i]:
 			
 			if letter in null:
 				print letter ,
 				
 			else:
 				print "_"	 
 				negative += 1
 					
 		if negative == 0:
 			print "\t\t\t\t! WIN !"
 			break

 		value = raw_input("\n\t\t\tEnter a character to guess\n\t\t\t\t")
 		
 		if len(value) > 1: 
        		print "Enter only one letter TRY AGAIN"
        		break
        #else:
 		null += value
 		if value not in answer[i]:
 			no_of_turns -= 1
 			print "\n\t\t\t\t\t\t\t\tWrong Word"
 			print +no_of_turns, " more turns"
 			if no_of_turns == 0:
 				print "\t\t\t  ! LOSE !"

if __name__ == '__main__':
	main()

