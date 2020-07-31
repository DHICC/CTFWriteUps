'''
Question link: friends' relationship
https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/friends-relationship-1/description/

Question description:

Jack is your friend and Sophia is his girlfriend. But due to some unknown reason ( unknown for us, they know it) Sophia started hating to Jack. 

Now, Jack is in big trouble but he has a solution, He knows that if he will gift T patterns of a particular type ( For pattern observation see the sample test cases) then Sophia will start loving again to Jack. 

But Jack is depressed now and need your help to gift her that type patterns of '*' and '#' of N lines. So, it's your responsibility to save your friend's relationship.

Example: 
Input: 2, 3, 4

Output: 

*####*
**##**
******

*######*
**####**
***##***
********

Question solution:
'''

T = int(input()) #get the number of patterns
for i in range(T):
    N = int(input()) #get line number of one pattern
    for m in range(1, N+1):
        #observe from the sample given at line16-25, row number = 2 * line number, and the number of # on each line is an even number ( = 2N-2m - m is interation num) 
        print("*" * m + "#" * (2*N - 2*m) + "*" * m) 
        #print out the pattern 
   
