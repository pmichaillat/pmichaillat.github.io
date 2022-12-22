---
title: "Minimalist LaTeX Template for Academic CVs" 
date: 2025-05-11
url: /f/
author: "Pascal Michaillat"
description: "This template produces an academic CV with LaTeX. The CV follows typographical best practices and has a minimalist design."
summary: "This template produces an academic CV with LaTeX. The CV follows typographical best practices and has a minimalist design." 
cover:
    image: "/f.png"
    alt: "CV produced with template"
editPost:
    URL: "https://github.com/pmichaillat/latex-cv"
    Text: "GitHub repository"
showToc: true
disableAnchoredHeadings: false
---

The template produces an academic CV with [LaTeX](https://www.latex-project.org). The CV adheres to typographical best practices and has a minimalist design. It is well suited for researchers at all levels, including students, postdocs, faculty members, and professional scientists. The design emphasizes structural clarity and visual simplicity.

---

## View

+ [LaTeX template for academic CVs](https://github.com/pmichaillat/latex-cv)
+ [CV produced by the template](/f.pdf)

---

## Features

+ The font for text and numbers is Source Serif Pro.
+ The CV uses only gray and black to reduce distraction and print flawlessly.
+ Margins, spacing, and font size are set for comfortable reading.
+ Headings and lists are designed so the CV is well organized and easy to skim.

---

## Text font

The font determines the appearance and readability of the entire CV, so choosing a good font is key. Following [Butterick's advice](https://practicaltypography.com/free-fonts.html), the template uses [Source Serif Pro](https://mirror.las.iastate.edu/tex-archive/fonts/sourceserifpro/doc/sourceserifpro.pdf) for the text. 

Source Serif Pro is a serif font. It is not part of typical CV templates so it has a fresh feel. And since it was designed in the last decade, it also has a modern feel.

The Source Pro family also includes a nice monospaced font: [Source Code Pro](https://mirrors.rit.edu/CTAN/fonts/sourcecodepro/doc/sourcecodepro.pdf). The template uses Source Code Pro as monospaced font for URLs.

---

## Math fonts and symbols

If required anywhere in the CV—in article or course titles—mathematical expressions are typeset just as in the [later-paper](https://github.com/pmichaillat/latex-paper) template. Here is a summary of [the math fonts used in the CV](https://pascalmichaillat.org/a/#math-fonts):

+ Roman letters - [Source Serif Pro font](https://ctan.mirrors.hoobly.com/macros/latex/contrib/mathastext/mathastext.pdf)
+ Greek letters - [Euler font](https://ctan.math.utah.edu/ctan/tex-archive/fonts/eulervm/doc/latex/eulervm/eulervm.pdf)
+ Calligraphic letters - [Euler font](https://ctan.math.utah.edu/ctan/tex-archive/fonts/eulervm/doc/latex/eulervm/eulervm.pdf)
+ Blackboard-bold font - [Fourier font](https://mirror.mwt.me/ctan/macros/latex/contrib/mathalpha/doc/mathalpha-doc.pdf) 
+ Symbols - [MnSymbol font](https://ftp.yz.yamagata-u.ac.jp/pub/CTAN/fonts/mnsymbol/MnSymbol.pdf) 

---

## Font size

The font size is 10pt, in line with [Butterick's recommendation](https://practicaltypography.com/point-size.html). It is easily readable but not too big, keeping the CV's appearance compact.

---

## Line spacing

Baseline spacing between lines is only 110% of the point size, but spacing is increased between the bullet points, so reading remains comfortable. Overall the line spacing prevents the text from appearing too cramped or too spread out.

---

## Text margins

The left and right margins are 1.2 inch. With such margins, plus the space taken by the bullet points, there are at most 90 characters per line, just as [Butterick recommends](https://practicaltypography.com/line-length.html) to ensure comfortable reading. 

The top margin is 0.9 inch, which is about standard. The bottom margin is 1.1 inch so the text [appears centered in the page](https://practicaltypography.com/page-margins.html). 

---

## Color scheme

Colors are distracting, and many colors are hard to read when they are printed in black and white. To reduce distraction and have a CV that prints well, the template only uses black for the main text, and gray for surrounding elements (headings, bullet points, footer).

---

## Title

The CV's title is just your name. The title is produced by the command `\name{}`. The title is typeset in small caps with a 25pt font size. 

--- 

## Contact information

The contact information is kept to a minimum: email address and website URL. The contact information is placed in the footer, at the bottom of each page. In practice phone numbers and mailing addresses are not used anymore, so it seems unnecessary to include them, especially in such a prominent position as the top of the CV. This information can be added to your website instead.

The footer also includes the date when the CV was last updated.

The footer font size is 8pt, just like footnotes would be, and the font color is gray. As a result, the footer is not too obtrusive.

The commands to populate the footer are `\grayfoot{C}{}`, `\grayfoot{L}{}`, and `\grayfoot{R}{}` in the document preamble.

---

## Block headings

The CV is organized in blocks containing key information. The blocks are introduced by order of importance:

+ Employment
+ Education
+ Articles published
+ Courses taught
+ Service
+ Awards

The block headings follow [Butterick's advice](https://practicaltypography.com/headings.html). Because they are in small caps and bold, and they are located at the top of each block, the headings are clearly visible and help organize the CV. But because the font size is not too large (12pt) and they are in gray, they [do not dominate the page](https://practicaltypography.com/resumes.html).

Block headings are produced with the command `\block{}`.

---

## Lists

All the information in the CV is organized in lists. Listed information is ordered in reverse chronological order. Two types of lists are used in the template:

+ Itemized list (`itemize` environment) - Used in most blocks of information
+ Reverse-ordered list (`etaremune` environment) - Used for article list, so articles are presented in reverse chronological order but numbered in chronological order

The list bullet points are small and gray, so they are [not overbearing](https://practicaltypography.com/resumes.html). Indentation is the same for all lists. To maintain a clean and simple structure, the template does not include pre-formatted nested lists.

---

## Organizing information

The CV highlights the [most relevant information](https://practicaltypography.com/resumes.html): names of schools, employers, journals, and so on. 

Scholars often give the full bibliographical information for their publications. That does not seem necessary: beside the name of the journal and date of publication, the rest of the information (such as journal volume and issue and DOI and page range) is not relevant to a CV. For transparency and convenience, publication can be linked to a webpage with the full text and full bibliographical information for interested readers.

---

## Overall length

How long should your CV be? After the PhD job market—where CVs are typically confined to a single page—academic CVs often become excessively long, which may dilute their effectiveness by burying relevant information. [Butterick advises](https://practicaltypography.com/resumes.html) students to stick to one page and older people to limit themselves to just a couple of pages. I would agree: my current CV [is three pages long](/cv.pdf).