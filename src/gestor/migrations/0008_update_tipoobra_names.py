from django.db import migrations


def normalize_tipo_obras(apps, schema_editor):
    TipoObra = apps.get_model('gestor', 'TipoObra')
    Livro = apps.get_model('gestor', 'Livro')

    # mapa de valores existentes (possíveis) para nomes canônicos
    mapping = {
        'livro': 'livro',
        'livros': 'livro',
        'e-book': 'ebook',
        'ebook': 'ebook',
        'audiobook': 'audiobook',
        'cd - audiolivro': 'audiobook',
        'capítulo de livro': 'capitulo_de_livro',
        'capitulo de livro': 'capitulo_de_livro',
        'capítulo': 'capitulo_de_livro',
        'periódico': 'periodico',
        'periodico': 'periodico',
        'tese/dissertação': 'tese_dissertacao',
        'tese': 'tese_dissertacao',
        'dissertação': 'tese_dissertacao',
        'mapa/atlas': 'mapa_atlas',
        'mapa': 'mapa_atlas',
        'atlas': 'mapa_atlas',
        'mídia audiovisual': 'midia_audiovisual',
        'midia audiovisual': 'midia_audiovisual',
        'dvd': 'midia_audiovisual',
        'recurso eletrônico': 'recurso_eletronico',
        'recurso eletronico': 'recurso_eletronico',
        'norma': 'norma',
        'obra rara': 'obra_rara',
    }

    canonical = [
        'livro', 'ebook', 'audiobook', 'capitulo_de_livro', 'periodico',
        'tese_dissertacao', 'mapa_atlas', 'midia_audiovisual', 'recurso_eletronico',
        'norma', 'obra_rara'
    ]

    # garantir entries canônicas
    canonical_objs = {}
    for name in canonical:
        obj, _ = TipoObra.objects.get_or_create(nome=name)
        canonical_objs[name] = obj

    # percorrer tipos existentes e reatribuir livros
    for old in list(TipoObra.objects.all()):
        old_name = (old.nome or '').strip().lower()
        target = mapping.get(old_name)
        if target:
            new_obj = canonical_objs[target]
            # mover referências de Livro
            Livro.objects.filter(tipo_obra_id=old.id).update(tipo_obra_id=new_obj.id)
            if old.id != new_obj.id:
                old.delete()
        else:
            # se já for canônico em forma diferente (ex: capitalização), tentar mapear
            if old_name in canonical:
                # já existe canonical com mesmo valor - nada a fazer
                continue
            # caso não mapeado, mover para null (opcional: podemos mapear tudo para 'livro')
            Livro.objects.filter(tipo_obra_id=old.id).update(tipo_obra=None)
            old.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0007_alter_tipoobra_id'),
    ]

    operations = [
        migrations.RunPython(normalize_tipo_obras),
    ]
