'''
Question link: https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/its-magic/

Question description: 
Sussutu is a world-renowned magician. And recently, he was blessed with the power to remove EXACTLY ONE element from an array.

Given, an array A (index starting from 0) with N elements. Now, Sussutu CAN remove only that element which makes the sum of ALL the remaining elements exactly divisible by 7.

Throughout his life, Sussutu was so busy with magic that he could never get along with maths. Your task is to help Sussutu find the first array index of the smallest element he CAN remove.
'''

Question solution: 
n = int(input())
a = list(map(int, input().split())) /*This is to split the input into a list.*/
b = []
 
sum = sum(a) /*To find the sum of all the integers in the list.*/
for i in range(n):
    if (sum - a[i]) % 7 == 0:
        b.append(a[i])
    
try:
    c = min(b)
    print(a.index(c)) /*To print the index of the integer, i when (sum - a[i]) % 7 == 0.*/
except:
    print(-1)
   
