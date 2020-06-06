'''
Write a python program to take in the number of levels and print a pyramid of stars.

Example:
    n = 5

    *
   * *
  * * *
 * * * *
* * * * *

'''

def pyramid_star(num):
    for i in range(1,num+1):
        # end by default prints '\n' which is 'new line'
        print(" " * (num - i), end = "")

        print("* " * i)

pyramid_star(50)

