from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from datetime import datetime
import pandas as pd
import time
import csv

def get_page(url_hit):
    req = Request(url_hit, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    return BeautifulSoup(webpage, 'html.parser')

def get_inc_details(incident_rows):
    item = {
            'date': incident_rows[1].findAll('td')[1].text,
            'time': incident_rows[2].findAll('td')[1].text,
            'location': incident_rows[3].findAll('td')[1].text,
            'operator': incident_rows[4].findAll('td')[1].text,
            'flight_no': incident_rows[5].findAll('td')[1].text,
            'route': incident_rows[6].findAll('td')[1].text,
            'ac_type': incident_rows[7].findAll('td')[1].text,
            'registration': incident_rows[8].findAll('td')[1].text,
            'cn_ln': incident_rows[9].findAll('td')[1].text,
            'total_aboard': incident_rows[10].findAll('td')[1].text.split(' ')[0],
            'passengers_aboard': incident_rows[10].findAll('td')[1].text.\
                replace(u'\xa0', u'').split(' ')[2].replace('(passengers:', ''),
            'crew_aboard': incident_rows[10].findAll('td')[1].text.\
                replace(u'\xa0', u'').split(' ')[3].replace('crew:', '')[:-1],
            'passengers_fatalities': incident_rows[11].findAll('td')[1].text.\
                replace(u'\xa0', u'').split(' ')[2].replace('(passengers:', ''),
            'crew_fatalities': incident_rows[11].findAll('td')[1].text.\
                replace(u'\xa0', u'').split(' ')[3].replace('crew:', '')[:-1],
            'ground': incident_rows[12].findAll('td')[1].text,
            'summary': incident_rows[13].findAll('td')[1].text
            }
    return item

main_page = get_page('http://www.planecrashinfo.com/database.htm')

divs = main_page.findAll('table')  
rows = divs[1].findAll('tr')

accident_list = []
for row_year in range(0, len(rows)):
    items = rows[row_year].findAll('td')
    base_page = 'http://www.planecrashinfo.com'
    for i in range(1,len(items)):
        year_page = items[i].text.lstrip().rstrip()
        hit_page = '{}/{}/{}.htm'.format(base_page, year_page, year_page)
        print(year_page)
        year_sub_page = get_page(hit_page)
        year_divs = year_sub_page.findAll('table')  
        year_rows = year_divs[0].findAll('tr')
        for j in range(1, len(year_rows)):
            year_items = year_rows[j].findAll('td')
            get_href = year_items[0].find_all(href=True)
            sub_page = '{}/{}/{}'.format(base_page, year_page, get_href[0]['href'])
            print(get_href[0]['href'])
            incident_page = get_page(sub_page)
            incident_divs = incident_page.findAll('table')
            incident_rows = incident_divs[0].findAll('tr')

            new_item = get_inc_details(incident_rows)
            accident_list.append(new_item)
            time.sleep(5)

accident_list = pd.DataFrame(accident_list)

accident_list.to_csv('data/raw.csv', 
                     sep = '|', 
                     encoding = 'utf-8',
                     index = False,
                     escapechar = '"',
                     quoting = csv.QUOTE_ALL)

#if incident_time == '?':
#    incident_dt = datetime.strptime(incident_date, '%B %d, %Y')
#elif ':' in incident_time:
#    incident_dt = '{} {}'.format(incident_date, incident_time)
#    incident_dt = datetime.strptime(incident_dt, '%B %d, %Y %H:%M')
#else:
#    incident_dt = '{} {}'.format(incident_date, incident_time)
#    incident_dt = datetime.strptime(incident_dt, '%B %d, %Y %H%M')