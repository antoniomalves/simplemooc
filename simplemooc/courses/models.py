from django.db import models

class CourseManager(models.Manager):
	def search(self, query):
		return self.get_queryset().filter(
			models.Q(name__icontains=query) | \
			models.Q(descritpion__icontains=query) # | == consulta "ou"
		)

class Course(models.Model):

	name = models.CharField('Nome', max_length=100)
	slug = models.SlugField('Atalho')
	descritpion = models.TextField('Descricao', blank=True) #blank == campo não obrigatorio
	start_date = models.DateField(
		'Data de Início', null=True, blank=True
	) # null = true --> ele pode ficar em branco no formulario, mas no BD vai assumir o valor nulo se nao tiver preenchido
	image = models.ImageField(
		upload_to='courses/images', verbose_name='Imagem',
		null=True, blank=True
	)

	created_at = models.DateTimeField(
		'Criado em', auto_now_add=True  # quando for criado será criado o valor para a variavel
	)
	updated_at = models.DateTimeField(
		'Atualizado em', auto_now=True #toda vez que for salvo altera o valor de updated_at
	)

	objects = CourseManager()

	def __str__(self):
		return self.name

	class Meta:
		verbose_name='Curso'
		verbose_name_plural='Cursos'
		ordering = ['name']
		