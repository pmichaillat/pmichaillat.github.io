---
title: "Minimalist LaTeX Template for Academic Papers" 
date: 2024-06-28
url: /a/
aliases: 
    - /d2/
    - /d2.pdf
    - /d2a.pdf
author: "Pascal Michaillat"
description: "This template produces an academic paper with LaTeX. The paper follows typographical best practices and has a minimalist design."
summary: "This template produces an academic paper with LaTeX. The paper follows typographical best practices and has a minimalist design." 
cover:
    image: "/a.png"
    alt: "Paper page produced with template"
editPost:
    URL: "https://github.com/pmichaillat/latex-paper"
    Text: "GitHub repository"
showToc: true
disableAnchoredHeadings: false
---

The template produces an academic paper with [LaTeX](https://www.latex-project.org). The paper adheres to typographical best practices and has a minimalist design. The template is particularly well suited for research papers. It is designed so papers are comfortable to read and easy to scan, both in print and on screen. 

---

## View

+ [LaTeX template for academic papers](https://github.com/pmichaillat/latex-paper)
+ [Research paper produced by the template](/a.pdf)
+ [Online appendix produced by the template](/aa.pdf)

---

## Features

+ The font for text, roman math, and numbers is Source Serif Pro.
+ The font for monospaced text (including URLs) is Source Code Pro.
+ The font for Greek and calligraphic math is Euler.
+ The font for blackboard bold is Fourier.
+ The font for mathematical symbols is MnSymbol.
+ No colors are used in the text (only black) to reduce distraction and so the paper prints well; colors are reserved for figures.
+ Margins, spacing, and font size are set for comfortable reading.
+ Headings and captions are designed so the paper is easy to scan.
+ Formatting is specified for theorems, propositions, lemmas, definitions, assumptions, corollaries, and remarks.
+ Formatting is specified for figures and tables.
+ Formatting is specified for appendix and a separate online appendix.
+ Formatting is specified for references.
+ All labels are set to make cross-referencing easy.

---

## Text font

The font determines the appearance and readability of the entire paper, so choosing a good font is key. Following [Butterick's advice](https://practicaltypography.com/free-fonts.html), the template uses [Source Serif Pro](https://mirror.las.iastate.edu/tex-archive/fonts/sourceserifpro/doc/sourceserifpro.pdf) for the text. 

Source Serif Pro is a serif font—a typical choice for long-form writing. Source Serif Pro is not part of typical paper templates (unlike Times New Roman or Palatino), so it has a new, fresh feel. And since Source Serif Pro was designed in the last decade, it also has a modern feel.

Moreover, the Source Pro family includes a nice monospaced font: [Source Code Pro](https://mirrors.rit.edu/CTAN/fonts/sourcecodepro/doc/sourcecodepro.pdf). The template uses Source Code Pro as monospaced font—giving the monospaced text and regular text a similar look. The monospaced font is used in particular to typeset URLs.

Another advantage of Source Serif Pro is that there is a sans-serif font in the Source Pro family: [Source Sans Pro](https://ctan.math.illinois.edu/fonts/sourcesanspro/doc/sourcesanspro.pdf). This [presentation template](/c/) uses Source Sans Pro, which gives presentations and papers produced by the two templates a similar look.

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

Finally, the template use the [MnSymbol font](https://ftp.yz.yamagata-u.ac.jp/pub/CTAN/fonts/mnsymbol/MnSymbol.pdf) for the symbols used in math mode. The default Computer Modern symbols are too light and thin in comparison to the Source Serif Pro and Euler letters, and as a result do not mix well with them. The advantage of the MnSymbol font is that its symbols are thicker, so they mix better with the letters. The symbols are also less curly, which gives them a more modern feel.[^1] 

[^1]: The `MnSymbol` package is incompatible with the `amssymb` package. So it is not possible to load `amssymb` with the template. Neither should it be required since `MnSymbol` provides a vast collection of symbols.

---

## Font size

The font size is 11pt, as [recommended by Butterick](https://practicaltypography.com/point-size.html). It is easily readable but not too big. (This is also the font size that Donald Knuth chose as default for TeX articles.)

---

## Line spacing

The line spacing is 150% of the point size. This is in line with [Butterick's advice](https://practicaltypography.com/line-spacing.html). Such spacing avoids that the text is too cramped or too spread out, and makes readings more comfortable.

---

## Text margins

The left and right margins are 1.3 inch. With such margins, there are always 85–90 characters per line, just as [Butterick recommends](https://practicaltypography.com/line-length.html). Longer lines are harder to read. The top margin is 1 inch, which is standard. The bottom margin is 1.2 inch so the text [appears centered in the page](https://practicaltypography.com/page-margins.html). 

---

## Color scheme

[As Butterick says](https://practicaltypography.com/color.html), it is better to use color with restraint. A lot of colors, especially bright ones, is distracting. Furthermore, many colors are hard to read when they are printed in black and white. To reduce distraction, and to have a paper that prints well, the template only uses the color black for text. In particular hyperlinks—to sections, references, equations, figures, tables, results, and footnotes—are not colored. 

The typical, bright boxes surrounding hyperlinks should be avoided as they are distracting without adding any information. At this point everyone knows that LaTeX documents include such hyperlinks.

---

## Title page

The template's title page contains all the required information: title, authors, date, abstract, affiliations, and acknowledgements. It is otherwise pretty minimalist. There are no "thanks" symbols, no "abstract" title, no indentation, no page numbers. These elements are common in papers, but they do not convey any useful information, so the template gets rid of them.

The title is bold, centered, and with a 24pt font size. Authors and date are centered and 12pt. The abstract is 11pt. Affiliations and acknowledgements are 9pt, just like the footnotes in the text.

An URL for the paper can be placed at the bottom of the title page by adding the command `\available{URL}` to the preamble of the document. Such URL allows readers to go easily to the latest version of the paper. With an optional argument, the command indicates where the paper has been published: `\available[Journal]{URL}` places both the journal name and URL at the bottom of the title page. The URL and journal name are displayed in small font (9pt) and gray so they are not too obtrusive.

---

## Headings

The template's headings follow [Butterick's advice](https://practicaltypography.com/headings.html). Section headings are a bit larger than the text (12pt) and bold. Section headings are centered to clearly separate sections. Subsection headings are bold. And paragraph headings are in italic, so they are noticeable but not too prominent. These headings are produced with the usual commands: `\section{}`, `\subsection{}`, and `\paragraph{}`.

The template does not tailor formatting for subsubsections and smaller headings. Such small headings are a sign that the paper's organization is too messy, and should be avoided.

---

## Theorems and other results

As is standard, the text of theorems is in italic—providing subtle emphasis. The theorem label is in small caps—again providing subtle emphasis. 

For consistency, propositions, lemmas, assumptions, definitions, and so on, are formatted just like theorems. The template comes with the following predefined environments:

+ Theorems: `\begin{theorem} ... \end{theorem}`
+ Propositions: `\begin{proposition} ... \end{proposition}`
+ Lemmas: `\begin{lemma} ... \end{lemma}`
+ Corollaries: `\begin{corollary} ... \end{corollary}`
+ Definitions: `\begin{definition} ... \end{definition}`
+ Assumptions: `\begin{assumption} ... \end{assumption}`
+ Remarks: `\begin{remark} ... \end{remark}`


---

## Figures

A figure should be placed at the top of the page where it is first mentioned—not in the middle of the page, and especially not at the end of the paper. Figure panels are centered by default. The figure label is in small caps—just like the theorem label. The figure caption is placed bellow the figure. An advantage of avoiding colors in the text is that the colors in figures stand out.

The figure environment is set up so it is easy to reference a figure (figure 1) or directly a panel in a figure (figure 1A). 

With the command `\note{Text}`, it is easy to enter a note below the figure caption with details about the figure and sources. The note's font size is 9pt, just like footnotes.

The code for a basic figure with one panel is the following:

```LaTeX
\begin{figure}[t]
\includegraphics[scale=0.3]{figure.pdf}
\caption{Figure caption}
\note{Note for figure.}
\label{1}\end{figure}
```

The code for a figure with two panels is the following:

```LaTeX
\begin{figure}[t]
\subcaptionbox{Panel caption\label{1}}{\includegraphics[scale=0.2]{1.pdf}}\hfill
\subcaptionbox{Panel caption\label{2}}{\includegraphics[scale=0.2]{2.pdf}}
\caption{Figure caption}
\note[Source]{Source for the figure.}
\label{3}\end{figure}
```

Finally, the code for a figure with six panels is the following:

```LaTeX
\begin{figure}[p]
\subcaptionbox{Panel caption\label{1}}{\includegraphics[scale=0.2]{1.pdf}}\hfill
\subcaptionbox{Panel caption\label{2}}{\includegraphics[scale=0.2]{2.pdf}}\\
\subcaptionbox{Panel caption\label{3}}{\includegraphics[scale=0.2]{3.pdf}}\hfill
\subcaptionbox{Panel caption\label{4}}{\includegraphics[scale=0.2]{4.pdf}}\\
\subcaptionbox{Panel caption\label{5}}{\includegraphics[scale=0.2]{5.pdf}}\hfill
\subcaptionbox{Panel caption\label{6}}{\includegraphics[scale=0.2]{6.pdf}}
\caption{Figure caption}
\note[Note]{Note for figure.}
\label{7}\end{figure}
```

With the above code, a specific panel in a figure can be referenced with `figure \ref{1}`, which produces figure 1A, and the entire figure can be referenced with `figure \ref{7}`, which produces figure 1. A panel can also be referenced without mentioning the figure: `panel \subref{1}` produces panel A.

---

## Tables

A table should be placed at the top of the page where it is first mentioned—not in the middle of the page, and especially not at the end of the paper. Tables are centered by default. The table label is in small caps—just like the figure label. The table caption is placed above the table, as usual. Top and bottom table lines are thicker to clearly demarcate the table. The text in the table has a font size of 9pt. The text is spaced vertically to be easily readable (spacing is insufficient in standard tables).

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
\label{1}\end{table}
```

The code for a more sophisticated table with panels is the following:

```LaTeX
\begin{table}[t]
\caption{Table caption}
\begin{tabular*}{\textwidth}[]{p{3.3cm}@{\extracolsep\fill}ccccc}
\toprule
& Column 1 &  Column 2 &  Column 3  &  Column 4 &  Column 5 \\
\midrule
\multicolumn{6}{l}{A. First panel}\\
Line 1: & A & C & V  & 9\% & 7.3\% \\
Line 2: & X &  H & O  & 1.1\% & 4\%   \\
\midrule
\multicolumn{6}{l}{B. Second panel}\\
Line 3: & U & B & J  & K & K \\
Line 4: & N & Y & T  & L & T \\
Line 5: & G & S & Q  & P & Q \\
\bottomrule
\end{tabular*}
\note{Note for table.}
\label{1}\end{table}
```

---

## Lists

Itemized and numbered list are customized to fit well with the surrounding text. The text after the items is aligned with indented text (the start of a paragraph). All items (bullet points and numbers) are grey so as not to be too prominent. All extra vertical spacing is removed so spacing between list lines is exactly the same as spacing between lines of text.

---

## Citations and references

The format of citations and references follow the guidelines from the [Chicago Manual of Style](https://www.chicagomanualofstyle.org/home.html), which are followed by most scientific journals in the US.

The reference list has a font size of 10pt, with the same spacing as the text. Each individual reference is indented for emphasis.

All [standard citation commands](https://ctan.math.washington.edu/tex-archive/macros/latex/contrib/natbib/natnotes.pdf) are usable in the template:

+ Textual citation: `\citet{NameYear}` gives Name (Year)
+ Textual citation with details: `\citet[p. 120]{NameYear}` gives Name (Year, p. 120)
+ Parenthetical citation: `\citep{NameYear}` gives (Name Year)
+ Parenthetical citation with details: `\citep[chapter 4]{NameYear}` gives (Name Year, chapter 4)
+ Author citation: `\citeauthor{NameYear}` gives Name
+ Year citation: `\citeyear{NameYear}` gives Year

---

## Appendix

The template makes it easy to add an appendix at the end of the paper. The appendix starts with the command `\appendix`. The formatting of the appendix strictly follows that of the main text.

All the appendix sections are clearly marked `Appendix` and are numbered as Appendix A, Appendix B, Appendix C, and so on. The appendix subsections are also numbered (for instance, A.1, A.2, B.1, B.2) so they can be referred to. 

All labels in the appendix start with an `A`, so it is clear that they point to some material in the appendix: for instance, corollary A1, figure A2, table A3, or equation (A10). All counters are reset at the beginning of the appendix (tables, figures, equations, and theorems) so all the labels start at A1, A2, and so on.

---

## Online appendix

Once a research paper gets published, the appendix must often be transformed into an online appendix. To help with this task, the repository also includes a template for online appendices. In the appendix template, the abstract is replaced by a table of contents. In addition, all the labels from the main text (equation numbers, figure and table numbers, theorem numbers, section numbers) continue to be usable in the online appendix. So the cross-references from main text to appendix are not broken even though the appendix is now in a separate file. [This requires the following](https://ctan.math.illinois.edu/macros/latex/required/tools/xr.pdf):

+ `appendix.tex` is in the same folder as `paper.tex`.
+ `paper.tex` is compiled first.
+ The auxiliary file `paper.aux` is available when `appendix.tex` is compiled.
    
---

## Submission to arXiv

The template is perfectly compatible with [arXiv](https://arxiv.org/). In particular, the template works with the TeXLive 2023 distribution, which is the LaTeX distribution [currently used by arXiv](https://info.arxiv.org/help/faq/texlive.html).

A paper based on the template can be submitted to arXiv in just three steps once it has been compiled with pdfTeX:

+ Adjust the preamble of the source file `paper.tex`: on line 3, replace `\bibliographystyle{bibliography}` by `\pdfoutput=1`. The `\bibliographystyle{bibliography}` command is not needed because arXiv produces the bibliography directly from the `paper.bbl` file. The `\pdfoutput=1` is required because the paper [is compiled with pdfTeX](https://info.arxiv.org/help/submit_tex.html#pdflatex).
+ Collect the required files into a folder. There should be four files: the source file `paper.tex`, the bibliography file `paper.bbl`, the style file `paper.sty`, and the figure file `figures.pdf`. 
+ Zip the folder and upload the zipped file to arXiv.