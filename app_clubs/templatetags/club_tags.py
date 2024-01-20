# from django import template
# from django.urls import reverse_lazy
#
# register = template.Library()
#
# navbar = [
#     {'id': 1, 'name': 'Все клубы', 'url': reverse_lazy('app_clubs:list_clubs')},
#     {'id': 2, 'name': 'Создать клуб', 'url': reverse_lazy('app_clubs:create_club')},
# ]
#
#
# @register.inclusion_tag('app_clubs/base/navbar.html')
# def show_navbar(item_selected):
#     return {'navbar': navbar, 'logo': 'Клубы', 'item_selected': item_selected}
