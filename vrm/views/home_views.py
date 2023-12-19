from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache




# @method_decorator(never_cache, name='dispatch')
@method_decorator(login_required, name='dispatch')
class Home(View):
    
    # @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        
        return render(request, 'generic.html')



