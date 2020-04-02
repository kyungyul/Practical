"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    try:
        result = int(input("Enter a integer: "))
        finished = True # when there is no ValueError, finished becomes True.
    except ValueError: #when there is a value Error, print this.
        print("Please enter a valid integer.")
print("Valid result is:", result)
