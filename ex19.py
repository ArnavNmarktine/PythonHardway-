def cheese_and_crackers(cheese_count,boxes_of_cracker):
    print(f"You have {cheese_count} cheese !")
    print(f"You have {boxes_of_crackers} boxes of crackers !")
    print(f"Man thats enough for a party !")
    print(f"Get a blanket. \n !")

print("We can just give the function number directly: ")
cheese_and_crackers(20,30)

print("OR, we can use variable from our script:")
amount_of_cheese =10 
amount_of_cracker =50 

cheese_and_crackers(amount_of_cheese , amount_of_cracker )

print("We can even do maths inside too: ")
cheese_and_crackers(10+20, 5+6)

print("And we cancombine two, variables and do maths")

