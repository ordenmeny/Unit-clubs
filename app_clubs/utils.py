from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy

from app_clubs.models import Club


class DataMixin:
    # Создается объект класса CreateView.
    # В нем ищется атрибут extra_context.
    # Но находится в родительском классе DataMixin
    # В инициализаторе extra_context изменяется: в него добавляется атрибут item_selected.
    extra_context = {}
    item_selected = None

    def __init__(self):
        # self - ссылка на класс CreateView
        self.extra_context['item_selected'] = self.item_selected


class RequiredClubMember(LoginRequiredMixin):
    for_admin = False

    def dispatch(self, request, *args, **kwargs):
        # получаем объекты пользователя и клуба
        current_user = request.user
        current_club = Club.objects.get(slug=self.kwargs['club_slug'])
        # делаем проверку, есть ли такой клуб у пользователя. Если нет-редирект!
        if not (current_club in current_user.clubs.all()):
            return redirect(reverse_lazy('app_clubs:home_page'))

        # Является ли страница только для админов? Проверка на админство
        if self.for_admin:
            if request.user not in current_club.admins.all():
                return redirect(reverse_lazy('app_clubs:home_page'))

        request.current_club = current_club
        return super().dispatch(request, *args, **kwargs)
