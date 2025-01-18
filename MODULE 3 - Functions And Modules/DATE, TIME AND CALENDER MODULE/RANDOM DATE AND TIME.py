import random
import time
def getRandomDate(stardate,enddate):
    print("random date between ",stardate,"and",enddate)
    randomgenerator = random.random()
    dateformat = '%m/%d/%Y'
    starttime = time.mktime(time.strptime(stardate,dateformat))
    endtime = time.mktime(time.strptime(enddate,dateformat))
    randomtime = starttime + randomgenerator*(endtime - starttime)
    randomdate = time.strftime(dateformat,time.localtime(randomtime))

    return randomdate

print (f"random date = {getRandomDate("1/1/2020", "1/18/2025")}")

