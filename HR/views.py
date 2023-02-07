from django.shortcuts import render
from datetime import date, datetime
from dateutil import relativedelta

def main_page(request):
    start_date = '14/8/2019'
    current_date = date.today().strftime("%d/%m/%Y")
    start_date = datetime.strptime(start_date, "%d/%m/%Y")
    end_date = datetime.strptime(current_date, "%d/%m/%Y")
    delta = relativedelta.relativedelta(end_date, start_date)
    print(f'{delta.years} years')
    print(f'date today is: {current_date}')
    data = {
        'current_date': date.today().strftime("%B %d, %Y"),
    }
    return render(request, 'HR/pages/mainView.html', data)