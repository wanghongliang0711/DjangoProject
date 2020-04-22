from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.http import HttpResponse,JsonResponse
from myapp.models import Users, Jsontable102
from functools import reduce
from django.views.generic import ListView
import json
# from myapp.view.BaseView import BaseView
# Create your views here.


def homepage(request):
    return render(request, "login.html")
    # template = get_template('login.html')
    # html = template.render(locals())
    # return HttpResponse(html)

def page_not_found(request, exception):
    return render(request, "error_page/404.html", {"exception": exception})

def server_error(request):
    return render(request, "error_page/500.html")

def userhomepage(request):
    return render(request, "user/userhomepage.html")

def datatable_basic(request):
    return render(request, "datatables/DataTable.html")

def line_basic(request):
    data1 = [1, 2, 3, "", 5, 6, 7, "", 9, 10, 11]
    data2 = [9, 8, 7, 4, "", 6, 7, 4, 3, 10, 8]
    data3 = [3, 8, 6, 4, 9, 6, 2, 8, 3, 1, 9]
    data4 = [5, 6, 9, 0, "", 2, 4, 5, 3, 1, 3]
    data5 = [9, 5, 9, 15, "", 2, 4, 1, 6, 1, 5]
    return render(request, "highcharts/line_basic.html", {"data1": data1,"data2": data2,"data3":data3,"data4":data4,"data5":data5} )

def line_basic_xAxis(request):
    data1 = [1, 2, 3, "", 5, 6, 7, "", 9, 10, 11]
    data2 = [9, 8, 7, 4, "", 6, 7, 4, 3, 10, 8]
    data3 = [3, 8, 6, 4, 9, 6, 2, 8, 3, 1, 9]
    data4 = [5, 6, 9, 0, "", 2, 4, 5, 3, 1, 3]
    data5 = [9, 5, 9, 15, "", 2, 4, 1, 6, 1, 5]
    return render(request, "highcharts/line_basic_xAxis.html", {"data1": data1,"data2": data2,"data3":data3,"data4":data4,"data5":data5} )


def registerpage(request):
    return render(request, "register.html")


@csrf_exempt
def register(request):
    if request.method == "POST":
        name = request.POST.get('username')
        pwd = request.POST.get('password')
        if name and pwd:
            filter_result = Users.objects.filter(username=name)
            if len(filter_result) == 0:
                Users.objects.create(username=name,password=pwd)
                return render(request, "login.html", {"error": "注册成功,请登录。"})
            else:
                return render(request, "register.html", {"error": "用户名已经存在！！！"})
        else:
            return render(request, "register.html", {"error": "出现未知参数！！！"})
    else:
        return render(request, "register.html", {"error": "这不是POST进来的！！！"})

