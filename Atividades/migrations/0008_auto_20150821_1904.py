# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models, migrations
from Atividades.models import Atividade
from Atividades.models import Categoria

def lancar_atividades(apps, schema_editor):
	esporte = Categoria.objects.get(nome="Esporte")
	cultura = Categoria.objects.get(nome="Cultura")
	lazer = Categoria.objects.get(nome="Lazer")

	Atividade.objects.create(nome='Parque das Nações Indígenas', endereco="Altos da Av. Afonso Pena, Campo Grande, MS", descricao="Vários equipamentos urbanos estão previstos para o local destacando-se as atuais instalações do Monumento ao Índio e Museu de Arte Contemporânea, além dos extensos caminhos de circulação utilizados como pistas de caminhadas. A área do logradouro é monitorada por um pelotão montado da Polícia Florestal do Estado, que tem sua sede no interior do parque", categoria=esporte, url='https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSn0nU8R_nUGYV34BOemcb8vDxNk9WiqApWm2BireHl1KS_MMSc')
	Atividade.objects.create(nome='Orla Morena', endereco="R. Antônio Norberto de Almeida, Amambaí, Campo Grande, MS", descricao="ótimo local para caminhas ao ar livre, ciclismo, skate, volei, basquete e futsal.", categoria=esporte, url='http://cdn1.campograndenews.com.br/uploads/tmp/images/5087688/wm-640x480-25cc51021ec77df2a90f728b2023ee35.jpg')
	Atividade.objects.create(nome='Pontal das Águas', endereco="R-262, sentido Três Lagoas, e sua entrada se localiza a 12 quilômetros do Anel Rodoviário (2,82 km após o Autódromo Internacional)", descricao="UA programação básica da Fazenda Pontal das Águas proporciona um dia inteiro de alegria, em contato com a natureza.", categoria=esporte, url='http://www.pontaldasaguas.com.br/img/ft-galeria_038.jpg')
	Atividade.objects.create(nome='Toca do Ouriço', endereco="35 km ao norte de Campo Grande pela saída da Av. Tamandaré.", descricao="A Toca do Ouriço é uma experiência única, por reunir no mesmo espaço Turismo de Aventura com pujante cachoeira, várias corredeiras, mata nativa com espécies vegetais de grande porte, animais silvestres", categoria=esporte, url='http://www.tocadoourico.com.br/files/aventurafotos/arvorismo_19053765_426x252_outside.JPG')
	Atividade.objects.create(nome='Praça Esportiva Belmar Fidalgo', endereco="R. Dom Aquino, 2536 - Centro, Campo Grande - MS", descricao="UNa Praça Belmar Fidalgo existem duas quadras poli esportivas, arena para quadras de areia, pista de cooper, banheiros, duchas, campo de futebol suíço, playground infantil, área para ginástica, sede administrativa, muito verde e uma forte iluminação. O local é muito frequentado, sobretudo aos finais de semana.", categoria=esporte, url='http://photos1.blogger.com/blogger/1199/3681/320/belmar.jpg')

	Atividade.objects.create(nome='Museu de Arte Contemporânea - MARCO', endereco="Endereço: Antônio Maria Coelho, 6000 – Parque das Nações Indígenas, Campo Grande, MS", descricao="O Museu de Arte Contemporânea de Mato Grosso do Sul – MARCO, unidade da Fundação de Cultura de Mato Grosso do Sul, foi criado através do Decreto nº 6266, em 17 de Dezembro de 1991. A primeira sede localizou-se na Avenida Calógeras, nº 2499, esquina com a Rua Marechal Cândido Mariano Rondon, em edifício adaptado para a finalidade museológica, permanecendo neste endereço até 1999, quando foi instalado provisoriamente, na Rua Barão do Rio Branco, nº1980.", categoria=cultura, url='http://www.fundacaodecultura.ms.gov.br/wp-content/uploads/sites/19/2014/11/Marco.jpg')
	Atividade.objects.create(nome='Arquivo Público', endereco="Av. Fernando Corrêa da Costa, 559 – Térreo | Centro, Campo Grande, MS", descricao="A atribuição do Arquivo Público Estadual é garantir a preservação da memória histórica do Estado de Mato Grosso do Sul, através da gestão dos documentos produzidos e acumulados pela administração direta, fundações e autarquias do poder executivo estadual. Neste sentido presta assessoria aos órgãos do executivo estadual e aos municípios de MS. Através de seus projetos, o Arquivo Público garante a produção de fontes para a pesquisa histórica.", categoria=cultura, url='http://www.fundacaodecultura.ms.gov.br/wp-content/uploads/sites/19/2014/11/2.jpg')
	Atividade.objects.create(nome='Biblioteca Pública Estadual Dr. Isaías Paim', endereco="Av. Fernando Corrêa da Costa, 559 – 2º Andar | Centro, Campo Grande, MS", descricao="A Biblioteca Pública Estadual Dr. Isaías Paim, criada pelo decreto nº 826, de 5 de dezembro de 1981 é unidade da Fundação de Cultura de Mato Grosso do Sul. Atualmente possui acervo com 43.580 exemplares dentre livros e periódicos, mas busca a cada ano atualizar o acervo de forma a compô-lo com obras que atendam às necessidades informacionais de seus leitores.", categoria=cultura, url='http://www.fundacaodecultura.ms.gov.br/wp-content/uploads/sites/19/2015/04/Biblioteca_Alexander-On%C3%A7a-300x169.jpg')
	Atividade.objects.create(nome='Casa do Artesão', endereco="Av. Calógeras, 2050 – Centro,Campo Grande, MS", descricao="Construída em 1923 para ser residência e comércio. Em 1924 é transformada na 1ª agência do Banco do Brasil do Estado. Inaugurada no dia 1º de setembro de 1975 como Casa do Artesão, onde se comercializa artesanato regional até hoje. E, em julho de 1994 foi tombada pelo Patrimônio Histórico Estadual.", categoria=cultura, url='http://www.fundacaodecultura.ms.gov.br/wp-content/uploads/sites/19/2014/11/casa-do-artesao-foto.jpg')
	Atividade.objects.create(nome='Centro Cultural', endereco="Rua 26 de agosto, 453 – Centro, Campo Grande, MS", descricao="O Centro Cultural José Octavio Guizzo (CCJOG) é um espaço dedicado a geração, formação e difusão da cultura sul-mato-grossense. Em quase duas décadas de funcionamento, o complexo arquitetônico CCJOG possui aparato que possibilita a realizção de oficinas de artes, espetáculos, exposições, palestras exibições de videos e eventos similares. Sua estrutura abriga a Sala de Convenções Rubens Corrêa, Galeria de Exposições Wega Nery, Ateliê de Artes, Sala de Ensaios Conceição Ferreira, Sala de Música, Sala Central e Teatro Aracy Balabanian. No CCJOG acontecem oficinas de dança, música, teatro, artes plásticas e capoeira, além de espetáculos e exposições.", categoria=cultura, url='http://www.fundacaodecultura.ms.gov.br/wp-content/uploads/sites/19/2014/11/centro-cultural-foto.jpg')

	Atividade.objects.create(nome='Parque Florestal Antonio de Albuquerque - Horto', endereco="Av. Pres. Ernesto Geisel", descricao="O Parque Florestal Antonio de Albuquerque dispõe atualmente de inúmeras opções de lazer com destaque para conchas de mocha e de medalha, parque infantil, pista de skate, teatro de arena, oficinas artísticas e culturais, além da Biblioteca Municipal Profª Ana Luiza do Prado Bastos.", categoria=lazer, url='http://cdn1.campograndenews.com.br/uploads/tmp/images/5030494/wm-640x480-4eb2b52be2f942f2d7ce09eeb38d83aa1b510861515fc.jpg')
	Atividade.objects.create(nome='Lago do Amor', endereco="Rua Sertãozinho , Campo Grande, MS", descricao="O Lago do Amor faz parte do complexo da Universidade Federal de Mato Grosso do Sul, revitalizado, ganhou bancos para os apreciadores de um pôr do sol de tirar o folego. Durante a manhã é habitual conviver com as capivaras, jacarés e algumas aves.Natureza linda com um por do sol esplendido, muitos animais pantaneiros situados na UFMS como capivaras, jacarés, macacos e tucanos. ideal para caminhar ou simplesmente aproveitar com o amor.", categoria=lazer, url='http://static.panoramio.com/photos/original/4139754.jpg')
	Atividade.objects.create(nome='Parque das Nações Indígenas', endereco="Altos da Av. Afonso Pena, Campo Grande, MS", descricao="Vários equipamentos urbanos estão previstos para o local destacando-se as atuais instalações do Monumento ao Índio e Museu de Arte Contemporânea, além dos extensos caminhos de circulação utilizados como pistas de caminhadas. A área do logradouro é monitorada por um pelotão montado da Polícia Florestal do Estado, que tem sua sede no interior do parque", categoria=lazer, url='http://media-cdn.tripadvisor.com/media/photo-o/03/31/31/d9/parque-das-nacoes-indigenas.jpg')
	Atividade.objects.create(nome='Reserva Canindé', endereco="A Reserva Canindé localiza-se a 27 Km do aeroporto internacional de Campo Grande/MS.", descricao="A Reserva Canindé, situada no município de Terenos/MS, está a apenas 27 km do aeroporto internacional de Campo Grande/MS. Possui área de 180 hectares, sendo 80% desta preservada ou em processo de recuperação natural.  Sua flora apresenta diversidade de espécies do cerrado e algumas espécies da mata atlântica. Tem uma fauna com  grande variedade de aves e animais. A inspiração do nome da reserva se deu devido à presença constante das araras canindé nesta região.", categoria=lazer, url='http://www.reservacaninde.com.br/fotos/diarias/g20111207002856.jpg')
	Atividade.objects.create(nome='Feira Central', endereco="Rua 14 de Julho, 3351 – Campo Grande / MS", descricao="A Feira Central de Campo Grande é uma feira localizada na cidade brasileira de Campo Grande, no estado de Mato Grosso do Sul. Também conhecida como feirona, é coordenada pela comunidade okinawana, que já se adaptou à culinária local. É semelhante a uma feira qualquer do Brasil. Os destaques são o tradicional espetinho com a mandioca amarela da terra e o sobá. Outras opções são o artesanato e o comércio de produtos típicos.", categoria=lazer, url='http://feiracentralcg.com.br/wp-content/uploads/2015/06/DSC_0936_2.jpg')

class Migration(migrations.Migration):

    dependencies = [
        ('Atividades', '0007_inclusao_de_exemplos_de_cg'),
    ]

    operations = [
    	#migrations.RunPython(lancar_atividades)    
    ]
