from gestor.domain.entities.livro import Livro

class LivroRepositorio:
    @staticmethod
    def obter_todos_livros():
        return Livro.objects.all()

    @staticmethod
    def obter_livro_por_id(livro_id):
        return Livro.objects.get(id=livro_id)

    @staticmethod
    def criar_livro(**kwargs):
        return Livro.objects.create(**kwargs)

    @staticmethod
    def atualizar_livro(livro, **kwargs):
        for chave, valor in kwargs.items():
            setattr(livro, chave, valor)
        livro.save()
        return livro

    @staticmethod
    def excluir_livro(livro):
        livro.delete()
