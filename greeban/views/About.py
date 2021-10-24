from django.views import View
from django.shortcuts import render


class About(View):
    def get(self, request):
        """
        :param request: click on the recipe link
        :return: returns an HTML page redirecting to recipe page
        """
        context = {}
        return render(request, 'greeban/about_us.html', context)

