from django import template
from decimal import Decimal
import locale

register = template.Library()

@register.filter
def multiply(value, arg):
    """Multiplies the value by the argument"""
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0

@register.filter
def currency(value):
    """Formats a number as GBP currency"""
    try:
        return f"£{float(value):.2f}"
    except (ValueError, TypeError):
        return "£0.00"

@register.filter
def discount_price(price, discount_percent):
    """Calculate discounted price"""
    try:
        discount = float(price) * (float(discount_percent) / 100)
        return float(price) - discount
    except (ValueError, TypeError):
        return price

@register.filter
def vat_amount(price, vat_rate=20):
    """Calculate VAT amount"""
    try:
        return float(price) * (float(vat_rate) / 100)
    except (ValueError, TypeError):
        return 0

@register.filter
def price_with_vat(price, vat_rate=20):
    """Calculate price including VAT"""
    try:
        vat = float(price) * (float(vat_rate) / 100)
        return float(price) + vat
    except (ValueError, TypeError):
        return price