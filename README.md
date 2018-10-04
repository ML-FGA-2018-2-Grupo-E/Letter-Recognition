# Letter Recognition

## Resumo

O [`Letter Recognition Data Set`](https://archive.ics.uci.edu/ml/datasets/letter+recognition) é uma base de dados de características de imagens de caracteres, cujo objetivo é tentar identificar corretamente as categorias de letras baseado em 16 atributos inteiros extraídos de imagens de varredura das letras.

| Características do conjunto de dados | Características do atributo | Tarefas associadas | Número de instâncias | Número de atributos  |
|:---:|:---:|:---:|:---:|:---:|
| Multivariada | Inteiro | Classificação | 20000 | 16 |

## Informações do conjunto de dados

O objetivo é identificar cada um de um grande número de exibições de pixels retangulares em preto-e-branco como uma das 26 letras maiúsculas no alfabeto inglês. As imagens dos caracteres foram baseadas em 20 fontes diferentes e cada letra dentro dessas 20 fontes foi aleatoriamente distorcida para produzir um arquivo de 20.000 estímulos únicos. Cada estímulo foi convertido em 16 atributos numéricos primitivos (momentos estatísticos e contagens de borda) que foram escalonados para se ajustarem a um intervalo de valores inteiros de 0 a 15.

## Informações sobre os atributos

#### Variável de interesse (classes)

1. **lettr**: capital letter (26 valores de A a Z)

#### Variáveis independentes (características)

2. **x-box**: horizontal position of box (inteiro) 
3. **y-box**: vertical position of box (inteiro) 
4. **width**: width of box (inteiro) 
5. **high**: height of box (inteiro) 
6. **onpix**: total # on pixels (inteiro) 
7. **x-bar**: mean x of on pixels in box (inteiro) 
8. **y-bar**: mean y of on pixels in box (inteiro) 
9. **x2bar**: mean x variance (inteiro) 
10. **y2bar**: mean y variance (inteiro) 
11. **xybar**: mean x y correlation (inteiro) 
12. **x2ybr**: mean of x * x * y (inteiro) 
13. **xy2br**: mean of x * y * y (inteiro) 
14. **x-ege**: mean edge count left to right (inteiro) 
15. **xegvy**: correlation of x-ege with y (inteiro) 
16. **y-ege**: mean edge count bottom to top (inteiro) 
17. **yegvx**: correlation of y-ege with x (inteiro)
