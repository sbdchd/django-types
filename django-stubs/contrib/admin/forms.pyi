from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, _UserType

class AdminAuthenticationForm(AuthenticationForm[_UserType]):
    required_css_class: str = ...

class AdminPasswordChangeForm(PasswordChangeForm[_UserType]):
    required_css_class: str = ...
