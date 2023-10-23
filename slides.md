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
title: Welcome to Slidev
mdc: true
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
imageSrc: assets/about-me.jpeg
job: Tech lead
line1: 
line2: 
social1: LinkedIn @lucas-c-mendes
social2: Github @lordmendes
social3: 
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
<img src="https://drive.google.com/file/d/1MnOhuIRW8ZfS11WXhg9u_B7ItrXK4Bam/view?usp=sharing">

---
layout: section
background: https://miro.medium.com/v2/resize:fit:1400/0*iacUogN9OLOqdPYY
---

# O que são Algoritmos Genéticos

---
layout: default
transition: slide-up
---

# teste