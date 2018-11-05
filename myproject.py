print("************TEXAS ROAD HOUSE**************")
print("****************MAIN MENU**************")
import time
time.sleep(1.5)
print('Please choose an entree.')
import time
time.sleep(1)
print('Your options are')
choice = input("""
A: Prime Rib
B: Bacon Burger
C: Cobb Salad
D: Ribeye
E: Babyback Ribs

Please enter your choice: """)

total = []

if choice == "A" or choice =="a":
  total.append(16.99)
  print('That is $16.99, I recommend getting that Medium Rare.  How would you like it cooked as well as')
elif choice == "B" or choice =="b":
  total.append(11.99)
  print('That is $11.99 and how would you like that cooked as well as')
elif choice == "C" or choice =="c":
  total.append(9.99)
  print('That is $9.99 and what type of dressing would you like with that salad as well as')
elif choice=="D" or choice=="d":
  total.append(8.99)
  print('That is $8.99 and it goes so well with our vegan wheat bread')
elif choice=="E" or choice=="e":
  total.append(14.99)
  print('That is $14.99 and I strongly suggest the baked beans with them')
import time
time.sleep(1)
print('What two sides would you like with that?')
sides = input("""
A: House Salad
B: Steak Fries
C: Sweet Potato Fries
D:anguished: Vegan Bread
E: Baked Beans
F: Homemade Applepie With Vanilla Ice Cream (additional $2.50)

Please enter your choice: """)

if choice == "A" or choice =="a":
  print('Perfect and for your second side?  The chef and I highly recommend the sweet potato fries.  They are both regular priced sides, not adding any additional cost to your entree')
elif choice == "B" or choice =="b":
  print('Perfect and for your second side?  I would recommend the Vegan Bread with those while the chef recommends the baked beans.  They are both regular priced sides, not adding any additional cost to your entree.')
elif choice == "C" or choice =="c":
  print('Perfect and for your second side?  The baked beans go great with those.  They are both regular priced sides, not adding any additional cost to your entree.')
elif choice=="D" or choice=="d":
  print('Perfect and for your second side?  I highly recommend the baked beans with that.  They are both regular priced sides which also makes it nice because there will be no additional cost to your entree.')
elif choice=="E" or choice=="e":
  print('Perfect and for your second side?  I highly recommend the Steak Fries with that.  They are both regular priced sides not adding any additional cost to your entree.')
elif choice =='F' or choice =='f':
  print('Great choice, we are very well know for our applepie and ice cream.  There is an additional $2.50 cost that will be added to the entree cost.  What would you like for your second side that comes with that entree?')
import time
time.sleep(1)
print('What kind of drink would you like?')
Drink = input("""
A: Soda
B: Beer
C: Traditional drinks
D: Malt
E: Water

Please enter your choice: """)

if choice == "A" or choice =="a":
  print('We have: 7up, pepsi, merinda, mountian dew, cock, fanta, and sprai')
elif choice == "B" or choice =="b":
  print('Perfect and for your second side?  I would recommend the Vegan Bread with those while the chef recommends the baked beans.  They are both regular priced sides, not adding any additional cost to your entree.')
elif choice == "C" or choice =="c":
  print('Perfect and for your second side?  The baked beans go great with those.  They are both regular priced sides, not adding any additional cost to your entree.')
elif choice=="D" or choice=="d":
  print('Perfect and for your second side?  I highly recommend the baked beans with that.  They are both regular priced sides which also makes it nice because there will be no additional cost to your entree.')
elif choice=="E" or choice=="e":
  print('Perfect and for your second side?  I highly recommend the Steak Fries with that.  They are both regular priced sides not adding any additional cost to your entree.')
elif choice =='F' or choice =='f':
  print('Great choice, we are very well know for our applepie and ice cream.  There is an additional $2.50 cost that will be added to the entree cost.  What would you like for your second side that comes with that entree?')

print(f"Your total fro you order is: {sum(total)}")