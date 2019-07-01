from nexusadspy import AppnexusClient
from nexusadspy import AppnexusReport
from datetime import datetime
import time
import json
import io
import os

client = AppnexusClient('.appnexus_auth.json')

def kpi_d(k):
    if k == 'CTR' : return 'ctr'
    if k == 'Conversions' : return 'total_convs'
    if k == 'Conversion Rate' : return 'convs_rate'
    if k == 'Viewability' : return 'view_rate'
    if k == 'CPA' : return 'cpa'
    if k == 'CPC' : return 'cpc'
    if k == 'CPM' : return 'ecpm'
    if k == 'Clicks' : return 'clicks'
    return None

def kpi_vc(k):
    if k == 'Completion Rate' : return 'completion_rate'
    if k == 'Viewability' : return 'view_rate'
    return None

def tiempo(day):
    date_object = datetime.strptime(day, '%m/%d/%Y')
    return date_object.strftime('%Y-%m-%d')

def report(adv, line, canal, kpi_1, start_date):

    start_date = tiempo(start_date)
    print adv, line, canal, kpi_1, start_date
    end_date = time.strftime('%Y-%m-%d')

    kpi_1_v1= kpi_d(kpi_1)

    print start_date, end_date, kpi_1_v1
    columns = ["imps",
            "media_cost"]
    if kpi_1_v1 != None: columns.append(kpi_1_v1)

    report_type ="advertiser_analytics"
    filters = [{"line_item_id": line}]
    reporte = AppnexusReport(advertiser_ids=adv,
                        start_date= start_date,
                        end_date= end_date,
                        filters=filters,
                        report_type=report_type,
                        columns=columns,
                        timezone='US/Eastern')
    m = reporte.get()
    print m
    imps = m[0]['imps']
    media_cost = m[0]['media_cost']
    kp_1 = ""
    if kpi_1_v1 != None: kp_1 = m[0][kpi_1_v1]

    if canal=='VC':

        kpi_1_v2= kpi_vc(kpi_1)

        columns = ["completions"]
        if kpi_1_v2 != None: columns.append(kpi_1_v2)

        report_type ="video_analytics_network"
        filters = [{"line_item_id": line}]
        reporte_video = AppnexusReport(advertiser_ids=adv,
                        start_date= start_date,
                        end_date= end_date,
                        filters=filters,
                        report_type=report_type,
                        columns=columns,
                        timezone='US/Eastern')
        j = reporte_video.get()

        imps = j[0]['completions']
        if kpi_1_v2 != None: kp_1 = j[0][kpi_1_v2]

    os.remove('.appnexus_auth.json')

    return [imps, media_cost, kp_1]

#print report("1769458", "4469675", "D", "CTR", "CPM", "10/1/2017")
