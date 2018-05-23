import os
from os.path import join
from django.views import generic
from .models import Reactionsmeta, Metabolites, Reactions, Genes
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse, Http404
from .forms import FeedbackForm
from django.contrib import messages
from cobra import core,test, io
from django.db.models import Q
from io import StringIO
from django.conf import settings
import sys
from gurobipy import *
import numpy
from libsbml import *
class HomepageView(generic.TemplateView):
    template_name = 'Recon/HomePage.html'
    context_object_name = 'Reactions_object'
    success_url = '/Recon/'

    def get(self, request, **kwargs):
        form = FeedbackForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            messages.add_message(request, messages.INFO, 'Feedback Submitted.')
            form.save()
            return redirect('feedback')
        return render(request, self.template_name, {'form': form})



class IndexView(generic.ListView):
    template_name = 'Recon/index.html'
    context_object_name = 'Reactions_object'

    def get_queryset(self):
        return Reactionsmeta.objects.all()


class MetaboliteIndex(generic.ListView):
    template_name = 'Recon/metabolites.html'
    context_object_name = 'Metabolite_object'

    def get_queryset(self):
        return Metabolites.objects.all()


class DetailView(generic.DetailView):
    model = Reactionsmeta
    template_name = 'Recon/reactions_detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['metabolites'] = Metabolites.objects.all()
        context['reactions'] = Reactions.objects.all()
        return context


class MetaboliteDetail(generic.DetailView):
    model = Metabolites
    template_name = 'Recon/metabolite_detail.html'

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        context = super(MetaboliteDetail, self).get_context_data(**kwargs)
        context['reactions'] = Reactions.objects.all()
        context['reactioninfo'] = Reactionsmeta.objects.filter(Q(metabolite1=pk)|Q(metabolite2=pk)|Q(metabolite3=pk) | Q(metabolite4=pk) |
                                                               Q(metabolite5=pk)|Q(metabolite6=pk)|Q(metabolite7=pk) |
                                                               Q(metabolite8=pk)|Q(metabolite8=pk)|Q(metabolite9=pk) |
                                                               Q(metabolite10=pk)|Q(metabolite11=pk)|Q(metabolite12=pk) |
                                                               Q(metabolite13=pk)|Q(metabolite14=pk)|Q(metabolite15=pk) |
                                                               Q(metabolite16=pk)|Q(metabolite17=pk)|Q(metabolite18=pk) |
                                                               Q(metabolite19=pk)|Q(metabolite20=pk)|Q(metabolite21=pk) |
                                                               Q(metabolite22=pk)|Q(metabolite23=pk)|Q(metabolite24=pk) |
                                                               Q(metabolite25=pk)|Q(metabolite26=pk)|Q(metabolite27=pk) |
                                                               Q(metabolite28=pk)|Q(metabolite29=pk)|Q(metabolite30=pk) |
                                                               Q(metabolite31=pk)|Q(metabolite32=pk)|Q(metabolite33=pk) |
                                                               Q(metabolite34=pk)|Q(metabolite35=pk)|Q(metabolite36=pk) |
                                                               Q(metabolite37=pk)|Q(metabolite38=pk)|Q(metabolite39=pk) |
                                                               Q(metabolite40=pk)|Q(metabolite41=pk)|Q(metabolite42=pk) |
                                                               Q(metabolite43=pk)|Q(metabolite44=pk)|Q(metabolite45=pk) |
                                                               Q(metabolite46=pk) | Q(metabolite47=pk) | Q(metabolite48=pk) |
                                                               Q(metabolite49=pk) | Q(metabolite50=pk) | Q(metabolite51=pk) |
                                                               Q(metabolite52=pk) | Q(metabolite53=pk) | Q(metabolite54=pk) |Q(metabolite55=pk) |
                                                               Q(metabolite56=pk) | Q(metabolite57=pk) | Q(metabolite58=pk) |Q(metabolite59=pk) |
                                                               Q(metabolite60=pk))
        return context

    def post(self, request, *args, **kwargs):
        selected = request.POST.getlist('checkbox', [])
        element = Reactionsmeta.objects.filter(pk__in=selected)
        reaction = Reactionsmeta.objects.all()
        context = dict(graphobject=selected, graphelement=element, graphurl=reaction)
        return render(request, 'Recon/combinegraph.html', context)


