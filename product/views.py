from django.shortcuts import render
from django.views import View
from .models import Foods
# Create your views here.



class ListView(View):
    def get(self, request):
        food =Foods.objects.all().order_by('-pk')

        return render(request, 'food/food_list.html',{'food':food})
