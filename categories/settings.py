from django.conf import settings
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _

ALLOW_SLUG_CHANGE = getattr(settings, 'ALLOW_SLUG_CHANGE', False)
RELATION_MODELS = getattr(settings, 'RELATION_MODELS', [])
M2M_REGISTRY = getattr(settings, 'M2M_REGISTRY', {})
FK_REGISTRY = getattr(settings, 'FK_REGISTRY', {})
THUMBNAIL_UPLOAD_PATH = getattr(settings, 'THUMBNAIL_UPLOAD_PATH', 'uploads/categories/thumbnails')
THUMBNAIL_STORAGE = getattr(settings, 'THUMBNAIL_STORAGE', settings.DEFAULT_FILE_STORAGE)
JAVASCRIPT_URL = getattr(settings, 'JAVASCRIPT_URL', getattr(settings, 'STATIC_URL', settings.MEDIA_URL) + 'js/')
SLUG_TRANSLITERATOR = getattr(settings, 'SLUG_TRANSLITERATOR', '')
RELATION_MODELS = getattr(settings, 'RELATION_MODELS', [])
CATEGORIES_SETTINGS = getattr(settings, 'CATEGORIES_SETTINGS', {})
REGISTER_ADMIN = getattr(settings, 'REGISTER_ADMIN', True)


if SLUG_TRANSLITERATOR:
    if callable(SLUG_TRANSLITERATOR):
        pass
    elif isinstance(SLUG_TRANSLITERATOR, basestring):
        from django.utils.importlib import import_module
        bits = SLUG_TRANSLITERATOR.split(".")
        module = import_module(".".join(bits[:-1]))
        SLUG_TRANSLITERATOR = getattr(module, bits[-1])
    else:
        from django.core.exceptions import ImproperlyConfigured
        raise ImproperlyConfigured(_('%(transliterator) must be a callable or a string.') %
                                   {'transliterator': 'SLUG_TRANSLITERATOR'})
else:
    SLUG_TRANSLITERATOR = lambda x: x



RELATIONS = [Q(app_label=al, model=m) for al, m in [x.split('.') for x in RELATION_MODELS]]

# The field registry keeps track of the individual fields created.
#  {'app.model.field': Field(**extra_params)}
#  Useful for doing a schema migration
FIELD_REGISTRY = {}

# The model registry keeps track of which models have one or more fields
# registered.
# {'app': [model1, model2]}
# Useful for admin alteration
MODEL_REGISTRY = {}
