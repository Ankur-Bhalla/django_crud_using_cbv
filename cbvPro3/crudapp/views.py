# CRUD (Create, Retreive, Update & Delete) operations using Class Based Views
# Use of TemplateView, ListView, DetailView, CreateView, UpdateView and DeleteView

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (View, TemplateView,
                                  ListView, DetailView,
                                  CreateView, DeleteView,
                                  UpdateView)
from . import models


# Create your views here.
class IndexView(TemplateView):
    # Just set this Class Object Attribute to the template page.
    # template_name = 'app_name/site.html'
    template_name = 'index.html'


class SchoolListView(ListView):
    # If you don't pass in this attribute,
    # Django will auto create a context name
    # for you with object_list!
    # Default would be 'school_list' i.e., (lower-case of model name School then _list)

    # Example of making our own:
    # context_object_name = 'schools'
    model = models.School  # here template name not passed. We need to create template as school_list.html
    # to link this view. Using href="{% url 'crudapp:list' %} in anchor tag of crudapp_base.html to call this view.


class SchoolDetailView(DetailView):
    # If you don't pass in this attribute,
    # Django will auto create a context name
    # for you with object
    # Default would be 'school' i.e., (lower-case of model name School only)

    # Example of making our own:
    # context_object_name = 'schools'
    context_object_name = 'school_detail'
    model = models.School
    # Create template name with same name as context_object_name
    template_name = "crudapp/school_detail.html"  # template_name is an attribute from DetailView class.


# CreateView -
# 1) Django CreateView is automatically creating a default html template that is expecting.
# It is expecting into be in format of all lower case model name (School and then _form)
# i.e., school_form.html. Always suggest to use default name for template and create school_form.html
# to add form to create new School.
# 2) Also, define a get_absolute_url method on the Model (here School). This is linked with CreateView to
# tell create view where to go after creating a page. Here, go back and reverse and figure out
# you should go to the detail page for whatever the primary key of school we have just created.
class SchoolCreateView(CreateView):
    fields = ("name", "principal", "location")
    model = models.School


class SchoolUpdateView(UpdateView):
    fields = ("name", "principal")  # this field will map to form which was created at school_form.html
    # for update
    model = models.School


class SchoolDeleteView(DeleteView):
    model = models.School  # create form in school_confirm_delete.html for delete
    success_url = reverse_lazy("crudapp:list")  # Once school is deleted call list of school view using reverse_lazy
