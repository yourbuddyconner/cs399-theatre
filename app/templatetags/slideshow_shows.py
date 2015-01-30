from django import template
from app.models import Show

@register.inclusion_tag('app/base.html', takesContext=True)
def menu_items(context):
    return {'shows': Show.objects.all()[:3]}