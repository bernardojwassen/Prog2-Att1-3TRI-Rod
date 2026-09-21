class Pessoa:
    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento

    def apresentar(self):
        return f"Nome: {self.nome}, Nascido(a) em: {self.data_nascimento}"


class Aluno(Pessoa):
    def __init__(self, nome, data_nascimento, matricula, curso, notas=None):
        super().__init__(nome, data_nascimento)
        self.matricula = matricula
        self.curso = curso
        self.notas = notas if notas else []

    def calcular_media(self):
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)

    def apresentar(self):
        media = self.calcular_media()
        return f"[Aluno] Matrícula: {self.matricula} | {super().apresentar()} | Curso: {self.curso} | Média: {media:.2f}"


class Professor(Pessoa):
    def __init__(self, nome, data_nascimento, matricula, disciplina):
        super().__init__(nome, data_nascimento)
        self.matricula = matricula
        self.disciplina = disciplina

    def apresentar(self):
        return f"[Professor] Matrícula: {self.matricula} | {super().apresentar()} | Disciplina: {self.disciplina}"


# Testando o sistema escolar
print("--- TESTE DO SISTEMA ESCOLAR ---")
aluno1 = Aluno("Ana Silva", "15/05/2005", "A123", "Engenharia", [8.5, 7.0, 9.0])
professor1 = Carlos = Professor("Carlos Souza", "10/10/1980", "P987", "Matemática")

print(aluno1.apresentar())
print(professor1.apresentar())