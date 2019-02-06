from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Beer(models.Model):
	beer_name = models.CharField(max_length=150)
	brewery_name = models.CharField(max_length=150)
	description = models.TextField()
	Reviewer = models.ForeignKey('Reviewer', on_delete=models.SET_NULL, null=True)
	
	def __str__(self):
		return self.beer_name + ' - ' + self.brewery_name
class Meta:
	permissions = (("can_change_availability", "Set tour as available"),)




class Reviewer(models.Model):

	PROVIDER_CHOICES =(
		('Garage Project', 'Garage Project'),
		('Tuatara', 'Tuatara'),
	)

	reviewer_first_name = models.CharField(max_length=30)
	reviewer_last_name = models.CharField(max_length=30)
	email_address = models.CharField(max_length=30)
	phone_number = models.CharField(max_length=15)
	provider = models.CharField(choices=PROVIDER_CHOICES, max_length=30)

	def __str__(self):
		return self.reviewer_first_name + ' ' + self.reviewer_last_name + ' - ' + self.provider

import uuid # Required for unique book instances

class BeerInstance(models.Model):
	beer = models.ForeignKey('Beer', on_delete=models.SET_NULL, null=True) 
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular tour across whole library")
	review_date = models.DateField(null=True, blank=True)
	description = models.CharField(max_length=500, help_text="This is the grey text")
	reviewer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	
	@property
	def is_in_progress(self):
		if self.review_date and date.today() > self.review_date:
			return True
		return False

	BEER_STATUS = (
		('1', 'Bad'),
		('2', 'Ok'),
		('3', 'good'),
		('4', 'Amazing'),
		('5', 'Exceptional')
	)

	status = models.CharField(max_length=1, choices=BEER_STATUS, blank=True, default='o', help_text='Beer Rating')
class Meta:
	permissions = (("can_mark_rating", "Set rating for beer"),) 