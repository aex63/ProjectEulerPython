
# Variables
n = list(range(1, 1000, 1))
m = [3,5]

#Use Hashtable to avoid duplicate. We only want values that can be multiplied by 3 OR 5
multisum = set() 

# Loop through range of numbers
for i in n:
    # For every int in our list of numbers to multiply with
    for x in m: 
        # i mod x: Only check where remainder 0: In other words the int can be multiplied by 3 or 5
        if i%x == 0:
            # Add matching ints to our hashtable
            multisum.add(i)

# Answersheet
print('Problem 1: Total sum of all natural numbers below 1000 which are multiples of', m[0], 'or', m[1], ':', sum(multisum))
