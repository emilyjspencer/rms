from numpy import * 

a = array([
    [8, 2, 22, 97, 38, 15, 0, 40, 0, 75],
    [49, 49, 99, 40, 17, 81, 18, 57, 60, 87],
    [81, 49, 99, 40, 17, 81, 18, 57, 60, 87],
    [52, 70, 95, 23, 4, 60, 11, 42, 69, 24],
    [22, 31, 16, 71, 51, 67, 65, 89, 41, 92],
    [24, 47, 32, 60, 99, 3, 45, 2, 44, 75],
    [32, 98, 81, 28, 64, 23, 67, 10, 26, 38], 
    [67, 26, 20, 68, 2, 62, 12, 20, 95, 63], 
    [24, 55, 58, 5, 66, 73, 99, 36, 97, 27],
    [21, 36, 23, 9, 75, 0, 76, 44, 20, 45]]
    )
m = reshape(a,(10,10))
print(m)

def findMaxProdConsec(a, consec):

    max_of_consecutive_numbers = 0 
    
    current_product = 1

    consec = 3

    # horizontal iteration
    
    for x in range(len(a)): # iterate through the entire grid
        for y in range(len(a[x]) - consec): # iterate through the 10 list items
            for z in range(consec): # iterate multiple times - 8 for each list item  8 2 22  then  2 22 97 etc
                print(z)
                current_product *= a[x][y+z] # + z for third iterator [0][0] = 8  [0][1] = 2  to get the next number in the third loop
                print(current_product)
                print("iterating across")
            if current_product > max_of_consecutive_numbers:
                max_of_consecutive_numbers = current_product
            current_product = 1

        print(max_of_consecutive_numbers)
        print("end of horizontal traversal")

        max_of_consecutive_numbers = max_of_consecutive_numbers
    

    # vertical traversal 
    for x in range(len(a) - consec): # iterate through the entire grid
        for y in range(len(a[x])): # iterate through the 10 list items
            for z in range(consec): # iterate multiple times - 8 49 81   49 81 52 etc
                print(z)
                current_product *= a[x + z][y] # moving down y axis
                print(current_product)
                print("iterating down")
            if current_product > max_of_consecutive_numbers:
                max_of_consecutive_numbers = current_product
            current_product = 1

        print(max_of_consecutive_numbers)
        print("end of vertical traversal")
        max_of_consecutive_numbers = max_of_consecutive_numbers

    # diagonal traversal south east
    for x in range(len(a) - consec):
        for y in range(len(a[x]) - consec):
            for z in range(consec):
                print(z)
                current_product *= a[x + z][ y + z]
                print(current_product)
                print("iterating down diagonal right")
            if current_product > max_of_consecutive_numbers:
                max_of_consecutive_numbers = current_product
            current_product = 1

        print(max_of_consecutive_numbers)
        print("end of diagonal south east traversal")
        max_of_consecutive_numbers = max_of_consecutive_numbers

    # diagonal traversal south west
    for x in range(len(a) - consec):
        for y in range(consec, len(a[x])): # initial value is at position 4 index 3
            for z in range(consec):
                print(z)
                current_product *= a[x + z][ y - z]
                print(current_product)
                print("iterating down diagonal left") # start at index of 3 i.e. position 4
            if current_product > max_of_consecutive_numbers:
                max_of_consecutive_numbers = current_product
            current_product = 1
           
        print(max_of_consecutive_numbers)
        print("end of diagonal south west traversal")
        max_of_consecutive_numbers = max_of_consecutive_numbers

        print("The answer is ********")
        print("*************************")
        print("**********************************")
    
        return max_of_consecutive_numbers



findMaxProdConsec(a, 3)

# sample output for first few iterations of horizontal traversal
"""
0
8
iterating across
1
16
iterating across
2
352
iterating across
352
0
2
iterating across
1
44
iterating across
2
4268
iterating across
4268
0
22
iterating across
1
2134
iterating across
2
81092
iterating across
81092
0
97
"""


# sample of output for first iterations of vertical traversal
"""
8
iterating down
1
392
iterating down
2
31752
iterating down
0
2
iterating down
1
98
iterating down
2
4802
iterating down
0
22
iterating down
1
2178
iterating down
2
215622
iterating down
0
97
iterating down
1
3880
iterating down
2
155200
iterating down
0
38
iterating down
1
646
iterating down
2
10982
iterating down
0
15
"""



# sample output for first iterations of diagonal south east traversal
"""
0
8
iterating down diagonal right
1
392
iterating down diagonal right
2
38808
iterating down diagonal right
931095
end of diagonal south east traversal
0
2
iterating down diagonal right
1
198
iterating down diagonal right
2
7920
iterating down diagonal right
931095
end of diagonal south east traversal
0
22
iterating down diagonal right
1
880
iterating down diagonal right
2
14960
iterating down diagonal right
931095
end of diagonal south east traversal
0
97
"""