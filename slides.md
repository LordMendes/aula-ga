---
theme: the-unnamed
background: https://source.unsplash.com/collection/94734566/1920x1080
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Slidev Starter Template
  Presentation slides for developers.

  Learn more at [Sli.dev](https://sli.dev)
drawings:
  persist: false
transition: slide-left
title: Algoritmo Genético
mdc: true
presenter: true
download: true
---

# Algoritmo Genético

Resolvendo problemas baseado na natureza


<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Iniciar <carbon:arrow-right class="inline"/>
  </span>
</div>

<div class="abs-br m-6 flex gap-2">
  <button @click="$slidev.nav.openInEditor()" title="Open in Editor" class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <carbon:edit />
  </button>
  <a href="https://github.com/slidevjs/slidev" target="_blank" alt="GitHub" title="Open in GitHub"
    class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <carbon-logo-github />
  </a>
</div>

<!--
The last comment block of each slide will be treated as slide notes. It will be visible and editable in Presenter Mode along with the slide. [Read more in the docs](https://sli.dev/guide/syntax.html#notes)
-->

---
layout: about-me
helloMsg: Sobre mim!
name: Lucas C. Mendes
imageSrc: >-
  https://github.com/LordMendes/aula-ga/blob/master/assets/about-me.jpeg?raw=true
job: Tech lead
line1: null
line2: null
social1: LinkedIn @lucas-c-mendes
social2: Github @lordmendes
social3: null
---



---
transition: fade-out
---

# Introdução

- Algoritmos evolutivos
- Oque é um GA?
- Os diferentes componentes de um GA
- Como implementar um GA em Python
  ```python
    class ga {
      ...
    }
  ```
- Aplicações de GA em diferentes áreas


---
layout: default
transition: slide-up
---

# Algoritmos evolutivos

A evolução natural é o processo pelo qual as espécies se adaptam ao seu ambiente ao longo do tempo. Ela é baseada nos seguintes princípios:

- Herança: os indivíduos passam seus genes para seus descendentes.
- Mutação: às vezes, os genes sofrem alterações, o que pode levar a novas características.
- Seleção natural: os indivíduos com características mais vantajosas têm mais chances de sobreviver e se reproduzir, passando essas características para seus descendentes.

---
layout: default
transition: slide-up
---

# Besouros numa ilha

Imagine uma ilha com uma população de besouros. Os besouros têm diferentes características, como tamanho, cor e forma. Alguns besouros são melhores adaptados ao ambiente da ilha do que outros.
<div grid="~ cols-6"  class="h-30 w-auto mb-8">
  <img src="https://github.com/LordMendes/aula-ga/blob/master/assets/besouros/besouro-amarelo.png?raw=true" />
  <img src="https://github.com/LordMendes/aula-ga/blob/master/assets/besouros/besouro-azul.png?raw=true" />
  <img src="https://github.com/LordMendes/aula-ga/blob/master/assets/besouros/besouro-preto.png?raw=true" />
  <img src="https://github.com/LordMendes/aula-ga/blob/master/assets/besouros/besouro-rosa.png?raw=true" />
  <img src="https://github.com/LordMendes/aula-ga/blob/master/assets/besouros/besouro-verde.png?raw=true" />
  <img src="https://github.com/LordMendes/aula-ga/blob/master/assets/besouros/besouro-vermelho.png?raw=true" />
</div>
A ilha tem um ambiente hostil, e os besouros precisam encontrar maneiras de sobreviver. Os besouros com características que os tornam mais aptos para sobreviver têm mais chances de se reproduzir e passar essas características para seus descendentes.

Ao longo do tempo, os besouros da ilha se adaptarão ao ambiente. Os besouros com características mais vantajosas serão mais comuns, e os besouros com características menos vantajosas serão menos comuns.


---
layout: section
background: https://miro.medium.com/v2/resize:fit:1400/0*iacUogN9OLOqdPYY
---

# O que são Algoritmos Genéticos
Principais Conceitos

<!--
Introduzir a existencia de conceitos, proximo slide já contém os conceitos
-->

---
layout: default
transition: slide-up
---

# Indivíduo / Individual

## Uma representação de uma possível solução para o problema.

No nosso exemplo as possíveis soluções são representadas pelos diversos besouros e através deles vamos tentar encontrar as carácteristicas que permitem ele sobreviver na ilha.
<div grid="~ cols-2" class="w-auto h-75">
  <img src="https://github.com/LordMendes/aula-ga/blob/master/assets/besouros/besouro-verde.png?raw=true" class="h-75"/>
  <img src="https://github.com/LordMendes/aula-ga/blob/master/assets/besouros/besouro-amarelo.png?raw=true" class="h-75"/>
</div>

---
layout: two-cols
transition: slide-up
---
# Fenótipo
<div class="p-4">

É a representação externa de uma solução, que é a maneira como a solução se comporta no mundo real

No exemplo podemos dizer que o fenótipo é o RGB da cor do besouro
```css
.besouro {
  color: rgb(100,50,255);
}
```
</div>
::right::
<div class="p-4">

# Genótipo
É a representação interna de uma solução, que é composta de genes. Os genes são unidades básicas de informação que podem ser combinadas para formar diferentes soluções.

Para facilitar as operações como a fitness, é melhor encontrar uma forma de converter o fenótipo em algo como um binário

```python
"01100100|00110010|11111111"
    RED  | GREEN  |  BLUE
```
No caso criamos um binário de 30 digitos onde cada 10 representam uma informação do RGB
</div>

---
layout: default
transition: slide-up
---

# População / Population

## Um conjunto de indivíduos que representam possíveis soluções para o problema.

Isso é representado no nosso exemplo por todos os besouros presentes na **POPULAÇÃO**  da ilha
<div class="w-auto flex justify-center h-70">
  <img src="https://github.com/LordMendes/aula-ga/blob/master/assets/conceitos/populacao.png?raw=true" />
</div>

---
layout: default
transition: slide-up
---

# Aptidão / Fitness

## Uma medida de quão bem um indivíduo resolve o problema.

É Literalmente uma "Nota" que é dada para a capacidade de sobrevivência de um indivíduo no ambiente

Geralmente é a parte mais problemática da construção de um GA, pois definir parametros que tornam o indivíduo apto pode ser complexo.

No nosso exemplo vamos usar somente a cor do besouro para definir a capacidade de adaptação dele no ambiente

<div grid="~ cols-6">
  <div class="flex justify-center"><span>0.27</span></div>
  <div class="flex justify-center"><span>0.38</span></div>
  <div class="flex justify-center"><span>0.45</span></div>
  <div class="flex justify-center"><span>0.71</span></div>
  <div class="flex justify-center"><span>0.83</span></div>
  <div class="flex justify-center"><span>0.97</span></div>
  <img src="https://github.com/LordMendes/aula-ga/blob/master/assets/besouros/besouro-amarelo.png?raw=true" />
  <img src="https://github.com/LordMendes/aula-ga/blob/master/assets/besouros/besouro-rosa.png?raw=true" />
  <img src="https://github.com/LordMendes/aula-ga/blob/master/assets/besouros/besouro-vermelho.png?raw=true" />
  <img src="https://github.com/LordMendes/aula-ga/blob/master/assets/besouros/besouro-preto.png?raw=true" />
  <img src="https://github.com/LordMendes/aula-ga/blob/master/assets/besouros/besouro-azul.png?raw=true" />
  <img src="https://github.com/LordMendes/aula-ga/blob/master/assets/besouros/besouro-verde.png?raw=true" />
</div>


---
layout: default
transition: slide-up
---

# Reprodução / Crossover

## O processo de geração de novos indivíduos a partir de indivíduos existentes.

O exemplo ajuda entender o processo de reprodução já que podemos assimilar o cruzamento entre diferentes besouros que irão gerar um novo besouro que herdará algumas caracteristicas dos pais

<div class="flex justify-center h-50">
  <img src="https://github.com/LordMendes/aula-ga/blob/master/assets/conceitos/crossover-copula.jpg?raw=true">
</div>

---
layout: default
transition: slide-up
---

# Reprodução / Crossover

<div>
  <div class="flex flex-row w-auto justify-around">
    <div class="w-66 flex flex-col justify-center ">
      <div class="flex justify-center w-auto">
        <span class="text-[#6232ff] font-black text-xl">Parent 1</span>
      </div>
      <div class="w-auto flex justify-around">
        <span>100</span>
        <span>50</span>
        <span>255</span>
      </div>
      <div>
        <span>01100100 00110010 11111111</span>
      </div>
    </div>
    <div class="w-66 flex flex-col justify-center ">
      <div class="flex justify-center w-auto">
        <span class="text-[#24b28c] font-black text-xl">Parent 2</span>
      </div>
      <div class="w-auto flex justify-around">
        <span>36</span>
        <span>178</span>
        <span>141</span>
      </div>
      <div>
        <span>00100100 10110010 10001101</span>
      </div>
    </div>
  </div>

  <div class="h-10"></div>

  <div class="flex flex-row w-auto justify-around">
    <div class="w-68 flex flex-col justify-center ">
      <div>
        <span>011001000 &nbsp&nbsp 011001011111111</span>
      </div>
    </div>
    <div class="w-68 flex flex-col justify-center ">
      <div>
        <span>001001001 &nbsp&nbsp 011001010001101</span>
      </div>
    </div>
  </div>
  <Arrow x1="200" y1="280" x2="620" y2="375" />
  <Arrow x1="330" y1="280" x2="330" y2="375" />

  <Arrow x1="620" y1="280" x2="200" y2="375" />
  <Arrow x1="750" y1="280" x2="750" y2="375" />

  <div class="h-25"></div>

  <div class="flex flex-row w-auto justify-around">
    <div class="w-68 flex flex-col justify-center ">
      <div>
        <span>001001001 &nbsp&nbsp 011001011111111</span>
      </div>
    </div>
    <div class="w-68 flex flex-col justify-center ">
      <div>
        <span>011001000 &nbsp&nbsp 011001010001101</span>
      </div>
    </div>
  </div>
  <div class="h-10"></div>
  <div class="flex flex-row w-auto justify-around">
    <div class="w-66 flex flex-col justify-center ">
      <div class="flex justify-center w-auto">
        <span class="text-[#24b2ff] font-black text-xl">Child 1</span>
      </div>
      <div class="w-auto flex justify-around">
        <span>36</span>
        <span>178</span>
        <span>255</span>
      </div>
      <div>
        <span>00100100 10110010 11111111</span>
      </div>
    </div>
    <div class="w-66 flex flex-col justify-center ">
      <div class="flex justify-center w-auto">
        <span class="text-[#64328d] font-black text-xl">Child 2</span>
      </div>
      <div class="w-auto flex justify-around">
        <span>100</span>
        <span>50</span>
        <span>141</span>
      </div>
      <div>
        <span>01100100 00110010 10001101</span>
      </div>
    </div>
  </div>
</div>


---
layout: default
transition: slide-up
---

# Reprodução / Crossover

Com base no exemplo anterior conseguimos ver como as alterações vão acontecer conforme o cruzamento de genes acontece, formando uma nova **geração** de **Indivíduos** com novas aptidões.

<div class="flex justify-center">
  <img src="https://github.com/LordMendes/aula-ga/blob/master/assets/conceitos/crossover.png?raw=true" class="h-60">
</div>



---
layout: default
transition: slide-up
---

# Seleção \ Selection

## O processo de escolha dos indivíduos mais aptos para se reproduzirem.

Existem diversos métodos de seleção, vamos falar aqui de 2 dos principais:
- **Torneio (Tournament)**
- **Roleta (Roulette)**
  - Normal
  - "Viciada"
  

---
layout: two-cols
transition: slide-up
---

# Roleta Comum

Nesse método escolhemos n indivíduos de uma maneira completamente aleatória para realizar  o crossover

<div class="w-auto flex justify-center">
  <img src="https://github.com/LordMendes/aula-ga/blob/master/assets/conceitos/roleta.png?raw=true" class="h-60"/>
</div>

::right::
# Roleta Viciada
Aqui a roleta é viciada, ou seja os indivíduos com a maior fitness da população tem mais chances de serem selecionados

<div class="w-auto flex justify-center">
  <img src="https://github.com/LordMendes/aula-ga/blob/master/assets/conceitos/roleta-viciada.png?raw=true" class="h-60"/>
</div>


---
layout: default
transition: slide-up
---

# Torneio (Tournament)

Provavelmente o método mais usado, o torneio se dá da seguinte forma:
- 2 ou mais membros são escolhidos aleatoriamente na população
- É feita uma comparação entre os dois e selecionamos o com a maior fitness para o crossover
  
---
layout: default
transition: slide-up
---
# Mutação / Mutation
## O processo de introdução de alterações aleatórias em indivíduos.

O processo de mutação pode ocorrer em qualquer momento do ciclo evolutivo, ele implica em uma mudança (geralmente) aleatória no gene do indivíduo

### Tipos de mutação

- **Mutação de ponto único**: Uma alteração aleatória é feita em um único gene.
- **Mutação multiponto**: Várias alterações aleatórias são feitas em vários genes.
- **Mutação de substituição**: Um gene é substituído por outro gene aleatório.
- **Mutação de inversão**: Uma seção de genes é invertida.
- **Mutação de transposição**: Dois genes são trocados de lugar.

---
layout: default
transition: slide-up
---
# Mutação / Mutation

<!--
Desenhar como funcionam as mutações
-->

---
layout: two-cols
transition: slide-up
---
# Vantagens
<div class="p-4">

  - Ajuda a garantir que o algoritmo não fique preso em um máximo local.
  - Pode ajudar a explorar novas soluções.
  - Pode ajudar a evitar que o algoritmo encontre um ótimo local local que não seja a solução ótima.

  <div class="w-auto flex justify-center">
    <img src="https://i.stack.imgur.com/XaKx6.png" class="h-40 mt-4"/>
  </div>


<!--
  o exemplo demonstra a variação que uma única mutação pode causar
-->
</div>


::right::
# Desvantagens
<div class="p-4">

  - Pode causar alterações que prejudicam a aptidão dos indivíduos.
  - Pode reduzir a eficiência do algoritmo genético.
  
  <div class="w-auto flex flex-col items-center mt-30">
    <h3 class="mb-4">Ponto único</h3>
    <div><span class="color-red">1</span>1111111 = 255</div>
    <div><span class="color-red">0</span>1111111 = 127</div>
  </div>

</div>

<!--
O exemplo do ponto único representa tanto uma vantagem quanto uma desvantagem
-->

---
layout: default
transition: slide-up
---

# Ciclo Evolutivo

<div class="w-auto flex justify-center ">
  <!-- <img src="https://github.com/LordMendes/aula-ga/blob/master/assets/conceitos/workflow.png?raw=true" class="h-100"/> -->
</div>