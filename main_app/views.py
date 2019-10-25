from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "index.html"

    # this method send data to index page
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        # set name to name and country variables
        context['name'] = "Srianth"
        context['country']="Bangladesh"

        # declare and define list
        list = [1,2,3,4,5]
        context['list'] = list

        return context

class AboutView(TemplateView):
    template_name = "about.html"


class PortfolioView(TemplateView):
    template_name = "portfolio.html"

    # this method send data to index page
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        # set name to name and country variables
        context['name'] = "Srianth"
        context['country']="Bangladesh"

        return context