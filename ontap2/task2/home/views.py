from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Beer, Reviewer, BeerInstance

@login_required
def home(request):
     # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    return render(request, 'home.html', context={ 'num_visits': num_visits})

@login_required
def beer_detail(request, id):
    try:
        beer = Beer.objects.get(id=id)
    except Beer.DoesNotExist:
        raise Http404('Beer not found')
    return render(request, 'beer_detail.html', {'beer': beer})

@login_required
def reviewer_detail(request, id):
    try:
        beer = Reviewer.objects.get(id=id)
    except Reviewer.DoesNotExist:
        raise Http404('Beer not found')
    return render(request, 'beer_detail.html', {'reviewer': reviewer})

from django.views import generic

class BeerListView(LoginRequiredMixin, generic.ListView):
    model = Beer
    paginate_by = 10
login_url = '/login/'	
redirect_field_name = 'redirect_to'	

class ReviewerListView(LoginRequiredMixin, generic.ListView):
    model = Reviewer
    paginate_by = 10
login_url = '/login/'	
redirect_field_name = 'redirect_to'


class BeerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Beer
login_url = '/login/'	
redirect_field_name = 'redirect_to'

class ReviewerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Reviewer
login_url = '/login/'	
redirect_field_name = 'redirect_to'

class BeerReviewDetailView(LoginRequiredMixin, generic.DetailView):
    model = BeerInstance
login_url = '/login/'	
template_name ='C:/Users/sjdix/ontap2/task2/home/templates/home/beerreview-detail.html'
redirect_field_name = 'redirect_to'

class ReviewerBeersByall(LoginRequiredMixin,generic.ListView):
    model = BeerInstance
    template_name ='C:/Users/sjdix/ontap2/task2/home/templates/home/all-reviews.html'
    paginate_by = 10

class ReviewerBeersByUserListView(LoginRequiredMixin,generic.ListView):
    model = BeerInstance
    template_name ='C:/Users/sjdix/ontap2/task2/home/templates/home/beerinstance_list_reviewer_user.html'
    paginate_by = 10
    
    def get_queryset(self):
        return BeerInstance.objects.filter(reviewer=self.request.user).order_by('review_date')
