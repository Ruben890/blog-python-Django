from django.contrib import admin
from .models import PostBLog, profile, Cometarios


@admin.register(PostBLog)
class Admin(admin.ModelAdmin):
    list_display = ('user', 'title', 'tipo', 'data',)
    ordering = ('data',)


@admin.register(profile)
class Admin(admin.ModelAdmin):
    pass

@admin.register(Cometarios)
class Admin(admin.ModelAdmin):
    list_display = ('author','data', )