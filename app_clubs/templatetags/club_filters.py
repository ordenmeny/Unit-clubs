from django import template

register = template.Library()


@register.filter
def list_content(lst, param):
    by, size = map(int, param.split(':'))
    return lst[0:len(lst) // by * by][:size]