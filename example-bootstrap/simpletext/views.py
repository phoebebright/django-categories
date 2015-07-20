
from django import forms
from django.core.urlresolvers import reverse_lazy

from django.utils.translation import ugettext_lazy as _
from django.views.generic.edit import  ModelFormMixin

from django.views.generic.edit import CreateView, UpdateView, DeleteView, ModelFormMixin
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from django import forms
from django.conf import settings

from .models import SimpleText



class TxtForm(forms.ModelForm):


    class Meta:
        model = SimpleText
        fields = '__all__'

class TxtListView(ListView):

    model = SimpleText
    fields = '__all__'


class TxtDetailView(DetailView):

    model = SimpleText
    fields = '__all__'


class TxtAddView(CreateView):

    form_class = TxtForm
    model = SimpleText



class TxtEditView(UpdateView):

    model = SimpleText
    form_class = TxtForm



