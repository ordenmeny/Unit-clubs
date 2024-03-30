from django import template

register = template.Library()


@register.filter
def list_content(lst, param):
    if param == "None":
        return lst
    by, size = map(int, param.split(':'))
    if len(lst) < by:
        return lst
    return lst[0:len(lst) // by * by][:size]


@register.filter
def tg_club(href):
    if 'https://t.me/' in href:
        href = href.replace('https://t.me/', '@')

    return href