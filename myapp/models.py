from django.db import models

# Create your models here.


class Users(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    power = models.IntegerField(default=1)  # 0 是管理员 1 是普通用户
    apply = models.IntegerField(default=1)  # 0 不可用 1 可用

    def __unicode__(self):
        return self.username


class Jsontable102(models.Model):
    createdtime = models.CharField(max_length=20)
    fileno = models.CharField(max_length=2)
    metatype = models.IntegerField()
    conditions_geodetic = models.IntegerField()
    metadata_unit_id = models.CharField(max_length=10)
    metadata_entry_time = models.CharField(max_length=20)
    metadata_dte_ip_addr = models.CharField(max_length=15)
    metadata_log_type = models.IntegerField()
    metadata_seq_no = models.CharField(max_length=37)
    metadata_tripid = models.CharField(max_length=5)
    metadata_tele_msg_id = models.CharField(max_length=10)
    metadata_event_code = models.CharField(max_length=5)
    metadata_event_type = models.IntegerField(null=True)
    metadata_positioning_data_positioning_time = models.CharField(max_length=20)
    metadata_positioning_data_lat = models.FloatField(null=True)
    metadata_positioning_data_lng = models.FloatField(null=True)
    metadata_positioning_data_quality = models.IntegerField()
    metadata_positioning_data_positioning_status = models.IntegerField()
    metadata_positioning_data_satellite_num = models.IntegerField()
    metadata_positioning_data_pdop = models.FloatField()
    metadata_positioning_data_direction = models.IntegerField()
    metadata_positioning_data_altitude = models.FloatField()
    metadata_positioning_data_status_brake = models.IntegerField()
    metadata_positioning_data_status_winker_r = models.IntegerField()
    metadata_positioning_data_status_winker_l = models.IntegerField()
    metadata_positioning_data_status_back = models.IntegerField()
    metadata_positioning_data_status_switch = models.IntegerField()
    metadata_positioning_data_actuator_status = models.IntegerField()
    metadata_positioning_data_area_no = models.IntegerField()
    metadata_positioning_data_speed_measure_type = models.IntegerField()
    metadata_positioning_data_velocity = models.IntegerField()
    metadata_ic_card_card_type = models.IntegerField(null=True)
    metadata_ic_card_card_data = models.CharField(max_length=20, null=True)
    metadata_ic_card_read_datetime = models.CharField(max_length=22, null=True)
    metadata_driving_contents_event_no = models.IntegerField(null=True)
    metadata_driving_contents_level = models.IntegerField(null=True)
    metadata_driving_contents_acceleration_x = models.FloatField(null=True)
    metadata_driving_contents_acceleration_y = models.FloatField(null=True)
    metadata_driving_contents_acceleration_z = models.FloatField(null=True)
    metadata_driving_contents_video_key = models.CharField(max_length=68, null=True)
    metadata_driving_contents_video_device_type = models.CharField(max_length=2, null=True)
    metadata_driving_contents_video_video_no = models.IntegerField(null=True)
    metadata_driving_contents_video_video_status = models.IntegerField(null=True)
    metadata_driving_contents_video_contents_id = models.CharField(max_length=55, null=True)
    metadata_driving_max_speed = models.FloatField(null=True)
    metadata_driving_speedover_speed_over_type = models.IntegerField(null=True)
    metadata_driving_speedover_detection_type = models.IntegerField(null=True)
    metadata_driving_speedover_speed_over_time = models.IntegerField(null=True)
    metadata_driving_speedover_speed_over_start_time = models.CharField(max_length=22, null=True)
    metadata_idling_event_detection_type = models.IntegerField(null=True)
    metadata_idling_event_idling_time = models.IntegerField(null=True)
    metadata_idling_event_idling_start_time = models.CharField(max_length=22, null=True)
    metadata_breakdown_event_data_breakdown_code = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.createdtime

    # def get_fields(self):
    #     return [(field.name, field.value_to_string(self)) for field in Jsontable102._meta.fields]
