from django.db import models

# -------------- Global application settings ------------------

class GlobalVariables(models.Model):
    """
    Model
    """
    group = models.CharField(max_length=50, verbose_name="Group")
    key = models.CharField(max_length=50, verbose_name="Key")
    value = models.TextField(max_length=1050, verbose_name="Value")
    description = models.TextField(max_length=1050, verbose_name="Description")

    class Meta:
        # the key must be unique
        index_together = unique_together = [['group', 'key']]
        ordering = ('group', 'key')

    def __str__(self):
        return f"group: {self.key} - key: {self.key} - value: {self.value}"
