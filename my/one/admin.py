from django.contrib import admin
from .models import Post

"""
Что бы создавать, удалять и редактировать нашы записи которые мы создали в models.py 
нужно их зарегестрировать в админ понеле
"""
admin.site.register(Post)  # зарегестрировали Post в админ понели
