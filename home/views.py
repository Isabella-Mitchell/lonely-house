from django.shortcuts import render
import datetime
from datetime import date, timedelta


def index(request):
    """A view to return the index page"""

    # Testing ISO format and types. Other ways to stringify this content

    y = date.fromisoformat("2020-01-31")
    print(y)
    print(type(y))
    print(y.strftime("%B"))
    z = str(y)
    print(z)
    print(type(z))

    # Python3 program to find number of days between two given dates

    def numOfDays(date1, date2):
        numOfDays = (date2-date1).days
        print(type(numOfDays))
        return numOfDays

    date1 = date(2018, 12, 13)
    date2 = date(2019, 2, 25)
    print(numOfDays(date1, date2), "days")

    # stack overflow - prints a list of date between two dates as datetime.date

    sdate = date(2019, 3, 22)   # start date
    edate = date(2019, 4, 9)   # end date

    def dates_bwn_twodates(start_date, end_date):
        for n in range(int((end_date - start_date).days)):
            yield start_date + timedelta(n)
    print(list(dates_bwn_twodates(sdate, edate)))

    b = [sdate+timedelta(days=x) for x in range((edate-sdate).days)]
    print(b)

    # prints a list of dates between two dates in ISO format

    for item in b:
        iso_date = item.isoformat()
        print(iso_date)

    return render(request, 'home/index.html')
