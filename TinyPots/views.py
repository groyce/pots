from django.views.generic import TemplateView

class AboutPage(TemplateView):
    template_name = 'about.html'

class ContactPage(TemplateView):
    template_name = 'contact.html'

class ShippingPage(TemplateView):
    template_name = 'shipping.html'

class SplashPage(TemplateView):
    template_name = 'index.html'

class TempHomePage(TemplateView):
    template_name = 'base.html'
