# 1. Listas
filme = ['Um Sonho de Liberdade', 'O Poderoso Chefão', 'Batman: O Cavaleiro das Trevas', 'O Poderoso Chefão II',
         '12 Homens e uma Sentença',
         'A Lista de Schindler', 'O Senhor dos Anéis: O Retorno do Rei',
         'Pulp Fiction - Tempo de Violência',
         'O Senhor dos Anéis: A Sociedade do Anel',
         'Três Homens em Conflito']

# 2. Conjuntos
print(filme)
filme.pop(0)
print(filme)
filme.insert(1, 'Um Sonho de Liberdade')
print(filme)

UltimosTresFilme = filme[7:]
FilmesRepetidos = filme + UltimosTresFilme
# Imprimir o resultado
print(FilmesRepetidos)

FilmesRepetidos = list(set(FilmesRepetidos))
print(FilmesRepetidos)
# 3 . Dicionários
filmes = {
    'Filmes': {
        '1. Um Sonho de Liberdade': {
            'nome': 'Um Sonho de Liberdade',
            'ano': 1994,
            'sinopse': 'Andy Dufresne é condenado a duas prisões perpétuas consecutivas pelas mortes de sua esposa e de seu amante. Porém, só Andy sabe que ele não cometeu os crimes. No presídio, durante dezenove anos, ele faz amizade com Red, sofre as brutalidades da vida na cadeia, se adapta, ajuda os carcereiros, etc.'
        },
        '2. O Poderoso Chefão': {
            'nome': 'O Poderoso Chefão',
            'ano': 1972,
            'sinopse': 'A série de filmes The Godfather consiste em três filmes de drama e suspense policial dirigidos por Francis Ford Coppola com base no romance homônimo do ítalo-americano Mario Puzo. A trilogia narra as tramas envolvendo a Família Corleone, umas das mais poderosas famílias da Máfia italiana nos Estados Unidos'
        },
        '3. Batman: O Cavaleiro das Trevas': {
            'nome': 'Batman: O Cavaleiro das Trevas',
            'ano': 2008,
            'sinopse': 'Batman tem conseguido manter a ordem em Gotham com a ajuda de Jim Gordon e Harvey Dent. No entanto, um jovem e anárquico criminoso, conhecido apenas como Coringa, pretende testar o Cavaleiro das Trevas e mergulhar a cidade em um verdadeiro caos.'
        },
        '4. O Poderoso Chefão II': {
            'nome': 'O Poderoso Chefão II',
            'ano': 1974,
            'sinopse': 'Depois da máfia matar sua família, o jovem Vito foge da sua cidade na Sicília e vai para os Estados Unidos. Lá, ele assassina Black Hand Fanucci, que exigia dos comerciantes uma parte dos seus ganhos. Com a morte de Fanucci, o poder de Vito cresce, mas sua família é o que mais importa para ele. Morando agora no Lago Tahoe, Michael planeja fazer incursões em Las Vegas e Havana com negócios ligados ao lazer, mas descobre que aliados como Hyman Roth estão tentando matá-lo.'
        },
        '5. 12 Homens e uma Sentença': {
            'nome': '12 Homens e uma Sentença',
            'ano': 1957,
            'sinopse': 'Seguindo o encerramento do caso do julgamento do assassinato cometido por um adolescente, os membros do júri devem chegar a um consenso sobre qual será o veredito. Enquanto os 12 indivíduos estão fechados em uma sala para tomar uma decisão, onze deles votam pela condenação do réu, porém um deles acredita na inocência do jovem e tenta convencer os outros a mudarem seus votos, dando início a um conflito que ameaça inviabilizar o delicado processo que vai decidir o destino do acusado.'
        },
        '6. A Lista de Schindler': {
            'nome': 'A Lista de Schindler',
            'ano': 1993,
            'sinopse': 'O alemão Oskar Schindler viu na mão de obra judia uma solução barata e viável para lucrar com negócios durante a guerra. Com sua forte influência dentro do partido nazista, foi fácil conseguir as autorizações e abrir uma fábrica. O que poderia parecer uma atitude de um homem não muito bondoso, transformou-se em um dos maiores casos de amor à vida da História, pois este alemão abdicou de toda sua fortuna para salvar a vida de mais de mil judeus em plena luta contra o extermínio alemão.'
        },
        '7. O Senhor dos Anéis: O Retorno do Rei': {
            'nome': 'O Senhor dos Anéis: O Retorno do Rei',
            'ano': 2003,
            'sinopse': 'O confronto final entre as forças do bem e do mal que lutam pelo controle do futuro da Terra Média se aproxima. Sauron planeja um grande ataque a Minas Tirith, capital de Gondor, o que faz com que Gandalf e Pippin partam para o local na intenção de ajudar a resistência.'
        },
        '8. Pulp Fiction - Tempo de Violência': {
            'nome': 'Pulp Fiction - Tempo de Violência',
            'ano': 1994,
            'sinopse': 'Assassino que trabalha para a máfia se apaixona pela esposa de seu chefe quando é convidado a acompanhá-la, um boxeador descumpre sua promessa de perder uma luta e um casal tenta um assalto que rapidamente sai do controle.'
        },
        '9. O Senhor dos Anéis: A Sociedade do Anel': {
            'nome': 'O Senhor dos Anéis: A Sociedade do Anel',
            'ano': 2001,
            'sinopse': 'Em uma terra fantástica e única, um hobbit recebe de presente de seu tio um anel mágico e maligno que precisa ser destruído antes que caia nas mãos do mal. Para isso, o hobbit Frodo tem um caminho árduo pela frente, onde encontra perigo, medo e seres bizarros. Ao seu lado para o cumprimento desta jornada, ele aos poucos pode contar com outros hobbits, um elfo, um anão, dois humanos e um mago, totalizando nove seres que formam a Sociedade do Anel.'
        },
        '10. Três Homens em Conflito': {
            'nome': 'Três Homens em Conflito',
            'ano': 1966,
            'sinopse': 'Nos Estados Unidos, durante a Guerra de Secessão, um pistoleiro misterioso tenta trabalhar em conjunto com um bandido e um caçador de recompensas para encontrar um tesouro escondido. Os homens são obrigados a forjar uma difícil aliança visto que cada um conhece apenas uma parte da localização da fortuna. O problema é que nenhum deles tem a intenção de dividir a riqueza.'
        }
    }
}

print("sd \n".format(filmes))
