#create(open) data.txt and write 'name' in it.
out_file= open('data.txt', 'w')
name = input("what is your name? ")
print(name, file=out_file)
out_file.close()
#open data.txt and read and print the name in the file
in_file= open('data.txt', 'r')
name= in_file.read().strip()
in_file.close()
print("your name is ",name)
#create(open) numbers.txt and right 17,42,400 on each line.
out_file = open('numbers.txt', 'w')
print("17", file=out_file)
print("42", file=out_file)
print("400", file=out_file)
out_file.close()
#read numbers.txt for first 2 line and add them up.
in_file= open('numbers.txt', 'r')
num1 = int(in_file.readline())
num2 = int(in_file.readline())
in_file.close()
print("line1 + line2 = ", num1+num2)
#read numbers.txt and add all the numbers and print the total number.
in_file =open('numbers.txt', 'r')
total= 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)
