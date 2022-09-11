from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.



@admin.register(Category)
class CategoryImportExport(ImportExportModelAdmin):
    pass
@admin.register(Slider)
class sliderImportExport(ImportExportModelAdmin):
    pass
@admin.register(trailer)
class trailerImportExport(ImportExportModelAdmin):
    pass