from django.shortcuts import render, get_object_or_404
from library.models import *
# Create your views here.
from django.db.models import Q # To perform OR query


def  jholivachnalay(request):
	jholivachnalay_list = Book.objects.all()
	context = {'jholivachnalay_list': jholivachnalay_list}
	return render(request,'jholivachnalay/book.html',context)
