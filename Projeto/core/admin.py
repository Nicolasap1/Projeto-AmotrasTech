from django.contrib import admin

from .models import  Cadastro_Livro,User, Category

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

@admin.register(Category)
class CatetoryAdmin(ModelAdminBase):
    list_display = (
        'name',
    )

@admin.register(Cadastro_Livro)
class CadastroLAdmin(ModelAdminBase):
    list_display = (
        'title',
        'content',
        'author',
        'category',
        'created_at',
    )