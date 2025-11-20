#Author: Gabriel Gardner
#GitHub username: supergabe2005
#Date: 11/12/25
#Description: Calculates and returns a list of primes numbers up to 100
#             by sorting through and marking true or false primes

def list_of_primes_up_to(limit=100):
    """
    Returns a list of all prime numbers up to and including the limit

    This function uses the Sieve of Eratosthenes algorithm to efficiently
    find all primes up to a given limit. It marks non-prime numbers as False
    and primes as True.

    args:
    limit (int): The upper bound for finding primes. Default is 100.

    returns:
    list: A list of all prime numbers up to and including the limit.
    """

    #step 1: initialize a list of booleans
    #create a list with limit + 1 elements, all set to True
    is_prime = [True] * (limit + 1)

    #mark 0 and 1 as not prime
    is_prime[0] = False
    is_prime[1] = False

    #step 2: remove multiples of 2
    #mark all even numbers (except 2) as not prime
    for i in range(4, limit + 1, 2):
        is_prime[i] = False

    #step 3: sieve via successive divisors
    #continue marking multiples of each prime found
    #check up to the square root of limit
    divisor = 3
    while divisor <= limit ** 0.5:
        #find the next index that is still marked True
        if is_prime[divisor]:
            #mark all multiples of this divisor as not prime
            for i in range(divisor * divisor, limit + 1, divisor):
                is_prime[i] = False

        divisor += 2  #only check odd divisors

    #step 4: extract the primes and return
    #use a list comprehension to collect all indices marked as True
    primes = [i for i in range(limit + 1) if is_prime[i]]

    #step 5: return list
    return primes