"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))
if score < 0:
    print("Invalid score")
    score = float(input("Enter score: "))
else:
    if score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    if 90 > score > 50:
        print("Passable")
    if 100>= score >= 90:
        print("Excellent")
if score < 50:
    print("Bad")