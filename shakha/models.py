from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from datetime import date
from django.utils import timezone
	
from django.db import models



# Create your models here.
@python_2_unicode_compatible  # only if you need to support Python 2
class Shakha(models.Model):
    """
    Description: Detail about shakha
    """
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    time = models.TimeField("Time when shakha start")
    
    DAYS_OF_WEEK = (
    ('0', 'Monday'),
    ('1', 'Tuesday'),
    ('2', 'Wednesday'),
    ('3', 'Thursday'),
    ('4', 'Friday'),
    ('5', 'Saturday'),
    ('6', 'Sunday'), 
    ('7','Daily'),  
    )

    days = models.CharField("Shakha Din",max_length=1, choices=DAYS_OF_WEEK,default='7')
    pic = models.ImageField(upload_to='images/',blank=True,null=True)
    def __str__(self):
	    	return self.name


@python_2_unicode_compatible  # only if you need to support Python 2
class Swaymsevak(models.Model):
    """
    Description: Basic list of swaymsevak
    """
    fname=models.CharField("first name",max_length=20)			
    mname = models.CharField("middle name", max_length=20,blank=True,null=True)
    lname = models.CharField("Last name", max_length=20)
    shakha=models.ForeignKey(Shakha,default=3)
    creted = models.DateField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
    	return self.fname+" "+self.mname+" "+self.lname


@python_2_unicode_compatible  # only if you need to support Python 2
class  Spersonal(models.Model):
	# addition additions in future job,
	"""
	Description: Personal information about each swaymsevak
	"""
	name= models.OneToOneField(
        Swaymsevak,
        on_delete=models.CASCADE,
        primary_key=True,
        default=1,
    )
	contact = models.CharField(max_length=10,blank=True,null=True )
	society = models.CharField(max_length=50,blank=True,null=True)
	basti = models.CharField(max_length=50,blank=True,null=True)
	dob = models.DateField("date of birth",blank=True,null=True)
	std =models.IntegerField(blank=True,null=True)
	location = models.CharField("Job or School location",max_length=50,blank=True,null=True)
	emailid= models.EmailField("Email Id",blank=True,null=True)
	degree = models.CharField(max_length=20,blank=True,null=True)
	def __str__(self):
		return self.name.fname+" "+self.name.mname+" "+self.name.lname
	def calculate_age(self):
		if self.dob :
			today = date.today()
			return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
	class Meta:
		verbose_name = "Personal Information Of Swaymsevak"
@python_2_unicode_compatible  # only if you need to support Python 2
class Gat(models.Model):
	name=models.CharField(max_length=30)
	shakha=models.ForeignKey(Shakha,default=3)

	gatnayak= models.OneToOneField(
        Swaymsevak,
        on_delete=models.CASCADE,
        default=1,
    )
	note=models.CharField(max_length=60, blank=True,null=True)
	def __str__(self):
		return self.name
		

@python_2_unicode_compatible  # only if you need to support Python 2
class Sshakha(models.Model):
	"""
	additionals in future : 
	
	"""
	"""
	Description: Shakha Related information about each swaymsevak
	"""
	name= models.OneToOneField(
        Swaymsevak,
        on_delete=models.CASCADE,
        primary_key=True,
        default=1,
    )
	Bool_Choice= (
    (True, 'yes'), (False, 'no')
    )
	Jimmedari_Choices=(
		('0','Tat'),
		('1','Pat'),
		('2','Gatnayak'),
		('3','Upgatnayak'),
		('4','Vyastha Pramukh'),
		('5','Geet Pramukh'),
		('6','Khel Pramukh'),
		('7','Gan Shikshak'),
		('8','Prathna Pramukh'),
		('9','Mukhy Shikshak'),
		('10','Shakha Karyvah'),
		('11','Palak'),
		)
	jimmedari = models.CharField(max_length=2, choices=Jimmedari_Choices,default='1')
	gat=models.ForeignKey(Gat,on_delete=models.CASCADE,default=7)
	topi = models.BooleanField(choices=Bool_Choice,default=False)
	shirt = models.BooleanField(choices=Bool_Choice,default=False)
	pant = models.BooleanField(choices=Bool_Choice,default=False)
	shocks = models.BooleanField(choices=Bool_Choice,default=False)
	shoes = models.BooleanField(choices=Bool_Choice,default=False)
	dand = models.BooleanField(choices=Bool_Choice,default=False)
	ganvesh_complete=models.BooleanField(choices=Bool_Choice,default=False)
	join_Year = models.PositiveSmallIntegerField("Year When You Join ", blank=True,null=True)
	Type_Choices= (
		('1','Bal'),
		('2','Tarun'),
		('3','Shishu'),
		('4','Praudh')
		)
	swaymsevak_type = models.CharField(max_length=1,choices=Type_Choices,blank=True,null=True,default='2') 
	def sangh_aayu(self):
		if self.dob :
			today = date.today()
			return today.year-self.year
	def __str__(self):
		return self.name.fname+" "+self.name.mname+" "+self.name.lname
	class Meta:
		verbose_name = "Shakha Related Information Of Swaymsevak"
	

@python_2_unicode_compatible  # only if you need to support Python 2
class Ghosh(models.Model):
	"""
	Description: List of Ghosh Swaymsevak
	"""
	name= models.OneToOneField(
        Swaymsevak,
        on_delete=models.CASCADE,
        primary_key=True,
        default=1,
    )
	Ghosh_Choices=(
		('v','Vamshi'),
		('s','Shankh'),
		('a','Anak'),
		)
	ghosh = models.CharField(max_length=1, choices=Ghosh_Choices,default='v')
	rachna = models.IntegerField("No. of Rachnas",default=1)
	def __str__(self):
		return self.name.fname+" "+self.name.mname+" "+self.name.lname


@python_2_unicode_compatible  # only if you need to support Python 2
class Sangh_Shikshan(models.Model):
	"""
	Description: List of Sangh Sikshit Swaymsevak
	"""
	name= models.OneToOneField(
        Swaymsevak,
        on_delete=models.CASCADE,
        primary_key=True,
        default=1,
    )
	Sikshan_Choices=(
    	('p','Prathmik'),
    	('P','Pratham'),
    	('D','Dwitiya'),
    	('T','Tritiya')
    	)  
	shikshan= models.CharField(max_length=1, choices=Sikshan_Choices)
	location = models.CharField("Where did", max_length=50)
	year= models.IntegerField(default=2015)  
	def __str__(self):
		return self.name.fname+" "+self.name.mname+" "+self.name.lname
	class Meta:
		verbose_name = "Sangh Shiksha"

@python_2_unicode_compatible  # only if you need to support Python 2
class Utsav(models.Model):
    """
    Description: List of Utsav performed
    """
    shakha=models.ForeignKey(Shakha)
    UtsavName_Choices = (
		('1','Varsh Pratipada'),
		('2','Hindu Samrajya Diwas'),
		('3','Gurupurnima'),
		('4','Raksha Bandhan'),
		('5','Vijyadashmi'),
		('6','Makar Sankranti')
    	)
    name = models.CharField("Utsav Name", max_length=1, choices=UtsavName_Choices)
    location = models.CharField("Where did", max_length=50)
    time = models.DateTimeField("When did")
    bal = models.PositiveSmallIntegerField()
    tarun = models.PositiveSmallIntegerField()    
    shishu = models.PositiveSmallIntegerField()
    any = models.PositiveSmallIntegerField()
    cost = models.PositiveSmallIntegerField()   
    feedback = models.CharField("feedback/Notes about Utsav", max_length=200) 
    vakta = models.CharField(max_length=20)

    def __str__(self):
    	return self.get_name_display() 