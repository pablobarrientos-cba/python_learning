import utility
from shopping import cart
from shopping.cart import buy

result = utility.multiply(3, 4)
print(result)

result = utility.divide(16, 3)
print(result)

print(cart.buy('hammer'))
print(buy('food'))
