# import requests, uuid, json

# def translate_text_json(text, target_language_code):
#     subscription_key = "abad6ede4b224489a65035c9abd4308b"
#     endpoint = "https://api.cognitive.microsofttranslator.com"

#     location = "eastus2"

#     path = '/translate'
#     constructed_url = endpoint + path

#     params = {
#         'api-version': '3.0',
#         'from': 'en',  # change the source language code if needed
#         'to': [target_language_code]
#     }

#     headers = {
#         'Ocp-Apim-Subscription-Key': subscription_key,
#         'Ocp-Apim-Subscription-Region': location,
#         'Content-type': 'application/json',
#         'X-ClientTraceId': str(uuid.uuid4())
#     }

#     # convert the input text to a list of dictionaries
#     if isinstance(text, str):
#         text = [{'text': text}]
#     elif isinstance(text, list):
#         text = [{'text': t} for t in text]
#     else:
#         #convert the object to a string and then to a list of dictionaries
#         text = [{'text': str(text)}]    

#     response = requests.post(constructed_url, params=params, headers=headers, json=text)
#     response_data = response.json()

#     # get the list of translated texts from the response
#     translated_text_list = [t['translations'][0]['text'] for t in response_data]

#     # create a dictionary with the translated text and return it as a JSON string
#     response_dict = {'translated_text': translated_text_list}
#     response_json = json.dumps(response_dict)

#     return response_json

import requests, uuid, json

def translate_values(input_data, target_language_code):
    """
    Helper function that takes a dictionary or list as input, and returns a copy of the input with the values translated.
    """
    if isinstance(input_data, dict):
        output_data = {}
        for key, value in input_data.items():
            if isinstance(value, str):
                # translate the value if it's a string
                output_data[key] = translate_text(value, target_language_code)
            else:
                # recursively call translate_values() if the value is a nested dictionary or list
                output_data[key] = translate_values(value, target_language_code)
    elif isinstance(input_data, list):
        output_data = []
        for item in input_data:
            if isinstance(item, str):
                # translate the item if it's a string
                output_data.append(translate_text(item, target_language_code))
            else:
                # recursively call translate_values() if the item is a nested dictionary or list
                output_data.append(translate_values(item, target_language_code))
    else:
        # return the input as-is if it's not a dictionary or list
        output_data = input_data
    return output_data

def translate_text(text, target_language_code):
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
        # convert the object to a string and then to a list of dictionaries
        text = [{'text': str(text)}]

    response = requests.post(constructed_url, params=params, headers=headers, json=text)
    response_data = response.json()

    # get the list of translated texts from the response
    translated_text_list = [t['translations'][0]['text'] for t in response_data]

    # create a dictionary with the translated text and return it as a JSON string
    response_dict = {'translated_text': translated_text_list}
    response_json = json.dumps(response_dict)

    return response_json

def translate_text_json(input_data, target_language_code):
    """
    Translates the values of a dictionary or list to the specified target language using the Microsoft Translator API.
    Returns the translated text as a JSON string.
    """
    translated_data = translate_values(input_data, target_language_code)
    return translate_text(json.dumps(translated_data), target_language_code)
