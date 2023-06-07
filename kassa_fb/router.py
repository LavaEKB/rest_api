class TwoDBRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'kassa_fb':
            return 'fbird'
        return None  # 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'kassa_fb':
            return 'fbird'
        return None  # 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'kassa_fb' and obj2._meta.app_label == 'kassa_fb':
            return True
        return None

    def allow_syncdb(self, db, model):
        if db == 'fbird' or model._meta.app_label == 'kassa_fb':
            return False
        else:
            return True