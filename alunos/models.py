from django.db import models

class Aluno(models.Model):
    # Informações pessoais
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14, unique=True)
    rg = models.CharField(max_length=20, blank=True, null=True)
    data_nascimento = models.DateField()
    sexo = models.CharField(
        max_length=10,
        choices=[("M", "Masculino"), ("F", "Feminino"), ("O", "Outro")]
    )

    # Contato
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    telefone_emergencia = models.CharField(max_length=15, blank=True, null=True)

    # Endereço
    cep = models.CharField(max_length=9)
    endereco = models.CharField(max_length=150)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

    # Acadêmico
    matricula = models.CharField(max_length=20, unique=True)

    # lista fixa de cursos
    curso = models.CharField(max_length=20,
        choices=[
        ("Informática", "Informática"),
        ("Administração", "Administração"),
        ("Enfermagem", "Enfermagem"),
        ("Direito", "Direito"),
        ("Apicultura", "Apicultura"),
        ("Alimentos", "Alimentos"),  ]
    )

    serie_ano = models.CharField(max_length=20)
    turno = models.CharField(
        max_length=20,
        choices=[
            ("Manhã", "Manhã"),
            ("Tarde", "Tarde"),
            ("Noite", "Noite"),
            ("Integral", "Integral"),
        ]
    )
    status = models.CharField(
        max_length=10,
        choices=[("Ativo", "Ativo"), ("Inativo", "Inativo")],
        default="Ativo"
    )
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nome} ({self.matricula})"
