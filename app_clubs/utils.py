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