from project.model.user import User
from project.repository.user_repository import UserRepository


class CadastroUsuario:
    def __init__(self):
        self.user_repository = UserRepository()

    def cadastrar(self) -> None:
        nome = input("Digite seu nome: ")
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")

        usuario = User(nome, email, senha)

        self.user_repository.save(usuario)
