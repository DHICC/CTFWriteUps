"""
Link to question: https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/two-strings-4/description/
Question:
Given two strings of equal length, you have to tell whether they both strings are identical.
Two strings S1 and S2 are said to be identical, if any of the permutation of string S1 is equal to the string S2. See Sample explanation for more details.
Input :
First line, contains an intger 'T' denoting no. of test cases.
Each test consists of a single line, containing two space separated strings S1 and S2 of equal length.
Output:
For each test case, if any of the permutation of string S1 is equal to the string S2 print YES else print NO.
Constraints:
1<= T <=100
1<= |S1| = |S2| <= 10^5
String is made up of lower case letters only.
Note : Use Hashing Concept Only . Try to do it in O(string length) .
"""

# Question solution:
t = int(input()) # to get the number of cases
while(t>0): # to know that it hasn't finished all the cases
    s1,s2=input().split() # split the strings
    a = sorted(s1) # sort the strings
    b = sorted(s2) # sort the strings
    if (len(s1)!=len(s2)): # if length of strings doesn't equal to each other
        print("NO") # what to do if so
        break # stop the loop
    else: # if length of strings equal to each other
        if a == b: 
            print("YES")
        else:
            print("NO")
    t =t-1 #-1 because 1 case is done so deduct from the total 
