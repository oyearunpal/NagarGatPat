from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from datetime import date
from django.utils import timezone
	
from django.db import models
from shakha.models import Swaymsevak
# Create your models here.

@python_2_unicode_compatible  # only if you need to support Python 2
class Book(models.Model):
	'''
	Description : Details about books
	'''
	name = models.CharField("Name of Book", max_length=50)
	price = models.PositiveSmallIntegerField(blank=True,null=True)
	publication = models.CharField(max_length=50,blank=True,null=True)
	Type_Choices =(
	('01','Bal'),
	('02','Bhakti'),
	('03','Dharma'),
	('04','Geet'),
	('05','Guruji'),
	('06','Inspiration'),
	('07','Jivani'),
	('08','Kahani'),
	('09','Kavita'),
	('10','Lekh Sangrah'),
	('11','Pravachan Sangrah'),
	('12','Rashtra'),
	('13','Sangh'),
	('14','Shakha'),
	('15','Smiriti'),
	('16','Speech'),
	('17','Suvichar'),
	('18','Vivekanand'),
	('19','Vyakti Vikas'),
	('20','Yoga'),
		)
	Language_Type = (
		('1','Hindi'),
		('2','English'),
		('3','Marathi'),
		('4','Gujrati'),
		('5','Others'),
		)

	book_type = models.CharField("Type of Book",max_length=2,choices=Type_Choices,default='1')
	language = models.CharField(max_length=1,choices=Language_Type,default='1')
	copies = models.PositiveSmallIntegerField(default=1)
	cover_image = models.ImageField(upload_to='books/',blank=True,null=True)
	def __str__(self):
	    	return self.name


@python_2_unicode_compatible  # only if you need to support Python 2
class Issue_Book(models.Model):
	'''
	Description : All transaction's detail
	'''
	book=models.ForeignKey(Book);
	swaymsevak=models.ForeignKey('shakha.Swaymsevak')
	check_in = models.DateField(auto_now_add=True,editable=True)
	# check_in.editable=True
	check_out = models.DateTimeField(auto_now=True)
	feedback = models.CharField(max_length=100, blank=True,null=True)
	rate = models.PositiveSmallIntegerField("Rate out of Five",blank=True,null=True)
	def __str__(self):
		    	return self.swaymsevak

