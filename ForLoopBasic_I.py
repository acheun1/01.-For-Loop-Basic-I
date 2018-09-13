#Basic - Print all the numbers/integers from 0 to 150.

for i in range(151):
    print(i)
    
#Multiples of Five - Print all the multiples of 5 from 5 to 1,000,000.

for i in range(5,1000001,5):
    print(i)

#Counting, the Dojo Way - Print integers 1 to 100.  If divisible by 5, print "Coding" instead. If by 10, also print " Dojo".

for i in range(1,51,1):
    if i%5==0:
        print("Dojo")
    if i%10==0 and i%5==0:
        print("Coding")
    else:
        print(i)

#Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

sum=0
for i in range(1,50,1):
    if i%2 != 0:
        sum=sum+i
print(sum)

#Countdown by Fours - Print positive numbers starting at 2018, counting down by fours (exclude 0).

for i in range(50,1,-4):
     print(i)

#Flexible Countdown - Based on earlier "Countdown by Fours", given lowNum, highNum, mult, print multiples of mult from lowNum to highNum, using a FOR loop.  
# For (2,9,3), print 3 6 9 (on successive lines)

for i in range(2, 9, 3):
    if i%2==0:
        print(i, end=" ")

#Predict
list = [3,5,1,2]
for i in list:
     print(i)

#OUTPUT = 3,5,1,2

list = [3,5,1,2]
for i in range(list):
   print(i)

#OUTPUT = error 
#list is not integer

list = [3,5,1,2]
for i in range(len(list)):
    print(i)

#OUTPUT = 3,5,1,2
#len capture len of list which 4