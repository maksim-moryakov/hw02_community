from django.contrib import admin

from .models import Group, Post

from django.conf import settings


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group',
    )
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    settings.EMPTY_VALUE_DISPLAY
    # Артём большое спасибо за помощь!!! Ты лучший!!!
    # потом удалю данные комментарии.


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description')
