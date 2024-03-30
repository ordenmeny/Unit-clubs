from django.urls import reverse_lazy

navbar = [
    {'selected': 'list_clubs', 'name': 'Все клубы', 'url': reverse_lazy('app_clubs:list_clubs', kwargs={'cat':'all'})},
    {'selected': 'create_club', 'name': 'Создать клуб', 'url': reverse_lazy('app_clubs:create_club')},
    {'selected': 'my_msg', 'name': 'Мои сообщения', 'url': reverse_lazy('app_clubs:my_notifs')},
    {'selected': 'login', 'name': 'Войти', 'url': reverse_lazy('users:login')},
    {'selected': 'signup', 'name': 'Регистрация', 'url': reverse_lazy('users:signup')},
]


def context_navbar(request, navbar=navbar):
    if request.user.is_authenticated:
        navbar = navbar[0:-2]
        navbar.append({'selected': 'profile_user', 'name': 'Профиль', 'url': reverse_lazy('app_clubs:profile_user')})
    else:
        navbar = navbar[-2:]

    return {'logo': 'Клубы', 'main_page_url': reverse_lazy('app_clubs:home_page'), 'menu_navbar': navbar}
