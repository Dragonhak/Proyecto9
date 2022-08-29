from django 						import forms
from django.contrib.auth.forms 		import UserCreationForm
from django.core.exceptions   		import ValidationError
from usuarios.models      			import Usuario

class UsuarioForm(UserCreationForm):
	username = forms.CharField(label="Nombre de usuario", required=True, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese nombre de usuario"}))
	first_name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese su nombre"}))
	last_name = forms.CharField(label="Apellido", required=True, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese su apellido"}))
	dni = forms.IntegerField(label="DNI", required=True, widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Ingrese su DNI"}))
	email = forms.EmailField(label="Correo", required=True, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese su direccion de correo"}))
	password1 = forms.CharField(label="Contraseña", required=True, widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Ingrese su contraseña"}))
	password2 = forms.CharField(label="Confirmación de contraseña", required=True, widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Confirmación de contraseña"}))

	class Meta:
		model = Usuario
		fields = ("first_name", "last_name", "username", "dni", "email")

	def clean_username(self):
		username = self.cleaned_data["username"]
		if not username.isalpha():
			raise ValidationError("El nombre de usuario no puede incluir numeros")
		return username