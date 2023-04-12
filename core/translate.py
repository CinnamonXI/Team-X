# import requests, uuid, json

# # Add your key and endpoint
# key = "abad6ede4b224489a65035c9abd4308b"
# endpoint = "https://api.cognitive.microsofttranslator.com"

# location, also known as region.
# required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
# location = "eastus2"

# path = '/translate'
# constructed_url = endpoint + path

# params = {
#     'api-version': '3.0',
#     'from': 'en',
#     'to': ['sw', 'ig']
# }

# headers = {
#     'Ocp-Apim-Subscription-Key': key,
#     # location required if you're using a multi-service or regional (not global) resource.
#     'Ocp-Apim-Subscription-Region': location,
#     'Content-type': 'application/json',
#     'X-ClientTraceId': str(uuid.uuid4())
# }

# You can pass more than one object in body.
# body = [{
#     'text': 'I would really like to drive your car around the block a few times!'
# }]

# request = requests.post(constructed_url, params=params, headers=headers, json=body)
# response = request.json()

# print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))

import requests, uuid, json

def translate_text_json(text, target_language_code):
    subscription_key = "abad6ede4b224489a65035c9abd4308b"
    endpoint = "https://api.cognitive.microsofttranslator.com"

    location = "eastus2"

    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'from': 'en',  # change the source language code if needed
        'to': [target_language_code]
    }

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # convert the input text to a list of dictionaries
    if isinstance(text, str):
        text = [{'text': text}]
    elif isinstance(text, list):
        text = [{'text': t} for t in text]
    else:
        #convert the object to a string and then to a list of dictionaries
        text = [{'text': str(text)}]    

    response = requests.post(constructed_url, params=params, headers=headers, json=text)
    response_data = response.json()

    # get the list of translated texts from the response
    translated_text_list = [t['translations'][0]['text'] for t in response_data]

    # create a dictionary with the translated text and return it as a JSON string
    response_dict = {'translated_text': translated_text_list}
    response_json = json.dumps(response_dict)

    return response_json