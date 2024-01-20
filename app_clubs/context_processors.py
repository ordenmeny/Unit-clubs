from django.urls import reverse_lazy

navbar = [
    {'selected': 'list_clubs', 'name': 'Все клубы', 'url': reverse_lazy('app_clubs:list_clubs')},
    {'selected': 'create_club', 'name': 'Создать клуб', 'url': reverse_lazy('app_clubs:create_club')},
]


def context_navbar(request):
    return {'logo': 'Клубы', 'menu_navbar': navbar}
