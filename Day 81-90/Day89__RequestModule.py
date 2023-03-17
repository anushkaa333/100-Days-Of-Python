import requests
from bs4 import BeautifulSoup


#********* I] requests.get

response = requests.get("https://jsonplaceholder.typicode.com/")
print(response.text)



# PS H:\100 Days of Python> cd ..
# PS H:\> myenv/Scripts/Activate.ps1
# (myenv) PS H:\> pip install requests
# Collecting requests
#   Downloading requests-2.28.2-py3-none-any.whl (62 kB)
#      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 62.8/62.8 kB 3.3 MB/s eta 0:00:00
# Collecting charset-normalizer<4,>=2
# Collecting idna<4,>=2.5
#   Downloading idna-3.4-py3-none-any.whl (61 kB)
#      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 61.5/61.5 kB ? eta 0:00:00
# Collecting urllib3<1.27,>=1.21.1
#   Downloading urllib3-1.26.14-py2.py3-none-any.whl (140 kB)
#      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 140.6/140.6 kB 8.2 MB/s eta 0:00:00
# Collecting certifi>=2017.4.17
#   Using cached certifi-2022.12.7-py3-none-any.whl (155 kB)
# Installing collected packages: urllib3, idna, charset-normalizer, certifi, requests
# Successfully installed certifi-2022.12.7 charset-normalizer-3.1.0 idna-3.4 requests-2.28.2 urllib3-1.26.14
# (myenv) PS H:\> cd "H:\100 Days of Python\Day 81-90"
# (myenv) PS H:\100 Days of Python\Day 81-90> python Day89.py




#********** II] requests.post

url  = "https://jsonplaceholder.typicode.com/guide/"

data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1,
}


headers = {
    'Content-type': 'application/json; charset=UTF-8',
}



response = requests.post(url, headers=headers, json=data)
print(response.text)



#********* Scrapping the required using bs4
# Here we will be scrapping data with h2 tag in html file


url = "https://www.codewithharry.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())

for heading in soup.find_all("h2"):
    print(heading.text)


# Welcome to 
# Recommended Courses
# Testimonials  