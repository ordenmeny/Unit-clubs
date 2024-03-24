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