# ![https://www.fiap.com.br/](https://img.shields.io/badge/FIAP-red.svg?longCache=true&style=for-the-badge) MBA - Artifical Intelligence & Machine Learning

#### Cintia Akie Nakano . RM 333603 // Lennon V. Alves Dias . RM 334415 // Mateus Aguiar Florentino . RM 334444

<h1 align="center">
    Estudo prático de um banco de dados em grafos
</h1>

## 👩‍🏫 Introdução

Uma empresa multinacional de tecnologia decide realizar um evento em escala mundial, com objetivo de apresentar e vender o seu novo portfólio, com diversas palestras, mesas redondas e stands com as maiores referências de especialistas no mercado. Além disso, o evento também busca conectar pessoas dessa área, visto que existem ramificações bem específicas tais como: exatas, biológicas e humanas.

Sendo assim, todo participante que realiza a inscrição no evento , ele deverá incluiro seu Linkedin na ficha cadastral. A partir dessa página, é possível extrair algumas informações tais como: emprego atual e anteriores, áreas de conhecimento, área de atuação, local de estudo, etc. Com os dados, temos uma rede de contatos que pode ser estruturada utilizando a última metodologia vista em sala de aula na disciplina de arquitetura de dados: banco de dados em grafos.

O termo “grafo” vem do uso da palavra na matemática. É usada para descrever uma coleção de nós, ou vertentes, que contém informações  e relações classificadas entre os nós. O banco de dados de grafos é pouco conhecido e difundido entre as empresas hoje em dia, e é utilizado para trabalhar com dados altamente interconectados, em que eles podem ser descritos como bancos mais “relacionais” do que uma típico banco de dados relacional. Isso por que as bases de grafos brilham quando o objetivo é capturar relações complexas em redes de informações. Portanto, no caso descrito acima, em que haja a necessidade de lidar com milhões de relaçãoes – amigos de amigos – essas consultas se enciaxam muito bem.


## 👫 Relações do banco de dados

Os bancos de dados de grafos funcionam melhor quando os dados com os quais se está trabalhando são altamente conectados e devem ser representados a partir de como se conectam ou se correlacionam com outros dados, normalmente por meio de relações ‘muitos para muitos’.
Associando a descrição de uma rede utilizando banco de dados de grafos, imagine que as pessoas na rede seriam os nós, os atributos de cada pessoa (como nome, idade, estado que reside, universidade que estudou, área de conhecimento, etc) seriam as propriedades, e as linhas conectando as pessoas com classificações como director, gerente, supervisor, analista indicariam as suas relações.

Como os nós relacionados são fisicamente ligados à base de dados, acessar essas relações é algo tão imediato quanto acessar os dados em si, e em vez de calcular a relação, como as bases de dados relacionais funcionam, as bases de dados de grafos simplesmente fazem a relação instantaneamente a partir do armazenamento. A quantidade de trabalho necessária para construir e exibir as visualizações de dados encontradas em redes sociais é menor, como determinar se você conhece ou não uma determinada pessoa por conta da proximidade que ela tem com outros amigos seus na plataforma. Outra aplicação para eles é encontrar padrões de conexão em dados que seriam difíceis de visualizar por meio de outras representações de dados.

De forma geral, os bancos de dados de grafos são uma combinação natural para aplicações que gerenciam relações ou interdependências entre entidades. Você normalmente vai encontrar bancos de grafos por trás de sistemas de recomendações, sistemas de gerenciamento de conteúdos e assets, sistemas de gerenciamento de acesso e identidade, etc.