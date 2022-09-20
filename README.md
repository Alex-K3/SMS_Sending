# SMS_Sending

SMS_Sending - отправка смс

## Установка:

1. Клонируйте репозиторий с githab `git clone https://github.com/Alex-K3/SMS_Sending.git`
2. Создайте и активируйте виртуальное окружение:

```
    python -m venv env
    env\Scripts\activate
```

3. Установите зависимости `pip install -r requirements.txt`
4. Зарегистрируйтесь на сайте twilio.com, затем необходимо получить SID и AUTH_TOKEN
5. Создайте в папке проекта файл settings.py и добавьте переменные SID, AUTH_TOKEN и PHONE_NUMBER

PHONE_NUMBER - номер, куда необходимо направить смс

Готово!