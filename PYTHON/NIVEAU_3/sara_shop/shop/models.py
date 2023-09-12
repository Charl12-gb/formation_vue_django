from django.db import models

class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='dishes/', null=True, blank=True)

    def __str__(self):
        return self.name

class Sauce(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='sauces/', null=True, blank=True)

    def __str__(self):
        return self.name

class Beverage(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='beverages/', null=True, blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    dish = models.ForeignKey('Dish', on_delete=models.CASCADE)
    sauce = models.ForeignKey('Sauce', on_delete=models.CASCADE, null=True)
    beverage = models.ForeignKey('Beverage', on_delete=models.CASCADE, null=True)
    processed = models.BooleanField(default=False)

    def calculate_total(self):
        total = self.dish.price
        if self.sauce:
            total += self.sauce.price
        if self.beverage:
            total += self.beverage.price
        return total

    def __str__(self):
        return f"Order {self.id} - Total: {self.calculate_total()}"

    def __str__(self):
        return f"Order {self.id} - {self.dish.name}"