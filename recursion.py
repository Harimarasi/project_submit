#series of even numbers
'''
def even(num1,num2):
    if num1 == num2+1:
        return
    else:
        if num1%2 == 0:
                print(num1)
    even(num1+1 , num2)
num1=int(input('enter the number'))    
num2=int(input('enter the number'))  
even(num1,num2)   
'''
# armstrong number
'''
def armstrong(num,power):
    if num == 0:
        return 0 
    return (num%10)**power + armstrong(num//10,power)
num = 371
power = len(str(num))
print('armstrong'if armstrong(num,power) == num else 'not armstrong')
'''
#desirable number
'''
def desirable(num,power):
    if num == 0:
        return 0 
    return (num%10)**power + desirable(num//10,power-1)
num = 135
power = len(str(num))
print(desirable(num,power))
print('desirable number'if desirable(num,power) == num else 'not desirable')
'''
#factorial
'''
def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num*factorial(num-1)
num=0
print(factorial(num))
'''
#strong number
'''
def factorial(num):
    if num == 0 or num==1 :
        return 1
    return num*factorial(num-1)
def sum_facts(num):
    if num==0:
        return 0
    return factorial(num%10) + sum_facts(num//10) 
    
num = 145
print('strong number'if sum_facts(num) == num else 'not strong number' )    
'''
# int to binary
'''
def binary(num,bin):
    if num ==1 or num == 0:
         a=bin+str(num)
         return a[::-1]
    return binary(num//2,bin+str(num%2))
num = 12
bin=''
print(binary(num,bin))
'''
#binary to int
'''
def integer(num,num2,length):
    if length == 0:
        return 0
    return ((num%10)*(2**(num2)))+integer(num//10,num2+1,length-1)
num=10
num2=0
length=len(str(num))
print(integer(num,num2,length))
'''     
#reversing number
'''
def reverse(num,rev):
    if num == 0:
        return rev
    return reverse(num//10,rev+str(num%10))
num=1234
rev=''
print(reverse(num,rev))        
'''
#polyprime
'''
def polyprime(num,res):
    if num == 0:
        return res
    a=num%10
    return polyprime(num//10,res+str(a))  
def prime(num,num2):
    if num2 == num//2+1:
        return True
    if num%num2 == 0 or num<2: 
        return False
    return prime(num,num2+1)    
num=1
res=''  
num2=2 
print( 'POLYPRIME' if(polyprime(num,res) == str(num) and prime(num,num2) == True) else'NOT POLYPRIME')

def polyprime(num,num2,b):
    if num2 == num//2+1:
        return True
    if num%2 == 0 or num<2:
        return False
    return polyprime(num,num2+1,b)
num=2
num2=2
b=str(num)[::-1]
print('polyprime'if polyprime(num,num2,b) == True and b == str(num) else 'not')

''' 
                  
#PRIME NUMBER USING COUNT
'''
def prime(num,num2,count):
    if num2 == num//2+1:
        return count
    if num%num2 == 0 or num<2:
        count=count+1 
    return prime(num,num2+1,count)           
num =2
num2=2
count=0
print('PRIME'if prime(num,num2,count) == 0 else 'NOT PRIME')
'''
#prime number
'''
def prime(num,val=1):
    if val == num+1:
        return 0
    if num%val == 0:
        return 1+prime(num,val+1)
    else:
        return 0+prime(num,val+1)
num=13
print('PRIME'if prime(num)==2 else 'NOT PRIME')                
'''
#emirp number
'''
def palindrom(num):
    if num == 0:
        return 0
    return num%10*10**(len(str(num))-1)+palindrom(num//10)
def prime(num,num2):
    if num2 == num//2+1:
        return True
    if num%num2 == 0 or num<2: 
        return False
    return prime(num,num2+1)   
num = 11
num2=2
print('EMIRP NUMBER'if prime(num,num2) == True and palindrom(num)!=num and 
      prime(palindrom(num),num2) == True else 'NOT EMIRP NUMBER' )
'''
#NUMBER IN FIBANOIC SERIES BY  USING POSITION
'''
def fib(pos):
    if pos == 1 or pos == 2:
        return pos-1
    return fib(pos-1)+fib(pos-2)
pos=5
print(fib(5))
'''
#TECH NUMBER
'''
def tech(num):
    if num == 0:
        return 0
    return (num%100)+ tech(num//100)   
num=1015
print('TECH NUMBER'if (tech(num))**2 == num else 'NOT TECH NUMBER')
'''
#armstrong numbersdef armstrong(num,power):
'''
def armstrong(num,power):
    if num == 0:
        return 0 
    return (num%10)**power + armstrong(num//10,power)    
def ran(num,num2):
    if num == num2+1:   
        return
    power=(len(str(num)))    
    if  armstrong(num,power) == num:
        print(num)
    return ran(num+1,num2)    
num=1
num2=200
ran(num,num2)
''' 








    