import pandas as pd
import requests
from bs4 import BeautifulSoup
from collections import defaultdict

#Used BeautifulSoup to do web-scraping of a table.
#Access the table needed to be scraped using it's class name.
URL = 'https://en.wikipedia.org/wiki/2019_in_spaceflight#Orbital_launches'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table', {'class':'wikitable collapsible'}).tbody

#Created list of all rows of the table.
rows = table.find_all('tr')
rl = list()
for tr in rows:
    columns = [v.text.replace('\n', '') for v in tr.find_all('td')]
    rl.append(columns)

#Created dictionary of all the dates.
value={}
import datetime
d1 = datetime.date(2019, 1, 1)
d2 = datetime.date(2019, 12, 31)
dates = (d1 + datetime.timedelta(days=i) for i in range((d2 - d1).days + 1))

#Initially assigned the values of all dates to be 0.
for d in dates:
    value[d]=0

get_month = {'January':1,'February':2,'March':3,'April':4,'May':5,"June":6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}

#Function to obtain the date in YYYY-MM-DD format.
def get_format(s):
    i = 0
    while(not s[i].isalpha()):
        i = i + 1
    date = s[:i]
    j = i
    while(s[i].isalpha()):
        i = i + 1
    month = s[j:i]
    j = i
    while(i==len(s)or s[i]!='['):
        i = i + 1
    time = s[j:i].split(':')
    d = datetime.date(2019,get_month[month],int(date))
    return d

#Utilizing the length of list in row_list(rl) to categorize if line is for Orbital launch or payload.
for line in rl[4:]:
    if(len(line)==5):
        date = line[0]
        date = get_format(date)
        flag = 0
    elif(len(line)==6 and flag==0 and (line[-1].split("[")[0] == 'Successful' or line[-1].split("[")[0] == 'Operational' or line[-1].split("[")[0] == 'En Route')):
        value[date]= 1 + value[date]
        flag = 1
    else:
        continue

#Tuple to store the final output
final = []
for v in value.keys():
    count = value[v]
    final.append((v.isoformat()+'T00:00:00+00:00',count))

df = pd.DataFrame(final, columns=['date', 'value'])
df.to_csv('output.csv',index = False)