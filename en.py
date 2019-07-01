import gspread
import rep_an
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
from threading import Timer


tracker = "Mexico Dic2018"
result = None


def rep(hoja):
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open(tracker).get_worksheet(hoja)

    live_all = sheet.findall("Live")

    for live in live_all:
        try:
            adv=       int(sheet.cell(live.row, 7).value)
            line=      int(sheet.cell(live.row, 8).value)
            canal=     sheet.cell(live.row, 11).value
            dsp=       sheet.cell(live.row, 12).value
            kpi_1=     sheet.cell(live.row, 33).value
            start_date=sheet.cell(live.row, 13).value

            if dsp != "AN" : continue

            print "Actualizando tracker ", tracker, " hoja ", hoja, " columna ", live.col, " fila ", live.row, "..."

            if dsp == "AN":
                result = rep_an.report(adv, line, canal, kpi_1, start_date)
            print result

            sheet.update_cell(live.row, 18,  result[0])
            sheet.update_cell(live.row, 30,  result[1])
            sheet.update_cell(live.row, 35,  result[2])
            sheet.update_cell(live.row, 9,  "Y")

        except:
            print "Problema en el Tracker ", tracker, " columna ", live.col, " fila ", live.row
            sheet.update_cell(live.row, 9,  "N")

    gr = "Ultima actualizacion de Appnexus Fecha: " + str(datetime.today())
    sheet.update_cell(1, 9,  gr)

def iniciar():
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    shet = client.open(tracker)

    hoja = 0
    while hoja < len(shet.worksheets()):
        rep(hoja)
        hoja += 1
        print hoja



def posponer():
    x=datetime.today()
    y=x.replace(day=x.day+1, hour=3, minute=0, second=0, microsecond=0)
    delta_t=y-x

    secs=delta_t.seconds+1

    t = Timer(secs, iniciar)
    t.start()

try:
    emp = raw_input("Pospone?(Y/N)")
    if emp == "Y": posponer()
    else: iniciar()
except:
    print "Intentelo otra vez"
