from django.contrib import admin
# Register your models here.
from .models import Hospital,Patient,BedAllocation

# admin.site.register(Hospital)   #These are default
# admin.site.register(Patient)
# admin.site.register(BedAllocation)


#Customizing

admin.site.site_header = "COVID PORTAL"
admin.site.site_title = "Covid Portal"
admin.site.site_url = "/beds"

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    fieldsets = (
        (None,{
            'fields': ('name','location','district','phone','sector')
        }),
        ('Bed Information',{
            'fields': ('covid_beds','normal_beds','icu_beds','ventilator')
        }),
        ('User Information', {
        'fields': ('user',)
        }),
    )

    list_display = ('upper_case_name','location','covid_beds','normal_beds','icu_beds','ventilator','total_beds')  #display details in frontpage

    @admin.display(description='Name')
    def upper_case_name(self,obj):
        return("%s" % (obj.name)).upper()   

    @admin.display(description='Total Beds' )
    def total_beds(self,obj):
        total_beds = obj.covid_beds+obj.normal_beds+obj.icu_beds+obj.ventilator
        return total_beds



    list_filter = ('district','sector') #creating filter option
    radio_fields = {"sector": admin.HORIZONTAL} #making sector coloumn as radio buttons
    ordering=['name'] #sorting according to name
    search_fields = ['name','location'] #creating a search bar
    

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display=('name','location','phone','category','status')
    search_fields = ['name','location'] #creating a search bar
    list_filter = ('location', 'district')


@admin.register(BedAllocation)
class BedAllocationAdmin(admin.ModelAdmin):
    raw_id_fields = ('patient','hospital')    #search bar appears in bed allocation near patient and hospital
    list_display = ('patient','hospital','category')

    def save_model(self, request, obj, form, change):
        patient = Patient.objects.get(pk = obj.patient.id)
        patient.status = 'A'
        patient.save()  #To automatically change patient status to admitted when a bed is allocated

        hospital = Hospital.objects.get(pk = obj.hospital.id)
        if obj.category == 'C':
            hospital.covid_beds = hospital.covid_beds-1
        hospital.save()              #to reduce number of covid beds when covid patients admitted
        super().save_model(request, obj, form, change)    