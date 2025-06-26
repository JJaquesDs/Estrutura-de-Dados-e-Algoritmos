# Explicação para inverter uma String em Python usando dois ponteiros #

 Obs.: Vale lembrar que isso fica diferente em outras linguagens porque Python é ruim para lidar com Strings e elas são imultáveis nessa linguagem

Primeiramente deve inicializar os ponteiros no inicio da string. Aqui inicalizado como:

````Python
direita, esquerda = 0, 0
````

Inicie um loop que vai até o final da string (len de str) para trabalhar dentro disso
Trabalhando dentro do loop, como queremos que as palavras sejam invertidas, faça o ponteiro "direita" parar sempre que encontrar um espaço vazio:

````Python
direita = 0

if str[int: direita] != ' ':
    pass
````

Dentro dessa condição, incremente o ponteiro da esquerda para começar a andar sobre a String
Quando o ponteiro direita bater no caractere vazio e esquerda andar sobre os caracteres, faça um else condição para a variável de saída receber a primeira palavra invertida
"saida" receberá a string desde o ponteiro percorrido da esquerda pra direita, voce deve incrementar o ponteiro da direita com + 1, porque por padrao o Python corta o index em -1
para inverter uma string em python, vc ultiliza o seguinte código:

````Python

p = "Hello World"
print(f"{p[:: -1]}")

````

Depois incremente o ponteiro direito uma casa para ele ir para a próxima palavra
E coloque o ponteiro da esquerda para iniciar novamente junto com ele

Note que quando acabar o while loop, voce precisará repetir o codigo para concatenar a ultima palavra
Printe ou retorne a palavra, mas faça isso a partir da posição 1 para ele nao começar do espaço em branco invertido