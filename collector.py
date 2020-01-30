from bs4 import BeautifulSoup
import requests
import psycopg2
import re

URL = 'https://raw.githubusercontent.com/kruser/interview-developer/master/python/leaderboard.html'


#Get the html and create a BeautifulSoup object
source_code = requests.get(URL).content
soup = BeautifulSoup(source_code, features="html.parser")
table = soup.find('table', id="battingLeaders")
rows = table.findAll('tr')


#Iterate through rest of rows and modify as needed
cleaned_rows = []
for tr in rows[1:]:
    td = tr.find_all('td')
    row = [i.text for i in td]

    #removing non letters
    pattern = re.compile('[^.,a-zA-Z0-9 \.]')
    row[1] = re.sub(pattern, '', row[1])

    #removing a blank column
    row.pop(3)
    cleaned_rows.append(tuple(row))   

#Connect to the database and insert each row to prexisting table
try:
    connection = psycopg2.connect(
                                    host="localhost",
                                    database="jackzerilli")
    cursor = connection.cursor()
    for row in cleaned_rows:
        print('adding row ', row[1])
        postgres_insert_query = """ INSERT INTO stats (rk, player, team, 
                    player_id, pos, g, ab, r, h, double, triple, hr, rbi, 
                    bb, so, sb, cs, ba, obp, slg, ops, ibb, hbp, sac, sf, 
                    tb, xbh, gdp, goo, ao, go_ao, np, pa) 
                    
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        
        cursor.execute(postgres_insert_query, row)
        count = cursor.rowcount
        print (count, "Record inserted successfully into mobile table")

    connection.commit()
    

except (Exception, psycopg2.Error) as error :
    if(connection):
        print("Failed to insert record into mobile table", error)

finally:
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")



