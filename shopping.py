print("Enter the names of 3 different products in the following prompts.")
product_1 = input("Enter a product name: ")
product_2 = input("Enter a product name: ")
product_3 = input("Enter a product name: ")
print("Please enter the prices of the listed products: ")
product_1_price =float(input ("Enter prodct price: "))
product_2_price = float(input ("Enter prodct price: "))
product_3_price = float(input ("Enter prodct price: "))
product_price_sum = product_1_price + product_2_price + product_3_price
rounded_product_price_sum = round(product_price_sum,2)
product_price_average_ =(product_price_sum/3)
rounded_price_average = round(product_price_average_,2)

print(f'''The total of {product_1}, {product_2}, {product_3} is 
R{rounded_product_price_sum} and the average price of the items is
R{rounded_price_average}.''')