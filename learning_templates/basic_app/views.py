from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict={'hello':'helloworld','number':1000}
    return render(request, 'basic_app/index.html',context_dict)
def base(request):
    return render(request, 'basic_app/base.html')
def other(request):
    return render(request, 'basic_app/other.html')
def relative_urls_templates(request):
    return render(request, 'basic_app/relative_url_templates.html')
