#Calculator
import math

def main():
    print('\nPlease select desired operation:')
    print('1)Addition \n2)Substraction \n3)Multiplication \n4)Division \n5)Modulus \n6)Exponential \n7)Square_root \n8)Square')    
    i = int(input())
    if i < 7:
         print("Please Enter 2 values: ")
         val1 = int(input())
         val2 = int(input())
         print("Entered values:",val1,'and',val2)
         if i == 1:
             Addition(val1,val2)
         elif i == 2:
             Substraction(val1,val2)
         elif i == 3:
             Multiplication(val1,val2)
         elif i == 4:
             Division(val1,val2)
         elif i == 5:
             Modulus(val1,val2)
         elif i == 6:
             Exponential(val1,val2)
                  
    else :
         if i == 7:    
             print("Please Enter a value: ")
             val1 = int(input())
             print("Entered Value:",val1)
             Square_root(val1)
         if i == 8:
             print("Please Enter a value: ")
             val1 = int(input())
             print("Entered Value:",val1)
             Square(val1)
         else :
                 print('Enter a valid choice')
    print("\nDo you want to perform another operation?")
    response = input('Enter y or n:')
    response.lower()
    if response == 'y':
         main()
    else :
         print("\nThank you!")
         
def Addition(val1,val2):
    x = val1 + val2
    print('Sum of',val1,'and',val2,'is:',x)
    
def Substraction(val1,val2):
    x = val1-val2
    print('Difference of',val1,'and',val2,'is:',x)

def Multiplication(val1,val2):
    x = val1*val2
    print('Product of',val1,'and',val2,'is:',x)
    
def Division(val1,val2):
    x = val1/val2
    print('Division of',val1,'and',val2,'is:',x)
    
def Modulus(val1,val2):
    x = val1 % val2
    print('Modulus of',val1,'and',val2,'is:',x)

def Exponential(val1,val2):
    x = val1 ** val2
    print('Exponential of',val1,'and',val2,'is:',x)    

def Square_root(val1):
    print('Square root of',val1,'is',math.sqrt(val1))

def Square(val1):
    x = val1 * val1
    print('Square of',val1,'is',x)    
   

main()
 
