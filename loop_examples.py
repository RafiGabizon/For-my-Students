from tkinter import *
menu=[
    {"first":{"Home Bread":12,"Fresh Salad":18,"Hummus":16,"French Fries":17}},
    {"main":{"Kebab":24,"Chicken":24,"Steak":113,"Combination":160}},
    {"desserts":{"Malabi":15,"Chocolate Cake":17,"Ice-Cream":8}},
    {"drinks":{"Coca-Cola":12,"Diet-Coke":12,"Mineral-Water":10,"Orange juice":12}}
]

order=["Fresh Salad","Chicken","Ice-Cream","Diet-Coke"]


total=0

for item in order:
    for cat in menu:
        for cat2 in cat.values():
            for dish in cat2:
                if item==dish:
                    total += cat2[dish]
                    print("price: ",cat2[dish])
                    print(total)
                

print("your total is: ", total)