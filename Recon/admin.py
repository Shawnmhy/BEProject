from django.contrib import admin
from Recon.models import Genes, Metabolites, Reactions, Reactionsmeta, Feedback
from django.db.models import Q
from functools import reduce

# Register your models here.


class MetaboliteAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name']

    def get_search_results(self, request, queryset, search_term):
        if '*' in search_term:
            search_term = search_term.replace('*', '.*')
            return queryset.filter(reduce(lambda x, y: x | y,
                                          [Q(**{'{}__iregex'.format(field): search_term})
                                           for field in self.search_fields])), True
        return super().get_search_results(request, queryset, search_term)


class ReactionAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name']

    def get_search_results(self, request, queryset, search_term):
        if '*' in search_term:
            search_term = search_term.replace('*', '.*')
            return queryset.filter(reduce(lambda x, y: x | y,
                                          [Q(**{'{}__iregex'.format(field): search_term})
                                           for field in self.search_fields])), True
        return super().get_search_results(request, queryset, search_term)


class GeneAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name']

    def get_search_results(self, request, queryset, search_term):
        if '*' in search_term:
            search_term = search_term.replace('*', '.*')
            return queryset.filter(reduce(lambda x, y: x | y,
                                          [Q(**{'{}__iregex'.format(field): search_term})
                                           for field in self.search_fields])), True
        return super().get_search_results(request, queryset, search_term)


class ReactionmetaAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name']

    def get_search_results(self, request, queryset, search_term):
        if '*' in search_term:
            search_term = search_term.replace('*', '.*')
            return queryset.filter(reduce(lambda x, y: x | y,
                                          [Q(**{'{}__iregex'.format(field): search_term})
                                           for field in self.search_fields])), True
        return super().get_search_results(request, queryset, search_term)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'date',)
    search_fields = ('name', 'email',)
    date_hierarchy = 'date'


admin.site.register(Genes, GeneAdmin)
admin.site.register(Metabolites, MetaboliteAdmin)
admin.site.register(Reactions, ReactionAdmin)
admin.site.register(Reactionsmeta, ReactionmetaAdmin)
admin.site.register(Feedback, FeedbackAdmin)


