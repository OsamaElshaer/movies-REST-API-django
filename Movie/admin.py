from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


# Register your models here.

@admin.register(Category)
class MovieImportExport(ImportExportModelAdmin):
    pass

@admin.register(Quality)
class QualityImportExport(ImportExportModelAdmin):
    pass

@admin.register(Featured)
class FurmoveiovieImportExport(ImportExportModelAdmin):
    pass
@admin.register(Movie)
class MovieImportExport(ImportExportModelAdmin):
    pass

@admin.register(Contry)
class ContryImportExport(ImportExportModelAdmin):
    pass

@admin.register(Year)
class yearImportExport(ImportExportModelAdmin):
    pass

