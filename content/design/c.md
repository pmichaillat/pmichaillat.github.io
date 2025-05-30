---
title: "Minimalist LaTeX Template for Academic Presentations" 
date: 2024-06-28
url: /c/
aliases: 
    - /d1/
    - /d1.pdf
author: "Pascal Michaillat"
description: "This template produces an academic presentation with LaTeX and Beamer. The presentation follows typographical best practices and has a minimalist design."
summary: "This template produces an academic presentation with LaTeX and the Beamer class. The presentation follows typographical best practices and has a minimalist design."
cover:
    image: "/c.png"
    alt: "Presentation slide produced with template"
editPost:
    URL: "https://github.com/pmichaillat/latex-presentation"
    Text: "GitHub repository"
showToc: true
disableAnchoredHeadings: false

---

The template produces an academic presentation using [LaTeX](https://www.latex-project.org) with the [Beamer class](https://ctan.org/pkg/beamer). The presentation adheres to typographical best practices and has a minimalist design. The template is particularly well suited for research presentations. It is designed to convey scientific arguments and results effectively.

---

## View

+ [LaTeX template for academic presentations](https://github.com/pmichaillat/latex-presentation)
+ [Research presentation produced by the template](/c.pdf)

---

## Features

+ The aspect ratio is 4:3.
+ There are no frills at the periphery of the slides.
+ The font for text, roman math, and numbers is Source Sans Pro.
+ The font for monospaced text (including URLs) is Source Code Pro.
+ The font for Greek and calligraphic math is Euler.
+ The font for blackboard bold is Fourier.
+ The font for mathematical symbols is MnSymbol.
+ No colors are used in the text (only grayscale) to reduce distraction; colors are reserved for figures and text alerts.
+ Margins, spacing, and font size are set for comfortable reading.
+ Formatting is specified for theorems, propositions, lemmas, definitions, assumptions, corollaries, and remarks.
+ Formatting is specified for figures and tables.
+ Section slides and final slide can easily be inserted into the presentation.

---

## 4:3 versus 16:9 aspect ratio

There has been a shift from slides with a 4:3 aspect ratio to wider slides with a 16:9 aspect ratio. This template sticks to the traditional 4:3 aspect ratio. 

First, 4:3 slides are better at effectively presenting supporting information. And slides are here as support, not as a substitute, for what the speaker is talking about. 4:3 slides force presenters to display only essential information on slides—leading to more effective presentations. 16:9 slides are often used to present two graphs at a time, or two paragraphs at a time, or a graph with some side text. This is confusing and possibly distracting for listeners, who do not know what to look at, and may be looking at the wrong part of the slide. 4:3 slides can only display one graph or one paragraph at a time—focusing the attention of the audience on that one piece of information. 

Second, lines of text on 16:9 slides are often excessively long. The lines cannot be read at one glance, so reading them distracts from the presentation. 

Third, 4:3 slides are more robust. They are easily readable will all projectors, both new and old. By contrast, the text of 16:9 slides becomes very small when they are displayed on old 4:3 projectors.

Fourth, 4:3 slides work better on tablets because most tablets have a 4:3 aspect ratio (iPads for instance). It has becomes very common to read or display slides on tablets, or watch online presentation on tablets. In that context, 4:3 slides display better.

Sometimes, however, host institutions or conferences require presenters to use 16:9 aspect ratio. The template can be adjusted to produce such slides. Just add the `aspectratio=169` option to the `\documentclass` command. Specifically, to produce a 16:9 presentation, the first line of `presentation.tex` should be:

```tex
\documentclass[11pt,aspectratio=169,xcolor={dvipsnames},hyperref={pdftex,pdfpagemode=UseNone,hidelinks,pdfdisplaydoctitle=true},usepdftitle=false]{beamer}
```

---

## Text font

Fonts matter in presentations—just as in papers. The font determines the appearance and readability of the entire presentation. For the presentation's text, the template uses [Source Sans Pro](https://mirror.las.iastate.edu/tex-archive/fonts/sourcesanspro/doc/sourcesanspro.pdf), which is one of the free fonts [recommended by Matthew Butterick](https://practicaltypography.com/free-fonts.html).

Source Sans Pro is a sans-serif font. This is an important feature, as sans-serif fonts are more readable than fonts with serif in presentations. Another advantage of Source Sans Pro is that it is not part of typical slide templates (unlike Fira Sans for instance), so it feels new and fresh. And since Source Sans Pro was designed in the last decade, it also feels modern.

Moreover, the Source Pro family includes a nice monospaced font: [Source Code Pro](https://mirrors.rit.edu/CTAN/fonts/sourcecodepro/doc/sourcecodepro.pdf). The template uses Source Code Pro as monospaced font—giving the monospaced text and regular text a similar look. The monospaced font is used in particular to typeset URLs.

Another advantage of Source Sans Pro is that it comes with a broad range of weight. For instance, the template uses the semibold font weight in places. To activate the semibold font instead of the usual bold font, use `\sbseries` and `\textsb{}` instead of `\bfseries` and `\textbf{}`.

A last advantage of Source Sans Pro is that there is a with-serif font in the Source Pro family: [Source Serif Pro](https://mirror.las.iastate.edu/tex-archive/fonts/sourceserifpro/doc/sourceserifpro.pdf). This [paper template](/a/) uses Source Serif Pro, which gives the presentations and papers produced by the two templates a similar look.

---

## Math fonts

LaTeX uses one font for text and other fonts for math. For consistency, the template sticks with [Source Sans Pro for roman math](https://ctan.mirrors.hoobly.com/macros/latex/contrib/mathastext/mathastext.pdf). It also uses Source Sans Pro for all the digits in math and basic punctuation (such as `.`, `?`, `%`, `;`, and `,`), so very basic mathematical expressions look the same in math and text. For example, the commands `3.5\%` and `$3.5\%$` produce the same results.

### Greek letters

There are some sans-serif Greek alphabets, but the letters look unusual and are hard to recognize. So for the Greek letters in math, the template uses the [Euler font](https://ctan.math.utah.edu/ctan/tex-archive/fonts/eulervm/doc/latex/eulervm/eulervm.pdf). These Greek letters look good, have the same thickness and height as the text letters, and are distinctive. For consistency, neither uppercase nor lowercase Greek letters are italicized.

All the standard Greek letters are available. A few variants are available as well: `\varepsilon`, `\varpi`, `\varphi`, and `\vartheta`. The variants `\varrho`, `\varsigma`, and `\varkappa` are not available with the Euler font.

### Calligraphic letters

The template also uses the [Euler font](https://ctan.math.utah.edu/ctan/tex-archive/fonts/eulervm/doc/latex/eulervm/eulervm.pdf) for calligraphic letters in math. These calligraphic letters fit well with the other fonts and are very readable. The calligraphic letters are produced with the `\mathcal{}` command.

### Blackboard-bold letters

The template uses the [Fourier font](https://mirror.mwt.me/ctan/macros/latex/contrib/mathalpha/doc/mathalpha-doc.pdf) as blackboard-bold font. It is cleaner than the default blackboard-bold font as it does not have serif. And it is slightly thicker than the default font so it matches well with Source Sans Pro and the Euler letters. The blackboard-bold letters are produced with the `\mathbb{}` command. 

### Bold characters

In the template, it is possible to bold any mathematical character (except blackboard-bold letters). This can be done using the `\bm{}` command in math. 

### Mathematical symbols

Finally, the template use the [MnSymbol font](https://ftp.yz.yamagata-u.ac.jp/pub/CTAN/fonts/mnsymbol/MnSymbol.pdf) for the symbols used in math mode. The default Computer Modern symbols are too light and thin in comparison to the Source Sans Pro and Euler letters, and as a result do not mix well with them. The advantage of the MnSymbol font is that its symbols are thicker, so they mix better with the letters. The symbols are also less curly, which gives them a more modern feel.[^1] 

[^1]: The `MnSymbol` package is incompatible with the `amssymb` package. So it is not possible to load `amssymb` with the template. Neither should it be required since `MnSymbol` provides a vast collection of symbols.

---

## Font size

The font size is 11pt. It is easily readable but not too big. It follows [Butterick's advice](https://practicaltypography.com/presentations.html) to choose a font size so as to be able to fit about 12 lines of text on one slide.

The template keeps one font size for all text. So the text is not smaller at different levels of itemized lists—which many Beamer themes impose by default but which is both distracting and clunky.

---

## Line spacing

The line spacing is 150% of the point size. This adds white space to the presentation, which helps with reading, and it limits the amount of stuff that can be written on one slide. There is a small amount of additional vertical spacing between items in lists to separate the items better. 

---

## Text margins

The information on the title slide, section titles, frame titles, and regular text are all aligned along the same left margin. (This requires various adjustments as these elements are not usually aligned in Beamer themes.) Lists are slightly indented to the right.

---

## Color scheme

[As Butterick says](https://practicaltypography.com/presentations.html), color should be used with restraint. A lot of colors, especially bright ones, is distracting. To reduce distraction, the template only uses grayscale. The text is in dark gray (85% black), not complete black, to avoid an uncomfortable degree of contrast. The list items—bullet points and numbers—are in lighter gray, to blend in the background.[^2] Colors are reserved for figures and text alerts. 

The typical, bright Beamer bullet points, headers, and footers, should be avoided as they are distracting.

[^2]: The template customizes formatting for three levels of itemized and numbered lists. More deeply nested lists should be avoided as they are a sign that the presentation's organization is too messy.

---

## No frills at the periphery

A [typical slide produced with Beamer](https://deic.uab.cat/~iblanes/beamer_gallery/large/Warsaw-default-default-17.png) might includes the following elements:

+ Outline of the talk above the title
+ Small navigation buttons in the bottom right-hand corner
+ Names of the authors and title of the talk at the bottom of the slide

Such clutter distracts listeners and takes their attention away from the main message of the slide—while conveying no useful information. The audience does not need that information in the middle of the talk. The slides produced by the template are devoid of such frills. 

In particular, the pesky navigation buttons are eliminated by placing 
`\setbeamertemplate{navigation symbols}{} ` in `presentation.sty`.

---

## Slide numbers

By default the slides are not numbered. This seems better for most presentations. Displaying slide numbers does nothing but makes the audience jittery at the thought of the sheer number of slides that remain to be covered in the talk.

But for anyone who wants to share the slide deck for comments, or who gives a presentation specifically to collect feedback, it might be helpful to have slides numbers—so the comments can be precisely linked to a slide. To introduce page numbers on slide, just uncomment the line `\setbeamertemplate{footline}[frame number]` in `presentation.sty`.

Once slide numbers are inserted at the bottom of all slides, it is possible to remove the slide number from the title slide. To do that, use `\frame[plain]{\titlepage}` instead of `\frame{\titlepage}` in `presentation.tex`. The page numbers will start appearing on the second slide.

---

## Title slide

The title slide avoids centered text and is otherwise pretty minimalist. The title is in large font (21pt), in small caps, and accentuated by a black line. Authors and dates are in slightly larger font than the text (12pt). The title slide also includes the permanent URL of the paper being presented. When the presentation is posted online, the URL allows readers to go from the presentation directly to the paper. The URL is displayed in small font (9pt) and gray so is not too obtrusive.

+ To specify the presentation authors, use the command `\information{First Author, Second Author}`. 
+ To add the location of the presentation or a date to the title page, add a second argument to the command:  `\information{First Author, Second Author}{Location -- Date}`.
+ The command takes an optional argument to specify the paper URL: `\information[URL]{First Author, Second Author}{Location -- Date}`. 

---

## Slide headline

The headline is in somewhat larger font than the text (14pt), in small caps, and aligned left. This follows [Butterick's recommendation](https://practicaltypography.com/presentations.html) to avoid centered headlines. The headline stands out, is easily readable, but does not take all the attention away from the text. 

The headline is set against the same white background as the text—not against a bright color background. This choice makes the headline easier to read and less distracting.

---

## Alerts

The template comes with a set of predefined alert commands:

+ Standard alert:
    + `\al{text}` colors the text in magenta.
    + `\al[n]{text}` colors the text in magenta on nth click.
+ Green alerts (for instance to indicate a positive number):
    + `\alg{text}` colors the text in green.
    + `\alg[n]{text}` colors the text in green on nth click.
+ Red alerts (for instance to indicate a negative number):
    + `\alr{text}` colors the text in red.
    + `\alr[n]{text}` colors the text in red on nth click.
+ Blue alerts (for instance to indicate a zero):
    + `\alb{text}` colors the text in blue.
    + `\alb[n]{text}` colors the text in blue on nth click.

The standard alert is set in magenta, which is a color that stands out but unlike red does not induce anger. [Apparently](https://www.canva.com/colors/color-meanings/magenta/):

> A color that, for centuries, has captivated many, magenta is a mixture of violet and red. Magenta is known as a color of harmony and balance. It's used in Feng Shui and is often considered spiritual.

Of course alerts should be used with restraint.

---

## Theorems and other results

As is standard, the text of theorems is in italic—providing subtle emphasis. The theorem label is in semibold—again providing subtle emphasis. To further emphasize theorems and clearly separate them from surrounding text, the template places theorems in a light gray rectangle with rounded corners.

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

An advantage of avoiding colors in the text is that colors in figures stand out. 

The template uses a white background for slides because figures have white backgrounds. Figures therefore seamlessly blend into the slide. With a colorful slide background, the figures background would stick out.

Figures are centered by default. 

The template is designed so the slide headline is used to caption the figure. It is not designed to accommodate a separate caption below the figure.

An easy way to insert figures into the template is to create a PDF file with all the figures that are featured in the presentation. To do that, create a Keynote or Powerpoint presentation; insert each figure as a slide background; and save the resulting presentation as PDF. With this method, all the figures have the exact same size. It is also possible to use Keynote or Powerpoint to annotate the figures created with an external software (Matlab, R, Python). The file `figures.pdf` in the repository was created from MATLAB graphs by this method.

The code for a slide with a basic figure is the following:

```tex
\begin{frame}
\frametitle{Figure caption}
\includegraphics[scale=0.3]{figure.pdf}
\end{frame}
```

The code for a slide with multiple figures displayed sequentially is the following:

```tex
\begin{frame}
\frametitle{Figure caption}
\includegraphics<1>[scale=0.3,page=1]{figures.pdf}%
\includegraphics<2>[scale=0.3,page=2]{figures.pdf}%
\includegraphics<3>[scale=0.3,page=3]{figures.pdf}%
\includegraphics<4>[scale=0.3,page=4]{figures.pdf}%
\end{frame}
```

---

## Tables

People sometimes copy-paste tables from their papers into their slides. That's not a good idea since it is not possible to read large tables with tiny numbers on slides. It seems more effective to keep the same font size in tables as in the text, and just present in the slide tables the key numbers from the paper tables. If listeners want more details, they will go to the paper.

Tables are centered by default, and fill the slide.

Here too, the template is designed so the slide headline is used to caption the table. It is not designed to accommodate a separate caption below the table.

The code for a slide with a basic table is the following:

```tex
\begin{frame}
\frametitle{Table caption}
\begin{tabular*}{\textwidth}{@{\extracolsep\fill}lccc}
\toprule
 & Column 1 & Column 2 & Column 3\\
\midrule
Line 1 & A  & B & C \\
Line 2 & D & E & F \\ 
Line 3 & G & H & I \\ 
\midrule
Line 4 & J & K & L \\ 
Line 5 & M & N & O \\ 
\bottomrule
\end{tabular*}
\end{frame}
```

---

## Section slide

The template has a command to divide the presentation into sections, which adds structure to longer talks. To produces the section slide, just use the following code:

```tex
\begin{frame}
\heading{Section title}
\end{frame}
```

The text on the section slide is in small caps, and with moderately large font (17pt).

This section slide is a good point to stop, recap what has already been showed, and discuss what comes ahead. It is also a good point to take questions.

---

## Pictograms

The template comes with a set of shortcuts to display common pictograms in text mode:

+ `\then` gives $\rightsquigarrow$
+ `\so` gives $\Rightarrow$
+ `\up` gives ↑
+ `\down` gives ↓
+ `\flat` gives →

---

## Navigation buttons

The template comes with navigation buttons. The buttons have white background, just like the slides. The button text is in light gray and small font (9pt). The buttons blend in the slides, unlike the typical, bright Beamer buttons that stand out and distract from the rest of the content.

Navigation buttons should be used with restraint as hopping from slide to slide with buttons disrupts the flow of the presentation. But buttons are sometimes helpful to go to key backup material.

Here is how to point a button to a specific slide:

+ Add a label at the top of the specific slide: `\begin{frame}[label=specificSlide]`.
+ Create a button in another slide that points to the labelled slide: `\hyperlink{specificSlide}{\beamergotobutton{Go to specific slide}}`.

---

## Slide breaks

Each slide should be prepared and planned carefully. There should be a reason why material is on a certain slide rather than on another slide. Nevertheless, sometimes, a slide contains too much material to fit on one slide, and it does not matter too much how the material is split across successive slides. One example is a slide with a long list of references. Another example is a slide with a long mathematical derivation. In these cases, the option `allowframebreaks` can be used to split slides automatically, using the following code:

```tex
\begin{frame}[allowframebreaks]
\frametitle{Slide title}
Long list of references or long derivation.
\end{frame}
``` 

Each successive slide is automatically numbered with an Arabic number in square brackets: [1], [2], [3], and so on. As the [Beamer user guide](https://tug.ctan.org/macros/latex/contrib/beamer/doc/beameruserguide.pdf) notes, however, the `allowframebreaks` option invites the creation of endless presentations that resemble more a paper projected on the wall than a presentation. So the option should only be used sporadically, in the specific cases mentioned above.

---

## Last slide

The template also come with a last slide, which is a just a gray square, and which is called with the command `\lastslide`. The last slide can be used instead of conclusion slides—to say thank you, to recap what the presentation showed, and to discuss next steps or related projects.

Conclusion slides are generally ineffective and even mildly upsetting. The audience has been listening for an hour or an hour and a half. They know what they have just been told. At that point they are happy to go on with their day without having to hear again a summary of the same material.