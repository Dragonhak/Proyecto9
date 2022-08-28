from django.shortcuts 		import render, redirect
from .forms 				import UsuarioForm

def registrar_usuario(request):
	template_name = "registrar.html"

	formulario = UsuarioForm()
	if request.method == "POST":
		formulario = UsuarioForm(request.POST)
		if formulario.is_valid():
			usuario = formulario.save()
			return redirect("login")

	ctx = {
		"form": formulario
	}
	return render(request, template_name, ctx)
