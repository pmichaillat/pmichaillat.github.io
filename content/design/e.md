---
title: "LaTeX Commands to Write Math" 
date: 2024-06-26
url: /e/
aliases: 
    - /d3/
author: "Pascal Michaillat"
description: "These commands simplify writing mathematical expressions with LaTeX while automatically respecting the rules of mathematical typography." 
summary: "This collection of commands simplifies writing mathematical expressions with LaTeX while automatically respecting the rules of mathematical typography." 
cover:
    image: "/e.png"
    alt: "Mathematical expressions produced with commands"
editPost:
    URL: "https://github.com/pmichaillat/latex-math"
    Text: "GitHub repository"
showToc: true
disableAnchoredHeadings: false

---

This collection of commands simplifies writing mathematical expressions with [LaTeX](https://www.latex-project.org) while automatically respecting the rules of mathematical typography. The commands were developed to write math in economics, but they might also be helpful to write math in other fields. 

---

## View

+ [LaTeX commands to write math](https://github.com/pmichaillat/latex-math)

---

## Features

The commands introduce the following functionalities:

+ Easily insert brackets (parentheses, absolute values, etc.) that scale automatically
+ Easily write functions and operators (exponential, log, expectation, probability, min, max, etc.) with brackets that scale automatically
+ Easily write partial and total derivatives and elasticities
+ Easily type statistical relations (iid variables, various limits)
+ Easily insert accents that scale automatically
+ Easily type blackboard-bold letters
+ Easily type Greek letters
+ Easily type uppercase calligraphic letters

---

## Brackets

The commands below produce brackets that scale automatically.

|        Bracket        |   Command   |             Output             |
| :-------------------- | :---------: | :----------------------------: |
| Parentheses           |   `\bp{x}`  |       $\left( x\right)$        |
| Square brackets       |   `\bs{x}`  |        $\left[x\right]$        |
| Curly brackets        |   `\bc{x}`  | $\left\lbrace x\right\rbrace$  |
| Angle brackets        |   `\ba{x}`  |       $\left< x\right>$        |
| Absolute value        |  `\abs{x}`  |  $\left\lvert x \right\rvert$  |
| Norm                  |  `\norm{x}` |  $\left\lVert x \right\rVert$  |
| Floor                 | `\floor{x}` | $\left\lfloor  x\right\rfloor$ |
| Ceiling               |  `\ceil{x}` |  $\left\lceil  x\right\rceil$  |
| Function argument[^1] |  `f\of{x}`  |             $f(x)$             |


[^1]: Spacing between the function `f` and the argument `(x)` is  appropriate. `f\bp{x}` gives $f\left( x\right)$, which introduces too much space between the function `f` and the argument `(x)`.

## Functions and operators

The commands below produce functions and operators with parentheses that scale automatically. All the commands work with and without arguments, and many also have an option to add a subscript. 

| Function or operator |     Command     |            Output            |
| :------------------- | :-------------: | :--------------------------: |
| Logarithm            |      `\ln`      |            $\ln$             |
|                      |     `\ln{x}`    |           $\ln(x)$           |
| Exponential          |      `\exp`     |            $\exp$            |
|                      |    `\exp{x}`    |          $\exp(x)$           |
| Indicator            |      `\ind`     |         $\mathbb{1}$         |
|                      |    `\ind{X}`    |       $\mathbb{1}(X)$        |
| Trace                |      `\tr`      |     $\operatorname{tr}$      |
|                      |     `\tr{M}`    |    $\operatorname{tr}(M)$    |
| Probability          |       `\P`      |         $\mathbb{P}$         |
|                      |     `\P[t]`     |        $\mathbb{P}_t$        |
|                      |     `\P{X}`     |       $\mathbb{P}(X)$        |
|                      |    `\P[t]{X}`   |      $\mathbb{P}_t(X)$       |
| Expectation          |       `\E`      |         $\mathbb{E}$         |
|                      |     `\E[t]`     |        $\mathbb{E}_t$        |
|                      |     `\E{X}`     |       $\mathbb{E}(X)$        |
|                      |    `\E[t]{X}`   |      $\mathbb{E}_t(X)$       |
| Variance             |      `\var`     |     $\operatorname{var}$     |
|                      |    `\var{X}`    |   $\operatorname{var}(X)$    |
|                      |   `\var[t]{X}`  |  $\operatorname{var}_t(X)$   |
| Standard deviation   |      `\sd`      |     $\operatorname{sd}$      |
|                      |     `\sd{X}`    |    $\operatorname{sd}(X)$    |
|                      |   `\sd[t]{X}`   |   $\operatorname{sd}_t(X)$   |
| Standard error       |      `\se`      |     $\operatorname{se}$      |
|                      |     `\se{X}`    |    $\operatorname{se}(X)$    |
|                      |   `\se[t]{X}`   |   $\operatorname{se}_t(X)$   |
| Covariance           |      `\cov`     |     $\operatorname{cov}$     |
|                      |   `\cov{X,Y}`   |  $\operatorname{cov}(X,Y)$   |
|                      |  `\cov[t]{X,Y}` | $\operatorname{cov}_t(X,Y)$  |
| Correlation          |     `\corr`     |    $\operatorname{corr}$     |
|                      |   `\corr{X,Y}`  |  $\operatorname{corr}(X,Y)$  |
|                      | `\corr[t]{X,Y}` | $\operatorname{corr}_t(X,Y)$ |
| Maximum              |      `\max`     |            $\max$            |
|                      |    `\max{x,y}`    |          $\max(x,y)$           |
|                      |  `\max[n]{y_n}` |        $\max_n(y_n)$         |
| Argmax               |    `\argmax`    |   $\operatorname{argmax}$    |
| Minimum              |      `\min`     |            $\min$            |
|                      |    `\min{x,y}`    |          $\min(x,y)$           |
|                      |  `\min[n]{y_n}` |        $\min_n(y_n)$         |
| Argmin               |    `\argmin`    |   $\operatorname{argmin}$    |
| Supremum             |      `\sup`     |            $\sup$            |
|                      |    `\sup{S}`    |          $\sup(S)$           |
|                      |  `\sup[n]{y_n}` |        $\sup_n(y_n)$         |
| Infimum              |      `\inf`     |            $\inf$            |
|                      |    `\inf{S}`    |          $\inf(S)$           |
|                      |  `\inf[n]{y_n}` |        $\inf_n(y_n)$         |

## Derivatives

The commands below produce various derivatives. Some of commands produce derivatives for displays while others produce derivatives for text. Some of the commands have an option to indicate the order of the derivative.

|      Derivative     |     Command     |                            Output                            |
| :------------------ | :-------------: | :----------------------------------------------------------: |
| Ordinary derivative |   `\od{y}{x}`   |                      $\frac{d y}{d x}$                       |
|                     |  `\od[n]{y}{x}` |                    $\frac{d^n y}{d x^n}$                     |
|                     |   `\odx{y}{x}`  |                          $d y/d x$                           |
|                     | `\odx[n]{y}{x}` |                        $d^n y/d x^n$                         |
| Partial derivative  |   `\pd{y}{x}`   |               $\frac{\partial y}{\partial x}$                |
|                     |  `\pd[n]{y}{x}` |             $\frac{\partial^n y}{\partial x^n}$              |
|                     |   `\pdx{y}{x}`  |                   $\partial y/\partial x$                    |
|                     | `\pdx[n]{y}{x}` |                 $\partial^n y/\partial x^n$                  |
|                     |  `\pd{y}{x}{z}` |     $\left.\frac{\partial y}{\partial x}\right\vert_{z}$     |
|                     | `\pdx{y}{x}{z}` |         $\left.\partial y/\partial x\right\vert_{z}$         |
| Ordinary elasticity |   `\oe{y}{x}`   |                   $\frac{d\ln y}{d\ln x}$                    |
|                     |   `\oex{y}{x}`  |                      $d\ln(y)/d\ln(x)$                       |
| Partial elasticity  |   `\pe{y}{x}`   |           $\frac{\partial\ln(y)}{\partial\ln(x)}$            |
|                     |   `\pex{y}{x}`  |               $\partial\ln(y)/\partial\ln(x)$                |
|                     |  `\pe{y}{x}{z}` | $\left.\frac{\partial\ln(y)}{\partial\ln(x)}\right\vert_{z}$ |
|                     | `\pex{y}{x}{z}` |     $\left.\partial\ln(y)/\partial\ln(x)\right\vert_{z}$     |


## Statistical relations

The commands below are shortcuts to produce statistical relations.

|                      Relation                     | Command |         Output        |
| :------------------------------------------------ | :------ | :-------------------: |
| Independent and identically distributed variables | `\iid`  | $\overset{iid}{\sim}$ |
| Almost sure convergence                           | `\asto` |  $\overset{as}{\to}$  |
| Convergence in probability                        | `\pto`  |   $\overset{p}{\to}$  |
| Convergence in distribution                       | `\dto`  |   $\overset{d}{\to}$  |
| Essential infimum and supremum                    | `\ees`  |  $\operatorname{ees}$ |


## Accents

The commands below are shortcuts to produce accents that scale automatically.

|   Accent  | Command  |        Output        |
| :-------- | :------: | :------------------: |
| Overline  | `\ol{x}` |    $\overline{x}$    |
| Overarrow | `\oa{x}` | $\overrightarrow{x}$ |
| Underline | `\ul{x}` |   $\underline{x}$    |
| Hat       | `\wh{x}` |    $\widehat{x}$     |
| Tilde     | `\wt{x}` |   $\widetilde{x}$    |


## Blackboard-bold letters

The commands below are shortcuts to produce blackboard-bold letters.

| Letter | Command |    Output    |
| :----- | :-----: | :----------: |
| R      |   `\R`  | $\mathbb{R}$ |
| N      |   `\N`  | $\mathbb{N}$ |
| Z      |   `\Z`  | $\mathbb{Z}$ |
| Q      |   `\Q`  | $\mathbb{Q}$ |
| C      |   `\C`  | $\mathbb{C}$ |

## Greek letters

The commands below are shortcuts to produce lowercase Greek letters.

| Lowercase letter | Command |     Output    |
| :--------------- | :-----: | :-----------: |
| alpha            |   `\a`  |    $\alpha$   |
| beta             |   `\b`  |    $\beta$    |
| chi              |   `\c`  |     $\chi$    |
| delta            |   `\d`  |    $\delta$   |
| epsilon          |   `\e`  |   $\epsilon$  |
| varepsilon       |  `\ve`  | $\varepsilon$ |
| phi              |   `\f`  |     $\phi$    |
| varphi           |  `\vf`  |   $\varphi$   |
| gamma            |   `\g`  |    $\gamma$   |
| eta              |   `\h`  |     $\eta$    |
| iota             |   `\i`  |    $\iota$    |
| kappa            |   `\k`  |    $\kappa$   |
| lambda           |   `\l`  |   $\lambda$   |
| mu               |   `\m`  |     $\mu$     |
| nu               |   `\n`  |     $\nu$     |
| omega            |   `\o`  |    $\omega$   |
| varpi            |  `\vp`  |    $\varpi$   |
| psi              |   `\p`  |     $\psi$    |
| rho              |   `\r`  |     $\rho$    |
| sigma            |   `\s`  |    $\sigma$   |
| theta            |   `\t`  |    $\theta$   |
| vartheta         |  `\vt`  |  $\vartheta$  |
| upsilon          |   `\u`  |   $\upsilon$  |
| xi               |   `\x`  |     $\xi$     |
| zeta             |   `\z`  |    $\zeta$    |

And the commands below are shortcuts to produce uppercase Greek letters.

| Uppercase letter | Command |     Output    |
| :--------------- | :-----: | :-----------: |
| delta            |   `\D`  |    $\Delta$   |
| phi              |   `\F`  |     $\Phi$    |
| gamma            |   `\G`  |    $\Gamma$   |
| lambda           |   `\L`  |   $\Lambda$   |
| omega            |   `\O`  |    $\Omega$   |
| sigma            |   `\S`  |    $\Sigma$   |
| theta            |   `\T`  |    $\Theta$   |
| upsilon          |   `\U`  |   $\Upsilon$  |
| xi               |   `\X`  |     $\Xi$     |


## Calligraphic letters

The commands below are shortcuts to produce calligraphic letters.

| Letter | Command |     Output    |
| :----- | :-----: | :-----------: |
| A      |  `\Ac`  | $\mathcal{A}$ |
| B      |  `\Bc`  | $\mathcal{B}$ |
| C      |  `\Cc`  | $\mathcal{C}$ |
| D      |  `\Dc`  | $\mathcal{D}$ |
| E      |  `\Ec`  | $\mathcal{E}$ |
| F      |  `\Fc`  | $\mathcal{F}$ |
| G      |  `\Gc`  | $\mathcal{G}$ |
| H      |  `\Hc`  | $\mathcal{H}$ |
| I      |  `\Ic`  | $\mathcal{I}$ |
| J      |  `\Jc`  | $\mathcal{J}$ |
| K      |  `\Kc`  | $\mathcal{K}$ |
| L      |  `\Lc`  | $\mathcal{L}$ |
| M      |  `\Mc`  | $\mathcal{M}$ |
| N      |  `\Nc`  | $\mathcal{N}$ |
| O      |  `\Oc`  | $\mathcal{O}$ |
| P      |  `\Pc`  | $\mathcal{P}$ |
| Q      |  `\Qc`  | $\mathcal{Q}$ |
| R      |  `\Rc`  | $\mathcal{R}$ |
| S      |  `\Sc`  | $\mathcal{S}$ |
| T      |  `\Tc`  | $\mathcal{T}$ |
| U      |  `\Uc`  | $\mathcal{U}$ |
| V      |  `\Vc`  | $\mathcal{V}$ |
| W      |  `\Wc`  | $\mathcal{W}$ |
| X      |  `\Xc`  | $\mathcal{X}$ |
| Y      |  `\Yc`  | $\mathcal{Y}$ |
| Z      |  `\Zc`  | $\mathcal{Z}$ |

## Complex numbers

The commands below designate parts of complex numbers.

|      Part      | Command  |         Output         |
| :------------- | :------: | :--------------------: |
| Real part      | `\Re(z)` | $\operatorname{Re}(z)$ |
| Imaginary part | `\Im(z)` | $\operatorname{Im}(z)$ |


## Existing LaTeX commands

Existing LaTeX commands continue to work as usual, with the exception of a few text commands that do not produce their usual output. These modified text commands are `\oe`, `\o`, and `\P`. These commands used to insert text symbols that are rarely used in scientific writing ($\text{\oe}$, $\text{\o}$, and $\text{\P}$). The commands now insert common mathematical symbols, so hopefully the modification is not problematic.

---

## Code snippets

The LaTeX commands are collected in a [LaTeX style file](https://github.com/pmichaillat/latex-math/blob/main/math.sty). This section shows how some of the most commonly used commands are defined. Some of the definitions require the `xparse` package.

For instance, the commands for parentheses are defined as follows:

```LaTeX
% Regular parentheses
\newcommand{\bp}[1]{\left( #1 \right)} 

% Parentheses for function arguments
\newcommand{\of}[1]{{\left( #1 \right)}}
```

The command for maximum and minimum are defined as follows:

```LaTeX
\usepackage{xparse}

% Maximum
\let\oldmax\max
\RenewDocumentCommand{\max}{o g}{%
\IfNoValueTF{#2}{\oldmax\IfValueT{#1}{_{#1}}}%
{\,{\oldmax\IfValueT{#1}{_{#1}}}\of{#2}}}

% Minimum
\let\oldmin\min
\RenewDocumentCommand{\min}{o g}{%
\IfNoValueTF{#2}{\oldmin\IfValueT{#1}{_{#1}}}%
{\,{\oldmin\IfValueT{#1}{_{#1}}}\of{#2}}}
```

Another set of commonly used commands are expected value and probability, which are coded as follows:

```LaTeX
\usepackage{xparse}

% Expectation
\NewDocumentCommand{\E}{o g}{%
\IfNoValueTF{#2}{\operatorname{\mathbb{E}}\IfValueT{#1}{_{#1}}}%
{\,{\operatorname{\mathbb{E}}\IfValueT{#1}{_{#1}}}\of{#2}}}

% Probability
\RenewDocumentCommand{\P}{o g}{%
\IfNoValueTF{#2}{\operatorname{\mathbb{P}}\IfValueT{#1}{_{#1}}}%
{\,{\operatorname{\mathbb{P}}\IfValueT{#1}{_{#1}}}\of{#2}}}
```

The commands for variance, covariance, correlation, and standard deviation are all coded in a similar way:

```LaTeX
\usepackage{xparse}

% Variance
\NewDocumentCommand{\var}{o g}{%
\IfNoValueTF{#2}{\operatorname{var}\IfValueT{#1}{_{#1}}}%
{\,{\operatorname{var}\IfValueT{#1}{_{#1}}}\of{#2}}}

% Covariance
\NewDocumentCommand{\cov}{o g}{%
\IfNoValueTF{#2}{\operatorname{cov}\IfValueT{#1}{_{#1}}}%
{\,{\operatorname{cov}\IfValueT{#1}{_{#1}}}\of{#2}}}

% Correlation
\NewDocumentCommand{\corr}{o g}{%
\IfNoValueTF{#2}{\operatorname{corr}\IfValueT{#1}{_{#1}}}%
{\,{\operatorname{corr}\IfValueT{#1}{_{#1}}}\of{#2}}}

% Standard deviation
\NewDocumentCommand{\sd}{o g}{%
\IfNoValueTF{#2}{\operatorname{sd}\IfValueT{#1}{_{#1}}}%
{\,{\operatorname{sd}\IfValueT{#1}{_{#1}}}\of{#2}}}
```

The argmin and argmax functions are easy to define:

```LaTeX
\DeclareMathOperator*{\argmax}{argmax}
\DeclareMathOperator*{\argmin}{argmin}
```

The commands for almost sure convergence, convergence in probability, and convergence in distribution are coded as follows:

```LaTeX
% Almost sure convergence
\newcommand{\asto}{\overset{as}{\to}}

% Convergence in probability
\newcommand{\pto}{\overset{p}{\to}}

% Convergence in distribution
\newcommand{\dto}{\overset{d}{\to}}
```

Finally, the exponential and logarithm functions are defined as follows:

```LaTeX
\usepackage{xparse}

% Logarithm
\let\oldln\ln
\RenewDocumentCommand{\ln}{g}{%
\IfNoValueTF{#1}{\oldln}%
{\,{\oldln}\of{#1}}}

% Exponential
\let\oldexp\exp
\RenewDocumentCommand{\exp}{g}{%
\IfNoValueTF{#1}{\oldexp}%
{\,{\oldexp}\of{#1}}}
```
