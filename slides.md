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
  <a href="https://github.com/LordMendes" target="_blank" alt="GitHub" title="Open in GitHub"
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
<!-- genes também são chamados de cromossomos -->
É a representação interna de uma solução, que é composta de genes. Os genes são unidades básicas de informação que podem ser combinadas para formar diferentes soluções.

Para facilitar as operações como a fitness, é melhor encontrar uma forma de converter o fenótipo em algo como um binário

```python
"01100100|00110010|11111111"
    RED  | GREEN  |  BLUE
```
No caso criamos um binário de 24 digitos onde cada 8 representam uma informação do RGB
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
<!-- Mistura da roleta simples com rinha-->

<div class="w-auto flex justify-center">
  <img src="https://github.com/LordMendes/aula-ga/blob/master/assets/conceitos/tournament.png?raw=true" class="h-60"/>
</div>

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

  <div class="w-auto flex justify-center">
    <img src="data:image/png;base64,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" class="h-40 mt-4"/>
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
# Elitismo
- No Elitismo a cada geração selecionamos os top indivíduos para irem para as próximas gerações, isso evita que por um "azar" uma boa solução seja perdida
- Elitismo é uma maneira de aumentar a pressão evolutiva do seu GA, ou seja, forçar a evolução do indivíduo
<div class="w-auto flex flex-col items-center justify-center mt-18">
  <div class="flex items-center">
    <div class="flex justify-center items-center w-50"><span>Top 3</span></div>
    <div class="flex justify-center items-center w-50"><span>Top 1</span></div>
    <div class="flex justify-center items-center w-50"><span>Top 2</span></div>
  </div>
  <div class="flex items-center mt-2">
    <Beetle fill="#34FFA9" class="w-50" showFitnessScore="true"/>
    <Beetle fill="#1DFF6C" class="w-50 pb-20" showFitnessScore="true"/>
    <Beetle fill="#7BFF61" class="w-50 pb-5" showFitnessScore="true"/>
  </div>
</div>
---
layout: default
transition: slide-up
---

# Ciclo Evolutivo

<!-- <div class="w-auto flex justify-center ">
  <img src="https://github.com/LordMendes/aula-ga/blob/master/assets/conceitos/workflow.png?raw=true" />
</div> -->
<iframe style="border:none" width="800" height="350" src="https://whimsical.com/embed/NWa2SXeViWnGZHyQSbtoN5@2Ux7TurymMTECoQFAE16"></iframe>


---
layout: default
transition: slide-up
---

# Ciclo Evolutivo

Juntando todos os conceitos com o nosso exemplo de besouros teríamos algo assim:
## Primeiramente iniciamos uma população com N indivíduos aleatórios
<div grid="~ cols-6 gap-4" class="mt-8">
  <Beetle fill="#E7A8F3" class="w-50"/>
  <Beetle fill="#7BD6A1" class="w-50"/>
  <Beetle fill="#34F2A9" class="w-50"/>
  <Beetle fill="#1D9B6C" class="w-50"/>
  <Beetle fill="#C83E4A" class="w-50"/>
  <Beetle fill="#F97C3D" class="w-50"/>
  
  <Beetle fill="#8EC20B" class="w-50"/>
  <Beetle fill="#A1F0B8" class="w-50"/>
  <Beetle fill="#0B75D9" class="w-50"/>
  <Beetle fill="#9D1F6A" class="w-50"/>
  <Beetle fill="#4F69C3" class="w-50"/>
  <Beetle fill="#5AC8B0" class="w-50"/>
  
  <Beetle fill="#3D9EFA" class="w-50"/>
  <Beetle fill="#DA7F0D" class="w-50"/>
  <Beetle fill="#F55A8E" class="w-50"/>
  <Beetle fill="#6E1B4C" class="w-50"/>
  <Beetle fill="#23A5E9" class="w-50"/>
  <Beetle fill="#B64D2F" class="w-50"/>
  
  <Beetle fill="#FD3C7B" class="w-50"/>
  <Beetle fill="#0F8D92" class="w-50"/>
  <Beetle fill="#57E648" class="w-50"/>
  <Beetle fill="#D14A21" class="w-50"/>
  <Beetle fill="#8316F9" class="w-50"/>
  <Beetle fill="#E292C7" class="w-50"/>  
</div>

---
layout: default
transition: slide-up
---

# Fitness
## Agora o algoritmo avaliará cada individuo da população

<!--
Tendo em vista que RGB é um vetor 3D usamos a relação da distancia euclidiana dividida pela distancia máxima para saber o quão proxima uma cor é da cor alvo
fitness= 1 − (distance/maxDistance)
​


