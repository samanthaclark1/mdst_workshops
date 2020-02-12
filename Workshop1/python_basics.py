"""
MDST Workshop 1 - Python Basics Starter Code
"""

# Add any imports you need here:


def part1(num):
    """
    Ask the user for a number. Depending on whether the number is even or odd,
    print out an appropriate (i.e. "even" or "odd") message to the user.
    """
x = int(input("enter a number:"))
if (x%2==0):
    print("Even")
else:
    print("Odd")

def part2():
    """
    Generate a random number between 1 and 9 (including 1 and 9). Ask the user
    to guess the number, then tell them whether they guessed too low, too high,
    or exactly right.
    (Hint: remember to use the user input lessons from the very first
    exercise).
    Keep the game going until the user types "exit".
    [ try checking the random module in python on google. Concepts: Infinite
    loops, if, else, loops and user/input].
    """
    x = randint(1,9)
    while ( y != 'exit'):
    y = int(input("guess the number:"))
    print("Guess:" y)
    if (x < y):
        print("too high")
    if (x > y):
        print("too low")
    if (x == y):
        print ("exactly right")


def part3(string):
    """
    Ask the user for a string and print out whether this string is a palindrome
    or not. (A palindrome is a string that reads the same forwards and
    backwards.)
    """
     y = string(input("enter a string:"))
        
     z = y[::-1]
     if(y == z):
          print("is a palindrome")
     if (y != z)
          print("is not a palindrome")


def part4a(filename, username, password):
     import base64
    """
    Encrypt your username and password using base64 module
    Store your encrypted username on the first line and your encrypted password
    on the second line.
    """
    user = base64.b64encode(username)
    passw = base64.b64encode(password)
    print ("Username" username)
     print ("Password" password)
def part4b(filename, password=None):
    """
    Create a function to read the file with your login information.
    Print out the decrypted username and password.
    If a password is specified, update the file with the new password.
    """
    user = ""
    passw = ""
    with open(filename) as file:
        user = file.readline()
        passw = file.readline()
        if(password != None):
            passw = password
            
    part4a(filename, user, passw)  


if __name__ == "__main__":
    part1(3)  # odd!
    part1(4)  # even!
    part2()
    part3("ratrace")  # False
    part3("racecar")  # True
    part4a("secret.txt", "naitian", "p4ssw0rd")
    part4b("secret.txt")
    part4b("secret.txt", password="p4ssw0rd!")
    part4b("secret.txt")
