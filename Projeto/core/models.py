from django.db import models

class Category(models.Model):
    name = models.CharField(
        db_column='tx_name',
        max_length=128,
        null=False,
        blank=False,
        unique=True,
        verbose_name='Name'
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

    