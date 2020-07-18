'''
Question: e-maze-in
https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/e-maze-in-1aa4e2ac/

Ankit is in maze. The command center sent him a string which decodes to come out from the maze. He is initially at (0, 0). String contains L, R, U, D denoting left, right, up and down. In each command he will traverse 1 unit distance in the respective direction.

For example if he is at (2, 0) and the command is L he will go to (1, 0).

Input:
Input contains a single string.

Output:
Print the final point where he came out.

Constraints:
1 ≤ |S| ≤ 200

Sample input: LLRDDR

Sample output: 0 -2
'''

user = input()

#For loop method
x,y = 0,0 

for letter in user:
    if letter == 'L': #left, moves negative x direction
        x -= 1 
    elif letter == 'R': #Right, moves positive x direction
        x += 1
    elif letter == 'D': #Down, moves negative y direction
        y -= 1
    else: #Up, moves positive y direction
        y += 1
        
print(x, y)

#Without the for loop method
print((user.count('R'))-(user.count('L')),(user.count('U'))-(user.count('D'))) 
#count() method returns the number of elements with the specified value. It can work for strings, lists & tuples
