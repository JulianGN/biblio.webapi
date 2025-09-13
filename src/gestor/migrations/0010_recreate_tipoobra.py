from django.db import migrations


def seed_tipo_obras(apps, schema_editor):
    """Apaga todos os registros antigos e insere os nomes corretos.

    Esta migração é intencionalmente apenas de dados: não altera o schema
    para evitar problemas de dependência e diferenças entre bancos (SQLite).
    """
    TipoObra = apps.get_model('gestor', 'TipoObra')
    # nomes corrigidos / desejados
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
    # Apagar registros antigos
    TipoObra.objects.all().delete()
    # Inserir os novos (mantém a tabela e FKs intactos)
    for nome in nomes:
        TipoObra.objects.create(nome=nome)


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0009_recreate_tipoobra'),
    ]

    operations = [
        migrations.RunPython(seed_tipo_obras, reverse_code=migrations.RunPython.noop),
    ]
