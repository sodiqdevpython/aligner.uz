from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Translation
from fuzzywuzzy import fuzz
from django.shortcuts import render

def align_texts(request):
    return render(request, 'index.html')

@csrf_exempt
def check_single_sentence(request):
    """
    Har bir gapni ingliz va o‘zbek tilida bazadan qidirish va moslikni tekshirish.
    """
    if request.method == 'POST':
        english_sentence = request.POST.get('english_sentence', '').strip()
        uzbek_sentence = request.POST.get('uzbek_sentence', '').strip()

        # Bazadan barcha matnlarni olish
        translations = Translation.objects.all()
        best_match_en = None
        best_score_en = 0
        best_match_uz = None
        best_score_uz = 0

        # Inglizcha matn uchun o‘xshashlikni hisoblash
        for translation in translations:
            score_en = fuzz.ratio(english_sentence.lower(), translation.english_text.lower())
            if score_en > best_score_en:
                best_match_en = translation
                best_score_en = score_en

        # O‘zbekcha matn uchun o‘xshashlikni hisoblash
        for translation in translations:
            score_uz = fuzz.ratio(uzbek_sentence.lower(), translation.uzbek_text.lower())
            if score_uz > best_score_uz:
                best_match_uz = translation
                best_score_uz = score_uz

        # Agar ikkala o‘xshashlik 90% yoki undan yuqori bo‘lsa
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

        return JsonResponse(response)

    return JsonResponse({'error': 'Faqat POST so‘rovlari qabul qilinadi.'})
