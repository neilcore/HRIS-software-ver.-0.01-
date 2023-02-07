from django.shortcuts import render
from .forms import NameForm

def my_account(request):

    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            print('------')
            print(request.POST)
    else:
        form = NameForm()
    return render(request, 'user/pages/MyAccountView.html', {'form': form})
