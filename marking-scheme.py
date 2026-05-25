import requests
import os
import time
import random

shortYear = ['25', '24', '23', '22', '21', '20', '19', '18', '17', '16', '15']
examSeries = ['s','w']

urls = {
    '9702': 'https://bestexamhelp.com/exam/cambridge-international-a-level/physics-9702',
    '9701': 'https://bestexamhelp.com/exam/cambridge-international-a-level/chemistry-9701',
    '9709': 'https://bestexamhelp.com/exam/cambridge-international-a-level/mathematics-9709',
    '9618': 'https://bestexamhelp.com/exam/cambridge-international-a-level/computer-science-9618'
}

paperComponents = {
    '9702': ['11', '12', '13', '21', '22', '23', '31', '32', '33', '41', '42', '43', '51', '52', '53'],
    '9701': ['11', '12', '13', '21', '22', '23', '31', '32', '33', '41', '42', '43', '51', '52', '53'],
    '9709': ['11', '12', '13', '21', '22', '23', '31', '32', '33', '41', '42', '43', '51', '52', '53', '61', '62', '63'],
    '9618': ['11', '12', '13', '21', '22', '23', '31', '32', '33', '41', '42', '43']
}


def downloadURL (year, series, component, subject):

    if not os.path.exists('downloads'):
        os.makedirs('downloads')

    filename = subject + "_" + series + year + '_ms_' + component + '.pdf' 

    try:
        req = requests.get(f'{urls[subject]}/20{year}/{filename}')

        if req.status_code == 200:
            with open (f'downloads/{filename}', 'wb') as f:
                f.write(req.content)
                print(f"Downloaded {filename}")
        else: 
            print(f"{filename} Not Found")

    except:
        print("Error Downloading")

# Random sleep time to not get rate limited
randomInterval = random.randint(2,5)

#  Subject Picker

print("""
1. Maths
2. Physics 
3. Chemistry
4. Computer Science
""")

choice = input("Enter Subject: ")

match choice:
    case '1':
        sub = '9709'
    case '2':
        sub = '9702'
    case '3':
        sub = '9701'
    case '4':
        sub = '9618'

for yearCounter in range (0 , len(shortYear)):
    for seriesCounter in range (0 , len(examSeries)):
        for componentCounter in range (0, len(paperComponents)):
            downloadURL(shortYear[yearCounter], examSeries[seriesCounter], paperComponents[sub][componentCounter], sub)
            time.sleep(randomInterval)