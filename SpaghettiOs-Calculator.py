#import lib
import math

#open input file and covert it to a lowercase string
file = open("input.txt")
text = (file.read()).lower()

#The letter data for a can of SpaghettiOs (a-z)
can = [27,28,29,26,32,31,28,26,28,30,39,32,27,25,441,35,26,37,30,31,28,25,31,26,26,36]

#calcuating the quantity of letters and find the ratio to cans
ratio = [0]*26

for i in range(26):
    ratio[i] = math.ceil((text.count(chr(97+i)))/can[i])

#print results
num = int(max(ratio))
cost = num*1.26
print("-------------------------------")
print("Number of cans:", num)
print("Cost: $", cost)
print("-------------------------------")