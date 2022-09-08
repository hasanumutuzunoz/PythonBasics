listCountries = ["Canada", "Turkey", "Mexico"]
print(listCountries)
listCountries.append("USA")
print(listCountries)
del(listCountries[1])
print(listCountries)
listCountries.insert(1, "Guatemala")
print(listCountries)

setCountries = {"Canada", "Turkey", "Mexico"}
print(setCountries)
setCountries.update(["USA"])
print(setCountries)
setCountries.remove("Turkey")
print(setCountries)
