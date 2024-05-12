from django.contrib import admin
from .models import Doctor,Patient,Appointment,PatientDischargeDetails,ContactModel

from django.contrib import admin
from .models import ProductCategory, Product, Comment, Order
# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Doctor, DoctorAdmin)

class PatientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Patient, PatientAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Appointment, AppointmentAdmin)

class PatientDischargeDetailsAdmin(admin.ModelAdmin):
    pass
admin.site.register(PatientDischargeDetails, PatientDischargeDetailsAdmin)

class ContactModelAdmin(admin.ModelAdmin):
    pass
admin.site.register(ContactModel, ContactModelAdmin)

admin.site.register(ProductCategory)
admin.site.register(Comment)
admin.site.register(Order)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)