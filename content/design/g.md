---
title: "Minimalist LaTeX Template for Academic Books" 
date: 2026-04-01
url: /g/
author: "Pascal Michaillat"
description: "This template produces an academic book with LaTeX. The book follows typographical best practices and has a minimalist design."
summary: "This template produces an academic book with LaTeX. The book follows typographical best practices and has a minimalist design." 
cover:
    image: "/g.png"
    alt: "Book produced with template"
editPost:
    URL: "https://github.com/pmichaillat/latex-book"
    Text: "GitHub repository"
showToc: true
disableAnchoredHeadings: false
---

The template produces an academic book with [LaTeX](https://www.latex-project.org). The book adheres to typographical best practices and has a minimalist design. The template is particularly well suited for research monographs and textbooks. It is designed so books are comfortable to read and easy to scan, both in print and on screen. 

---

## View

- [LaTeX book template](https://github.com/pmichaillat/latex-book)
- [Book produced by the template](/g.pdf)

---

## Features

- The font for text, roman math, and numbers is Source Serif Pro.
- The font for monospaced text (including URLs) is Source Code Pro.
- The font for Greek and calligraphic math is Euler.
- The font for blackboard bold is Fourier.
- The font for mathematical symbols is MnSymbol.
- No colors are used in the text (only black) to reduce distraction and so the book prints well.
- Margins, spacing, and font size are set for comfortable reading.
- Headings and captions are designed so the book is easy to scan.
- Formatting is specified for parts, chapters, sections, subsections, and run‑in paragraphs.
- Formatting is specified for theorems, propositions, lemmas, definitions, assumptions, corollaries, and remarks.
- Formatting is specified for figures and tables.
- Formatting is specified for appendices, bibliography, and index.
- All labels are set to make cross-referencing easy.

---

## Text font

The font determines the appearance and readability of the entire book, so choosing a good font is key. Following [Butterick's advice](https://practicaltypography.com/free-fonts.html), the template uses [Source Serif Pro](https://mirror.las.iastate.edu/tex-archive/fonts/sourceserifpro/doc/sourceserifpro.pdf) for the text. 

Source Serif Pro is a serif font—a typical choice for long-form writing such as books. Source Serif Pro is not part of typical LaTeX book templates (unlike Times New Roman or Palatino), so it has a new, fresh feel. And since Source Serif Pro was designed in the last decade, it also has a modern feel.

Moreover, the Source Pro family includes a nice monospaced font: [Source Code Pro](https://mirrors.rit.edu/CTAN/fonts/sourcecodepro/doc/sourcecodepro.pdf). The template uses Source Code Pro as monospaced font—giving the monospaced text and regular text a similar look. The monospaced font is used in particular to typeset URLs and code fragments.

Finally, there is a sans-serif font in the Source Pro family: [Source Sans Pro](https://ctan.math.illinois.edu/fonts/sourcesanspro/doc/sourcesanspro.pdf). The [latex-presentation template](https://github.com/pmichaillat/latex-presentation) uses Source Sans Pro, giving the resulting presentations an appearance similar to the books and papers produced with these templates.

---

## Math fonts

LaTeX uses one font for text and other fonts for math. For consistency, the template sticks with [Source Serif Pro for roman math](https://ctan.mirrors.hoobly.com/macros/latex/contrib/mathastext/mathastext.pdf). It also uses Source Serif Pro for all the digits in math and basic punctuation (such as `.`, `?`, `%`, `;`, and `,`), so very basic mathematical expressions look the same in math and text. For example, the commands `3.5\%` and `$3.5\%$` produce the same results.

### Greek letters

For the Greek letters in math, the template uses the [Euler font](https://ctan.math.utah.edu/ctan/tex-archive/fonts/eulervm/doc/latex/eulervm/eulervm.pdf). These Greek letters look good, have the same thickness and height as the text letters, and are distinctive. For consistency, neither uppercase nor lowercase Greek letters are italicized.

All the standard Greek letters are available. A few variants are available as well: `\varepsilon`, `\varpi`, `\varphi`, and `\vartheta`. The variants `\varrho`, `\varsigma`, and `\varkappa` are not available with the Euler font.

### Calligraphic letters

The template also uses the [Euler font](https://ctan.math.utah.edu/ctan/tex-archive/fonts/eulervm/doc/latex/eulervm/eulervm.pdf) for calligraphic letters in math. These calligraphic letters fit well with the other fonts and are very readable. The calligraphic letters are produced with the `\mathcal{}` command.

### Blackboard-bold letters

The template uses the [Fourier font](https://mirror.mwt.me/ctan/macros/latex/contrib/mathalpha/doc/mathalpha-doc.pdf) as blackboard-bold font. It is cleaner than the default blackboard-bold font as it does not have serif. And it is slightly thicker than the default font so it matches well with Source Serif Pro and the Euler letters. The blackboard-bold letters are produced with the `\mathbb{}` command. 

### Bold characters

In the template, it is possible to bold any mathematical character (except blackboard-bold letters). This can be done using the `\bm{}` command in math. 

### Mathematical symbols

Finally, the template uses the [MnSymbol font](https://ftp.yz.yamagata-u.ac.jp/pub/CTAN/fonts/mnsymbol/MnSymbol.pdf) for the symbols used in math mode. The default Computer Modern symbols are too light and thin in comparison to the Source Serif Pro and Euler letters, and as a result do not mix well with them. The advantage of the MnSymbol font is that its symbols are thicker, so they mix better with the letters. The symbols are also less curly, which gives them a more modern feel.[^1] 

[^1]: The `MnSymbol` package is incompatible with the `amssymb` package. So it is not possible to load `amssymb` with the template. Neither should it be required since `MnSymbol` provides a vast collection of symbols.

---

## Font size

The font size is 11pt, as [recommended by Butterick](https://practicaltypography.com/point-size.html). It is easily readable but not too big. This size works well for continuous reading over many pages, which is important in a book.

---

## Line spacing

The line spacing is 150% of the point size. This is in line with [Butterick's advice](https://practicaltypography.com/line-spacing.html). Such spacing avoids that the text is too cramped or too spread out, and makes readings more comfortable over long stretches of text.

---

## Text margins

The left and right margins are 1.3 inch. With such margins, there are always 85–90 characters per line, just as [Butterick recommends](https://practicaltypography.com/line-length.html). Longer lines are harder to read. The top margin is 1 inch, which is standard. The bottom margin is 1.2 inch so the text [appears centered in the page](https://practicaltypography.com/page-margins.html). 

---

## Color scheme

[As Butterick says](https://practicaltypography.com/color.html), it is better to use color with restraint. A lot of colors, especially bright ones, is distracting. Furthermore, many colors are hard to read when they are printed in black and white. To reduce distraction, and to have a book that prints well, the template only uses the color black for text. In particular hyperlinks—to parts, chapters, sections, references, equations, figures, tables, results, and footnotes—are not colored. 

The typical, bright boxes surrounding hyperlinks should be avoided as they are distracting without adding any information. At this point everyone knows that LaTeX documents include such hyperlinks.

---

## Title page

The template's title page contains the required information for a research monograph: title, subtitle, authors, and date. It is otherwise minimalist.   

The title is bold, centered, and with a large font size. The subtitle (if any) appears below the title. Authors and date are centered and slightly smaller. Everything is laid out with ample vertical white space so the title page feels clean.

All these elements are controlled from the preamble of `book.tex`:

```latex
\title{Research Monograph}
\subtitle{How to Use the Book Template}
\author{First Author, Second Author}
\date{Month Year}
```

---

## Book structure

The template is based on LaTeX's standard `book` class and organizes content into front matter, main matter, appendices, and back matter:

- Front matter: title page and preface (`\chapter*{Preface}`).
- Main matter: several parts and chapters.
- Appendices: technical material at the end of the book.
- Back matter: acknowledgments, bibliography, and index.

The skeleton in `book.tex` illustrates a typical structure:

```latex
\chapter*{Preface}
\input{preface}

\part{First half of the book}
\chapter{Introduction}
\input{chapter1}
\chapter{Sections and content}
\input{chapter2}
\chapter{Math}
\input{chapter3}

\part{Second half of the book}
\chapter{Lists, figures, and tables}
\input{chapter4}
...

\appendix
\part{Technical appendix}
\chapter{Generic technical topic}
\input{appendixA}
...

\backmatter
\chapter{Acknowledgments}
\input{acknowledgements}
\bibliography{book.bib}
\printindex
```

Users can rename parts and chapters, or add and remove them, by editing `book.tex` and the corresponding `chapter*.tex` and `appendix*.tex` files.

---

## Table of contents

The table of contents is produced with the standard `\tableofcontents` command. Its appearance is customized so that:

- Parts are in bold.
- Chapter titles use small caps.
- Section titles use regular font.
- Dot leaders and spacing are set for clarity.

The depth of the table of contents is set so that chapters and sections appear; subsections are omitted to keep the table of contents compact and easy to scan.

---

## Headings

The template's headings follow [Butterick's advice](https://practicaltypography.com/headings.html) and extend the paper template's conventions to parts and chapters.

- Part headings use large bold type and are centered on an otherwise mostly empty page (a classic book design).
- Chapter headings are bold, large, and preceded by "CHAPTER X." in small caps.
- Section headings are a bit larger than the text (12pt) and bold.
- Subsection headings are bold.
- Paragraph headings are run‑in, in italic, so they are noticeable but not too prominent.

These headings are produced with the usual commands: `\part{}`, `\chapter{}`, `\section{}`, `\subsection{}`, and `\paragraph{}`. The template does not tailor formatting for subsubsections and smaller headings. Such small headings are a sign that the book's organization is too messy, and should be avoided.

---

## Theorems and other results

As is standard, the text of theorems is in italic—providing subtle emphasis. The theorem label is in small caps—again providing subtle emphasis. 

For consistency, propositions, lemmas, assumptions, definitions, and so on, are formatted just like theorems. The template comes with the following predefined environments:

- Theorems: `\begin{theorem} ... \end{theorem}`
- Propositions: `\begin{proposition} ... \end{proposition}`
- Lemmas: `\begin{lemma} ... \end{lemma}`
- Corollaries: `\begin{corollary} ... \end{corollary}`
- Definitions: `\begin{definition} ... \end{definition}`
- Assumptions: `\begin{assumption} ... \end{assumption}`
- Remarks: `\begin{remark} ... \end{remark}`
- Results: `\begin{result} ... \end{result}`

---

## Figures

Figures in books should appear close to where they are discussed. The template is configured so that figures typically appear at the top of the page where they are first mentioned. The template uses black-and-white figures for consistency with the text and for print. Figure panels are centered by default. The figure label is in small caps—just like the theorem label. The figure caption is placed below the figure.

The figure environment is set up so it is easy to reference a figure (figure 1.1) or directly a panel in a figure (figure 1.1A). 

With the command `\note{Text}`, it is easy to enter a note below the figure caption with details about the figure and sources. The note's font size is 9pt, just like footnotes.

The code for a basic figure with one panel is the following:

```LaTeX
\begin{figure}[t]
\includegraphics[scale=0.3,page=1]{\pdf}
\caption{Figure caption}
\note{Note for figure.}
\label{f:figure1}\end{figure}
```

The code for a figure with two panels is the following:

```LaTeX
\begin{figure}[t]
\subcaptionbox{Panel caption\label{f:panel1}}{\includegraphics[scale=0.2,page=1]{\pdf}}\hfill
\subcaptionbox{Panel caption\label{f:panel2}}{\includegraphics[scale=0.2,page=2]{\pdf}}
\caption{Figure caption}
\note[Source]{Source for the figure.}
\label{f:figure2}\end{figure}
```

Finally, the code for a figure with six panels is the following:

```LaTeX
\begin{figure}[p]
\subcaptionbox{Panel caption\label{f:panel3}}{\includegraphics[scale=0.2,page=1]{\pdf}}\hfill
\subcaptionbox{Panel caption\label{f:panel4}}{\includegraphics[scale=0.2,page=2]{\pdf}}\\
\subcaptionbox{Panel caption\label{f:panel5}}{\includegraphics[scale=0.2,page=3]{\pdf}}\hfill
\subcaptionbox{Panel caption\label{f:panel6}}{\includegraphics[scale=0.2,page=4]{\pdf}}\\
\subcaptionbox{Panel caption\label{f:panel7}}{\includegraphics[scale=0.2,page=5]{\pdf}}\hfill
\subcaptionbox{Panel caption\label{f:panel8}}{\includegraphics[scale=0.2,page=6]{\pdf}}
\caption{Figure caption}
\note[Note]{Note for figure.}
\label{f:figure3}\end{figure}
```

---

## Tables

Tables are formatted similarly to the paper template but sized and spaced for a book page. They should be placed at the top of the page where they are first mentioned—not in the middle of the page, and especially not all at the end of the book. Tables are centered by default. The table label is in small caps—just like the figure label. The table caption is placed above the table, as usual. Top and bottom table lines are thicker to clearly demarcate the table. The text in the table has a font size of 9pt. The text is spaced vertically to be easily readable.

The command `\note{Text}` can also be used to enter a note below the table, to provide details about the table and sources.

The code for a basic table is the following:

```LaTeX
\begin{table}[t]
\caption{Table caption}
\begin{tabular*}{\textwidth}[]{p{3.3cm}@{\extracolsep\fill}cccc}
\toprule
& \multicolumn{2}{c}{Columns 1–2} & \multicolumn{2}{c}{Columns 3–4}\\
\cmidrule{2-3}\cmidrule{4-5}
& Column 1 &  Column 2 &  Column 3  &  Column 4 \\
\midrule
Line 1: & A & B & C  & d \\
Line 2: & E &  F & G  & H   \\
Line 3: & K & V & P  & K  \\
Line 4: & J & M & N  & K  \\
\bottomrule
\end{tabular*}
\note{Note for table.}
\label{t:table1}\end{table}
```

A more sophisticated table with panels follows the same structure as in the paper template.

---

## Lists

Itemized and numbered lists are customized to fit well with the surrounding text. The text after the items is aligned with indented text (the start of a paragraph). All items (bullet points and numbers) are grey so as not to be too prominent. All extra vertical spacing is removed so spacing between list lines is exactly the same as spacing between lines of text.

---

## Citations

The template uses author-year citation style, as in the paper template, and requires the `natbib` package. All `natbib` [citation commands](https://ctan.math.washington.edu/tex-archive/macros/latex/contrib/natbib/natnotes.pdf) are usable in the template:

- Textual citation: `\citet{NameYear}` gives Name (Year)
- Textual citation with details: `\citet[p.~120]{NameYear}` gives Name (Year, p. 120)
- Parenthetical citation: `\citep{NameYear}` gives (Name Year)
- Parenthetical citation with details: `\citep[chapter 4]{NameYear}` gives (Name Year, chapter 4)
- Author citation: `\citeauthor{NameYear}` gives Name
- Year citation: `\citeyear{NameYear}` gives Year

---

## References

The reference list has a font size of 10pt, with the same spacing as the text. Each individual reference is indented for emphasis.

The references are formatted according to the guidelines from the [Chicago Manual of Style](https://www.chicagomanualofstyle.org/home.html), which are followed by many scientific publishers.

- An article published in a journal appears as follows: Zagorsky, Jay L. 1998. "Job Vacancies in the United States: 1923 to 1994." *Review of Economics and Statistics* 80 (2): 338–345. `https://doi.org/10.1162/003465398557438`.
- A working paper appears as follows: Leamer, Edward E. 2008. "What's a Recession, Anyway?" NBER Working Paper 14221. `https://doi.org/10.3386/w14221`.
- A book appears as follows: Murphy, Kevin P. 2022. *Probabilistic Machine Learning: An Introduction*. Cambridge, MA: MIT Press.
- An article published as part of a collection appears as follows: Stock, James H. and Mark W. Watson. 1993. "A Procedure for Predicting Recessions with Leading Indicators: Econometric Issues and Recent Experience." In *Business Cycles, Indicators and Forecasting*, edited by James H. Stock and Mark W. Watson, chap. 2. Chicago: University of Chicago Press.
- A data entry appears as follows: BLS. 2024. "Job Openings: Total Nonfarm." FRED, Federal Reserve Bank of St. Louis. `https://fred.stlouisfed.org/series/JTSJOL`.
- A website entry appears as follows: BLS. 2020. "Labor Force Statistics from the Current Population Survey: Overview." `https://perma.cc/RN3P-S4SL`.

---

## Appendices

The template makes it easy to add appendices at the end of the book. The appendices start with the command `\appendix`. The formatting of the appendices strictly follows that of the main text, but chapter headings are relabeled as "APPENDIX A.", "APPENDIX B.", and so on.

All appendix chapters are clearly marked `Appendix` in the headings and in the table of contents. Labeling follows LaTeX's standard `book` conventions, so all counters (equations, figures, tables, theorems) automatically pick up appendix letters: for instance, equation (A.1), figure A.2, table A.3, or theorem A.1.

---

## Index

The template includes an index built with `imakeidx`. Index entries are created with the standard `\index{entry}` command, and the index is printed with `\printindex` at the end of the book.

By default, the style:

- Adds the index as a chapter in the back matter.
- Places the Index entry in the table of contents, alongside the Bibliography.
- Uses lowercase index entries unless they are proper nouns.

Users can disable the index by commenting out the lines that load `imakeidx` and call `\makeindex` in `book.sty`, and by removing `\printindex` from `book.tex`.

