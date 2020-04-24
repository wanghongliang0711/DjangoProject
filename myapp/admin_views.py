from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.http import HttpResponse,JsonResponse
from myapp.models import Users, Jsontable102
from functools import reduce
from django.views.generic import ListView
import json
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.clickjacking import xframe_options_exempt
# from myapp.view.BaseView import BaseView
# Create your views here.

@xframe_options_exempt
def adminhomepage(request):
    print("adminhomepage")
    data1 = [1, 2, 3, "", 5, 6, 7, "", 9, 10, 11]
    data2 = [9, 8, 7, 4, "", 6, 7, 4, 3, 10, 8]
    data3 = [3, 8, 6, 4, 9, 6, 2, 8, 3, 1, 9]
    data4 = [5, 6, 9, 0, "", 2, 4, 5, 3, 1, 3]
    data5 = [9, 5, 9, 15, "", 2, 4, 1, 6, 1, 5]
    return render(request, "highcharts/line_basic.html", {"data1": data1,"data2": data2,"data3":data3,"data4":data4,"data5":data5} )

@xframe_options_exempt
def show_chart_table(request):
    strip = Jsontable102.objects.filter(metadata_unit_id='21C100552').values(
        'metadata_positioning_data_positioning_time',
        'metadata_positioning_data_quality',
        'metadata_positioning_data_direction',
        'metadata_positioning_data_lat', 'metadata_positioning_data_lng',
        'metadata_positioning_data_velocity', 'metadata_tripid','metadata_positioning_data_satellite_num')

    # django版本2.2,filter后得到的数据(列表里的字典,键值对先后顺序不固定,是随机的)
    # 只能先写死了
    biaotou = [{'title': 'time'}, {'title': 'quality'}, {'title': 'velocity'}, {'title': 'direction'}, {'title': 'lat'},
               {'title': 'lng'}, {'title': 'tripid'}, {'title':'satellite_num'}]

    allvalue, pt, gsq, vel, lat, satellite_num= [], [], [], [], [], []
    # allvalue也先写死了,最方便
    for i in strip:
        allvalue.append([i['metadata_positioning_data_positioning_time'], i['metadata_positioning_data_quality'],
                         i['metadata_positioning_data_velocity'], i['metadata_positioning_data_direction'],
                         i['metadata_positioning_data_lat'], i['metadata_positioning_data_lng'], i['metadata_tripid'],
                         i['metadata_positioning_data_satellite_num']])
        pt.append(i['metadata_positioning_data_positioning_time'])
        gsq.append(i['metadata_positioning_data_quality'])
        vel.append(i['metadata_positioning_data_velocity'])
        lat.append(i['metadata_positioning_data_lat'])
        satellite_num.append(i['metadata_positioning_data_satellite_num'])

    rst = {'context': allvalue, 'tablehead': biaotou, 'pt': pt, 'gsq': gsq, 'vel': vel, 'lat': lat, 'satellite_num':satellite_num}
    return render(request, 'admin/admin_chart_table.html', rst)


def blake_show13(request):
    unitid = request.GET.get('nuit_id').strip()

    position = request.GET.get('time').strip()

    all102 = Jsontable102.objects.filter(metadata_unit_id=unitid).values(
        'metadata_positioning_data_positioning_time',
        'metadata_positioning_data_quality',
        'metadata_positioning_data_direction',
        'metadata_positioning_data_lat', 'metadata_positioning_data_lng',
        'metadata_positioning_data_velocity',
        'metadata_unit_id', 'metadata_tripid','metadata_positioning_data_satellite_num')
    value100 = []
    for i, j in enumerate(list(all102)):
        if position in j['metadata_positioning_data_positioning_time']:
            break
    if i < 30:
        start_i = 0
    else:
        start_i = i - 30
    for k in list(all102)[start_i:i + 30]:
        value100.append([k['metadata_positioning_data_positioning_time'], k['metadata_positioning_data_quality'],
                         k['metadata_positioning_data_velocity'], k['metadata_positioning_data_direction'],
                         k['metadata_positioning_data_lat'], k['metadata_positioning_data_lng'], k['metadata_tripid'],
                         k['metadata_positioning_data_satellite_num']])

    # value100里的内容也按顺序先写死了
    return JsonResponse({'data': value100})


def Show13(r):
    unitid = r.GET.get('nuit_id').strip()

    position = r.GET.get('time').strip()

    all102 = Jsontable102.objects.filter(metadata_unit_id=unitid).values(
        'metadata_positioning_data_positioning_time',
        'metadata_positioning_data_quality',
        'metadata_positioning_data_direction',
        'metadata_positioning_data_lat', 'metadata_positioning_data_lng',
        'metadata_positioning_data_velocity',
        'metadata_unit_id', 'metadata_tripid')
    value100 = []
    for i, j in enumerate(list(all102)):
        if position in j['metadata_positioning_data_positioning_time']:
            break
    if i < 30:
        start_i = 0
    else:
        start_i = i - 30
    for k in list(all102)[start_i:i + 30]:
        value100.append([k['metadata_positioning_data_positioning_time'], k['metadata_positioning_data_quality'],
                         k['metadata_positioning_data_velocity'], k['metadata_positioning_data_direction'],
                         k['metadata_positioning_data_lat'], k['metadata_positioning_data_lng'], k['metadata_tripid']])

    # value100里的内容也按顺序先写死了
    return JsonResponse({'data': value100})


def login_varify(username, passwoed):
    # 0-登录成功 1-用户名错误 2-密码错误 3-被禁用 4-管理员登录
    flag = "1"
    filter_result = Users.objects.filter(username=username).values('password', 'power', 'apply')
    if filter_result:
        if filter_result[0]['password'] == passwoed:
            if filter_result[0]['power'] == 0:
                flag = "4"   # 4-管理员登录
            elif filter_result[0]['apply'] == 0:
                flag = "3"  # 3-用户被禁用
            else:
                flag = "0"  # 0-登录成功
        else:
            flag = "2"  # 2-密码错误
    return flag


class Jsontable102List(ListView):
    # model = Jsontable102
    context_object_name = 'allJs102'
    template_name = 'testTrip.html'

    # 如果想只取部分对象,则要写下面的这些内容,使用过滤器
    def get_queryset(self):
        allJs102 = Jsontable102.objects.filter(metadata_log_type__lt=100)
        return allJs102
