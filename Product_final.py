class Product:
  def __init__(self, name, amount, price):
      self.name = name
      self.amount = amount
      self.price = price

  def get_price(self, quantity):
      
      if quantity <= 0:
            raise ValueError("Quantity must be a positive number.")
      
      if quantity < 10:
          return self.price * quantity
      
      if quantity >= 10 and quantity <= 99:
          total_price = self.price * quantity
          discount = (total_price) * (10/100)
          return total_price - discount
      
      if quantity >= 100:
          total_price = self.price * quantity
          discount = (total_price) * (20/100)
          return total_price - discount
          
          
  
  def make_purchase(self, quantity):
      
      try:
        if quantity > self.amount:
            raise ValueError("Not enough stock to complete the purchase.")
        price = self.get_price(quantity)
        print('Total price charged: ', price)
        self.amount -= quantity
      except ValueError as e:
            print(f"Error: {e}")


# create product object
# make purchases against different product quantities (make sure to run each test case)
# do not forget to handle exceptions
# print the remaining stock after each purchase

product = Product("Laptop", 50, 1000)  

try:
    product.make_purchase(5)  
    product.make_purchase(10)  
    product.make_purchase(50)  
    product.make_purchase(100) 
    product.make_purchase(51) 
except Exception as e:
    print(f"Exception caught during purchase: {e}")