@csrf_exempt
def handlejson(request):
    file = request.FILES.get('json',None)
    # python3.5不能直接将bytes转为json对象,故需要转为str再,3.7就可以了
    temfile = ''
    for ck in file.chunks():
        temfile += str(ck.decode())
    jsondt = json.loads(temfile)
    jsonrst=[]
    if jsondt['metatype'] == 102:
       checklist = Jsontable102.objects.filter(metadata_unit_id=jsondt['metadata'][0]['unit_id']).values_list(
       'metadata_positioning_data_positioning_time', flat=True)
       for metadata in jsondt['metadata']:
       # 先判断要上传的文件是否在数据库里有了已经
         if checklist == None or metadata['positioning_data']['positioning_time'] not in checklist:
           # 开始往数据库里传
           jsonrst.append(Jsontable102(createdtime=jsondt['createdtime'],fileno=jsondt['fileno'],metatype=102,
                   conditions_geodetic=jsondt['conditions']['geodetic'],metadata_unit_id=metadata['unit_id'],
                   metadata_entry_time=metadata['entry_time'],metadata_dte_ip_addr=metadata['dte_ip_addr'],
                   metadata_log_type=metadata['log_type'],metadata_seq_no=metadata['seq_no'],metadata_tripid=metadata['seq_no'][26:30],
                   metadata_tele_msg_id=metadata['tele_msg_id'],metadata_event_code=metadata['event_code'],
                   metadata_event_type=metadata['event_type'] if metadata.__contains__('event_type') else None,
                   metadata_positioning_data_positioning_time=metadata['positioning_data']['positioning_time'],
                   metadata_positioning_data_lat=metadata['positioning_data']['lat'] if metadata['positioning_data'].__contains__('lat') else None,
                   metadata_positioning_data_lng=metadata['positioning_data']['lng'] if metadata['positioning_data'].__contains__('lat') else None,
                   metadata_positioning_data_quality=metadata['positioning_data']['quality'],
                   metadata_positioning_data_positioning_status=metadata['positioning_data']['positioning_status'],
                   metadata_positioning_data_satellite_num=metadata['positioning_data']['satellite_num'],
                   metadata_positioning_data_pdop=metadata['positioning_data']['pdop'],
                   metadata_positioning_data_direction=metadata['positioning_data']['direction'],
                   metadata_positioning_data_altitude=metadata['positioning_data']['altitude'],
                   metadata_positioning_data_status_brake=metadata['positioning_data']['status']['brake'],
                   metadata_positioning_data_status_winker_r=metadata['positioning_data']['status']['winker_r'],
                   metadata_positioning_data_status_winker_l=metadata['positioning_data']['status']['winker_l'],
                   metadata_positioning_data_status_back=metadata['positioning_data']['status']['back'],
                   metadata_positioning_data_status_switch=metadata['positioning_data']['status']['switch'],
                   metadata_positioning_data_actuator_status=metadata['positioning_data']['actuator_status'],
                   metadata_positioning_data_area_no=metadata['positioning_data']['area_no'],
                   metadata_positioning_data_speed_measure_type=metadata['positioning_data']['speed_measure_type'],
                   metadata_positioning_data_velocity=metadata['positioning_data']['velocity'],
                   metadata_ic_card_card_type=metadata['ic_card']['card_type'] if metadata.__contains__('ic_card') else None,
                   metadata_ic_card_card_data=metadata['ic_card']['card_data'] if metadata.__contains__('ic_card') else None,
                   metadata_ic_card_read_datetime=metadata['ic_card']['read_datetime'] if metadata.__contains__('ic_card') else None,
                   metadata_driving_contents_event_no=metadata['driving_contents']['event_no'] if (metadata.__contains__('driving_contents') and metadata['driving_contents'].__contains__('event_no')) else None,
                   metadata_driving_contents_level=metadata['driving_contents']['level'] if (metadata.__contains__('driving_contents') and metadata['driving_contents'].__contains__('level')) else None,
                   metadata_driving_contents_acceleration_x=metadata['driving_contents']['acceleration_x'] if (metadata.__contains__('driving_contents') and metadata['driving_contents'].__contains__('acceleration_x')) else None,
                   metadata_driving_contents_acceleration_y=metadata['driving_contents']['acceleration_y'] if (metadata.__contains__('driving_contents') and metadata['driving_contents'].__contains__('acceleration_x')) else None,
                   metadata_driving_contents_acceleration_z=metadata['driving_contents']['acceleration_z'] if (metadata.__contains__('driving_contents') and metadata['driving_contents'].__contains__('acceleration_x')) else None,
                   metadata_driving_contents_video_key=metadata['driving_contents']['video_key'] if (metadata.__contains__('driving_contents') and metadata['driving_contents'].__contains__('video_key')) else None,
                   metadata_driving_contents_video_device_type=metadata['driving_contents']['video'][0]['device_type'] if (metadata.__contains__('driving_contents') and metadata['driving_contents'].__contains__('video')) else None,
                   metadata_driving_contents_video_video_no=metadata['driving_contents']['video'][0]['video_no'] if (metadata.__contains__('driving_contents') and metadata['driving_contents'].__contains__('video')) else None,
                   metadata_driving_contents_video_video_status=metadata['driving_contents']['video'][0]['video_status'] if (metadata.__contains__('driving_contents') and metadata['driving_contents'].__contains__('video')) else None,
                   metadata_driving_contents_video_contents_id=metadata['driving_contents']['video'][0]['contents_id'] if (metadata.__contains__('driving_contents') and metadata['driving_contents'].__contains__('video')) else None,
                   metadata_driving_max_speed=metadata['driving']['max_speed'] if metadata.__contains__('driving') else None,
                   metadata_driving_speedover_speed_over_type=metadata['driving_speedover']['speed_over_type'] if metadata.__contains__('driving_speedover') else None,
                   metadata_driving_speedover_detection_type=metadata['driving_speedover']['detection_type'] if metadata.__contains__('driving_speedover') else None,
                   metadata_driving_speedover_speed_over_time=metadata['driving_speedover']['speed_over_time'] if metadata.__contains__('driving_speedover') else None,
                   metadata_driving_speedover_speed_over_start_time=metadata['driving_speedover']['speed_over_start_time'] if metadata.__contains__('driving_speedover') else None,
                   metadata_idling_event_detection_type=metadata['idling_event']['detection_type'] if metadata.__contains__('idling_event') else None,
                   metadata_idling_event_idling_time=metadata['idling_event']['idling_time'] if metadata.__contains__('idling_event') else None,
                   metadata_idling_event_idling_start_time=metadata['idling_event']['idling_start_time'] if metadata.__contains__('idling_event') else None,
                   metadata_breakdown_event_data_breakdown_code=metadata['breakdown_event_data']['breakdown_code'] if metadata.__contains__('breakdown_event_data') else None
                   ))
    Jsontable102.objects.bulk_create(jsonrst)
    return render(request,'user/index.html')


