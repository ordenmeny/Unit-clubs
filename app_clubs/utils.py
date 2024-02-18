from django.contrib.auth.mixins import LoginRequiredMixin


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
    pass
    # делается проверка: если текущий пользователь есть в текущем клубе, то ...
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)

    # проверка: если текущий пользователь является админом к текущем клубе, то...
