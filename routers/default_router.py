

class DefaultAppRouter:
    
    apps = ['admin', 'auth', 'contenttypes', 'sessions']
    
    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.apps:
            return 'settings'
        return None
    
    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.apps:
            return 'settings'
        return None
    
    def allow_relation(self, obj1, obj2, **hints):
        if(
            obj1._meta.app_label in self.apps and
            obj2._meta.app_label in self.apps
        ):
            return True
        return None
      
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.apps:
            return db== 'settings'
        return None
    
    
      
    
    