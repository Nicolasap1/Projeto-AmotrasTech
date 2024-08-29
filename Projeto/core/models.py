from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin
from django.urls import reverse

class User(AbstractUser,PermissionsMixin):
    username = models.CharField(
        db_column = 'tx_username',
        null=False,
        max_length=64,
        unique=True
    )
    password = models.CharField(
        db_column='tx_password',
        null= False,
        max_length = 104
    )
    name = models.CharField(
        db_column = 'tx_name',
        null=True,
        max_length=256
    )
    email = models.EmailField(
        db_column = 'tx_email',
        null = True,
        blank = True,
        max_length = 256
    )
    last_login = models.DateTimeField(
        db_column='dt_last_login',
        null=True
    )
    is_active = models.BooleanField(
        db_column = 'cs_active',
        null = False,
        default = True
    )
    is_superuser = models.BooleanField(
        db_column='cs_superuser',
        null= True,
        default = False
    )
    is_staff = models.BooleanField(
        db_column = 'cs_staff',
        null= True,
        default = False
    )
    is_default = models.BooleanField(
        db_column = 'cs_default',
        null= False,
        default = False
    )
    def get_absolute_url(self):
        return reverse ('user_detail', kwargs={'pk':self.id})

    def __str__ (self):
        return self.username

    class Meta:
        managed = True
        db_table = 'auth_User'

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = True
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Cadastro_Livro(models.Model):
    title = models.CharField(
        db_column='tx_title',
        max_length=128,
        null=False,
        verbose_name='Title'
    )
    description = models.CharField(
        db_column= 'text_description',
        max_length=128,
        default='Add',
        verbose_name='Description'
    )

    content = models.TextField(
        db_column='tx_content',
        null=False,
        verbose_name='Content'
    )

    criado_por = models.CharField(
        db_column='tx_author',
        max_length= 25,
        default='Add',
        blank=False,
        verbose_name='Author'
    )

    image = models.ImageField(
        db_column='tx_image',
        blank=True,
        null=False,
        verbose_name= 'Imagem',
        upload_to='livros/'
    )

    author = models.ForeignKey(
        'User',
        on_delete=models.DO_NOTHING,
        db_column='id_author',
        null=False,
        verbose_name='Adicionado por:'
    )
    
    category = models.ForeignKey(
        'Category',
        on_delete=models.DO_NOTHING,
        db_column='id_category',
        null=False,
        verbose_name='Category'
    )
    created_at = models.DateTimeField(
        db_column='dt_created',
        auto_now_add=True,
        null=True,
        verbose_name='Created at'
    )

    def __str__(self):
        return self.title

    class Meta:
        managed = True
        db_table = 'cadastro_livro'
        verbose_name = 'Cadastro_Livro'
        verbose_name_plural = 'Cadastros_Livros'

class Cadastro_Usuario(models.Model):
    name = models.CharField(
        db_column='tx_title',
        max_length=128,
        null=False,
        verbose_name='Name'
    )
    email = models.CharField(
        db_column='tx_name',
        null=False,
        verbose_name='Email'
    )

    password = models.CharField(
        max_length=8, 
        db_column='tx_password',
        null=False,
        verbose_name='Password',
    )

    created_at = models.DateTimeField(
        db_column='dt_created',
        auto_now_add=True,
        null=True,
        verbose_name='Created at'
    )

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'cadastro_usuario'
        verbose_name = 'Cadastro_Usuario'
        verbose_name_plural = 'Cadastros_Usuarios'




    