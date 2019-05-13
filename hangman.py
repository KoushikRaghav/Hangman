import random
no_of_turns = 5
null = ''
with open("text.txt") as f:
        answer = f.read().split()

item = random.choice(answer) 
def option_switch():
  option = int(input("\t\t\tTo start the game, press 1 \n\t\t\t\t"))
  print answer  
  if option == 1:
    play_game()
  else:
    print "\t\t\t\tBYE"

def main():
  print("\t\t\t----HANGMAN----\n")
  print("\t\t\t--WELCOME USER--\n")
  option_switch()

def play_game():
  #no_of_turns = 5
  #with open("text.txt") as f:
   #     answer = f.read().split()
  #print answer
  get_character()
  #item = random.choice(answer)  
  #print_letters(item,null)
  #null = ''
  #print_letters(item)
def print_letters(item,null):    
#  while no_of_turns > 0:
    #i = 0
 # negative = 0  
   
  #for letter in item:
      
   # if letter in null:
    #  print letter ,
       
    #else:
     #  print "_"  
    #negative += 1
  get_character()
  #win(negative)
    #get_character()  
#def win(negative):
 # if negative == 0:
  #  print "\t\t\t\t! WIN !"
  #eturn 1       
  #get_character()      
def get_character():
  while no_of_turns > 0:    
    negative = 0  
    null = ''
    for letter in item:
      
      if letter in null:
        print letter ,
       
      else:
        print "_"  
        negative += 1
    if negative == 0:
       print "\t\t\t\t! WIN !"
       break
    value = raw_input("\n\t\t\tEnter a character to guess\n\t\t\t\t")
    null += value
    if len(value) > 1: 
         print "Enter only one letter TRY AGAIN"
         break

         
    #null += value

    #if negative == 0:
     #  print "\t\t\t\t! WIN !"
      # break   

    wrong(value,no_of_turns)  
    #d = win(negative)
   # print_letters(item,null)
   # wrong(value,no_of_turns) 

def wrong(value,no_of_turns):  
  #while no_of_turns > 0:
    if value not in item:
     no_of_turns -= 1
     print "\n\t\t\t\t\t\t\t\tWrong Word"
     print +no_of_turns, " more turns"
     if no_of_turns == 0:
       print "\t\t\t  ! LOSE !"

  #return 1 





if __name__ == '__main__':
  main()

