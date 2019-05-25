from bs4 import BeautifulSoup
import urllib
from string import ascii_uppercase
import pandas as pd

## Get player list and url
#player_df = pd.DataFrame(columns=['player_name', 'player_page'])
#
#for char in ascii_uppercase:
#    print(char)
#    hit_link = 'http://bwfbadminton.com/players/?char={}&country=&page_size=20000&page_no=1'.format(char)
#    response = urllib.request.urlopen(hit_link)
#    raw_html = response.read()
#    soup_html = BeautifulSoup(raw_html, 'html.parser')    
#    raw_player_list = soup_html.findAll('div', attrs={'class': 'player'})
#    for step in raw_player_list:
#        for tag in step.findAll('a', title=True):
#            p_url = tag['href']
#            p_name = tag['title']
#        player_df = player_df.append({'player_name': p_name, 'player_page': p_url}, ignore_index=True)
#
#player_df.to_csv('./player_profile.csv',sep = '|', header=True,index=False)

## Rankings

hit_link = 'http://bwfbadminton.com/rankings/2/bwf-world-rankings/6/men-s-singles/2018/31/?rows=100&page_no=1'
response = urllib.request.urlopen(hit_link)
raw_html = response.read()
soup_html = BeautifulSoup(raw_html, 'html.parser') 

table = soup_html.find_all('table')[0]











for i in resultSet:
    stats.append(i.contents[0], i.contents[1].text)


table = soup_html.find_all('table')[0]
body = table.find_all('tr')
temp = body.findAll('tr')

result = []
for tr in body:
    print(tr)
    
body[0]

th_all = soup.find_all('th')
result = []
for th in th_all:
    result.extend(th.find_all(text='A'))

#row_marker = 0
#for row in table.find_all('tr'):
#    column_marker = 0
#    columns = row.find_all('td')
#    for column in columns:
#        
#        temp = column.find_all('a')
#        
#        print(column.get_text())
#        temp_df.append(column.get_text())
#        column_marker += 1



























 

table = soup_html.find_all('table')[0]

findtr = table.find_all('tr')
findtd = findtr[3].find_all('td')






with open("temp1.html", "w") as file:
    file.write(str(body))




#
#
#
#
#
#table = soup_html.find_all('table')[0]
#
##new_table = pd.DataFrame(columns=range(0,12), index = [0]) # I know the size 
#
#temp_df = []
#
#row_marker = 0
#for row in table.find_all('tr'):
#    column_marker = 0
#    columns = row.find_all('td')
#    for column in columns:
#        
#        temp = column.find_all('a')
#        
#        print(column.get_text())
#        temp_df.append(column.get_text())
##        new_table.iat[row_marker,column_marker] = column.get_text()
#        column_marker += 1
#        
#        
#        
        
        
        
        
        
        
        
        
        
        
#        
#        
#
#
#temp = row.find(attrs={'class' : 'tooltip'})
#
#<a class="tooltip" href="http://bwfbadminton.com/player/25831/viktor-axelsen" title="Viktor AXELSEN">
#                        Viktor AXELSEN                    </a>
#
#aa = columns.find('a', title=True)
#findAll('a', title=True)
#<a class="tooltip" href="http://bwfbadminton.com/player/25831/viktor-axelsen" title="Viktor AXELSEN">
#
#
#
#
#for a in columns.find('a', href=True):
#    print (a['href'])
#
#
#
#temp = soup_html.findAll('tr')
#
#col_head = soup_html.findAll('th')
#for col in col_head:
#    print(col[0])
#
#
#
#
#temp = soup_html.findAll('tr')
#
#temp = soup_html.findAll(center=6)
# 
#with open("temp1.html", "w") as file:
#    file.write(str(row))
#    
##<td align="center">6</td>
#
#for hit in soup_html.findAll(attrs={'align' : 'center'}):
#    print (hit.contents[2].strip())
#
##player_df.to_csv('./player_profile.csv',sep = '|', header=True,index=False)
