from math import sqrt


def say_hello(name):
    result = "Hello, {}!".format(name)
    return result


'''
PIRMSKAITLIS IR SKAITLIS, KAS DALĀS AR 1 UN PATS AR SEVI, UN KURAM IR TIEŠI DIVI DALĪTĀJI

2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, ...

'''


def check_if_prime(number):
    if number <= 1:
        return False
    is_prime = True
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            is_prime = False
            break
    return is_prime
