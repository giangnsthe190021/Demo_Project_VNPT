from django import template
import logging

logger = logging.getLogger(__name__)

register = template.Library()

@register.filter
def enumerate(value, start=0):
    logger.info(f"Enumerate called with value: {value}, type: {type(value)}, start: {start}")
    if value is None:
        return []
    try:
        return list(enumerate(value, start))
    except TypeError:
        logger.error(f"Cannot enumerate value: {value}, type: {type(value)}")
        return []