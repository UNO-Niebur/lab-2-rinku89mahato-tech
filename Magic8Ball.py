#Magic8Ball.py
#Name: Rinku Mahato
#Date: 01/31/2026
#Assignment: Lab2 
#Purpose: ask user for their question and response receives randomly from created list. 

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  response = ["Yes", "No.", "I don't know", "May be", "Very doubtful"]
  #Prompt the user for their question.
  question = input("Do you know AI? ")
  #Answer question randomly with one of the options from your earlier list.
  length = len(response)
  r = random.random()* length
  r = int(r)
  print(r) # int value

  response_1 = response[r]
  print(response_1)


if __name__ == '__main__':
  main()
