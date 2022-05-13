# accept name of product and in turn returns their respective price
def product():
    item = {"umbrella": 320, "book": 40, "bag": 500, "soap": 32, "watch": 1000, "phone": 9000, "pen": 10, "pencil": 5}
    select = input("Enter the name of the product you want:")
    price = item[select]
    return select,price
select,price=product()
outcome = "The price of {} is {:.2f}".format(select,price)
print(outcome)
