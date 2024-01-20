class DataMixin:
    extra_context = {}
    item_selected = None

    def __init__(self):
        self.extra_context['item_selected'] = self.item_selected
