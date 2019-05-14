import random

#Method to check for lose
def checkForLose(item, value, no_of_turns):

  if value not in item:
      no_of_turns -= 1
      print "\n\t\t\t\t\t\t\t\tWrong Word"
      print +no_of_turns, " more turns"
      if no_of_turns == 0:
        print "\t\t\t  ! LOSE !"
  return no_of_turns

#Method to get value 
def getValue():

  value = raw_input("\n\t\t\tEnter a character to guess\n\t\t\t\t")
  return value

#Method to check for win
def checkForWin(count):

  if count == 0:
    return 1 

#Method to print letters of the word
def printLetters(item, null):

  count = 0
  for letter in item:
      if letter in null:
        print letter ,
       
      else:
        print "_",  
        count += 1
  return count      

#Method to initiate game logic        
def gameFlow(answer, item, no_of_turns, null):

  while no_of_turns > 0:    
      
    count = printLetters(item,null)
    c = checkForWin(count)
    if(c == 1):
      print "\t\t\t\t! WIN !"
      break
  
    value = getValue()
    if len(value) > 1: 
            print "\t\t\tEnter only one letter"
    null += value
    no_of_turns = checkForLose(item,value,no_of_turns)     

#Method to open file contents and return array
def fileOpen():

  with open("text.txt") as f:
    answer = f.read().split()
  return answer

#Method to start the game   
def startGame():

  answer = fileOpen()
  print answer
  print "\nTotal Number of turns = 5\n"
  item = random.choice(answer) 
  #print item
  no_of_turns = 5
  null = ''
  gameFlow(answer,item,no_of_turns,null)

#Method to select options to play or exit the game
def selectOption():

  option = int(input("\t\t\tTo start the game, press 1 \n\t\t\t\t"))
  if option == 1:
    startGame()
  else:
    print "\t\t\t\tBYE"

#main method
def main():

  print("\t\t\t----HANGMAN----\n")
  print("\t\t\t--WELCOME USER--\n")
  selectOption()

if __name__ == '__main__':

  main()

