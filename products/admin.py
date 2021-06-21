from django.contrib import admin

from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter
from products.models import *
from modeltranslation.admin import TranslationAdmin


admin.site.register(BoxSizes)


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('name', 'preview_text')
    list_display_links = ('name', )
# admin.site.register(Product)
#admin.site.register(SubCategory)
 
@admin.register(SubCategory)
class CategoryAdmin(TranslationAdmin):
    list_display = ('name', 'preview_text')
    list_display_links = ('name', )
# нужен чтобы наследовать дочерние модели
class ModelAChildAdmin(PolymorphicChildModelAdmin):
    """ Base admin class for all child models """
    base_model = Product  # Optional, explicitly set here.

    # By using these `base_...` attributes instead of the regular ModelAdmin `form` and `fieldsets`,
    # the additional fields of the child models are automatically added to the admin form.
    
    """
    то же что ModelAdmin.form 
    base_form = ...
    """

    # то же что и ModelAdmin.fieldset для обычных  моделей
    # Позволяет изменить макет страниц добавления и редактирования объекта.

    """
    base_fieldsets = (
        ...
    )
    """


# Child модель
@admin.register(BoxType1)
class ModelBAdmin(ModelAChildAdmin):
    base_model = BoxType1  # Explicitly set here!
    # define custom features here

# Child модель
@admin.register(BoxType2)
class ModelBAdmin(ModelAChildAdmin):
    base_model = BoxType2  # Explicitly set here!
    # define custom features here


@admin.register(FolderType1)
class ModelBAdmin(ModelAChildAdmin):
    base_model = FolderType1  # Explicitly set here!
    # define custom features here

@admin.register(FolderType2)
class ModelBAdmin(ModelAChildAdmin):
    base_model = FolderType2  # Explicitly set here!
    # define custom features here


@admin.register(Placement)
class ModelBAdmin(TranslationAdmin):
    base_model = Placement 

@admin.register(Note2)
class ModelBAdmin(TranslationAdmin):
    base_model = Note2

@admin.register(Banner)
class BanerAdmin(TranslationAdmin):
    base_model = Banner


# Базовая модель
@admin.register(Product) # Декоратор для регистрации
class ProductParentAdmin(PolymorphicParentModelAdmin):
    """ The parent model admin """
    base_model = Product  # Optional, explicitly set here.
    child_models = (BoxType2, BoxType1,  FolderType1, FolderType2,Placement,Note2)
    list_filter = (PolymorphicChildModelFilter,)  # This is optional
   