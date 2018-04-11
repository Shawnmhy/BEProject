from django.views import generic
from .models import Reactionsmeta, Metabolites, Reactions, Genes
from django.shortcuts import render
import json
from graphviz import Digraph
import networkx


class HomepageView(generic.ListView):
    template_name = 'Recon/HomePage.html'
    context_object_name = 'Reactions_object'

    def get_queryset(self):
        return Reactionsmeta.objects.all()


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


class GeneIndex(generic.ListView):
    template_name = 'Recon/gene_index.html'
    context_object_name = 'Gene_object'

    def get_queryset(self):
        return Genes.objects.all()


class GeneDetail(generic.DetailView):
    model = Genes
    template_name = 'Recon/gene_detail.html'



class GraphView(generic.ListView):
    model = Reactionsmeta
    template_name = 'Recon/Graph.html'


def search(request):
    q = request.GET.get("q")
    if '$' in q:
        q = q.replace('$', '.*')
    if q:
        ReactResul = Reactionsmeta.objects.filter(id__contains=q)
        MetaResul = Metabolites.objects.filter(id__contains=q)
        GeneResul = Genes.objects.filter(id__contains=q)

    else:
            # you may want to return Customer.objects.none() instead
        ReactResul= Reactionsmeta.objects.all()
        GeneResul = Genes.objects.all()
        MetaResul = Metabolites.objects.all()
    context = dict(result_1=MetaResul, q=q, result_2=ReactResul, result_3 = GeneResul)
    return render(request, "Recon/search.html", context)





