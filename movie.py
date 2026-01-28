rating = float(input("Enter the Rating: "))
if rating >= 4.5:
    print("Movie is a Blockbuster")
elif rating >= 3.5:
    print("Movie is a Hit")
elif rating >= 3:
    print("Movie is Good ") 
elif rating >= 2:
    print("Movie is Average")
elif rating >= 1.5:
    print("Movie is Below Average")
else:
    print("Movie is a Headache")