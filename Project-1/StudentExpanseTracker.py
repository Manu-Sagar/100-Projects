print("===Student Expanse Tracker===")

expances=[]
while True:
    print("\n1.Add Expanses")
    print("2.View Expanse")
    print("3.Calaculate Total Expanxe")
    print("4.Find the Highest Expanse")
    print("5.Exit\n")

    choice=int(input("Enter Your Choice:"))
    if choice==1:
        category=input("Enter the expanse category:")
        
        amount=float(input("Enter the Expanse Amount:"))

        expanse={
            "category":category,
            "amount":amount
        }

        expances.append(expanse)
        print("Expanse Added Successfully")
    elif choice==2:
        if(len(expances)==0):
            print("No Expanses Found")
        else:
            for expanse in expances:
                print(f"Category:{expanse['category']},Amount:{expanse['amount']}")
    elif choice==3:
        total=0
        for expanse in expances:
            total+=expanse['amount']
        print(f"Total Expanse:{total}")

    elif choice==4:
        if(len(expances)==0):
            print("No Expanses Found")
        else:
            highest=expances[0]
            for expance in expances:
                if expanse['amount']>highest['amount']:
                    highest=expanse
            print(f"Highest Expanse:Category:{highest['category']},Amount:{highest['amount']}")
    elif choice==5:
        print("Thank You for Using the Tracker")
        print("Exiting from the Tracker")
        break
    else:
        print("Invalid Choice")