class GeneIndex(generic.ListView):
    template_name = 'Recon/gene_index.html'
    context_object_name = 'Gene_object'

    def get_queryset(self):
        return Genes.objects.all()


class GeneDetail(generic.DetailView):
    model = Genes
    template_name = 'Recon/gene_detail.html'



def search(request):
    q = request.GET.get("q")
    if '*' in q:
        q = q.replace('*', '.*')
    if q:
        ReactResul = Reactionsmeta.objects.filter(id__iregex=q)
        MetaResul = Metabolites.objects.filter(id__iregex=q)
        GeneResul = Genes.objects.filter(id__iregex=q)

    else:
            # you may want to return Customer.objects.none() instead
        ReactResul= Reactionsmeta.objects.all()
        GeneResul = Genes.objects.all()
        MetaResul = Metabolites.objects.all()
    context = dict(result_1=MetaResul, q=q, result_2=ReactResul, result_3 = GeneResul)
    return render(request, "Recon/search.html", context)


class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout


def upload(request):
    if request.method == "POST":
        handle_upload_file(request.FILES['file'], str(request.FILES['file']))
        return HttpResponseRedirect('/Recon/upload/set_constraints')
    return render(request, 'Recon/upload.html')


def constraints(request):
    if request.method == "POST":
        handle_upload_file(request.FILES['file'], str(request.FILES['file']))
        filename = request.FILES['file'].name
        if filename == "3HAO.lp":
           gurobi = gurobipy.read("/Users/mihaoyang/Desktop/BEProject7/Recon/File/3HAO.lp")
           with Capturing() as output:
               gurobi.optimize()
           model = io.read_sbml_model("/Users/mihaoyang/Desktop/BEProject7/Recon/File/Recon2_2.xml")
           model.objective = "3HAO"
           with Capturing() as output1:
               model.summary()
               model.optimize().objective_value
           context = dict(a1=output, a2=output1)
           return render(request, 'Recon/set_constraints.html', context)

        if filename == "2AMADPTm.lp":
            gurobi = gurobipy.read("/Users/mihaoyang/Desktop/BEProject7/Recon/File/2AMADPTm.lp")
            with Capturing() as output:
                gurobi.optimize()
            model = io.read_sbml_model("/Users/mihaoyang/Desktop/BEProject7/Recon/File/Recon2_2.xml")
            model.objective = "2AMADPTm"
            with Capturing() as output1:
                model.summary()
                model.optimize().objective_value
            context = dict(a1=output, a2=output1)
            return render(request, 'Recon/set_constraints.html', context)

        if filename == "2HATVLACthc.lp":
            gurobi = gurobipy.read("/Users/mihaoyang/Desktop/BEProject7/Recon/File/2HATVLACthc.lp")
            with Capturing() as output:
                gurobi.optimize()
            model = io.read_sbml_model("/Users/mihaoyang/Desktop/BEProject7/Recon/File/Recon2_2.xml")
            model.objective = "2HATVLACthc"
            with Capturing() as output1:
                model.summary()
                model.optimize().objective_value
            context = dict(a1=output, a2=output1)

            return render(request, 'Recon/set_constraints.html', context)
    return render(request,'Recon/set_constraints.html')


def handle_upload_file(file, filename):
    path = 'Recon/File/'
    if not os.path.exists(path):
        os.makedirs(path)
    with open(path + filename, 'wb+')as destination:
        for chunk in file.chunks():
            destination.write(chunk)



