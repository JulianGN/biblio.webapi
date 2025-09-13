from django.db import migrations, models


def seed_tipo_obras(apps, schema_editor):
    TipoObra = apps.get_model('gestor', 'TipoObra')
    nomes = [
        'livro', 'ebook', 'audiobook', 'capitulo_de_livro', 'periodico',
        'tese_dissertacao', 'mapa_atlas', 'midia_audiovisual', 'recurso_eletronico',
        'norma', 'obra_rara'
    ]
    for nome in nomes:
        TipoObra.objects.get_or_create(nome=nome)


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0008_update_tipoobra_names'),
    ]

    operations = [
        # Remover FK de Livro para permitir dropar a tabela
        migrations.RemoveField(
            model_name='livro',
            name='tipo_obra',
        ),
        # Apagar a tabela antiga TipoObra
        migrations.DeleteModel(
            name='TipoObra',
        ),
        # Recriar TipoObra com a definição correta
        migrations.CreateModel(
            name='TipoObra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
            ],
        ),
        # Re-adicionar campo tipo_obra em Livro apontando para a nova tabela
        migrations.AddField(
            model_name='livro',
            name='tipo_obra',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET_NULL, to='gestor.tipoobra'),
        ),
        # Popular com os nomes canônicos
        migrations.RunPython(seed_tipo_obras),
    ]