-->

<div grid="~ cols-6 gap-4" class="mt-8">
  <Beetle fill="#E7A8F3" class="w-50" showFitnessScore="true"/>
  <Beetle fill="#7BD6A1" class="w-50" showFitnessScore="true"/>
  <Beetle fill="#34F2A9" class="w-50" showFitnessScore="true"/>
  <Beetle fill="#1D9B6C" class="w-50" showFitnessScore="true"/>
  <Beetle fill="#C83E4A" class="w-50" showFitnessScore="true"/>
  <Beetle fill="#F97C3D" class="w-50" showFitnessScore="true"/>
  
  <Beetle fill="#8EC20B" class="w-50" showFitnessScore="true"/>
  <Beetle fill="#A1F0B8" class="w-50" showFitnessScore="true"/>
  <Beetle fill="#0B75D9" class="w-50" showFitnessScore="true"/>
  <Beetle fill="#9D1F6A" class="w-50" showFitnessScore="true"/>
  <Beetle fill="#4F69C3" class="w-50" showFitnessScore="true"/>
  <Beetle fill="#5AC8B0" class="w-50" showFitnessScore="true"/>
  
  <Beetle fill="#3D9EFA" class="w-50" showFitnessScore="true"/>
  <Beetle fill="#DA7F0D" class="w-50" showFitnessScore="true"/>
  <Beetle fill="#F55A8E" class="w-50" showFitnessScore="true"/>
  <Beetle fill="#6E1B4C" class="w-50" showFitnessScore="true"/>
  <Beetle fill="#23A5E9" class="w-50" showFitnessScore="true"/>
  <Beetle fill="#B64D2F" class="w-50" showFitnessScore="true"/>
  
  <Beetle fill="#FD3C7B" class="w-50" showFitnessScore="true"/>
  <Beetle fill="#0F8D92" class="w-50" showFitnessScore="true"/>
  <Beetle fill="#57E648" class="w-50" showFitnessScore="true"/>
  <Beetle fill="#D14A21" class="w-50" showFitnessScore="true"/>
  <Beetle fill="#8316F9" class="w-50" showFitnessScore="true"/>
  <Beetle fill="#E292C7" class="w-50" showFitnessScore="true"/>  
</div>

---
layout: default
transition: slide-up
---

# Seleção
## Usaremos o método de torneio para o exemplo
<div class="flex flex-col">
  <div class="flex flex-row justify-center items-center">
    <div class="flex flex-row justify-center items-center p-8">
      <Beetle fill="#E292C7" class="w-30" showFitnessScore="true"/>
      VS
      <Beetle fill="#1D9B6C" class="w-30" showFitnessScore="true"/>
      =
      <Beetle fill="#1D9B6C" class="w-30" showFitnessScore="true"/>
    </div>
    <div class="flex flex-row justify-center items-center p-8">
      <Beetle fill="#D14A21" class="w-30" showFitnessScore="true"/>
      VS
      <Beetle fill="#23A5E9" class="w-30" showFitnessScore="true"/>
      =
      <Beetle fill="#23A5E9" class="w-30" showFitnessScore="true"/>
    </div>
  </div>

  <div class="flex flex-row justify-center items-center">
    <div class="flex flex-row justify-center items-center p-8">
      <Beetle fill="#F55A8E" class="w-30" showFitnessScore="true"/>
      VS
      <Beetle fill="#A1F0B8" class="w-30" showFitnessScore="true"/>
      =
      <Beetle fill="#A1F0B8" class="w-30" showFitnessScore="true"/>
    </div>
    <div class="flex flex-row justify-center items-center p-8">
      <Beetle fill="#C83E4A" class="w-30" showFitnessScore="true"/>
      VS
      <Beetle fill="#8316F9" class="w-30" showFitnessScore="true"/>
      =
      <Beetle fill="#C83E4A" class="w-30" showFitnessScore="true"/>
    </div>
  </div>

  <div class="flex flex-row justify-center items-center">
    <div class="flex flex-row justify-center items-center p-8">
      <Beetle fill="#8EC20B" class="w-30" showFitnessScore="true"/>
      VS
      <Beetle fill="#1D9B6C" class="w-30" showFitnessScore="true"/>
      =
      <Beetle fill="#1D9B6C" class="w-30" showFitnessScore="true"/>
    </div>
    <div class="flex flex-row justify-center items-center p-8">
      <Beetle fill="#6E1B4C" class="w-30" showFitnessScore="true"/>
      VS
      <Beetle fill="#DA7F0D" class="w-30" showFitnessScore="true"/>
      =
      <Beetle fill="#6E1B4C" class="w-30" showFitnessScore="true"/>
    </div>
  </div>

