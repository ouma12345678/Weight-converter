#python weight converter 

weight=float(input("Enter your Weight :"))
unit = input("Kilograms or Pounds (K or L):")

if unit=="K":
    weight=weight * 2.205
    unit="Lbs."
elif unit=="L":
    weight=weight /  2.205
    unit="Kgs."
else:
    print(f"{unit} was not valid")

print(f"Your Weight is: {weight}{unit}") 

