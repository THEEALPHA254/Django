from django.contrib import admin

# Register your models here.
from .models import Fee_balance
admin.site.register(Fee_balance)

from .models import Fee_payments
admin.site.register(Fee_payments)

