# -*- coding: utf-8 -*-
import random

def main():
    print "Welcome to the Lottery numbers generator."
    while True:
        rand = []
        number = int(raw_input("Please enter how many random numbers would you like to have? "))
        print "Do you want %s" % number
        print random.sample(range(0, 45), number)

        new = raw_input("You need more random numbers? Yes/No? ").lower()
        if new == "no":
            break

if __name__ == "__main__":
    main()
