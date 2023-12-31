from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
# Create your views here.


@csrf_exempt
def index(request):
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')

        if text == '' or text == '0':
            response = f'''
            CON {main_menu()}
            {main_menu_list()}
            '''

        elif text in ['1', '2', '3', '4', '5', '6']:

            if text == '1':
                response = f'''
                END Transfer of funds is currently being implemented.
                '''

            elif text == '2':
                response = '''
                END Momo Pay & Pay Bill feature is currently being implemented.
                '''

            elif text == '3':
                response = '''
                END Airtime & Bundles feature is currently being implemented.
                '''

            elif text == '4':
                response = '''
                END Cash out allowed.
                '''

            elif text == '5':
                response = '''
                END Financial services feature is currently being implemented.
                '''

            elif text == '6':
                response = '''
                END My wallet feature is currently being implemented.
                '''

        else:
            response = f'''
            CON {incorrect_choice()}
            {main_menu()}
            {main_menu_list()}
            '''

        print(request.POST)

        return HttpResponse(response)


def main_menu():
    return 'Menu'


def incorrect_choice():
    return 'Incorrect choice, try again.'


def main_menu_list():
    return '''1. Transfer Money
    2. MoMoPay & Pay Bill
    3. Artime & Bundles
    4. Allow Cash Out
    5. Financial Services
    6. My Wallet
    '''
