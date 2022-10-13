from django.contrib import admin
from escola.models import Aluno, Curso, Matricula


class AlunosDisplay(admin.ModelAdmin):
    list_display = ('id', 'nome', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20

class CursosDisplay(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao', 'nivel')
    list_display_links = ('id', 'codigo_curso')
    search_fields = ('codigo_curso',)

class MatriculaDisplay(admin.ModelAdmin):
    list_display =  ('id', 'aluno', 'curso', 'periodo')
    list_display_links = ('id',)

admin.site.register(Matricula, MatriculaDisplay)
admin.site.register(Curso, CursosDisplay)
admin.site.register(Aluno, AlunosDisplay)
