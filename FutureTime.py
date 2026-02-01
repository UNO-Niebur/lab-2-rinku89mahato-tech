#FutureTime.py
#Name: Rinku Mahato
#Date: 01/31/2026
#Assignment: Lab 2
# Calcaute future - hours , minute and time by adding moreminutes to user inputs to hours and minuts,

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  #print(now)
  currentHour = (now.hour - 6) % 24
  currentMinute = now.minute

  #print (f"currentHour: {currentHour} , currentMinute: {currentMinute}") #this is just for checking,

  #calculating more minuts and hours from moreminutes
  moreminute = 20

  futureminute = (currentMinute + moreminute) % 60
  extraHour = (currentMinute + moreminute) // 60

  #print(f"futureminute: {futureminute}")
  #print(f"extraHour: {extraHour}")

  ####TODO:
  #Ask user for hours
  inputhours = int(input("enter hours:"))
  #Ask user for minutes
  inputminutes = int(input("enter minutes:"))

  ####Calculate the time after the user-supplied time has passed.

  new_min = (inputminutes + futureminute) % 60
  
  #print(f"new future minute: {new_min}")

  new_extra_hour = (inputminutes + futureminute) // 60

  #print(f"new_extra_hour: {new_extra_hour}")

  new_hour = (currentHour + inputhours + extraHour + new_extra_hour) % 24

  print(f"future hour: {new_hour}")
  print(f"future minute: {new_min}")
  
  #Do not use any if statements in calculating the time.

  ####Output the future time in standard format "HH:MM"

  future_time = str(new_hour) + ":" + str(new_min)
  print(f"future time: {future_time}")


if __name__ == '__main__':
  main()
