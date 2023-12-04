from django.contrib import admin

from .models import Regions
from .models import District
from .models import ObjectType
from .models import ObjectsDesk
from .models import ObjectsGoal
from .models import ObjectsDesk1
from .models import Objects_main

admin.site.register(Regions)
admin.site.register(District)
admin.site.register(ObjectType)
admin.site.register(ObjectsDesk)
admin.site.register(ObjectsGoal)
admin.site.register(ObjectsDesk1)
admin.site.register(Objects_main)