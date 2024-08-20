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
    name = models.CharField(
        db_column='tx_name',
        max_length=128,
        null=False,
        blank=False,
        unique=True,
        verbose_name='Name'
    )

    tipo = models.CharField(
        db_column='tx_tipo',
        max_length=128,
        null=False,
        blank=False,
        unique=True,
        verbose_name='tipo'
    )

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Post(models.Model):
    title = models.CharField(
        db_column='tx_title',
        max_length=128,
        null=False,
        verbose_name='Title'
    )
    content = models.TextField(
        db_column='tx_content',
        null=False,
        verbose_name='Content'
    )
    author = models.ForeignKey(
        'User',
        on_delete=models.DO_NOTHING,
        db_column='id_author',
        null=False,
        verbose_name='Author'
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
        db_table = 'post'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class Comment(models.Model):
    post = models.ForeignKey(
        'Post',
        on_delete=models.DO_NOTHING,
        db_column='id_posts',
        null=False,
        verbose_name='Post'
    )
    author = models.ForeignKey(
        'User',
        on_delete=models.DO_NOTHING,
        db_column='id_author',
        null=False,
        verbose_name='Author'
    )
    content = models.TextField(
        db_column='tx_content',
        null=False,
        verbose_name='Content'
    )
    created_at = models.DateTimeField(
        db_column='dt_created',
        auto_now_add=True,
        null=True,
        verbose_name='Created at'
    )

    def __str__(self):
        return f'Comment by {self.author}'

    class Meta:
        managed = True
        db_table = 'comment'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    