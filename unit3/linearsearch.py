def linearSearchProduct(Productlist, targetproduct):
   indices =  [] 
   for index,product in enumerate(productList):
     if product == targetProduct:
       indices.append(index)
   return indices
product = ["shoes", "boot", "loafter", "shoes", ] 
target = "shoes"
target2 = 'apple'
result = linearSearchProduct(Product.target)
print(result)