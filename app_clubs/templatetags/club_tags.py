from django import template

register = template.Library()


@register.inclusion_tag('app_clubs/base/main_img.html')
def show_main_img(height, title=None, opacity=None, src=None):
    context = {
        'height_img': height,
    }
    if title:
        context['title'] = title
    if opacity:
        context['opacity'] = opacity

    if src:
        context['src'] = src
    else:
        context['src'] = 'app_clubs/images/main_page.png'

    return context
