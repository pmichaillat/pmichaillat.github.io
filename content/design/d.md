---
title: "Minimalist MATLAB Template for Scientific Figures" 
date: 2023-10-07
url: /d/
aliases: 
    - /d4/
    - /d4.pdf
author: "Pascal Michaillat"
description: "This template produces a set of scientific figures with MATLAB. The figures adhere to best practices for the visual display of quantitative information."
summary: "This template produces a set of scientific figures with MATLAB. The figures adhere to best practices for the visual display of quantitative information."
cover:
    image: "/d.png"
    alt: "Figure produced with template"
editPost:
    URL: "https://github.com/pmichaillat/matlab-figures"
    Text: "GitHub repository"
showToc: true
disableAnchoredHeadings: false

---

The template produces basic scientific figures using [MATLAB](hhttps://matlab.mathworks.com). The figures adhere to best practices for the visual display of quantitative information—with the aim to convey quantitative information effectively on screen and in print.

---

## View

+ [MATLAB template for scientific figures](https://github.com/pmichaillat/matlab-figures)
+ [Figures produced by the template](/d.pdf)

---

## Features

+ The font on the axes and annotations is Helvetica.
+ Font sizes and line thicknesses are set for comfortable reading once the figures are inserted [in pairs in a paper](/d2/).
+ A collections of color palettes is provided, both for qualitative displays and sequential displays. 
+ The template produces a collection of basic figures with different plot types and different features:
    * Time series plots: single or multiple series, with or without period areas, with or without above-below areas
    * Scatter plots: transparent or not, connected or not, with or without above-below areas
+ Figure dimensions are set to minimize the white space around the content.
+ The figure aspect ratio is 4:3 so the figure can easily be annotated with a presentation software.
+ On a Mac, the figures can easily be annotated with Keynote. This procedure is more user friendly, and more flexible, than annotating the figures directly in MATLAB. The Keynote file `figures.key` illustrates how to annotate the figures produced by the template.

--- 

## General principles

The default figures produced by MATLAB do not look particularly good, especially once they are inserted in papers or presentations.  The lines are too thin, the font size is too small, the color palette has been overused, and so on. As a result, they do not convey information as effectively as they could.

The goal of this template is to produce figures that can be easily inserted into papers and presentations and that convey information effectively. The template attempts to follow the data visualization best practices developed by [Edward Tufte](https://www.edwardtufte.com/tufte/) in [*The Visual Display of Quantitative Information*](https://www.edwardtufte.com/tufte/books_vdqi). This book is the classic reference on statistical graphics, charts, and tables. Using many examples, it explains how to display data for precise, effective, and quick analysis. One of the main message of the book is to maximize the data-ink ratio—that is, to minimize as much as possible ink that does not convey information.

--- 

## Font type

Fonts matter in figures, just as in papers and presentations. The font determines the appearance and readability of the figure. To improve readability, sans-serif font are recommended for the text in figures.  The simplified letter forms of sans-serif fonts are not encumbered by serifs, which improves the readability of characters at very small sizes. The clean and simple lines of sans-serif fonts also enhance the figure's visual presentation.

The template uses Helvetica, which is a [classic, quality](https://practicaltypography.com/helvetica-and-arial-alternatives.html) font and is supported by MATLAB both for displaying on screen and for printing (most fonts are not). An advantage of Helvetica is that it is legible at all sizes, even small. This is useful for figures, in which some annotations must be small to fit in the space available.[^1] 

[^1]: In fact, Helvetica is recommended by many science publishers, including [Nature](https://www.nature.com/documents/nature-final-artwork.pdf) and [Springer](https://www.springer.com/gp/authors-editors/journal-author/journal-author-helpdesk/manuscript-preparation/1260).

---

## Font size

Beside the typeface, another key choice is the font size used in the figures. The template picks a size so the text in the figure is about the same size as footnote text once the figure is inserted in the paper (about 9pt). This way the figure will be easily readable (smaller text would be difficult to read). Of course, lettering should be consistently sized throughout the figure. Variance of font size within an illustration should be minimal. As a rule of thumb, text should appear no smaller than 7pt at intended size; 6pt is the minimum for superscript and subscript characters.

---

## Colors

A collection of color palettes are provided, both for qualitative displays and sequential displays. The palettes were created by [Cynthia Brewer](https://sites.psu.edu/cbrewer/) and are available on [ColorBrewer](https://colorbrewer2.org). The colors have been optimized to convey qualitative and quantitative information as effectively as possible.

---

## Dimensions

Figure dimensions are set to minimize the white space around the content. The figure aspect ratio is 4:3 so the figure can easily be inserted into a presentation software and annotated there.

---

## Lines

Line thicknesses are set for comfortable reading once the figures are inserted [in pairs in a paper](/d2/). Line weights and strokes should be set between 0.25pt and 1pt at the final size.

--- 

## Plot types

The template produces a collection of figures with different plot types and different features.

It produces a range of time series plots: single or multiple series, with or without period areas, with or without above-below areas.


It also produces a range of scatter plots: transparent or not, connected or not, with or without above-below areas.

---

## Annotations

On a Mac, the figures can easily be annotated with Keynote. This procedure is more user friendly, and more flexible, than annotating the figures directly in MATLAB. The Keynote file `figures.key` illustrates how to annotate the figures produced by the template.

First, create a Keynote presentation. Insert each figure as a slide background. Annotate the slide as desired. Finally, save the resulting presentation as PDF (such as `figures.pdf`). With this method, all the figures have the exact same size, and each figure can be inserted individually into a LaTeX document, using `\includegraphics[scale=0.2,page=X]{figures.pdf}` to insert page X of the collection of figures called `figures.pdf`.

---

## Scaling for different figure sizes

The template is tailored for the common case in which the figures are inserted [in pairs in an academic paper](/d2/). The scaling factor in LaTeX to insert two figures side by side is 0.2. The template is designed so that the PDF pages created by MATLAB, and annotated through Keynote, have readable font and line sizes once they are scaled by a factor of 0.2. For instance to obtain 8pt text and 1pt lines, we need 8/0.2 = 40pt text and 1/0.2 = 5pt lines in Keynote. This is what the current template produces.

To insert bigger figures into LaTeX, the template should be adjusted so that the final figures maintain the same text and line sizes as the current figures. For instance to insert twice-larger figures, the scaling factor in LaTeX can be increased to 0.4. Then all the font, line, and marker sizes should be divided by two in the template so all text, markers, and lines maintain a consistent size across figures, irrespective of the figure size.