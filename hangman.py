import random

def fileOpen():
  with open("text.txt") as f:
    answer = f.read().split()
  return answer
  
def selectOption():
  option = int(input("\t\t\tTo start the game, press 1 \n\t\t\t\t"))
  answer = fileOpen()
  print answer
  item = random.choice(answer)  
  #print item
  if option == 1:
    playGame(answer,item)
  else:
    print "\t\t\t\tBYE"

def main():
  print("\t\t\t----HANGMAN----\n")
  print("\t\t\t--WELCOME USER--\n")
  selectOption()

def playGame(answer,item):
  no_of_turns = 5
  null = ''
  getInput(answer,item,no_of_turns,null)
        
def getInput(answer,item,no_of_turns,null):

  while no_of_turns > 0:    
    negative = 0  
    
    for letter in item:
      
      if letter in null:
        print letter ,
       
      else:
        print "_",  
        negative += 1

    if negative == 0:
       print "\t\t\t\t! WIN !"
       break

    value = raw_input("\n\t\t\tEnter a character to guess\n\t\t\t\t")
    
    if len(value) > 1: 
         print "Enter only one letter TRY AGAIN"
         break

    null += value     
    if value not in item:
      no_of_turns -= 1
      print "\n\t\t\t\t\t\t\t\tWrong Word"
      print +no_of_turns, " more turns"
      if no_of_turns == 0:
        print "\t\t\t  ! LOSE !"

if __name__ == '__main__':
  main()

