from django.db import models


class CustomModelManager(models.Manager):
    def get_ro_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except self.model.DoesNotExist:
            return None