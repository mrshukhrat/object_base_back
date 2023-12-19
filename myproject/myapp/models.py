from django.db import models
from django.contrib.auth.models import Group

Group.objects.get_or_create(name='Admins')
Group.objects.get_or_create(name='Editors')
Group.objects.get_or_create(name='Viewers')
from django.contrib.auth.models import Permission

# Assign permissions to the 'Admins' group
admins_group = Group.objects.get(name='Admins')
admins_group.permissions.add(
    Permission.objects.get(codename='add_user'),
    Permission.objects.get(codename='change_user'),
    Permission.objects.get(codename='delete_user'),
    # Add more permissions as needed
)

# Assign permissions to the 'Editors' group
editors_group = Group.objects.get(name='Editors')
editors_group.permissions.add(
    Permission.objects.get(codename='change_user'),
    # Add more permissions as needed
)

# Assign permissions to the 'Viewers' group
viewers_group = Group.objects.get(name='Viewers')
viewers_group.permissions.add(
    # Add permissions for viewing data
)

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

    images1 = models.FileField(upload_to='.', blank=False,unique=False, null=True )
    images2 = models.FileField(upload_to='.', blank=False,unique=False, null=True )
    images3 = models.FileField(upload_to='.', blank=False,unique=False, null=True )
    images4 = models.FileField(upload_to='.', blank=False,unique=False, null=True )
    images5 = models.FileField(upload_to='.', blank=False,unique=False, null=True )

    user_id = models.CharField(max_length=100, blank=False,unique=False, null=True)
    name = models.CharField(max_length=100, blank=True, unique=True, null=True,)
    object_type_id=models.CharField(max_length=100, blank=False,unique=False, null=True)
    object_goal_id=models.CharField(max_length=100, blank=False,unique=False, null=True)
    object_desk_id=models.CharField(max_length=100, blank=False, unique=False, null=True)
    object_desk1_id=models.CharField(max_length=100, blank=False, unique=False, null=True)
    contracts_file = models.FileField(upload_to='.', blank=False,unique=False, null=True)
    object_age = models.CharField(max_length=100, blank=False,unique=False, null=True)
    regions = models.CharField(max_length=100, blank=False,unique=False, null=True)
    district = models.CharField(max_length=100, blank=False,unique=False, null=True)
    regions_name = models.CharField(max_length=100, blank=False,unique=False, null=True)
    district_name = models.CharField(max_length=100, blank=False,unique=False, null=True)
    address = models.CharField(max_length=100, blank=False,unique=False, null=True)
    address_id = models.CharField(max_length=100, blank=False,unique=False, null=True)
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


