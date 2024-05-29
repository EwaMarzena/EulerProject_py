### 1. Multiples of 3 and 5
'''If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.  Find the sum of all the multiples of 3 or 5 below 1000.  ANSWER = 233168.'''

def multiples_of_3_and_5(below):
    pack = set()
    for i in range(1, below):
        if i%3 == 0: pack.add(i)
        if i%5 == 0: pack.add(i)
    print(pack)
    sum = 0
    for i in pack:
        sum += i  
    print(sum)   
            
#multiples_of_3_and_5(1000)

### 2. Even Fibonacci Numbers
'''Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, … 
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms. 
ANSWER = 4613732'''

def even_fibonacci_numbers(below):
    fibonacci = [1,2]
    sum = 0
    for i in range(2, below):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
        if fibonacci[i] > 4000000: break
        #print(fibonacci[i])
        if fibonacci[i]%2 == 0: sum += fibonacci[i]
    print(sum)

#even_fibonacci_numbers(100)

###3. Largest Prime Factor
'''The prime factors of 13195 are 5, 7, 13 and 29.  
What is the largest prime factor of the number 600851475143?  
ANSWER = 6857'''

import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1): 
        if n%i == 0:
            return False #not a prime
    return True #is prime number

def largest_prime_factor(number):
    factors = []
    for i in range(2, math.floor(math.sqrt(number) + 1)):
        if is_prime(i):
            if number % i == 0: factors.append(i)
    print(factors[-1])

#largest_prime_factor(600851475143)

### 4. Largest Palindrome Product
'''A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.  
Find the largest palindrome made from the product of two 3-digit numbers.  
ANSWER = 906609'''

def if_palindrome(result):
    number = str(result)
    l = len(number)
    for i in range(0, math.floor(l/2)):
        if number[i] != number[l-i-1]: return False
    return True

def largest_palindrome_product():
    greatest_palindrome = 0
    for i in range(999, 0, -1):
        for j in range(999, 0, -1):
            if if_palindrome(i * j):
                if (greatest_palindrome < i*j): greatest_palindrome = i * j
    return(greatest_palindrome)

#print(largest_palindrome_product()) 
    
### 5. Smallest Multiple
'''2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.  
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?  
ANSWER = 232,792,560'''

import itertools

def smallest_multiple():
    #div = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    div = [11, 12, 13, 14, 15, 16, 17, 18, 19]
    for i in itertools.count(start = 20, step = 20): #if number divisible by 20 -> also divisible by 2, 5, 10 withour any reminder
        for j in div:
            if i % j != 0: break
        else: return i

#print(smallest_multiple())

### 6. Sum Square Difference
'''The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + … + 10^2 = 385  The square of the sum of the first ten natural numbers is, (1 + 2 + … + 10)^2 = 552 = 3025  Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.  Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.  ANSWER = 25164150'''

def sum_square_difference():
    l = []
    sum1 = sum2 = 0
    for i in range (1, 101):
        sum1 += i**2
        sum2 += i
    sum2 = sum2**2
    return(sum2-sum1)
#print(sum_square_difference())    

### 7. 10001st prime
'''By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.  What is the 10,001st prime number?  ANSWER = 104,743'''

#import itertools
'''def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1): 
        if n%i == 0:
            return False #not a prime
    return True #is prime number'''
def prime():
    listing = []
    for i in itertools.count(start = 2, step = 1):
        if is_prime(i): listing.append(i)
        if len(listing) == 10001: return listing[-1]

#print(prime())

### 8. Largest Product in a Series
'''The four adjacent digits in the 1000-digit number (below) that have the greatest product are 9 × 9 × 8 × 9 = 5832.  Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?  ANSWER = 23,514,624,000'''

def largest_product_in_a_series(filename):
    file = open(filename, 'r')
    number = file.read()

    greatest_result = 0
    indeks = 0

    for i in range(len(number)-13):
        temp = 1
        for j in range(i, i+13):
            temp *= int(number[j])
        if greatest_result < temp: 
            greatest_result = temp
            indeks = i
    return greatest_result, number[indeks:indeks+13]
print(largest_product_in_a_series('C:\\Users\\Ewa\\GIT_projects\\project_euler\\problem_8.txt'))