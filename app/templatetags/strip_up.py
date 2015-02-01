from django import template

#@register.inclusion_tag('app/base.html', takesContext=True)
register = template.Library()
@register.filter(name='strip_up')
def strip_up(string, welp):
    s = welp.strip("\\")
    s = s.strip("\/")
    if s=='':
        return 'HOME'
    return s.upper()