def myfunction(aList):
    product = 1
    for item in aList:
	    product = product * item
    return product

things=[2, 4, 6, 8]
print(myfunction(things))

