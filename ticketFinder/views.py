from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from ticketFinder.utils import render_to_pdf #created in step 4

# Create your views here.
def index(request):
    return render(request, 'index.html')

def GET_eCode(request):
    ecode = request.GET.get('eCode')

class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('pdf.html')
        context = {
            "invoice_id": 123,
            "customer_name": "John Cooper",
            "amount": 1399.99,
            "today": "Today",
        }
        html = template.render(context)
        pdf = render_to_pdf('pdf.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "pdf%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response