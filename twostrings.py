t = int(input()) # to get the number of cases
while(t>0): # to know that it hasn't finished all the cases
    s1,s2=input().split() # split the strings
    a = sorted(s1) # sort the strings
    b = sorted(s2) # sort the strings
    if (len(s1)) != (len(s2)): # if length of strings doesn't equal to each other
        print("No") # what to do if so
        break # stop the loop
    else: # if length of strings equal to each other
        if a == b: 
            print("yes")
        else:
            print("no")
    t =t-1 #-1 because 1 case is done so deduct from the total
