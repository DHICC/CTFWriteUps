# Read the .md file for detailed question analysis and method
T = int(input())
for x in range(1, T + 1):
    n = input()
    original_array = input().split()
    
    # Set foot as the last element of array
    foot = original_array[-1]
    bool up = true;
    
    # First check for edge case n == 1, if it's just one element it will always be a mountain
    # I forgot to do this during the contest out of panic and I lost about 10 minutes rip
    if n == 1:
        print(0)
        break

    # Reverse loop through the array
    for i in xrange(c-1, 0, -1){
        # If minima is reached
        if up == false and v[i] > foot:
            print(i + 1)
            break
    
        # If maxima is reached
        elif up == true and v[i] < foot:
            up = false
        
        # If end of array is reached and array is still good
        if i == 0:
            print(0)
            break
        
        # Set foot to be a 1-lagging variable
        foot = v[i]
