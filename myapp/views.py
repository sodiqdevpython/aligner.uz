import json
import openai
import re
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import get_least_used_token
from django.shortcuts import render


def align_texts(request):
    return render(request, 'index.html')

# @csrf_exempt
# def gpt_align(request):
#     if request.method != "POST":
#         return JsonResponse({"error": "Only POST allowed"})

#     english = request.POST.get("english", "")
#     uzbek = request.POST.get("uzbek", "")

#     # 1) Eng kam ishlatilgan tokenni olish
#     token_obj = get_least_used_token()
#     if not token_obj:
#         return JsonResponse({"error": "No active API tokens available"}, status=500)

#     openai.api_key = token_obj.token

#     # 2) Prompt yaratish
#     prompt = f"""
# You are an AI alignment assistant. Your task is to compare an English sentence with its Uzbek translation and determine whether they match in meaning.

# ### Input:
# - English sentence: "{english}"
# - Uzbek sentence: "{uzbek}"

# Analyze deeply and return ONLY valid JSON in the structure below:

# {{
#   "english": "<corrected or cleaned>",
#   "uzbek": "<corrected or cleaned>",
#   "is_match": true,
#   "similarity_score": 0,
#   "comment": "<short explanation>"
# }}
#     """

#     # 3) Modelni chaqirish
#     try:
#         response = openai.chat.completions.create(
#             model="gpt-4o-mini",
#             messages=[{"role": "user", "content": prompt}],
#             temperature=0.1,
#             max_tokens=2000,
#         )
#         content = response.choices[0].message["content"]

#         # 4) usage_count +1
#         token_obj.usage_count += 1
#         token_obj.save()

#         # 5) JSON sifatida qaytarish
#         return JsonResponse({"result": content})

#     except Exception as e:
#         return JsonResponse({"error": str(e)}, status=500)


def cleanup_json(text):
    # Remove markdown fences
    text = re.sub(r"```json", "", text, flags=re.IGNORECASE)
    text = re.sub(r"```", "", text)
    return text.strip()


@csrf_exempt
def gpt_align(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST allowed"}, status=400)

    english = request.POST.get("english", "")
    uzbek = request.POST.get("uzbek", "")
    prompt = request.POST.get("prompt", "")

    # Token selection
    token_obj = get_least_used_token()
    if not token_obj:
        return JsonResponse({"error": "No active tokens"}, status=500)

    openai.api_key = token_obj.token

    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )

        raw = response.choices[0].message.content

        cleaned = cleanup_json(raw)

        # Update usage
        token_obj.usage_count += 1
        token_obj.save()

        return JsonResponse({"result": cleaned})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)