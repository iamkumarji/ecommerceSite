from django.views import View
from django.shortcuts import render


class Termsandcondi(View):
    def get(self, request):
        """
        :param request: click on the recipe link
        :return: returns an HTML page redirecting to recipe page
        """
        context = {}
        return render(request, 'greeban/termsandcondi.html', context)

