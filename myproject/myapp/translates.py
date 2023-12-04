from modeltranslation.translator import register, TranslationOptions

from myapp.models import Menu
from myapp.models import Museum


@register(Menu)
class MenuTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Museum)
class MuseumTranslationOptions(TranslationOptions):
        fields = ('name','description','address')