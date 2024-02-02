from django import template

register = template.Library()


@register.inclusion_tag('app_clubs/base/main_img.html')
def show_main_img(height_img, title=None):
    context = {
        'height_img': height_img,
    }
    if title:
        context['title'] = title

    return context
