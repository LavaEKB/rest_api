class OneDBRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'kassa':
            return 'default'
        return None  # 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'kassa':
            return 'default'
        return None  # 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'kassa' and obj2._meta.app_label == 'kassa':
            return True
        return None

    def allow_syncdb(self, db, model):
        if db == 'default' or model._meta.app_label == 'kassa':
            return False
        else:
            return True