from django.db import models


size_choice = (("10","10"),
                ("20","20"),
                ("30","30")
            )

quality_choice = (("high","high"),
                ("low","low"),
                ("mediam","mediam")
                )

colour_choice = (("red","red"),
                ("blue","blue"),
                ("green","green"),
                ("black","black")
                )

class ProductMainModel(models.Model):
    Title = models.CharField(max_length=20)
    description = models.TextField()
    Price = models.CharField(max_length=10)
    unique_code = models.CharField(max_length=100,unique=True)
    size = models.CharField(max_length=10,choices=size_choice)
    Quality = models.CharField(max_length=10,choices=quality_choice)

    def __str__(self):
        return str(self.id)


class ProductColourModel(models.Model):
    Product = models.ForeignKey(ProductMainModel,on_delete=models.CASCADE)
    Colour = models.CharField(max_length=20,choices=colour_choice)

    def __str__(self):
        return str(self.id)


class ProductImageModel(models.Model):
    Product = models.ForeignKey(ProductMainModel,on_delete=models.CASCADE)
    Image = models.ImageField(upload_to ='imagefolder')

    def __str__(self):
        return str(self.id)

