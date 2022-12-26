from django.db import models
#automaticaly genereted number
class generateNumbers(models.Model):
	prefix = models.CharField(max_length=3, blank=False, unique=True)
	description = models.CharField(max_length=50, blank=False, unique=True)
	year = models.BooleanField(default=True)
	month = models.BooleanField(default=True)
	number = models.PositiveSmallIntegerField()
	last_number = models.CharField(max_length=50, blank=True)

	class Meta:
		ordering = ('prefix', 'year', 'month', )
		
	def __str__(self):
		return f"{self.prefix} {self.year} {self.month}"
