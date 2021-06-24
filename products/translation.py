from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'preview_text')


#register(Category, CategoryTranslationOptions)


@register(SubCategory)
class subCategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'preview_text')


#register(SubCategory, subCategoryTranslationOptions)


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'detail_text', 'preview_text')


#register(Product, ProductTranslationOptions)


@register(BoxSizes)
class BoxTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Note2)
class Note2TranslationOptions(TranslationOptions):
    fileds = ('name',)

@register(BoxType2)
class Note2TranslationOptions(TranslationOptions):
    fileds = ('name',)

@register(Placement)
class Note2TranslationOptions(TranslationOptions):
    fileds = ('name',)
@register(FolderType1)
class Note2TranslationOptions(TranslationOptions):
    fileds = ('name',)

@register(FolderType2)
class Note2TranslationOptions(TranslationOptions):
    fileds = ('name',)


@register(Banner)
class BannerTranslationOptions(TranslationOptions):
    fields = ("mainimage", )

