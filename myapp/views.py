from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from fuzzywuzzy import fuzz
from .models import Translation, AlignerSetting

def align_texts(request):
    return render(request, 'index.html')


@csrf_exempt
def check_single_sentence(request):
    """
    Har bir gap yoki abzast (front-enddan alignment_type bilan keladi).
    admin panelidagi AlignerSetting.use_db ga qarab:
      True  -> DB bilan fuzzy taqqoslash
      False -> oddiy (algoritmik) yo'l
    """
    if request.method == 'POST':
        alignment_type = request.POST.get('alignment_type', 'sentence')
        english_sentence = request.POST.get('english_sentence', '').strip()
        uzbek_sentence = request.POST.get('uzbek_sentence', '').strip()

        # Admin sozlamasini olish:
        config = AlignerSetting.objects.first()  # Faqat bitta yozuv bor deb faraz qilamiz
        use_db = config.use_db if config else False  # Agar sozlama topilmasa default False

        if use_db:
            # 1) DB bilan Fuzzy taqqoslash
            translations = Translation.objects.all()
            best_match_en = None
            best_score_en = 0
            best_match_uz = None
            best_score_uz = 0

            for tr in translations:
                score_en = fuzz.ratio(english_sentence.lower(), tr.english_text.lower())
                if score_en > best_score_en:
                    best_match_en = tr
                    best_score_en = score_en

            for tr in translations:
                score_uz = fuzz.ratio(uzbek_sentence.lower(), tr.uzbek_text.lower())
                if score_uz > best_score_uz:
                    best_match_uz = tr
                    best_score_uz = score_uz

            # 2) 90% dan yuqori bo‘lsa "mos"
            if best_score_en >= 90 and best_score_uz >= 90:
                response = {
                    'english': best_match_en.english_text,
                    'uzbek': best_match_uz.uzbek_text
                }
            else:
                response = {
                    'english': english_sentence,
                    'uzbek': 'Moslik bajarilmadi'
                }

        else:
            # use_db = False bo'lsa, bazaga murojaat qilmaymiz.
            # Oddiy "algoritmik" deya, shunchaki kirib kelgan matnni
            # juftlik sifatida qaytaramiz (yoki xohlagan yana biror texnikangiz bo'lsa, o'sha).
            response = {
                'english': english_sentence,
                'uzbek': uzbek_sentence
            }

        return JsonResponse(response)

    return JsonResponse({'error': 'Faqat POST so‘rovlari qabul qilinadi.'})
