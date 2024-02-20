from django.urls import reverse_lazy

navbar = [
    {'selected': 'list_clubs', 'name': 'Все клубы', 'url': reverse_lazy('app_clubs:list_clubs')},
    {'selected': 'create_club', 'name': 'Создать клуб', 'url': reverse_lazy('app_clubs:create_club')},
    {'selected': 'login', 'name': 'Войти', 'url': reverse_lazy('users:login')},
    {'selected': 'signup', 'name': 'Регистрация', 'url': reverse_lazy('users:signup')},
    # {'selected': 'create_post', 'name': 'Создать пост', 'url': reverse_lazy('app_clubs:create_post')},
    # {'selected': 'create_event', 'name': 'Создать событие', 'url': reverse_lazy('app_clubs:create_event')},
]


def context_navbar(request):
    return {'logo': 'Клубы', 'main_page_url': reverse_lazy('app_clubs:home_page'), 'menu_navbar': navbar}
