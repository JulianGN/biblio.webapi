from gestor.domain.repositories.livro_repository import LivroRepositorio

class LivroCasosDeUso:
    @staticmethod
    def listar_livros():
        return LivroRepositorio.obter_todos_livros()

    @staticmethod
    def obter_livro(livro_id):
        return LivroRepositorio.obter_livro_por_id(livro_id)

    @staticmethod
    def criar_livro(dados):
        return LivroRepositorio.criar_livro(**dados)

    @staticmethod
    def atualizar_livro(livro_id, dados):
        livro = LivroRepositorio.obter_livro_por_id(livro_id)
        return LivroRepositorio.atualizar_livro(livro, **dados)

    @staticmethod
    def excluir_livro(livro_id):
        livro = LivroRepositorio.obter_livro_por_id(livro_id)
        LivroRepositorio.excluir_livro(livro)
