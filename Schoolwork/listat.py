units = {"Ballista", "Hoplite", "Armored chariot"}
units.add("Bowman")
print(units)

brandKey = "brand"
modelKey = "model"
yearKey = "year"
priceKey = "price"

#Dictionary
carInfo = {
 brandKey: "Ford", 
 modelKey: "Escort", 
 yearKey: 1995, 
 priceKey: 995
 }

model = carInfo["model"]
print(model)

carInfo["color"] = "blue"
print(carInfo)

price = carInfo.pop("price", 0)
print(price)

price = carInfo.pop("price", 0)
print(price)