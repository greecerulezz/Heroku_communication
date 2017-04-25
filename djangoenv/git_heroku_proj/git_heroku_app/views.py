from django.http import HttpResponse
from django.views.generic.base import View


class HomePageView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("<h2>Hello World!!!</h2>"
                            "<img src='http://www.amir.ninja/content/images/2015/12/Hello-World.png' width='600'>")

