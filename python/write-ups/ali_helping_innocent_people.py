'''
Question: Ali and Helping innocent people

Question link: https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/cartag-948c2b02/ 

Arpasland has surrounded by attackers. A truck enters the city. The driver claims the load is food and medicine from Iranians. Ali is one of the soldiers in Arpasland. He doubts about the truck, maybe it's from the siege. He knows that a tag is valid if the sum of every two consecutive digits of it is even and its letter is not a vowel. Determine if the tag of the truck is valid or not.

We consider the letters "A","E","I","O","U","Y" to be vowels for this problem.

Input:
The first line contains a string of length 9. The format is "DDXDDD-DD", where D stands for a digit (non zero) and X is an uppercase english letter.

Output:
Print "valid" (without quotes) if the tag is valid, print "invalid" otherwise (without quotes)

Sample input: 12X345-67
Sample output: invalid
'''

# Write your code here
vowels = ['A', 'E', 'I', 'O', 'U', 'Y'] #from the question, list of vowels to be checked against the given character in the string. 
plateNumber = input() #input the question into the variable called plateNumber
prev = plateNumber[0] #to store the previous digit's index. when starting, it is the first value
isPrinted = False #by default is false, tracks if anything has been printed yet. 
for currentIndex in range(1, len(plateNumber)): #iterating through the plateNumber string. 
    current = plateNumber[currentIndex] #the value of the current index saved into the variable current
    try:
      current = int(current)
      if prev != -1 and (int(prev) + int(current)) % 2 != 0: #checks if prev value is -1 and if it is not then check if prev + current value is odd number 
          print('invalid')
          isPrinted = True #since it is odd, and something is printed, change isPrinted to true
          break
      else:
          prev = int(current) #since it is even, update prev value to the current value and continue to next iteration
          continue
    except:
      if current not in vowels or current == '-': #if current is character, check if it exist in the list of vowels or if it is a dash
        prev = -1 #reset prev to -1 as digits after no longer count as consecutive from the one before the character
        continue
      else:
        print('invalid')
        isPrinted = True # if it does, something is printed, and change isPrinted to true 
        break

if isPrinted == False: #if nothing has been printed thus far, print valid 
    print('valid')
