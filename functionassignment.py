
   
def calculate_discount(price, discount_percent):
    
    if discount_percent >= 20:
        discounted_price = price - (price * discount_percent / 100)
        return discounted_price
    return price

price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

    # Calculate the final price
final_price = calculate_discount(price, discount_percent)

    # Print the result
print(f"Final price after discount: ${final_price}")


