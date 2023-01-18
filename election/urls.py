"""election URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from e_vote.views import index_view, sign_up_view
from e_vote.views import home_view
from e_vote.views import position_view, edit_position_view, delete_position_view
from e_vote.views import edit_candidate_view, delete_candidate_view, add_candidate_view, candidate_view
from e_vote.views import voter_view, edit_voter_view, delete_voter_view, add_voter_view
from e_vote.views import vote_view, edit_vote_view, delete_vote_view, add_vote_view, candidate_pdf_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index page'),
    path('sign_up/', sign_up_view, name='sign_up_page'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('home_view/', home_view, name='home page'),
    path('position/', position_view, name='position_page'),
    path('edit_position/<int:position_id>/',
         edit_position_view, name='edit_position_page'),
    path('delete_position/<int:position_id>/',
         delete_position_view, name='delete_position_page'),

    path('candidate/', candidate_view, name="candidate_page"),
    path('add_candidate/', add_candidate_view, name="add_candidate_page"),
    path('edit_candidate/<int:candidate_id>/',
         edit_candidate_view, name='edit_candidate_page'),
    path('delete_candidate/<int:candidate_id>/',
         delete_candidate_view, name='delete_candidate_page'),
    path('candidate_pdf/', candidate_pdf_view, name="candidate_pdf_page"),

    path('voter/', voter_view, name='voter_page'),
    path('add_voter/', add_voter_view, name='add_voter_page'),
    path('edit_voter/<int:voter_id>/', edit_voter_view, name='edit_voter_page'),
    path('delete_voter/<int:voter_id>/',
         delete_voter_view, name='delete_voter_page'),

    path('vote/', vote_view, name='vote_page'),
    path('add_vote/', add_vote_view, name='add_vote_page'),
    path('edit_vote/<int:vote_id>/', edit_vote_view, name='edit_vote_page'),
    path('delete_vote/<int:vote_id>/', delete_vote_view, name='delete_vote_page')

]
