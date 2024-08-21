from django.contrib import admin

from .models import  User

class ModelAdminBase(admin.ModelAdmin):
    list_per_page = 20

@admin.register(User)
class UserAdmin(ModelAdminBase):
    list_display = (
        'id',
        'username',
        'name',
        'email',
        'is_superuser',
        'is_active',
    )

