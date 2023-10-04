from django.db import models
from authentication.models import Account


# CollectionAddress Model
class CollectionAddress(models.Model):
    street = models.CharField(max_length=500)
    city = models.CharField(max_length=500)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state} {self.postal_code}"


# Batch Model
class Batch(models.Model):
    pickup_date = models.DateField()
    start_date = models.DateField()
    end_date = models.DateField()
    # TODO data validation

    def __str__(self):
        return f"Batch ID: {self.pk}"


# FoodCollectorBatch Model
class FoodCollectorBatch(models.Model):
    food_collector = models.ForeignKey(Account, on_delete=models.PROTECT)
    batch = models.ForeignKey(Batch, on_delete=models.PROTECT)

    def __str__(self):
        return f"Food Collector: {self.food_collector}, Batch: {self.batch}"


# FoodItem Model
class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True, blank=True)
    price = models.PositiveIntegerField()
    batch = models.ForeignKey(Batch, on_delete=models.PROTECT)
    vendor = models.ForeignKey(Account, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


# FoodItemImage Model
class FoodItemImage(models.Model):
    src = models.FileField(upload_to="food_item_images")
    food_item = models.ForeignKey(FoodItem, on_delete=models.PROTECT)

    def __str__(self):
        return f"Image for {self.food_item.name}"


# FoodOrder Model
class FoodOrder(models.Model):
    ORDER_STATUSES = [
        ('submitted', 'Submitted'),
        ('processed', 'Processed'),
        ('revised', 'Revised'),
        ('transit', 'Transit'),
        ('delivered', 'Delivered'),
        ('completed', 'Completed'),
    ]

    user_id = models.ForeignKey(Account, on_delete=models.PROTECT)
    food_item = models.ManyToManyField(FoodItem, through='FoodItemFoodOrder')
    quantity = models.PositiveIntegerField()
    collection_address = models.ForeignKey(CollectionAddress, on_delete=models.PROTECT)
    batch_id = models.ForeignKey(Batch, on_delete=models.PROTECT)
    order_status = models.CharField(max_length=20, choices=ORDER_STATUSES, default='submitted')

    def __str__(self):
        return f"Order ID: {self.pk}, User: {self.user_id}, Status: {self.get_order_status_display()}"


# FoodItemFoodOrder Model
class FoodItemFoodOrder(models.Model):
    food_item = models.ForeignKey(FoodItem, on_delete=models.PROTECT)
    food_order = models.ForeignKey(FoodOrder, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"Food Order ID: {self.food_order.pk}, Food Item: {self.food_item.name}, Quantity: {self.quantity}"


# Menu Model
class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    batch = models.ForeignKey(Batch, on_delete=models.PROTECT)

    def __str__(self):
        return f"Menu ID: {self.pk}, Batch: {self.batch}"


# VendorMenu Model
class VendorMenu(Menu):
    vendor_menu_id = models.AutoField(primary_key=True)
    vendor = models.ForeignKey(Account, on_delete=models.PROTECT)

    def __str__(self):
        return f"Vendor Menu ID: {self.pk}, Vendor: {self.vendor}"


# VendorFoodItem Model
class VendorFoodItem(models.Model):
    vendor_menu = models.ForeignKey(VendorMenu, on_delete=models.PROTECT)
    name = models.ForeignKey(FoodItem, on_delete=models.PROTECT)
    quantity_offered = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} ({self.quantity_offered} available)"
