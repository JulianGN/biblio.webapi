from django.db import migrations, models


def seed_tipo_obras(apps, schema_editor):
    TipoObra = apps.get_model('gestor', 'TipoObra')
    nomes = [
        'Livro',
        'e-book',
        'Audiobook',
        'Capítulo de Livro',
        'Periódico',
        'Tese/Dissertação',
        'Mapa/Atlas',
        'Mídia Audiovisual',
        'Recurso Eletrônico',
        'Norma',
        'Obra Rara',
    ]
    for nome in nomes:
        TipoObra.objects.get_or_create(nome=nome)


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0005_unidade_email_unidade_site_unidade_telefone'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoObra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='livro',
            name='tipo_obra',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET_NULL, to='gestor.tipoobra'),
        ),
        migrations.RunPython(seed_tipo_obras),
    ]
