from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=15)
    password = forms.CharField(max_length=25, widget=forms.PasswordInput)
    
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        
class PasswordVerificationForm(forms.Form):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(PasswordVerificationForm, self).__init__(*args, **kwargs)

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not self.user.check_password(password):
            raise forms.ValidationError('Incorrect password')
        return password
    
# from django import forms
# from .models import Cuestionario, Pregunta

# class CuestionarioForm(forms.ModelForm):
#     class Meta:
#         model = Cuestionario
#         fields = ('titulo', 'descripcion', 'asistencia')

# class PreguntaForm(forms.ModelForm):
#     class Meta:
#         model = Pregunta
#         fields = ('texto',)

# PreguntaFormSet = forms.inlineformset_factory(
#     Cuestionario,
#     Pregunta,
#     form=PreguntaForm,
#     extra=3,  # minimum number of questions
#     max_num=40,  # maximum number of questions
#     validate_max=True
# )