#you need to design a program for a courier company to calculate the cost of sending a parcel
#ask the user to enter the price of the package they would like to purchase
#ask the user to enter the total distance of delivery in kms.
#Now add on the delivery costs to get the final product:
#Air R0.36 per km or freight R0.25 per km
#Full insurance R50.00 or limited insurance R25.00
#Gift R15.00 or no gift R0.00
#priority R100.00 or standard delivery R20.00
package_price = int(float(input("""Enter the price of the package you would like to purchase: """)))
distance = int(float(input("Enter the total distance of the delivery in Kilometers:")))
print ("For shipping preferences, please choose between Air at R0.36 per km, or Freight at R0.25 per km")
shipping = input("Enter: 'Air' or 'Freight'")
distance_cost = 0
if shipping in ['Freight']:
    distance_cost = 0.25
elif shipping in ['Air']:
    distance_cost = 0.36

print ("Choose between Full insurance (R50.00), or Limited insurance (R25.00)")
insurance = input("Enter: 'Full' or 'Limited'?")

insurance_cost = 0
if insurance in ['Full']:
    insurance_cost = 50
elif insurance in ['Limited']:
    insurance_cost = 25
print ("Would you like to add a Gift for R15.00?")
gift = input("Enter: 'Yes' or 'No'")
gift_cost = 0
if gift in ['Yes']:
    gift_cost = 15
elif gift in ['No']:
    gift_cost = 0

print ("Priority delivery for R100.00, or Standard delivery for R20.00?")
delivery = input("Enter: 'Priority' or 'Standard'")
delivery_quality = 0
if delivery in ['Priority']:
    delivery_quality = 100

elif delivery in ['Standard']:
    delivery_quality = 20

total_cost = package_price + distance*distance_cost + insurance_cost + gift_cost + delivery_quality
print (f"""Total cost:
R{total_cost}""")
