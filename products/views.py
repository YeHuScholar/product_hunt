from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from 

# Create your views here.


def product_list(request):
    return render(request, 'product_list.html')

@login_required()
def publish(request):
    if request.method == 'GET':
        return render(request, "publish.html")
    elif request.method == 'POST':
        title = request.POST['标题']
        intro = request.POST['介绍']
        url = request.POST['APP链接']
        icon = request.FILES['APP图标']
        image = request.FILES['大图']

        product = Product()
        return render(request, 'publish.html')
