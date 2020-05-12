import random

import requests


def create_object(value):
    headers = {
        'X-Parse-Application-Id': '7ua4rZuIBq02bvFSV5WhovrfFHmG7NKxwu2wFtpI',
        'X-Parse-REST-API-Key': 'tnXnATKAgOhW0Q6LkGjpvoCBuJeT83gXAJMK9lS0',
        'Content-Type': 'application/json',
        # (Optional) Required only if you set up the security:
        #'X-Parse-Session-Token': '[User session token for Back4App]',
    }

    data = {
        'value': int(value),
    }

    r = requests.post(
            'https://parseapi.back4app.com/classes/moisture', 
            json=data, 
            headers=headers
        )

    if r.status_code != 201:
        #print(f'Error occurred while sending data to DB {r.status_code}: {r.reason} ({r.text})')
        print('Dupa')
    else:
        #print(f'Created new record in DB for value {value}')
        print('Dupa2')

    return r

if __name__ == '__main__':
    for _  in range(10):
        create_object(random.randint(50, 500))
    
    print("\nCheck your database dashboard ;)")
