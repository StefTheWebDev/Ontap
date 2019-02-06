from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('beers/', views.BeerListView.as_view(), name='beers'),
    path('reviewers/', views.ReviewerListView.as_view(), name = 'reviewers'),
    path('beer/<int:pk>', views.BeerDetailView.as_view(), name='beer-detail'),
	path('beer/<int:pk>', views.BeerDetailView.as_view(), name='beer_detail'),
    path('reviewer/<int:pk>', views.ReviewerDetailView.as_view(), name='reviewer_detail'),
]
urlpatterns += [   
    path('myreviews/', views.ReviewerBeersByUserListView.as_view(), name='my-reviewer'),
]

urlpatterns += [   
    path('beer/', views.ReviewerBeersByall.as_view(), name='all-reviews'),
]