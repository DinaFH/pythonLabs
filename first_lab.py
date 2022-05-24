import math
from collections import Counter
import sys

#problem 1
def euc_distance(p1,p2):
  distance = math.sqrt((p1['x']-p2['x'])**2 + (p1['y']-p2['y'])**2)
  return(distance) 

p1 = {'x':2.0, 'y':3.0}
p2 = {'x':4.0, 'y':6.0}
print(euc_distance(p1,p2))
######################################################################################
#problem 2
def unique_list(l):
    x = []
    for a in l:
        if a not in x:
           x.append(a)
    return x
myList=[1,2,2,3,3,3,3,4,5,10]
print(unique_list(myList)) 
#or using set() built in function in python
newList=list(set(myList))
print(newList)

########################################################################################
#problem 3
def get_front(str):
      return str[:math.ceil(len(str)/2)]
def get_back(str):
  return str[math.ceil(len(str)/2):]
a = "Hello"
b = "World"
print(f"({get_front(a)} + {get_front(b)}) + ({get_back(a)} + {get_back(b)})")
###########################################################################################
#problem 4

####################################################################################
#problem 5
def remove_vowel(s):
    return "".join([ x for x in s if x not in "aeouiAEOUI" ])
str="Dina"
print(remove_vowel(str))
#########################################################################################
#problem 6

def find_location(str,char):
  out = []
  for i in range(len(st)):
   if (st[i] == ch):
    out.append(i) 
    return out
st = "Google"
ch = "o"
print(find_location(st,ch))
################################################################################################
#Report


#creates a set using curly brackets
snekSet = {"cobra","viper","snek"}
print(snekSet[2])
##############Using enumerate##############
snekSet = {"cobra","viper","snek"}
snekSetEnum = enumerate(snekSet)
snekList = list(snekSetEnum) #[(0, ‘cobra’), (1, ‘snek’), (2, ‘viper’)]

#################################################################################################
#creates a tuple using parentheses
snekTuple = ("cobra","viper","snek")
#prints the third object in the tuple
print(snekTuple[2])
##############Using enumerate##############
snekTuple = ("cobra","viper","snek")
for i in enumerate(snekTuple):
  print(I)

#(0, ‘cobra’)
#(1, ‘viper’)
#(2, ‘snek’)

##############################################################################################
# Program to show the use of lambda functions
double = lambda x: x * 2
print(double(5)) #10
#########################################################
# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))
print(new_list)
#Output:[4, 6, 8, 12]
#########################################################
# Program to double each item in a list using map()
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2 , my_list))
print(new_list)
#Output:
#[2, 10, 8, 12, 16, 22, 6, 24]
########################################################


# Import operator module  
import operator  
# Take two input numbers from user  
x = int(input("Enter first integer number: "))  #2
y = int(input("Enter second integer number: "))  #3
###### Mathematical Operations Functions 
print(operator.add(x,y)) #5
print(operator.sub(x,y)) #-1
print(operator.mul(x,y)) #6
print(operator.truediv(x,y)) #0.6666666666666666
print(operator.floordiv(x,y)) #0
print(operator.mod(x,y)) #2
print(operator.pow(x,y)) #8
###### Relational Operations Functions ###########
#less than 
print(operator.lt(x,y)) #True 
#less than or equal
print(operator.le(x,y)) #True
#greater than
print(operator.gt(x,y)) #False
#greater than or equal
print(operator.ge(x,y)) #False
#equal
print(operator.eq(x,y)) #False
#not equal
print(operator.ne(x,y)) #True