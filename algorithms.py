
''' Python Interview Practice File ''' 

''' Topics include:

1) Return whether string has constant value or not (itr and recursive solution)
2) Retuirn nth term in fibonacci sequence (slow solution, w/explicit dictionary memoization & implicit python lib memoization)

'''

#return whether string has constant value in it or not
def containsConstantItr(string):
    vowels = "aeiou"

    for i in string:
        if i not in vowels:
            print(i)
            print("yes")
            break

def containsConstantRec(string):

    vowels = "aeiou"

    if string[0] not in vowels:
        print(string[0])
        return "yes"
    else:
        return containsConstantRec(string[1:])

#_______________________________________________________________________

#return nth term in fibonacci sequence: 1,1,2,3,5,8,13...
def fibonacciRetN(nTerm):

    if(nTerm==1):
        return 1
    elif(nTerm == 2):
        return 2
    elif(nTerm >2):
        return fibonacciRetN(nTerm-1) + fibonacciRetN(nTerm-2)


#fibonacci momoized for efficiency aka store values in cache and reduce redundance calculations
# by utilizing cache 

#EXPLICIT MEMOIZATION 

#define fibonacci_cache dictionary
fibonacci_cache = {}

def fibonacciRetNMemoizedE(nTerm):

    #if we have cached the value, then return it
    if nTerm in fibonacci_cache:
        return fibonacci_cache[nTerm]

    if(nTerm==1):
        value =  1
    elif(nTerm == 2):
        value = 2
    elif(nTerm >2):
        value = fibonacciRetNMemoizedE(nTerm-1) + fibonacciRetNMemoizedE(nTerm-2) 

    #cache the value and return in
    fibonacci_cache[nTerm] = value
    return value

#IMPLICIT MEMOIZATION 
from functools import lru_cache
@lru_cache(maxsize = 1000)

def fibonacciRetNMemoizedI(nTerm):
    if(nTerm==1):
        return 1
    elif(nTerm == 2):
        return 2
    elif(nTerm >2):
        return fibonacciRetNMemoizedI(nTerm-1) + fibonacciRetNMemoizedI(nTerm-2) 


#IMPLICIT MEMOIZATION WITH CHECKS/CATCH FOR NON-POSITIVE INTEGER ERRORS
from functools import lru_cache
@lru_cache(maxsize=1000)

def fibonacciMemoIBest(nTerm):
    if type(nTerm) != int:
        raise TypeError("nth term value must be an integer (e.g. 1, 2, 3...)")
    if nTerm <1:
        raise ValueError("Integer must be a positive integer greater than 1")

    if(nTerm == 1):
        return 1
    if(nTerm == 2):
        return 1
    if(nTerm > 2):
        return fibonacciMemoIBest(nTerm - 1) + fibonacciMemoIBest(nTerm - 2)
#____________________________________________________________________________________

''' MAIN '''
def main ():

    #input_str_1 = "abc de"
    #input_str_2 = "LuCiDProGrAmMiNG"
    #containsConstantRec(input_str_1)
    #containsConstantRec(input_str_2)

    #for n in range(1,50):
    #   nTerm2 = fibonacciRetN(n)
    #  print(nTerm2)

    for n in range(1,200):
        print(n, ":", fibonacciRetNMemoizedE(n))

    # note ratio between consecutive terms in fibonacci sequence converges to golden ratio 1.618...
    # golden ratio think golden breeding bunnies, and the lengths of squares starting from center in fibonacci spiral 
    for n in range(1,50):
        print(fibonacciMemoIBest(n+1)/ fibonacciMemoIBest(n))

main()