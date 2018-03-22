from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from datetime import date, timedelta

from .models import *
# Create your views here.
from django.db.models import Q  # To perform OR query
import csv


def home(request):
    shakha_list = Shakha.objects.all()
    context = {'shakha_list': shakha_list}
    return render(request, 'shakha/home.html', context)


def upload_csv(request, file_name):
    with open(file_name) as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if len(Spersonal.objects.filter(contact=row[4])) > 0:
                continue
            if len(row[3].split()) == 3:
                swaymsevak = Swaymsevak(fname=row[3].split()[0], mname=row[3].split()[1], lname=row[3].split()[2])
            elif len(row[3].split()) == 2:
                swaymsevak = Swaymsevak(fname=row[3].split()[0], lname=row[3].split()[1])
            else:
                swaymsevak = Swaymsevak(fname=row[3])

            swaymsevak.save()
            basti = ""
            if not (row[1] is ""):
                basti = row[1]
            spersonal = Spersonal(name=swaymsevak.id, emailid=row[5], contact=row[4], basti=basti, degree=row[6])
            spersonal.save()
            sshakha = Sshakha(name=swaymsevak.id, swaymsevak_type=2, topi=row[7], belt=row[8], shirt=row[9],
                              pant=row[10], shocks=row[11], shoes=row[12])
            sshakha.save()


def nagar_about(request):
    shakha_swaymsevak_count = Shakha.objects.annotate(Count('swaymsevak'))
    swaymsevak_list = Swaymsevak.objects.all()
    # shakha_list = Shakha.objects.all()
    today = date.today()
    # today = date.today()+ timedelta(days=14) #To increase today

    if today.day > 20:
        if today.month is 12:
            birthday_next_10days = swaymsevak_list.filter(
                Q(spersonal__dob__day__gte=today.day, spersonal__dob__month=today.month) | Q(
                    spersonal__dob__day__lte=31 - today.day, spersonal__dob__month=1))
        else:
            birthday_next_10days = swaymsevak_list.filter(
                Q(spersonal__dob__day__gte=today.day, spersonal__dob__month=today.month) | Q(
                    spersonal__dob__day__lte=31 - today.day, spersonal__dob__month=today.month + 1))
    else:
        birthday_next_10days = swaymsevak_list.filter(spersonal__dob__day__range=[today.day, today.day + 10],
                                                      spersonal__dob__month=today.month)

    donut_value = []
    for i in shakha_swaymsevak_count:
        # a='{label:'+str(i.name)+',value:'+str(i.swaymsevak__count)+'}'
        a = dict(value=str(i.swaymsevak__count), label=str(i.name))
        donut_value.append(a)

    return render(request, 'shakha/nagar_about.html', {
        'donut_value': donut_value, 'shakha_swaymsevak_count': shakha_swaymsevak_count,
        'birthday_next_10days': birthday_next_10days,
    })


def tarun_contact(request):
    swaymsevak_list = Swaymsevak.objects.all()
    swaymsevak_list_tarun = swaymsevak_list.values("fname", "mname", "lname", "spersonal__contact",
                                                   "spersonal__emailid").exclude(spersonal__contact__exact='').exclude(
        spersonal__contact__isnull=True)
    return render(request, 'shakha/nagar_query.html', {'result': swaymsevak_list_tarun})


