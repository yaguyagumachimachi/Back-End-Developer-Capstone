from django.db import models

# Create your models here.


class Menu(models.Model):
    Title = models.CharField(max_length=255, unique=True)
    Price = models.DecimalField(max_digits=6, decimal_places=2)
    Inventory = models.SmallIntegerField()

    def __str__(self):
        return f'{self.Title} : {str(self.Price)}'

    # class Meta:
    #     unique_together = ('Title', 'Price')


class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests = models.PositiveSmallIntegerField()
    BookingDate = models.DateField()

    def __str__(self):
        return f'{self.Name} : {str(self.No_of_guests)} : {str(self.BookingDate)}'

    # class Meta:
    #     unique_together = ('Name', 'Price')
