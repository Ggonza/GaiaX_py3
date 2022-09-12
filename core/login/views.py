from django.contrib import messages
from django.contrib.auth.views import LoginView, FormView, AuthenticationForm
from django.urls import reverse_lazy
from django.shortcuts import render, HttpResponseRedirect, redirect
from core.comedor.models import UserUser
from django.contrib.auth import login, authenticate,logout

class loginFormView (FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = 'comedor:AdmGeneral'

    # def login_user(request):
    #     if request.method == "POST":
    #         username = request.POST.get['username']
    #         password = request.POST.get ['password']
    #         user = authenticate(request, username = username, password = password)
    #         uzer = request.user.id
    #         print('asd: ',uzer)
    #
    #         if user is not None:
    #             login(request, user)
    #             return HttpResponseRedirect('comedor:AdmGeneral')
    #             print('IIIIIID::', user.id)
    #         else:
    #             messages.success('Hubo un error al loggear usuario')
    #             return HttpResponseRedirect('login:loginUser')
    #     else:
    #         return render(request, 'auth fail')

    # def dispatch(self, request, *args, **kwargs):
    #     varTest = request.user.id
    #     return super().dispatch(request,*args,**kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        aa= self.request.user.id
        query = UserUser.objects.get(id=aa).rol_idrol.rol_name
        if query == 'rector':
            return redirect('comedor:AdmGeneral')
        if query == 'profesor':
            return redirect('comedor:listasUsc')
        if query == 'cocinero':
            return redirect('comedor:CocinaProd')
        return redirect(self.success_url)
# sobreescribiendo el metodo CONTEXTDATA
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'GAIA sesión'
        return context

def logout_view(request):
    logout(request)
    return render(request,'login.html')
