mobile={"company":"oppo",
         "color":"red",
         "price":90000}
print(type(mobile))
print(len(mobile))
# accessing items
print(mobile["company"])
print(mobile.get("color"))
print(mobile.keys())
print(mobile.values())
print(mobile.items())
# change value
mobile["price"]=10000
print(mobile)
mobile.update({"price":8000})
print(mobile)
# # adding new items
mobile["year"]=2019
# print(mobile)
# removing items
mobile.pop("price")
print(mobile)
del mobile["color"]
print(mobile)
# remove last item
mobile.popitem()
print(mobile)
# clear dictionary
mobile.clear()
print(mobile)