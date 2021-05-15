from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Hospital, Patient, BedAllocation
from django.db.models import Sum
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import PatientForm
from django.shortcuts import redirect

# Create your views here.
# from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello world. You're at the polls index.")

# def index(request):
#     return render(request, 'beds/summary.html')
# @login_required
# def dashboard(request):
#     return render(request, 'beds/dashboard.html')

def index(request):
    normal_beds = Hospital.objects.aggregate(total=Sum('normal_beds'))
    covid_beds = Hospital.objects.aggregate(total=Sum('covid_beds'))
    icu = Hospital.objects.aggregate(total=Sum('icu_beds'))
    ventilator = Hospital.objects.aggregate(total=Sum('ventilator'))

    page = request.GET.get('page', 1)
    hospital_list = Hospital.objects.all()
    paginator = Paginator(hospital_list, 5)
    try:
        hospitals = paginator.page(page)
    except PageNotAnInteger:
        hospitals = paginator.page(1)
    except EmptyPage:
        hospitals = paginator.page(paginator.num_pages)

    context = {
        'normal_beds': normal_beds,
        'covid_beds': covid_beds,
        'icu': icu,
        'ventilator': ventilator,
        'hospitals': hospitals
    }
    return render(request, 'beds/summary.html', context)

@login_required
def dashboard(request):
    
    return render(request, 'beds/dashboard.html')

def patient_reg(request):
    form = PatientForm(request.POST or None)
    context= {
    'form':form
    }
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'beds/patient_registration.html', context)