</div>

---
layout: default
transition: slide-up
---

# Crossover
<!-- ## Pegamos os indivíduos selecionados e realizamos o crossover -->

<div class="flex flex-col justify-center items-center">
  <div class="flex flex-row justify-center items-center">
    <div class="flex flex-col items-center p-2">
      <Beetle fill="#1D9B6C" class="w-30" showFitnessScore="true"/>
      <span >1D9B6C</span>
      <span class="text-xs"><span class="text-red">0001110</span> <span class="text-blue">11001101101101100</span></span>
    </div>
    <div class="flex flex-col items-center p-2">
      <Beetle fill="#23A5E9" class="w-30" showFitnessScore="true"/>
      <span>23A5E9</span>
      <span class="text-xs"><span class="text-blue">0010001</span> <span class="text-red">11010010111101001</span></span>
    </div>
    <carbon:arrow-right class="inline"/>
    <div class="flex flex-row gap-4">
      <div class="flex flex-row gap-4">
        <div class="flex flex-col justify-center items-center">
          <Beetle fill="#1DA5E9" class="w-30" showFitnessScore="true"/>
          <span>1DA5E9</span>
          <span class="text-red text-xs">000111011010010111101001</span>
        </div>
      </div>
      <div class="flex flex-row gap-4">
        <div class="flex flex-col justify-center items-center">
          <Beetle fill="#239B6C" class="w-30" showFitnessScore="true"/>
          <span>239B6C</span>        
          <span class="text-blue text-xs">001000111001101101101100</span>
        </div>
      </div>
    </div>
  </div>

  <div class="flex flex-row justify-center items-center p-2">
    <div class="flex flex-col items-center p-2">
      <Beetle fill="#A1F0B8" class="w-30" showFitnessScore="true"/>
      <span>A1F0B8</span>
      <span class="text-xs"><span class="text-red">1010000111110000</span> <span class="text-blue">10111000</span></span>
    </div>
    <div class="flex flex-col items-center p-2">
      <Beetle fill="#C83E4A" class="w-30" showFitnessScore="true"/>
      <span>C83E4A</span>
      <span class="text-xs"><span class="text-blue">1100100000111110</span> <span class="text-red">01001010</span></span>
    </div>
    <carbon:arrow-right class="inline"/>
    <div class="flex flex-row gap-4">
      <div class="flex flex-row gap-4">
        <div class="flex flex-col justify-center items-center">
          <Beetle fill="#A1F04A" class="w-30" showFitnessScore="true"/>
          <span>A1F04A</span>
          <span class="text-red text-xs">101000011111000001001010</span>
        </div>
      </div>
      <div class="flex flex-row gap-4">
        <div class="flex flex-col justify-center items-center">
          <Beetle fill="#B8C83E" class="w-30" showFitnessScore="true"/>
          <span>B8C83E</span>        
          <span class="text-blue text-xs">101110001100100000111110</span>
        </div>
      </div>
    </div>
  </div>

  <div class="flex flex-row justify-center items-center p-2">
    <div class="flex flex-col items-center p-2">
      <Beetle fill="#1D9B6C" class="w-30" showFitnessScore="true"/>
      <span>23A5E9</span>
      <span class="text-xs"><span class="text-red">000111011001</span> <span class="text-blue">101101101100</span></span>
    </div>
    <div class="flex flex-col items-center p-2">
      <Beetle fill="#6E1B4C" class="w-30" showFitnessScore="true"/>
      <span>23A5E9</span>
      <span class="text-xs"><span class="text-blue">011011100001</span> <span class="text-red">101101001100</span></span>
    </div>
    <carbon:arrow-right class="inline"/>
    <div class="flex flex-row gap-4">
      <div class="flex flex-row gap-4">
        <div class="flex flex-col justify-center items-center">
          <Beetle fill="#1D9B4C" class="w-30" showFitnessScore="true"/>
          <span>1D9B4C</span>
          <span class="text-red text-xs">000111011001101101001100</span>
        </div>
      </div>
      <div class="flex flex-row gap-4">
        <div class="flex flex-col justify-center items-center">
          <Beetle fill="#B6C6E1" class="w-30" showFitnessScore="true"/>
          <span>B6C6E1</span>        
          <span class="text-blue text-xs">101101101100011011100001</span>
        </div>
      </div>
    </div>
  </div>
</div>


---
layout: default
transition: slide-up
---

