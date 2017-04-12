
# Below is a link to a 10-day weather forecast at weather.com
# Use urllib and BeautifulSoup to scrape data from the weather table.
# Print a brief synopsis of the weather for the next 10 days.
# Include the day, date, high temp, low temp, and chance of rain.
# You can customize the text as you like, but it should be readable
# for the user.  You will need to target specific classes or other
# attributes to pull some parts of the data.
# (e.g.  Wednesday, March 22: the high temp will be 48 with a low of 35, and a 20% chance of rain). (25pts)
import urllib.request
from bs4 import BeautifulSoup


url = "https://weather.com/weather/tenday/l/USIL0225:1:US"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read(), "html.parser")

print(soup.prettify())


headers = [x.text.strip() for x in soup.findAll("th")]

data_list = [[y.text.strip() for y in x.findAll("td")] for x in soup.find("table",{"class" : "twc-table"}).findAll("tr")]

data_list = data_list[1:]

for i in range(len(data_list)):
    del(data_list[i][0])
    if i != 0:
        if data_list[i][0][:3] == "Wed":
            day_of_week = "Wednesday"
        elif data_list[i][0][:3] == "Thu":
            day_of_week = "Thursday"
        elif data_list[i][0][:3] == "Tue":
            day_of_week = "Tuesday"
        elif data_list[i][0][:3] == "Sat":
            day_of_week = "Saturday"
        else:
            day_of_week = data_list[i][0][:3] + "day"
        length_of_day = 3
    else:
        day_of_week = data_list[i][0][:5]
        length_of_day = 5

    print(day_of_week + ", " + data_list[i][0][length_of_day:] + ": the high will be " + data_list[i][2][:3] + "the low will be " + data_list[i][2][3:] + ", there  " + data_list[i][5] + " chance of rain.")





