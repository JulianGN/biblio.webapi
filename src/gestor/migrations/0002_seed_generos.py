from django.db import migrations

def seed_generos(apps, schema_editor):
    Genero = apps.get_model('gestor', 'Genero')
    generos = [
        'Ficção', 'Não Ficção', 'Romance', 'Fantasia', 'Terror', 'Biografia', 'História', 'Ciência'
    ]
    for nome in generos:
        Genero.objects.create(nome=nome)

class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_generos),
    ]
