from .models import Category, Tag
from django.contrib.auth.models import User
from discussion.models import Question, Answer
# from .trans import translate_text_json
# import json
# import ast
# from django.core.serializers import serialize

# def queryset_to_json(queryset):
#     queryset_json = serialize('json', queryset)
#     queryset_list = json.loads(queryset_json)
#     return [item['fields'] for item in queryset_list]

# def extract_translated_text(json_str, output_type=dict):
#     data = json.loads(json_str)
#     translated_text = data["translated_text"][0]
#     if output_type == dict:
#         translated_text = json.loads(translated_text)
#         return translated_text
#     elif output_type == list:
#         translated_text = json.loads(translated_text)
#         return translated_text
#     else:
#         raise ValueError("Invalid output type. Only 'dict' and 'list' are supported.")

def categories(request):
    # LANGUAGE_CODE = request.LANGUAGE_CODE
    queryset = Question.objects.order_by('-likes')[:5]
    # queryset_json = json.dumps(queryset_to_json(queryset))

    # print('\n\n\n\n', queryset_json, '\n\n\n\n')
    # translated_questions = translate_text_json(queryset_json, LANGUAGE_CODE)
    # latest_post = extract_translated_text(translated_questions)
    # print(latest_post,'\n\n\n\n')
    # print(translated_questions, '\n\n\n\n')
    return {
        'categories': Category.objects.all(),
        'tags': Tag.objects.all(),
        'latest_post': queryset,
        'top_members': User.objects.all()[:4],
        'total_users': User.objects.all().count(),
        'total_questions': Question.objects.all().count(),
        'total_answers': Answer.objects.all().count(),
    }

