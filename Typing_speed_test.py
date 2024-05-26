# Typing speed test program

import matplotlib.pyplot as plt
import time as t

times = []
mistakes = 0

typed = input("Enter the word you would like to practice: ").lower()
print("Type the word",typed,"as fast as possible 5 times.")
input("Press enter to continue")

while len(times)<5:
  start=t.time()
  word = input("Type the word: ")
  end = t.time()
  time_taken = end-start
  times.append(time_taken)
  
  if word!=typed:
    mistakes+=1

print("You made "+str(mistakes)+" mistakes")
print("Now let us see your evolution!")
t.sleep(6)

x=[1,2,3,4,5]
y=times
plt.plot(x,y)
legends = ['1', '2', '3', '4', '5']
plt.xticks(x,legends)
plt.ylabel("Time Taken")
plt.xlabel("Your attempts")
plt.title("Your typing speed")
plt.show()