class Objects_contract(models.Model):
    regions_name = models.CharField(max_length=100, blank=True, unique=True, null=True,)
    district_name=models.CharField(max_length=100, blank=False,unique=False, null=True)
    region_id=models.CharField(max_length=100, blank=False,unique=False, null=True)
    district_id=models.CharField(max_length=100, blank=False, unique=False, null=True)
    contract_number=models.CharField(max_length=100, blank=False, unique=False, null=True)
    contract_date = models.FileField(upload_to='.', blank=False,unique=False, null=True)
    start_date = models.CharField(max_length=100, blank=False,unique=False, null=True)
    end_date = models.CharField(max_length=100, blank=False,unique=False, null=True)
    ap_start = models.CharField(max_length=100, blank=False,unique=False, null=True)
    ap_end = models.CharField(max_length=100, blank=False,unique=False, null=True)
    taq = models.CharField(max_length=100, blank=False,unique=False, null=True)
    imt = models.CharField(max_length=100, blank=False,unique=False, null=True)
    k_number = models.CharField(max_length=100, blank=False,unique=True, null=True)
    contract_event = models.CharField(max_length=100, blank=False,unique=False, null=True)
    yanvar = models.CharField(max_length=100,blank=False,unique=False, null=True)
    fevral = models.CharField(max_length=100,blank=False,unique=False, null=True)
    mart = models.CharField(max_length=100, blank=False,unique=False, null=True)
    aprel = models.CharField(max_length=100,blank=False,unique=False, null=True)
    may = models.CharField(max_length=100, blank=False,unique=False, null=True)
    iyun = models.CharField(max_length=100, blank=False,unique=False, null=True)
    iyul = models.CharField(max_length=100,blank=False,unique=False, null=True)
    avgust = models.CharField(max_length=100, blank=False,unique=False, null=True)
    sentabr = models.CharField(max_length=100, blank=False,unique=False, null=True)
    oktabr = models.CharField(max_length=100, blank=False,unique=False, null=True)
    noyabr = models.CharField(max_length=100, blank=False,unique=False, null=True)
    dekabr = models.CharField(max_length=100, blank=False,unique=False, null=True)


    contract_price = models.CharField(max_length=100, blank=False,unique=False, null=True)
    cont_auth = models.CharField(max_length=100,blank=False,unique=False, null=True)
    str_address = models.CharField(max_length=100,blank=False,unique=False, null=True)
    phone = models.CharField(max_length=100, blank=False,unique=False, null=True)
    xisob_number = models.CharField(max_length=100,blank=False,unique=False, null=True)
    mfo = models.CharField(max_length=100, blank=False,unique=False, null=True)
    bank_name = models.CharField(max_length=100, blank=False,unique=False, null=True)
    auth_name = models.CharField(max_length=100,blank=False,unique=False, null=True)
    auth_address = models.CharField(max_length=100, blank=False,unique=False, null=True)
    auth_str = models.CharField(max_length=100, blank=False,unique=False, null=True)
    auth_phone = models.CharField(max_length=100, blank=False,unique=False, null=True)
    auth_price_number = models.CharField(max_length=100, blank=False,unique=False, null=True)
    auth_mfo = models.CharField(max_length=100, blank=False,unique=False, null=True)
    auth_bank = models.CharField(max_length=100, blank=False,unique=False, null=True)


    auk_lot = models.CharField(max_length=100, blank=False,unique=False, null=True)
    auk_cont = models.CharField(max_length=100, blank=False,unique=False, null=True)
    auk_area = models.CharField(max_length=100, blank=False,unique=False, null=True)
    auth_price = models.CharField(max_length=100, blank=False,unique=False, null=True)

    obj_type = models.CharField(max_length=100, blank=False,unique=False, null=True)
    obj_name = models.CharField(max_length=100, blank=False,unique=False, null=True)
    obj_regions_name = models.CharField(max_length=100, blank=True, unique=True, null=True,)
    obj_district_name=models.CharField(max_length=100, blank=False,unique=False, null=True)
    obj_region_id=models.CharField(max_length=100, blank=False,unique=False, null=True)
    obj_district_id=models.CharField(max_length=100, blank=False, unique=False, null=True)

    obj_address = models.CharField(max_length=100, blank=False,unique=False, null=True)
    obj_f_type = models.CharField(max_length=100, blank=False,unique=False, null=True)

    obj_address = models.CharField(max_length=100, blank=False,unique=False, null=True)
    obj_min_kv = models.CharField(max_length=100, blank=False,unique=False, null=True)
    obj_area = models.CharField(max_length=100, blank=False,unique=False, null=True)
    obj_f_area = models.CharField(max_length=100, blank=False,unique=False, null=True)


    obj_kz = models.CharField(max_length=100, blank=False,unique=False, null=True)
    obj_kk = models.CharField(max_length=100, blank=False,unique=False, null=True)
    obj_kx = models.CharField(max_length=100, blank=False,unique=False, null=True)
    obj_ko = models.CharField(max_length=100, blank=False,unique=False, null=True)
    obj_ij_st = models.CharField(max_length=100, blank=False,unique=False, null=True)
    obj_year_stavka = models.CharField(max_length=100, blank=False,unique=False, null=True)
    obj_year_price = models.CharField(max_length=100, blank=False,unique=False, null=True)
    obj_im_type = models.CharField(max_length=100, blank=False,unique=False, null=True)
    obj_cont_url = models.CharField(max_length=100, blank=False,unique=False, null=True)


    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name