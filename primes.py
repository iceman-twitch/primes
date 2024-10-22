
import time

#Lets Find Primes

primes = {}

def FindPrimes():
    count = 0
    number = 2
    while True:
        if count > 10:
            break
        if len(primes) >= 1:
            isprime = True
            for key, value in primes.items():
                if number % value == 0: # If it pass this condition the number is not Prime
                    isprime = False
                    break
            if isprime: # If its a prime add it to the dictionary
                primes[count] = number
                print(number)
            count = count + 1
            number = number + 1
            continue
        else: # if we have no numbers in the table just add the first numbers and its number 2.
            primes[count] = number
            print(number)
            count = count + 1
            number = number + 1
            continue
        
        
FindPrimes()