@csrf_exempt
def handlenmea(r):
    file = r.FILES.get('nmea',None)
    file = str(file.read())
    import re
    allgsr = re.findall(r'GSENSORD,(-?\d+,-?\d+,-?\d+)', file)
    allspd = re.findall(r'SPEED,(\d+)', file)
    alltm = re.findall(r'GPRMC,(\d{6})', file)
    gsensor, speed, tm= [],[],[]
    for i in allgsr:
        gps3 = [int(ii) for ii in i.split(',')]
        gps2 = list(map(lambda x : (x*0.001)**2,gps3))
        gps1 = reduce(lambda x, y : x + y,gps2)
        gsensor.append(gps1**(1/2))
    for j in allspd:
        speed.append(int(j))
    for k in alltm:
        tm.append(int(k))
    print("*********")
    print(tm)
    rst = {'gsensor':gsensor,'speed':speed,'tm':tm}
    return render(r,'forpcviewer.html',rst)

@csrf_exempt
def login(request):
    if request.method == "POST":
        name = request.POST.get('username')
        pwd = request.POST.get('password')
        print("88888")
        if name and pwd:
            LoginResult = login_varify(name, pwd)  # 0-登录成功 1-用户名错误 2-密码错误 3-被禁用 4-管理员登录
            if LoginResult == "0":   # 普通用户登录成功
                return render(request, "user/index.html")
            elif LoginResult == "4":
                print("管理员登录sccess")  # TODO  理员登录sccess
            else:
                return render(request, "login.html", {"LoginResult": LoginResult})
        else:
            return render(request, "login.html", {"error": "出现未知参数！！！"})
        template = get_template('login.html')
        html = template.render(locals())
        return HttpResponse(html)
    else:
        # template = get_template('login.html')
        # login = "这不是POST进来的！！！"
        # html = template.render(locals())
        # return HttpResponse(html) {"login": "这不是POST进来的！！！"}
        return render(request, "login.html", {"error": "这不是POST进来的！！！"})


def test(r):
    strip = Jsontable102.objects.filter(metadata_unit_id='21C100552').values(
        'metadata_positioning_data_positioning_time',
        'metadata_positioning_data_quality',
        'metadata_positioning_data_direction',
        'metadata_positioning_data_lat', 'metadata_positioning_data_lng',
        'metadata_positioning_data_velocity', 'metadata_tripid')

    # django版本2.2,filter后得到的数据(列表里的字典,键值对先后顺序不固定,是随机的)
    # 只能先写死了
    biaotou = [{'title': 'time'}, {'title': 'quality'}, {'title': 'velocity'}, {'title': 'direction'}, {'title': 'lat'},
               {'title': 'lng'}, {'title': 'tripid'}]

    allvalue, pt, gsq, vel, lat = [], [], [], [], []
    # allvalue也先写死了,最方便
    for i in strip:
        allvalue.append([i['metadata_positioning_data_positioning_time'], i['metadata_positioning_data_quality'],
                         i['metadata_positioning_data_velocity'], i['metadata_positioning_data_direction'],
                         i['metadata_positioning_data_lat'], i['metadata_positioning_data_lng'], i['metadata_tripid']])
        pt.append(i['metadata_positioning_data_positioning_time'])
        gsq.append(i['metadata_positioning_data_quality'])
        vel.append(i['metadata_positioning_data_velocity'])
        lat.append(i['metadata_positioning_data_lat'])

    rst = {'context': allvalue, 'tablehead': biaotou, 'pt': pt, 'gsq': gsq, 'vel': vel, 'lat': lat}
    return render(r, 'test.html', rst)


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
    for k in list(all102)[i - 30:i + 30]:
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
