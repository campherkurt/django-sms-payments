from south.modelsinspector import add_introspection_rules
from django.db.models import CharField

#UUIDField from http://www.djangosnippets.org/snippets/335/
try:
    import uuid
except ImportError:
    from django.utils import uuid


class UUIDField(CharField) :
    
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = kwargs.get('max_length', 32 )
        try:
            self.auto = kwargs['auto']
            del kwargs['auto']
        except KeyError:
            self.auto = True
        CharField.__init__(self, *args, **kwargs)
    
    def pre_save(self, model_instance, add):
        if add :
            value=getattr(model_instance,self.attname)
            if not value:
                if not self.blank:
                    if self.auto:
                        value = unicode(uuid.uuid4()).replace('-','')
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super(CharField, self).pre_save(model_instance, add)
add_introspection_rules([], ["^checkoutservice\.lib\.fields\.UUIDField"])


