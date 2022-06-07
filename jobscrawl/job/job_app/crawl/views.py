from django.shortcuts import render, redirect
from django.views import generic as views

# Create your views here.
from job_app.crawl.crawl_jobs_ch import crawl_data_from_jobs_ch
from job_app.crawl.models import Job
from  datetime import datetime


class IndexPage(views.TemplateView):
    """ start function, return context data for show in html"""
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # self.object is a Profile instance
        jobs = Job.objects.all().order_by('title')
        today=str(datetime.today()).split(' ')[0]
        context['jobs']=jobs
        context['today']=today

        return context



def StoreNewJobs(request):
    """ this function start the crawling and store the result to db"""
    crawl_data_from_jobs_ch()
    return redirect('index')


