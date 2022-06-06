from django.shortcuts import render, redirect
from django.views import generic as views

# Create your views here.
from job_app.crawl.crawl import crawl_data_from_jobs_ch
from job_app.crawl.models import Job


class IndexPage(views.TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # self.object is a Profile instance
        jobs = Job.objects.all()
        context['jobs']=jobs
        return context



def StoreNewJobs(request):
    crawl_data_from_jobs_ch()
    return redirect('index')


