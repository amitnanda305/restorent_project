from django.db import models


class ItemList(models.Model):
    category_name = models.CharField(max_length=15)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "Item Category"
        verbose_name_plural = "Item Categories"


class Items(models.Model):
    item_name = models.CharField(max_length=15)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(ItemList, related_name='items', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='items/')

    def __str__(self):
        return self.item_name


class AboutUs(models.Model):
    description = models.TextField()

    def __str__(self):
        return "About Us Content"


class Feedback(models.Model):
    user_name = models.CharField(max_length=15)
    description = models.TextField()
    rating = models.IntegerField()
    image = models.ImageField(upload_to='feedback/', blank=True, null=True)  # Optional image

    def __str__(self):
        return self.user_name


class BookTable(models.Model):
    name = models.CharField(max_length=15)
    phone_number = models.BigIntegerField()
    email = models.EmailField()
    total_person = models.IntegerField()
    booking_date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.booking_date}"
