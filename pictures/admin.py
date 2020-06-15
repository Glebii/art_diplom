from django.contrib import admin
from .models import Picture , Trend ,Painter

# Register your models here.

@admin.register(Picture)
class PictureModelAdmin(admin.ModelAdmin):
    pass

@admin.register(Trend)
class TrendModelAdmin(admin.ModelAdmin):
    pass

@admin.register(Painter)
class PainterModelAdmin(admin.ModelAdmin):
    pass
