from django.db import models

class FileUpload(models.Model):
    english_file = models.FileField(upload_to='uploads/')
    uzbek_file = models.FileField(upload_to='uploads/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Faylni bazaga saqlash

        # Fayllarni qatorlarga ajratib, Translation modeliga qo'shish
        from .models import Translation

        with open(self.english_file.path, 'r', encoding='utf-8') as eng_file, \
             open(self.uzbek_file.path, 'r', encoding='utf-8') as uzb_file:
            
            english_sentences = [line.strip() for line in eng_file.readlines() if line.strip()]
            uzbek_sentences = [line.strip() for line in uzb_file.readlines() if line.strip()]

            # Uzunlikni tekshirish
            if len(english_sentences) != len(uzbek_sentences):
                raise ValueError("Inglizcha va O‘zbekcha fayllardagi qatorlar soni bir xil bo‘lishi kerak.")

            # Translation modeliga kiritish
            for en_sentence, uz_sentence in zip(english_sentences, uzbek_sentences):
                if not Translation.objects.filter(english_text=en_sentence).exists():
                    Translation.objects.create(english_text=en_sentence, uzbek_text=uz_sentence)

class Translation(models.Model):
    english_text = models.TextField(unique=True)  # Key: Inglizcha
    uzbek_text = models.TextField()              # Value: O‘zbekcha

    def __str__(self):
        return f"{self.english_text[:50]} -> {self.uzbek_text[:50]}"
