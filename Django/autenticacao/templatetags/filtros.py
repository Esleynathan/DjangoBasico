from django import template

register = template.Library()

@register.filter(name = 'teste')
def teste(v1):
    return f"Esse campo esta sendo filtrado pelo template {v1}"