def index(request, shakha_id):
    shakha = get_object_or_404(Shakha, pk=shakha_id)
    swaymsevak_list = Swaymsevak.objects.all().filter(shakha=shakha_id)
    swaymsevak_count = Swaymsevak.objects.all().filter(shakha=shakha_id).count()
    purn_ganvesh_count = swaymsevak_list.filter(sshakha__ganvesh_complete=True).count()
    gat_swaymsevak_count = swaymsevak_list.exclude(sshakha__jimmedari='0').count()
    tarun_count = swaymsevak_list.filter(sshakha__swaymsevak_type='2').count()
    bal_count = swaymsevak_list.filter(sshakha__swaymsevak_type='1').count()
    shishu_count = swaymsevak_list.filter(sshakha__swaymsevak_type='3').count()
    gat_count = Gat.objects.filter(gatnayak__shakha=shakha_id).count()
    sangh_shikshit = Sangh_Shikshan.objects.filter(name__shakha=shakha_id).count()
    shakha_toli = swaymsevak_list.exclude(sshakha__jimmedari='1').exclude(sshakha__jimmedari='0').exclude(
        sshakha__jimmedari='3').exclude(sshakha__jimmedari__isnull=True).exclude(sshakha__jimmedari__exact='')
    # Exclude result of blank or none society name
    list_society = Spersonal.objects.filter(name__shakha=shakha_id).exclude(society__isnull=True).exclude(
        society__exact='').values('society').distinct()
    list_basti = Spersonal.objects.filter(name__shakha=shakha_id).exclude(basti__isnull=True).exclude(
        basti__exact='').values('basti').distinct()

    # [{'society': u'Jai Durga'}, {'society': u'Sainath Chal'} ]
    '''
		value_ListSociety=[]
		for i in list_society:
			a=[]
			a.append(str(i['society']))
			a.append(Spersonal.objects.filter(society=str(i['society'])).count())
			value_ListSociety.append(a)
	# value_ListSociety= [['Jai Durga', 4], ['Sainath Chal', 1], ['', 33], 
	['Vrindavan', 7], ['Pimpleshwar', 4], ['Yadav Sangh Society', 2],
	 ['Gokuldham', 1], ['Premnivas', 4], ['Abhay', 4], ['Ambika', 1],]
	'''
    value_ListSociety = []
    donut_value = []
    # for i in list_society:
    #     a = dict(society=str(i['society']),
    #              value=Spersonal.objects.filter(name__shakha=shakha_id).filter(society=str(i['society'])).count())
    #     value_ListSociety.append(a)
    #     donut_value.append(a)

    for i in list_basti:
        a = dict(basti=str(i['basti']),
                 value=Spersonal.objects.filter(name__shakha=shakha_id).filter(basti=str(i['basti'])).count())
        value_ListSociety.append(a)
        donut_value.append(a)
    # for i in list_society:
    #     a = dict(label=str(i['society']),
    #              value=Spersonal.objects.filter(name__shakha=shakha_id).filter(society=str(i['society'])).count())
    #     donut_value.append(a)

    # Show list of swaymsevak having birthday in next 10 days
    # today = date.today()+ timedelta(days=14) #To increase today

    today = date.today()
    if today.day > 20:
        if today.month is 12:
            birthday_next_10days = swaymsevak_list.filter(
                Q(spersonal__dob__day__gte=today.day, spersonal__dob__month=today.month) | Q(
                    spersonal__dob__day__lte=31 - today.day, spersonal__dob__month=1))
        else:
            birthday_next_10days = swaymsevak_list.filter(
                Q(spersonal__dob__day__gte=today.day, spersonal__dob__month=today.month) | Q(
                    spersonal__dob__day__lte=31 - today.day, spersonal__dob__month=today.month + 1))
    else:
        birthday_next_10days = swaymsevak_list.filter(spersonal__dob__day__range=[today.day, today.day + 10],
                                                      spersonal__dob__month=today.month)

    return render(request, 'shakha/index.html', {
        'shakha': shakha, 'swaymsevak_list': swaymsevak_list, 'gat_swaymsevak_count': gat_swaymsevak_count,
        'purn_ganvesh_count': purn_ganvesh_count, 'swaymsevak_count': swaymsevak_count, 'gat_count': gat_count,
        'sangh_shikshit': sangh_shikshit, 'value_ListSociety': value_ListSociety,
        'donut_value': donut_value, 'birthday_next_10days': birthday_next_10days, 'shakha_toli': shakha_toli,
        'bal_count': bal_count, 'tarun_count': tarun_count, 'shishu_count': shishu_count
    })


def swaymsevak_detail(request, swaymsevak_id):
    swaymsevak = get_object_or_404(Swaymsevak, pk=swaymsevak_id)
    shakha = get_object_or_404(Shakha, pk=shakha_id)

    return render(request, 'shakha/swaymsevak_detail.html', {
        'shakha': shakha, 'swaymsevak': swaymsevak
    })


def shakha_swaymsevak(request, shakha_id):
    shakha = get_object_or_404(Shakha, pk=shakha_id)
    swaymsevak_list = Swaymsevak.objects.all().filter(shakha=shakha_id)

    return render(request, 'shakha/shakha_swaymsevak.html', {
        'shakha': shakha, 'swaymsevak_list': swaymsevak_list,
    })


def shakha_shikshit(request, shakha_id):
    swaymsevak_shikshit = Sangh_Shikshan.objects.filter(name__shakha=shakha_id)
    shakha = get_object_or_404(Shakha, pk=shakha_id)

    return render(request, 'shakha/shakha_shikshit.html', {
        'shakha': shakha, 'swaymsevak_shikshit': swaymsevak_shikshit,
    })


def shakha_ghosh(request, shakha_id):
    swaymsevak_ghosh = Ghosh.objects.filter(name__shakha=shakha_id)
    shakha = get_object_or_404(Shakha, pk=shakha_id)

    return render(request, 'shakha/shakha_ghosh.html', {
        'shakha': shakha, 'swaymsevak_ghosh': swaymsevak_ghosh,
    })


def shakha_ganvesh(request, shakha_id):
    swaymsevak_ganvesh = Sshakha.objects.filter(name__shakha=shakha_id)
    shakha = get_object_or_404(Shakha, pk=shakha_id)

    return render(request, 'shakha/shakha_ganvesh.html', {
        'shakha': shakha, 'swaymsevak_ganvesh': swaymsevak_ganvesh,
    })


def shakha_gat(request, shakha_id):
    shakha_gat = Gat.objects.filter(gatnayak__shakha=shakha_id)
    shakha = get_object_or_404(Shakha, pk=shakha_id)
    swaymsevak_gat = Sshakha.objects.filter(gat__in=shakha_gat).values('gat__name', 'name__fname', 'name__mname',
                                                                       'name__lname', 'name__spersonal__contact',
                                                                       'ganvesh_complete', 'name__id', )
    # to access spersonal 'name__spersonal'
    swaymsevak_list = Swaymsevak.objects.all().filter(shakha=shakha_id)
    sshakha = Sshakha.objects.all().filter(name__shakha=shakha_id)
    swaymsevak_no_gat = swaymsevak_list.exclude(sshakha__in=sshakha)
    return render(request, 'shakha/shakha_gat.html', {
        'shakha': shakha, 'swaymsevak_gat': swaymsevak_gat,
        'shakha_gat': shakha_gat, 'swaymsevak_no_gat': swaymsevak_no_gat,
    })
