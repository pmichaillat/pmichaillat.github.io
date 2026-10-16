---
title: "Minimalist LaTeX Template for Academic CVs" 
date: 2026-10-15
url: /f/
aliases:
    - /f1.pdf
author: Pascal Michaillat
description: "This template produces an academic CV with LaTeX. The template follows typographical best practices and has a minimalist design."
summary: "This template produces an academic CV with LaTeX. The template follows typographical best practices and has a minimalist design. Also available is a variant of the template that produces a one-page CV." 
cover:
    image: /f.png
    alt: "CV produced with the template"
showToc: false
disableAnchoredHeadings: false
buttons:
    - name: Code
      url: https://github.com/pmichaillat/latex-cv
    - name: Preview
      url: /f.pdf

---
---

The template produces an academic CV with [LaTeX](https://www.latex-project.org). The template adheres to typographical best practices and has a minimalist design. It is well suited for graduate students, postdocs, faculty members, and other researchers. The design emphasizes structural clarity and visual simplicity. A variant of the template is also available to produce a one-page CV.

---

## Main features

+ The font for text and numbers is Source Serif Pro.
+ Dedicated math fonts and symbols are included to typeset formulas cleanly.
+ The template uses only gray and black to reduce distraction and print flawlessly.
+ Margins, spacing, and font size are set for comfortable reading.
+ Headings, lists, and footer are designed so the CV is well organized and easy to skim.
+ A variant of the template produces a one-page CV.

---

## Text font

The font determines the appearance and readability of the entire CV, so choosing a good font is key. Following [Butterick's advice](https://practicaltypography.com/free-fonts.html), the template uses [Source Serif Pro](https://mirror.las.iastate.edu/tex-archive/fonts/sourceserifpro/doc/sourceserifpro.pdf) for the text. 

Source Serif Pro is a serif font. It is not part of typical CV templates so it has a fresh feel. And since it was designed in the 21st century, it also has a modern feel.

---

## Math fonts and symbols

If required anywhere in the CV—in titles of articles or courses—mathematical expressions are typeset using the [following math fonts](/a/#math-fonts):

+ Roman letters - [Source Serif Pro font](https://mirror.las.iastate.edu/tex-archive/fonts/sourceserifpro/doc/sourceserifpro.pdf)
+ Greek letters - [Euler font](https://ctan.math.utah.edu/ctan/tex-archive/fonts/eulervm/doc/latex/eulervm/eulervm.pdf)
+ Calligraphic letters - [Euler font](https://ctan.math.utah.edu/ctan/tex-archive/fonts/eulervm/doc/latex/eulervm/eulervm.pdf)
+ Blackboard-bold letters - [Fourier font](https://mirror.mwt.me/ctan/macros/latex/contrib/mathalpha/doc/mathalpha-doc.pdf) 
+ Symbols - [MnSymbol font](https://ftp.yz.yamagata-u.ac.jp/pub/CTAN/fonts/mnsymbol/MnSymbol.pdf) 

---

## Font size

The font size is 10pt, in line with [Butterick's recommendation](https://practicaltypography.com/point-size.html). It is easily readable but not too big, keeping the CV's appearance compact.

---

## Line spacing

The baseline is set to 1.1 times LaTeX's normal baseline. At a 10pt font size, that normal baseline is 12pt, so the baseline is 13.2pt, or about 130% of the font size—in line with [Butterick's advice](https://practicaltypography.com/line-spacing.html).. Spacing between bullet points is larger than the spacing between lines, so reading remains comfortable. Overall the line spacing prevents the text from appearing too cramped or too spread out.

---

## Text margins

The left and right margins are 1.3 inches. With such margins, plus the space taken by the bullet points, there are at most 90 characters per line, just as [Butterick recommends](https://practicaltypography.com/line-length.html) to ensure comfortable reading. 

The top margin is 1 inch, which is standard. The bottom margin is 1.1 inch so the text [appears centered in the page](https://practicaltypography.com/page-margins.html). 

---

## Color scheme

Colors are distracting, and many colors are hard to read when they are printed in black and white. To reduce distraction and have a CV that prints well, the template only uses black for the main text, and gray for surrounding elements (headings, bullet points, footer, lines).

---

## Title

The CV title is just your name. The title is produced by the command `\name{}`. It is centered and typeset in black small caps at a 25pt font size. The small caps are letterspaced. 

--- 

## Contact information

The contact information is kept to a minimum: email address and website URL. The contact information is placed in the footer, at the bottom of each page. In practice phone numbers and mailing addresses are not used anymore, so it seems unnecessary to include them, especially in such a prominent position as the top of the CV. This information can be added to your website instead.

The footer also includes the date when the CV was last updated.

The footer font size is 8pt, just like footnotes would be, and the font color is gray. As a result, the footer is not too obtrusive.

The commands to populate the footer, used in the document preamble, are `\cvfoot{L}{}` for the website, `\cvfoot{C}{}` for the email address, and `\cvfoot{R}{}` for the date.

---

## Block headings

The CV is organized in blocks containing key information. The blocks are ordered by importance:

+ Employment
+ Education
+ Books, articles, and preprints
+ Courses
+ Service
+ Grants
+ Awards

Each block heading is produced with `\block{}`. The command places a gray horizontal rule above a heading set in letterspaced small caps. Because the headings sit at the top of each block, they are clearly visible and help organize the CV. But because the font is gray and not larger than the text font, the headings [do not dominate the page](https://practicaltypography.com/resumes.html).

---

## Lists

All the information in the CV is organized in lists. Listed information is ordered in reverse chronological order. Two types of lists are used in the template:

+ Itemized list (`itemize` environment) - Used in most blocks of information
+ Reverse-ordered list (`etaremune` environment) - Used for the article list, so articles are presented in reverse chronological order but numbered in chronological order

The bullet points are empty and gray, so they are [not overbearing](https://practicaltypography.com/resumes.html). Indentation is the same for all lists. To maintain a clean and simple structure, the template does not include nested lists.

---

## Organizing information

The CV highlights the [most relevant information](https://practicaltypography.com/resumes.html): names of schools, names of employers, names of journals, and so on. Fields within an entry are separated with `\sep`, which inserts a black centered dot. Coauthors are indicated with the command `\with{}`.

Scholars often give the full bibliographical information for their publications. That does not seem necessary: besides the name of the journal and date of publication, the rest of the information (such as journal volume, issue, DOI, and page range) is not relevant to a CV. For transparency and convenience, each publication can be linked to a webpage with the full text and full bibliographical information. The same applies to courses, books, data, and software. These links are uncolored.

---

## Overall length

How long should your CV be? During the PhD job market, CVs are typically confined to a single page. After that, academic CVs often become excessively long, which may dilute their effectiveness by burying relevant information. [Butterick advises](https://practicaltypography.com/resumes.html) students to stick to one page and older people to limit themselves to just a couple of pages, which seems like very good advice.

---

## One-page CV

The repository also includes a variant of the template that produces [a one-page CV](/fo.pdf). The one-page CV might be particularly helpful for job-market candidates and others who are required to fit their CV on one page. Compared to the baseline CV, the one-page variant has 1.2 inch side margins, a 0.8 inch top margin, and a 1 inch bottom margin. Its line spacing is 1.05 times LaTeX's normal baseline, and the spacing between list items is tighter.