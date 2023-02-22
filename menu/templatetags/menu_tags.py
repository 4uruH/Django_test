from django import template
from menu.models import *

register = template.Library()


@register.inclusion_tag('menu/draw_menu.html')
def draw_menu(filter=None):
    sub_menus = []
    menu_title = ""
    data = SubMenu.objects.select_related('menu_title').filter(menu_title=filter)
    for el in data:
        sub_menus.append([el.title, el.url])
        menu_title = el.menu_title
    return {"sub_menus": sub_menus, "menu_title": menu_title}
