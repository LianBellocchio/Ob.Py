import requests
import json

# URL de inicio de sesión de Riot Games
LOGIN_URL = 'https://auth.riotgames.com/api/v1/authorization'

# URL de generación de clave API de Riot Games
API_KEY_URL = 'https://developer.riotgames.com/api-keys'

# Datos de inicio de sesión
USERNAME = 'ahnillitor'
PASSWORD = '270404Gnb'

# Leer la clave API actual del archivo fetch_game_data.py
with open('fetch_game_data.py', 'r') as f:
    contents = f.read()
    api_key = contents.split('"')[1]

# Verificar si la clave API actual todavía es válida
headers = {'X-Riot-Token': api_key}
response = requests.get('https://na1.api.riotgames.com/lol/platform/v3/champion-rotations', headers=headers)
if response.status_code == 200:
    print('La clave API actual todavía es válida')
else:
    print('La clave API actual ha expirado')

    # Realizar la solicitud de inicio de sesión
    response = requests.post(LOGIN_URL, json={
        'client_id': 'riot-developer-portal',
        'nonce': '1',
        'redirect_uri': 'https://developer.riotgames.com/redirect-uri',
        'response_type': 'token id_token',
        'scope': 'openid email profile',
        'state': '1'
    })

    # Obtener el URI de redireccionamiento
    redirect_uri = response.history[0].headers['location']

    # Realizar la solicitud de inicio de sesión en el formulario
    response = requests.post(redirect_uri, data={
        'login': 'ahnillitor',
        'password': '270404Gnb'
    }, allow_redirects=False)

    # Obtener el URI de redireccionamiento final
    redirect_uri = response.headers['location']

    # Realizar la solicitud de autorización de clave API
    response = requests.post(API_KEY_URL, headers={'Referer': redirect_uri})
    api_key_data = json.loads(response.text)

    # Leer la nueva clave API y escribirla en el archivo fetch_game_data.py
    new_api_key = api_key_data['key']
    with open('fetch_game_data.py', 'w') as f:
        f.write(contents.replace(api_key, new_api_key))
        print('Se ha generado una nueva clave API y se ha escrito en el archivo fetch_game_data.py')
