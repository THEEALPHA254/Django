from django.contrib import admin

# Register your models here.
from .models import Students
admin.site.register(Students)

from .models import Hostels
admin.site.register(Hostels)

from .models import HostelAllocation
admin.site.register(HostelAllocation)

