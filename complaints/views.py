from django.shortcuts import render, redirect
from .models import Complaint, auto_tag
from .forms import ComplaintForm
from django.http import HttpResponse
import csv

def complaint_list_create(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.tag = auto_tag(complaint.description)
            complaint.save()
            return redirect('complaint_list')
    else:
        form = ComplaintForm()

    complaints = Complaint.objects.all()
    return render(request, 'complaint_list.html', {'form': form, 'complaints': complaints})

def download_complaints_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="complaints.csv"'

    writer = csv.writer(response)
    writer.writerow(['Title', 'Description', 'Tag'])

    for complaint in Complaint.objects.all():
        writer.writerow([complaint.title, complaint.description, complaint.tag])

    return response
 
