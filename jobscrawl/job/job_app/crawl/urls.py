from django.urls import path

from job_app.crawl.views import IndexPage

urlpatterns = [
    path('',IndexPage.as_view()),
]