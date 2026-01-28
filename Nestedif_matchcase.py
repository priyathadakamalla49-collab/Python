bill = int(input("Enter Bill Price: "))
payment =input("Enter Payment Method: ") #Credit,Cash,Debit,Netbanking
if payment == "credit":
    bank = input("Enter Bank name: ") #HDFC,SBI
    if bank == "HDFC":
        total = bill - (bill * 10/100)
        print("The final amount is ",total)
    elif bank == "SBI":
        total = bill - (bill * 5/100)
        print("The final amount is ",total)
    else:
        total = bill - (bill * 2/100)
        print("The final amount is ",total)
elif payment == "cash":
    total = bill - (bill * 1/100)
    print("The final amount is ",total)
else:

    print("No discount")


#Match_case

month = int(input("Enter Month Number: "))
match month:
    case 1:
        print("The Month is January")
    case 2:
        print("The Month is February")
    case 3:
        print("The Month is March")
    case 4:
        print("The Month is April")
    case 5:
        print("The Month is May")
    case 6:
        print("The Month is June")
    case 7:
        print("The Month is July")
    case 8:
        print("The Month is August")
    case 9:
        print("The Month is September")
    case 10:
        print("The Month is October")
    case 11:
        print("The Month is November")
    case 12:
        print("The Month is December")
    case _:
        print("Invalid Month Number")
