# Python Task 

# 1.Write a program to count the number of vowels in a given string.
a = input("Enter word: ")
count = 0
vowels = "aeiouAEIOU"
for i in range(0,len(a)):
    if a[i] in vowels:
        count+=1
print(count)

# 2.Write a program to reverse a given string.
a = input("Ente Word:")
rev =""
for i in range(len(a)-1,-1,-1):
    rev += a[i]
print(rev)

# 3.Write a program to count the number of words in a sentence.
a = input("Enter Sentence: ")
count = 1
for i in range(0,len(a)):
    if a[i] == " ":
        count+=1
print(count)

# 4.Write a program to check whether a given string is a palindrome.
a = input("Enter String: ")
rev = ""
for i in range(len(a)-1,-1,-1):
    rev += a[i]
print(rev)
if rev == a:
    print("Given String is Palindrome")
else:
    print("Given string is not palindrome")
# 5.Write a program to convert all characters of a string to uppercase.
a = input("Enter String: ")
print(a.upper())

# 6.Write a program to find the sum of all elements in a given list.
l = list(map(int,input("Enter List Elements:").split()))
print(l)
sum = 0
for i in l:
    sum+=i
print(sum)

# 7.Write a program to find the largest element in a list.
l = list(map(int,input("ENter list elements:").split()))
print(l)
le = 0
for i in l:
    if le < i:
        le = i
print(le,"is the largest element in the list")
# 8.Write a program to count the number of even numbers in a list.
l = list(map(int,input("ENter list elements:").split()))
print(l)
count = 0
for i in l:
    if i % 2 == 0:
        count += 1
print(count)
# 9.Write a program to reverse a list.
l = list(map(int,input("Enter List Elements:").split()))
print(l)
l.reverse()
print(l)

# 10.Write a program to check whether a given element exists in a list.
l = list(input("Enter List Elements:").split())
g = input("Enter element:")
if g in l:
    print(True)
else:
    print(False)
# solve these questions and make a linked in post about the concepts

