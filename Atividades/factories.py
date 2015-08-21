import factory
from Atividades.models import Atividade

class AtividadeFactory(factory.django.DjangoModelFactory):

	class Meta:
		model = Atividade

	nome = factory.Sequence(lambda i: "Atividade {0}".format(i))
	descricao = "uma descricao aleatoria de uma atividade super legal"