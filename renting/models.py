from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class HouseOffer(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255, choices=(
        ('Квартиры, апартаменты', "Квартиры, апартаменты"),
        ('Дома, коттеджи', "Дома, коттеджи"),
        ('Комнаты', "Комнаты"),
        ('Апарт-отели', "Апарт-отели"),
        ("Отели, гостиницы", "Отели, гостиницы"),
        ("Мини-гостиницы", "Мини-гостиницы"),
        ("Гостевые дома", "Гостевые дома"),
        ("Глэмпинги, базы отдыха", "Глэмпинги, базы отдыха"),
        ("Хостелы", "Хостелы"),
        ("Студии", "Студии"),  
    ))
    price = models.DecimalField(max_digits=10, decimal_places=2)
    guests = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(100)
        ]
    )
    bedrooms = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )
    bathrooms = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=255)
    #amenities = models.JSONField()



    def __str__ (self):
        return self.title

class HouseImage(models.Model):
    offer = models.ForeignKey(HouseOffer, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images", blank=True)