# Mutation

- Assim como na vida real, mutações normalmente são raras, como nosso fenótipo é o RGB e nosso genótipo um binário de 24 digitos, uma mutação de ponto único faria pouca diferença, então vou optar por fazer uma mutação em cada um dos componentes do RGB. <br/>
- Cada ponto terá uma chance de 5% de ocorrer.

<div class="flex flex-row justify-center items-center">
  <div class="flex flex-col gap-4 items-center mt-2 justify-center">
    <div class="flex flex-row justify-center items-center h-[70px]">
         1 mutação
    </div>
    <div class="flex flex-row justify-center items-center h-[70px]">
         3 mutações
    </div>
    <div class="flex flex-row justify-center items-center h-[70px]">
         Nenhuma mutação
    </div>
  </div>
  <div class="flex flex-col gap-4 items-start mt-2">
    <div class="flex flex-row justify-center items-center">
      <Beetle fill="#B6C6E1" class="w-30 mb-2" size="70"/>
      <span class="text-red text-xs">10110110</span> <span class="text-green text-xs">11000110</span> <span class="text-blue text-xs mr-8">11100001</span>
    </div>
    <div class="flex flex-row justify-center items-center">
      <Beetle fill="#1D9B4C" class="w-30 mb-2" size="70"/>
      <span class="text-red text-xs">00011101</span> <span class="text-green text-xs">10011011</span> <span class="text-blue text-xs mr-8">01001100</span>
    </div>
    <div class="flex flex-row justify-center items-center">
      <Beetle fill="#B8C83E" class="w-30 mb-2" size="70"/>
      <span class="text-red text-xs">10111000</span> <span class="text-green text-xs">11001000</span> <span class="text-blue text-xs mr-8">00111110</span>
    </div>
  </div>
  <carbon:arrow-right class="inline"/>
    <div class="flex flex-col gap-4 items-start mt-2">
    <div class="flex flex-row justify-center items-center">
      <Beetle fill="#96C6E1" class="w-30 mb-2" size="70"/>
      <!-- 100101101100011011100001 -->
      <span class="text-red text-xs">10<span class="text-white">0</span>10110</span> <span class="text-green text-xs">11000110</span> <span class="text-blue text-xs mr-8">11100001</span>
    </div>
    <div class="flex flex-row justify-center items-center">
      <Beetle fill="#9D93CC" class="w-30 mb-2" size="70"/>
      <!-- 100111011001001111001100 -->
      <span class="text-red text-xs"><span class="text-white">1</span>0011101</span> <span class="text-green text-xs">1001<span class="text-white">0</span>011</span> <span class="text-blue text-xs mr-8"><span class="text-white">1</span>1001100</span>
    </div>
    <div class="flex flex-row justify-center items-center">
      <Beetle fill="#B8C83E" class="w-30 mb-2" size="70"/>
      <span class="text-red text-xs">10111000</span> <span class="text-green text-xs">11001000</span> <span class="text-blue text-xs mr-8">00111110</span>
    </div>
  </div>
</div>


---
layout: default
transition: slide-up
---

# Condição de parada

Na ultima etapa de cada geração checamos se o objetivo estabelecido foi alcançado, ele pode ser:
- Limite de gerações
- Resultado esperado
- Estagnação nos resultados das ultimas N gerações

<!-- Estagnação pode ser algo esperado -->

---
layout: center
transition: slide-up
---
# Como modelar um GA


---
layout: two-cols
transition: slide-up
---

# Principais (pra mim) <!-- principais porque elas darão a direção das demais-->
1. Tenha uma boa definição do problema 
   <!-- no caso do exemplo eu assumi que a ilha teria um bioma verde, mas essa solução não funciona para um um bioma como o deserto -->
2. Consiga uma boa representação para os genes
   <!-- Como representar a solução de uma maneira que o computador entenda -->
3. Consiga uma maneira de sintetizar as informações de forma a pontuar os indivíduos
   <!-- Onde o filho chora e mãe não vê -->
::right::
# Perguntas importantes <!-- Essas podem (e vão)  ser ajustadas durante o processo -->
1. Qual método de seleção usar?
2. Qual mutação é a ideal pro meu problema? Eu preciso de mutação? Qual a probabilidade da mutação acontecer?
3. Qual meu critério de parada?
   1. Vou rodar até obter uma solução?
   2. vou rodar por 30 gerações?
4. Qual será o tamanho da minha população?


---
layout: default
transition: slide-up
---

# Pergunta final

## - Rodei, meu resultado está bom?
## - Como posso ajustar?

