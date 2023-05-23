from django.urls import path
from basic_app import views
app_name="basic_app"
urlpatterns=[
    path("other/",views.other,name="other"),
    path('relative/',views.relative_urls_templates),
    path('base/',views.base,name="base"),
]