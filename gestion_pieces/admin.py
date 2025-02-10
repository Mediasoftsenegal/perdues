from django.contrib import admin

# Register your models here.
# gestion_pieces/admin.py
from django.contrib import admin
from .models import PieceDisparue

admin.site.register(PieceDisparue)