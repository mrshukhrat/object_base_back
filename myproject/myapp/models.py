from django.db import models
class Regions(models.Model):
    title = models.CharField(verbose_name="Title",max_length=50,blank=True, null=True)


    def __str__(self):
            return self.title

class ObjectType(models.Model):
    title = models.CharField(verbose_name="Title",max_length=50,blank=True, null=True)


    def __str__(self):
            return self.title
class ObjectsGoal(models.Model):
    title = models.CharField(verbose_name="Title",max_length=50,blank=True, null=True)


    def __str__(self):
            return self.title

class ObjectsDesk(models.Model):
    title = models.CharField(verbose_name="Title",max_length=50,blank=True, null=True)


    def __str__(self):
            return self.title


class ObjectsDesk1(models.Model):
    title = models.CharField(verbose_name="Title",max_length=50,blank=True, null=True)


    def __str__(self):
            return self.title

class District(models.Model):
    title = models.CharField(verbose_name="Title", max_length=50, blank=True, null=True)
    regions_id=models.ForeignKey(
            Regions, on_delete=models.PROTECT, default=1
            )
    def __str__(self):
             return self.title


class Objects_main(models.Model):
    name = models.CharField(max_length=100, blank=True, unique=True, null=True,)
    object_type_id=models.CharField(max_length=100, blank=False,unique=False, null=True)
    object_goal_id=models.CharField(max_length=100, blank=False,unique=False, null=True)
    object_desk_id=models.CharField(max_length=100, blank=False, unique=False, null=True)
    object_desk1_id=models.CharField(max_length=100, blank=False, unique=False, null=True)
    images = models.FileField(upload_to='.', blank=False,unique=False, null=True )
    contracts_file = models.FileField(upload_to='.', blank=False,unique=False, null=True)
    object_age = models.CharField(max_length=100, blank=False,unique=False, null=True)
    regions = models.CharField(max_length=100, blank=False,unique=False, null=True)
    district = models.CharField(max_length=100, blank=False,unique=False, null=True)
    regions_name = models.CharField(max_length=100, blank=False,unique=False, null=True)
    district_name = models.CharField(max_length=100, blank=False,unique=False, null=True)
    address = models.CharField(max_length=100, blank=False,unique=False, null=True)
    k_number = models.CharField(max_length=100, blank=False,unique=True, null=True)
    author = models.CharField(max_length=100, blank=False,unique=False, null=True)
    lat = models.CharField(max_length=100,blank=False,unique=False, null=True)
    lng = models.CharField(max_length=100,blank=False,unique=False, null=True)
    surface = models.CharField(max_length=100, blank=False,unique=False, null=True)
    area = models.CharField(max_length=100,blank=False,unique=False, null=True)
    gas = models.CharField(max_length=100, blank=False,unique=False, null=True)
    water = models.CharField(max_length=100, blank=False,unique=False, null=True)
    electricity = models.CharField(max_length=100,blank=False,unique=False, null=True)
    Rented = models.CharField(max_length=100, blank=False,unique=False, null=True)
    contracts = models.CharField(max_length=100, blank=False,unique=False, null=True)
    marked = models.CharField(max_length=100, blank=False,unique=False, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name