# use the filter() function along with a lambda to solve the "Filtering by Star Rating" problem.
def filter_by_rating(product,rating):
    filterting_products=dict(filter(lambda product:product[1] == rating,product.items()))
    return filterting_products if filterting_products else "No Result Found"

print(filter_by_rating({
  "Luxury Chocolates" : "*****",
  "Tasty Chocolates" : "****",
  "Aunty May Chocolates" : "*****",
  "Generic Chocolates" : "***"
}, "*****"))

#return {k:v for k,v in d.items() if d[k]==rating} or 'No results found'