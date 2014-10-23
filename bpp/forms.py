# -*- encoding: utf-8 -*-

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Hidden
from crispy_forms_foundation.layout import Layout, Fieldset, ButtonHolder, Submit

from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.forms import AuthenticationForm


class MyAuthenticationForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kw):
        self.helper = FormHelper()
        self.helper.form_class = "custom"
        self.helper.form_action = '.'
        self.helper.layout = Layout(
            Fieldset(
                u'Zaloguj się!',
                'username',
                'password',
                Hidden(REDIRECT_FIELD_NAME, request.GET.get(REDIRECT_FIELD_NAME, "/bpp/"))),
             ButtonHolder(
                Submit('submit', u'Zaloguj się', css_id='id_submit'),
            ))
        AuthenticationForm.__init__(self, request, *args, **kw)
