from haystack import indexes
from Recon.models import Metabolites, Genes, Reactions


class GenesIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True,use_template=True)

    def get_model(self):
        return Genes

    def index_queryset(self, using=None):
        return self.get_model().objects.all()


class MetabolitesIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Metabolites

    def index_queryset(self, using=None):
        return self.get_model().objects.all()


class ReactionsIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Reactions

    def index_queryset(self, using=None):
        return self.get_model().objects.all()


