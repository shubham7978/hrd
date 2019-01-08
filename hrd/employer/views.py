from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Job, Company
from django.template import loader


def index(request):
 #return HttpResponse("Hello,world. This is the employer view.")
 latest_job_list=Job.objects.order_by('-pub_date')[:5]
 #output=', '.join([j.title for j in latest_job_list])
 #return HttpResponse(output)
 #template=loader.get_template('employer/index.html')
 context= {
  'latest_job_list': latest_job_list,
 }
 #return HttpResponse(template.render(context, request))
 return render(request, 'employer/index.html', context)
# Create your views here.

def description(request, job_id):
 #return HttpResponse("You are looking at job  %s." % job_id)
 '''try:
  job=Job.objects.get(pk=job_id)
 except Job.DoesNotExist:
  raise Http404("Job does not exist")
 '''
 job=get_object_or_404(Job, pk=job_id)
 return render(request, 'employer/description.html', {'job':job})

