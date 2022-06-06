from django.shortcuts import render
from django.views import generic as views

# Create your views here.
from job_app.crawl.models import Job


class IndexPage(views.TemplateView):
    template_name = 'index.html'



def StoreNewJobs():
    pass
    # new_jobs=Job(
    #
    # )
    # new_jobs.save()

