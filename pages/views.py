from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from pages.models import ViewType


# two types of views
# function based views
@login_required
def test(request: HttpRequest, ) -> HttpResponse:
    # return HttpResponse("<h1>Test works</h1>")
    # view_types = ["function based views", "class based views"]
    view_types = ViewType.objects.all()
    return render(request, "pages/test.html",
                  {"view_types": view_types})


# class based views
class TestView:
    def get(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse("Test works")


class HomeView(TemplateView):
    template_name = 'home.html'
