from django.urls import path, re_path
from . import views

urlpatterns = [
    #HomePage
    path('', views.HomepageView.as_view(), name='homepage'),

    #general information
    re_path('^reaction/$', views.IndexView.as_view(), name = 'reactions_index'),

    #detail reaction
    re_path(r'^reaction/(?P<pk>\w+)/$', views.DetailView.as_view(), name = 'detail_reaction'),

     #metabolite_detail
    re_path(r'^metabolite/(?P<pk>\w+)/$', views.MetaboliteDetail.as_view(), name='detail_metabolite'),

    # metabolite_index
    re_path(r'^metabolite/$', views.MetaboliteIndex.as_view(), name = 'metabolite_index'),

    # gene_index
    re_path(r'^gene/$', views.GeneIndex.as_view(), name = 'gene_index'),

    # gene_detail
    re_path(r'^gene/(?P<pk>\w+)/$', views.GeneDetail.as_view(), name='gene_detail'),

    re_path(r'^search/$', views.search, name='search'),

    #Generate combine graph

    path(r'^search/', views.search, name='search_result'),

    path('', views.HomepageView.as_view(success_url='/Recon/'), name='feedback'),

    #File Upload

    re_path(r'^upload/$', views.upload, name='upload'),

    #step 2 set constraints
    re_path(r'^upload/set_constraints/$', views.constraints, name='set_constraints'),



]