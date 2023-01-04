product1 = input("please enter the name of a product: ")
product2 = input("and another: ")
product3 = input("and another: ")
price1 = float(input("enter the price of product1: "))
rounded_price1 = round(price1, 2)
price2 = float(input("enter the price of product2: "))
rounded_price2 = round(price2, 2)
price3 = float(input("enter the price of product3: "))
rounded_price3 = round(price3, 2)
total_price = (rounded_price1 + rounded_price2 + rounded_price3)
total_price_rounded = round(total_price, 2)
average_price = (rounded_price1+rounded_price2+rounded_price3)/3
average_rounded = round(average_price, 2)
print(f"the total of {product1},{product2},{product3} is £{total_price_rounded} and the average price of the items is £{average_rounded}")


#wasn't sure if every amount was to be rounded to 2 dp but did anyway