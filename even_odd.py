num = int(input("Enter Number: "))
even_sum = 0
odd_sum = 0
while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        even_sum += digit
    else:
        odd_sum += digit
    num = num // 10
if even_sum > odd_sum:
    print("Even is greater than Odd")
else:
    print("Odd is greater than Even")