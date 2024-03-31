from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'display_image')  # 画像のプレビューも表示する

    def display_image(self, obj):
        return obj.image.url if obj.image else 'No image'

    display_image.short_description = 'Image Preview'  # 列の見出しを設定

admin.site.register(Post, PostAdmin)
