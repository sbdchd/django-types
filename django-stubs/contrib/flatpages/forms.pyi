from typing import Any

import django.forms as forms

class FlatpageForm(forms.ModelForm):
    url: Any = ...
    def clean_url(self) -> str: ...
