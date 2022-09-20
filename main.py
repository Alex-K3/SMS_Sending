from twilio.rest import Client
import settings


def sending_sms(text='Wake up...', receiver='+79999999999'):
    try:    
        account_sid = settings.SID
        auth_token = settings.AUTH_TOKEN

        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=text,
            from_=settings.PHONE_NUMBER,
            to=receiver
        )

        return 'The message was successfully sent!'

    except Exception as ex:
        return 'Something was wrong... :(', ex


def main():
    text = input('Please enter your message: ')
    receiver = input('Please enter your number phone: ')
    print(sending_sms(text=text, receiver=receiver))


if __name__=="__main__":
    main()