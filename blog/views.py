from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime
from blog.models import homework

# Create your views here.
def timetable(request):
    date_time_str = request.GET.get('date', None)
    date_time_obj = datetime.strptime(date_time_str , '%Y-%m-%d')
    data = homework.objects.filter(date__year=date_time_obj.year, date__month=date_time_obj.month, date__day=date_time_obj.day)
    data = list(data)
    cnt = round(len(data) / 2)
    new_data = []
    for i in range(cnt):
        new_list = []
        new_list.append(data[i * 2])
        if i * 2 + 1 < len(data):
            new_list.append(data[i * 2 + 1])
        new_data.append(new_list)

    return render(request, 'blog/timetable.html', {'homework': new_data, 'date':date_time_str})

def VIOL(request):
    date_list = []
    for a in homework.objects.all():
        date_list.append(str(a.date)[:10])
    date_list = set(date_list)

    result={}
    for a in date_list:
        result[a]=[0, 0]

    for a in homework.objects.all():
        result[str(a.date)[:10]][1] += 1
        if a.is_completed:
            result[str(a.date)[:10]][0] += 1

    result2 = []
    for key in result.keys():
        result2.append([key, result[key][0], result[key][1]])

    return render(request, 'blog/Badapple.html', { 'result': result2 })

@api_view(['POST'])
def update_timetable(request):
    id = request.POST.get('id', None)
    title = request.POST.get('title', None)
    memo = request.POST.get('memo', None)
    is_completed = request.POST.get('is_completed', None)
    if is_completed == "true":
        is_completed = True
    else:
        is_completed = False

    item = homework.objects.filter(id=id)[0]
    item.title = title
    item.memo = memo
    item.is_completed = is_completed
    item.save()

    return Response({'data':'success'})

@api_view(['POST'])
def create_timetable(request):
    title = request.POST.get('title', None)
    memo = request.POST.get('memo', None)
    is_completed = request.POST.get('is_completed', None)
    if is_completed == "true":
        is_completed = True
    else:
        is_completed = False
    date = request.POST.get('date', None)

    item = homework()
    item.title = title
    item.memo = memo
    item.is_completed = is_completed
    date_time_obj = datetime.strptime(date , '%Y-%m-%d')
    item.date = date_time_obj
    item.save()

    return Response({'data':item.id})