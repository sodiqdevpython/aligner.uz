from django.contrib import admin
from .models import FileUpload, Translation, AlignerSetting

@admin.register(FileUpload)
class FileUploadAdmin(admin.ModelAdmin):
    list_display = ('english_file', 'uzbek_file')

@admin.register(Translation)
class TranslationAdmin(admin.ModelAdmin):
    list_display = ('english_text', 'uzbek_text')

# Yangi sozlamaning admin registratsiyasi
@admin.register(AlignerSetting)
class AlignerSettingAdmin(admin.ModelAdmin):
    list_display = ('use_db',)
