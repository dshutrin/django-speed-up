from django.db import models


# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=256, verbose_name="Заголовок", unique=True)
	media = models.ImageField(verbose_name="Превью", upload_to="previews")
	body = models.TextField(verbose_name="Содержание")

	def __str__(self):
		return f"Пост '{self.title}'"

	class Meta:
		verbose_name = "Пост"
		verbose_name_plural = "Посты"

