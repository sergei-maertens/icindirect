from django.views.generic import FormView

from .forms import ClaimForm


# TODO: should be throttled?

class ClaimView(FormView):
    form_class = ClaimForm
    template_name = 'claims/claim_form.html'
