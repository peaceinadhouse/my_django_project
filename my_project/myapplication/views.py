from django.shortcuts import render

def home(request):

    data = {
            'title': 'Quote of the Month',
            'quote': 'The kingdom of God is within you'
            }
    return render(request, 'index.html', data)

def faith(request):
    data = {
        'title': 'Inspirational Faith Verses'
        }
    return render(request, 'faith.html', data)

def hope(request):
    data = {
        'title': 'Inspirational Hope Verses'
        }
    return render(request, 'hope.html', data)


def love(request):
    data = {
        'title': 'Inspirational Love Verses'
        }
    return render(request, 'love.html', data)


def purpose(request):
    data = {
        'title': 'Inspirational Purpose Verses'
        }
    return render(request, 'purpose.html', data)

def truthtalknature(request):
    data = {
         'title': 'This Month Message',

         }
    return render(request, 'truthtalknature.html', data)

# Create your views here.
