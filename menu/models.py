from django.db import models


class Menu(models.Model):
    menu_title = models.CharField(max_length=256, unique=True, primary_key=True, verbose_name='title')

    def __str__(self):
        return self.menu_title


class SubMenu(models.Model):
    title = models.CharField(max_length=256, verbose_name='title')
    menu_title = models.ForeignKey(Menu, on_delete=models.DO_NOTHING)
    url = models.CharField(max_length=256, default='#')

    def __str__(self):
        return self.title