Um GA assim como todo código não vai rodar de forma esperada desde o começo.
<div class="flex justify-center items-center">
  <img src="https://miro.medium.com/v2/resize:fit:1400/1*bp4cwdGXkfE2RzZclJ6VRw.jpeg" class="h-60"/>
</div>


---
layout: section
transition: slide-up
background: assets/artigo/capa.png
---
# Uso real
ROI Extraction in Thermographic Breast Images
Using Genetic Algorithms
<br/><i class="text-sm">L. C. Mendes, E. O. Rodrigues, S. C. Izidoro, A. Conci and P. Liatsis</i>


---
layout: default
transition: slide-up
---
# Definição do problema
## Segmentar a região de interesse em termografias de mama
<div class="p-8 flex justify-center items-center ">
  <img src="https://github.com/LordMendes/aula-ga/blob/master/assets/artigo/roi.png?raw=true" class="max-h-80"/>
</div>

---
layout: two-cols
transition: slide-up
---
# Definição do Indivíduo

## Fenótipo

- Uma cardioide representada por:
  - Coordenada X
  - Coordenada Y
  - Tamanho

::right::
<div class="mb-22" ></div>

## Genótipo

- O cromossomo seria um binário (gray code) de 10 dígitos para cada uma das representações
```python
class Individual:
  cardioid = Cardioid()

class Cardioid:
  x_coordinate = Coordinate()
  y_coordinate = Coordinate()
  size = Coordinate()

class Coordinate:
  decimal
  binary
  gray_code
```

<!--
10 digitos era o menor valor para representar a maior dimensão da imagem
-->


---
layout: default
transition: slide-up
---

# Fitness

1. Tendo em vista que a imagem é monocromática (somente 1 canal, o RGB por exemplo são 3)
Ao analisar uma amostragem das termografias eu notei que os pixels brancos (áreas com mais calor) circundavam a região de interesse
e também que o fundo sempre era composto de pixels pretos

<div class="p-8 flex justify-center items-center ">
  <img src="https://github.com/LordMendes/aula-ga/blob/master/assets/artigo/roi.png?raw=true" class="max-h-40"/>
</div>

1. Com base nessa observação optei por usar o valor da cor dos pixels dentro da cardioide como uma forma de pontuar o individuo


---
layout: default
transition: slide-up
---

# Fitness

3. Com isso em mente defini 4 ranges dentro do canal de cor e penalizar ou gratificar o individuo de acordo com isso
```python
  color_interval = [0, 45, 140, 200, 256]
  color_weights = [-25, 5, 25, -27.5]
```

4. No fim a fitness é uma média ponderada da quantidade dos pixels dentro de cada range
   
```python
def fitness():
  ...
  # Calculate the total color score.
  total_color_score = sum(
      color_weights[i] * pixel_volume[i] for i in range(4))

  # Calculate the fitness score.
  fitness_score = total_color_score / abs(total_weight)

  self.score = fitness_score
  return fitness_score
```

---
layout: section
transition: slide-up
---

# Código do artigo
https://github.com/LordMendes/ROI-Extraction-in-Thermographic-Breast-Images-Using-Genetic-Algorithms


---
layout: section
---

# Execício

Uma empresa de manufatura está tentando otimizar sua produção para maximizar a eficiência e minimizar os custos. A empresa produz três tipos de produtos, A, B e C, e deseja determinar a melhor alocação de recursos para maximizar o lucro total. Cada produto requer diferentes recursos, tempo e mão de obra para ser produzido. A empresa tem um orçamento fixo para cada período de produção e quer encontrar a alocação ideal de recursos que maximiza o lucro total.

Os recursos disponíveis são limitados e incluem matérias-primas, horas de trabalho e espaço de armazenamento. Cada produto tem uma demanda de mercado específica e uma margem de lucro associada. Além disso, existem restrições de tempo, espaço e recursos que devem ser consideradas durante o processo de produção. A empresa deseja encontrar a melhor combinação de quantidades de produtos A, B e C a serem produzidos, levando em consideração as restrições mencionadas.

---
layout: section
---
## Características

| Característica            | Produto A | Produto B | Produto C |
|---------------------------|-----------|-----------|-----------|
| Tempo de produção (horas) | 1         | 2         | 3         |
| Valor (R$)                | 100       | 200       | 300       |
| Espaço ocupado (m²)       | 1         | 2         | 3         |

## Restrições

- Orçamento: R$ 10.000
- Tempo de trabalho: 100 horas
- Espaço de armazenamento: 100 m²

---
layout: center
---
# Valeu!
# Obrigado!