from django.db import models
from taggit.managers import TaggableManager
from taggit.models import GenericTaggedItemBase, TagBase


class ItemTag(TagBase):
    image = models.ImageField(
        upload_to='IMG/main.png',
        verbose_name='Изображение',
        blank=True
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание',
        )

    class Meta:
        verbose_name = ("Категория")
        verbose_name_plural = ("Категории")


class TaggedItem(GenericTaggedItemBase):
    tag = models.ForeignKey(
        ItemTag,
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name='Категория',
    )


class Item(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название',)
    description = models.TextField(verbose_name='Описание',)
    slug = models.CharField(unique=True, max_length=50,)
    price = models.DecimalField( max_digits=8,  decimal_places=2,  verbose_name='Новая цена')
    image = models.ImageField( verbose_name='Изображение', upload_to='IMG/main.png', blank=True,)
    
    