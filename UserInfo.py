# This program shows how to pull self info


import dotenv       
import os
import canvasapi


# load variables from .env file
dotenv.load_dotenv(dotenv.find_dotenv())


# ensure access token is available
TOKEN = os.environ.get('CANVAS_ACCESS_TOKEN')

if TOKEN == None:
    print("No access token found. Please set `CANVAS_ACCESS_TOKEN`")
    exit()


# retrieve base URL of canvas
BASE_URL = os.environ.get('CANVAS_URL')


canvas_api = canvasapi.Canvas(BASE_URL, TOKEN)

result = canvas_api.get_user('self')
result.get_profile.__name__

print('=================')
print(result.get_profile)
print('=================')