---
title: "Minimalist Hugo Template for Academic Websites" 
date: 2025-05-11
url: /b/
aliases: 
    - /d5/
author: "Pascal Michaillat"
description: "This template produces a personal academic website with Hugo. The website has a minimalist design and is hosted on GitHub Pages."
summary: "This template produces a personal academic website with Hugo. The website has a minimalist design based on the PaperMod theme and is hosted on GitHub Pages." 
cover:
    image: "/b.png"
    alt: "Webpage produced with template"
editPost:
    URL: "https://github.com/pmichaillat/hugo-website"
    Text: "GitHub repository"
showToc: true
disableAnchoredHeadings: false

---

The template produces a personal website with [Hugo](https://gohugo.io), which is a very fast, open-source static website generator. The website design is based on [PaperMod](https://github.com/adityatelange/hugo-PaperMod), which is a minimalist, fast, and flexible Hugo theme. Finally, the website is hosted on [GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages); but it could easily be hosted on other services.

The design has been customized for academic websites. The first goal was to obtain a minimalist website that is easy to navigate. The second goal was to obtain a website that highlights the research and teaching material. The third goal was to have a website that performs well (fast to load, good SEO, good accessibility). The website [performs very well](https://github.com/pmichaillat/hugo-website#performance) on mobile and desktop devices—just like the original PaperMod theme. The final goal was to design a website that is easy to maintain and expand.

---

## View

+ [Hugo template for academic websites](https://github.com/pmichaillat/hugo-website)
+ [Website produced by the template](https://pascalmichaillat.org/hugo-website/)

---

## Key features

+ Webpages are organized in several sections, which are available from any page through the menu and from the homepage through buttons: papers, courses, data, and so on.
+ The template accepts LaTeX expressions to typeset math on all webpages.
+ The template provides social icons specific to academia: CV, email address, office location, office hours, Zoom room, GitHub profile, Substack profile, Google Scholar profile, Bluesky and Twitter accounts, and so on.
+ An archive page is automatically generated so visitors can easily see the most recent material added to the website.
+ A list of keywords used in papers and courses is automatically generated so visitors can easily see the topics covered in research and teaching.
+ The metadata for webpages, which appear below the webpage title, are tailored to the academic context.
+ Color scheme, font, spacing, and general appearance are streamlined and as minimalist as possible.
+ Tables, code blocks, quote blocks, itemized and numbered lists are formatted to fit seamlessly with the rest of the website.

---

## Installation

### On your local machine

+ Since the website is hosted on GitHub Pages, it is convenient to install [GitHub Desktop](https://desktop.github.com) first. Via GitHub Desktop, you will be able to install the website on your local machine and update the website from your local machine—without ever going to GitHub.
+ Next, install [Hugo](https://gohugo.io/installation/). On a Mac, this is easily done with [Homebrew](https://brew.sh). Simply run the following command in the terminal: `brew install hugo`.
+ If you already have Hugo on your machine, make sure to install the latest version. You can verify the installed version with: `hugo version`. To update Hugo if it is outdated on your local machine, run: `brew upgrade hugo`. 
+ Then, clone the template repository to your local machine. This can be done in two steps:
  1. Click "Use this template" and then "Create a new repository" at the top of the repository [on GitHub](https://github.com/pmichaillat/hugo-website).
  2. Once the new repository is created on your GitHub account, open GitHub Desktop and click "File" and then "Clone repository". Find the newly created repository under the "GitHub.com" tab and clone it.
+ Update the `baseURL` parameter in `config.yml` with the website URL that you plan to use.

### On your GitHub account

+ The first time that you push your repository to GitHub, you need to allow GitHub Actions and GitHub Pages so the website can be built and deployed to GitHub Pages.
+ The first step is to ask GitHub to [publish the website](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#publishing-with-a-custom-github-actions-workflow) with a GitHub Actions workflow.  GitHub offers a ready-made workflow to publish a Hugo website, called `Deploy Hugo site to Pages`. This workflow must be enabled in the [Pages Settings](https://github.com/pmichaillat/hugo-website/settings/pages) of your GitHub repository. You can view the workflow in the `.github/workflows/hugo.yml` file.
+ Once GitHub Actions are enabled, GitHub will build and publish the website as soon as the repository is updated. 
+ If you would like to update the GitHub Actions workflow (for instance because it became outdated and fails to deploy the site), you can find the [most recent workflow on GitHub]( https://github.com/actions/starter-workflows/blob/main/pages/hugo.yml). You can place this file directly in the `.github/workflows` folder to replace the old `hugo.yml` file.

---

## Usage

### Local development

To check that everything works and to slowly develop your website, start by rebuilding the website locally. In the terminal, navigate to the website directory via `cd` and run:

```console
hugo server
```

The command builds the website with Hugo and starts a local web server. The website is available at [http://localhost:1313](http://localhost:1313) in any web browser. 

Hugo automatically rebuilds the site and refreshes the webpage in the browser as you change the content and template files in the repository. This allows you to see changes instantly as you are developing the website. 


### Online deployment

Once your website is ready to be made public, commit the changes to the content and template files and push them to your GitHub repository via GitHub Desktop. 

Then, the GitHub Actions workflow will build the website with Hugo and deploy it to GitHub Pages. The workflow used by GitHub Actions is in the `hugo.yml` file stored in the `.github/workflows` folder. 

It usually takes a few minutes for the website to be deployed and go live. Using Hugo, the workflow will convert content files into HTML pages, handles static assets, generates URLs and organizes pages, and finally create a static website. 

The current version of the website is built with Hugo v0.147.2 via GitHub Actions.

---

## Configuration file

The `config.yml` file contains all the parameters to configure the website. Upon cloning the source code to your local machine, make sure to update them and add any additional parameter that you would like to customize. Such parameters include:

+ `baseURL` - The website URL
+ `title` - Your name, to be used as title of the website
+ `params:author` - Your name, to be used in HTML meta tags to specify the author of the webpage's content (this only adds a meta tag to the header of the homepage, it doesn't have any direct impact on the appearance or functionality of the webpage itself)
+ `params:description` - A short description (less than 155 characters) of who you are, to be used in HTML meta tags to specify the content of the webpage (this description often appears in search engine results below the title of the webpage)
+ `params:googleAnalyticsID` - The website's Google Analytics ID (the website supports Google Analytics 4)
+ `params:profileMode:title` - Your name, to be used as title on the homepage
+ `params:profileMode:subtitle` - A description of who you are, to be used as a subtitle on the homepage
+ `params:profileMode:imageTitle` - Your name, to be used as tag for your profile picture
+ `params:socialIcons` - The URLs to your [social accounts and contact information](#social-icons)
+ `cover:hiddenInList` - Set to `true` to hide cover images in paper, course, and data lists
+ `pagination: pagerSize:` - The maximum number of entries to show on each list page

---

## Content files

The `content` folder contains all the content files for the website. These files are written in [Markdown](https://www.markdownguide.org), a simple markup language designed to make writing on the web fast and easy. Each file corresponds to one page of the website. 

Most of the files organized in four sections, which are available from any page through the navigation menu and from the homepage through buttons:

+ [Papers](https://pascalmichaillat.org/hugo-website/papers/) - Published and unpublished research papers, stored in the `papers` subfolder
+ [Courses](https://pascalmichaillat.org/hugo-website/courses/) - Undergraduate and graduate courses, stored in the `courses` subfolder
+ [Data](https://pascalmichaillat.org/hugo-website/data/) - Data projects, stored in the `data` subfolder
+ [Books](https://pascalmichaillat.org/hugo-website/books/) - Books, stored in the `books` subfolder

The section pages include a list of the items in the section (books, papers, courses, data), with links to individual items. These lists are updated automatically as content files are added, deleted, or modified in the specific subfolders.

### New items

To add a new paper to the website, for instance, add a file `new_paper.md` into the `papers` subfolder. That new paper will automatically be listed on the [page with the other papers](https://pascalmichaillat.org/hugo-website/papers/). It is convenient to [use archetypes](#archetypes) to generate new files easily. 

By default, the URL of the new paper would be `baseURL/papers/new_paper/`. But the URL can be customized in the `new_paper.md` file with the `url` parameter. For instance, with `url: /paperx/`, the URL of the new paper is simplified to `baseURL/paperx/`.

### New sections

It is also easy to add new sections to the website, for instance to list software, blog entries, and so on. To add a list of software, create a new `software` subfolder into the `content` folder. Then add a content file such as `new_software.md` into the `software` subfolder. That new section will be available at `baseURL/software/`. 

You can for instance link to it with a button from the homepage. To do that, simply add the following snippet into the `config.yml` file, below `profileMode:buttons`:

```yml
- name: Software
  url: software/
```
You can also add a link to the new section in the menu bar. To do that, simply add the following snippet into the `config.yml` file, below `menu:main`:

```yml
- name: Software
  url: software/
  weight: 4
```

### Other content files

The `content` folder contains a few additional files, which are not part of sections.

+ `location.md` - Mailing and office addresses, including a map of the university
+ `officehours.md` - Schedule and location for office hours

It is possible to add any number of files in the `content` folder. By default, any `new_file.md` file will be available at `baseURL/new_file/`.

---

## Static files

The `static` folder contains the static files (files not processed or rendered by Hugo) for the website. The `static` folder contains a few files used in the homepage:

+ `picture.jpeg` - Picture appearing on the homepage.
+ `cv.pdf` - Curriculum vitae linked to the [CV icon](#social-icons) on the homepage. This CV is built from the [latex-cv](https://github.com/pmichaillat/latex-cv) template.
+ `favicon.io`, `favicon-32x32.png`, `favicon-16x16.png`, `apple-touch-icon.png` - Favicon appearing in the menu bar next to the website title, and in the browser next to the URL. It is easy to produce [new favicons](https://favicon.io).

The `static` folder could also include the PDF files and images to which the website links. It could contain:

+ Papers and online appendices in PDF format
+ Presentations in PDF format
+ Lecture notes in PDF format
+ Figures from the papers in PNG format

This is for instance how I organized the static files [on my website](https://github.com/pmichaillat/pmichaillat.github.io). But in the template, to be more flexible and portable, these files are located directly in the folder for the individual page where they are used: `content/papers/paper1/`, `content/papers/paper2/`, `content/courses/course1/`, and so on.

---

## Keywords

A list of all the [keywords (tags)](https://pascalmichaillat.org/hugo-website/tags/) used in papers and courses is automatically generated and added to the website. The tag list is accessible from the homepage. The list can also be added to the menu bar. To do that, simply add the following snippet into the `config.yml` file, below `menu:main`:

```yml
- name: Keywords
  url: tags/
  weight: 5
```

Specific tags can be added to any webpage with the `tags` parameter. Such tags appear at the bottom of the page in small gray buttons. 

The tag list is generated by default, but it can be customized through the file `_index.md` placed in the  `content/tags/` folder. The file defines for instance the description of the page for search engines (`description`) as well as the title of the page (`title`).

---

## Archive

The website also features [an archive](https://pascalmichaillat.org/hugo-website/archive/). The archive displays a reverse-chronological list of all papers, books, courses, and data projects. 

If you set the parameter `params:ShowAllPagesInArchive` to `false`, not all the website's pages are showed in the archive. The list of sections displayed in the archive is then controlled by the parameter `params:MainSections` in the `config.yml` file. The current value of that parameter is 

```yml
params:MainSections: ["books","courses","papers","data"]
```    

which means that the archive displays all the items from the sections `books`, `courses`, `papers`, and `data`.

The archive is accessible from the homepage. Add the following snippet below `menu:main:` in the `config.yml` file to make the archive available from the menu: 

```yml
- name: Archive  
  url: archive/  
  weight: 7
```

The archive is available at `baseURL/archive/`.

---

## Social icons

The template includes various social icons that are commonly used in academia. All the icons are defined in the file `layouts/partials/svg.html`; additional icons can be added there. To place any icon on the homepage, the icon type and icon url should be specified below `params:socialIcons:` in `config.yml`.

For instance, if your CV is called `cv.pdf` and placed in the `static` folder, an icon linking to your CV can be added as follows:

```yml
- name: CV
  url: cv.pdf
```
If your office hours are listed on the page `officehours.md` in the `content` folder, an icon linking to your office hours can be added as follows:

```yml
- name: Office Hours
  url: officehours/
```

If your office address is listed on the page `location.md` in the `content` folder, an icon linking to your address can be added as follows:

```yml
- name: Location
  url: location/
```

If your Zoom room is located at `https://www.zoom.us/my/user`, it is possible to link to it by adding the following snippet:

```yml
- name: Zoom
  url: https://www.zoom.us/my/user
```

If your Google Scholar profile is located at `https://scholar.google.com/citations?user=user`, link to it by adding the following snippet:

```yml
- name: Google Scholar
  url: https://scholar.google.com/citations?user=user
```

Similarly, if your GitHub profile is located at `https://github.com/user`, link to it by adding the following snippet:

```yml
- name: GitHub
  url: https://github.com/user
```

If your email is `user@gmail.com`, you can link to it by adding the following snippet:

```yml
- name: Email
  url: mailto:user@gmail.com
```

Finally, if you have a Bluesky account `@user.bsky.social`, you can link to it by adding the following snippet:

```yml
- name: Bluesky
  url: https://bsky.app/profile/user.bsky.social
```

---

## Typesetting math

It is easy to typeset math on any website page. Simply enter LaTeX commands into the Markdown file, and the commands will be rendered synchronously with [KaTeX](https://katex.org). For instance:

+ `$x\in \mathbb{N}$` gives $x\in \mathbb{N}$
+ `$\xi^\ast = 4 + \max f(x)$` gives $\xi^\ast = 4 + \max f(x)$
+ `$\ln(\theta+\mathcal{Y}) = \int x^2 dx$` gives $\ln(\theta+\mathcal{Y}) = \int x^2dx$. 

It is also possible to display equations on any webpage. For example, `$$\lambda\exp{\frac{\beta}{\alpha^3}} = \max_{t\in\mathbb{R}}(x(t)+z(t)^2)$$` is rendered as:

$$\lambda\exp{\frac{\beta}{\alpha^3}} = \max_{t\in\mathbb{R}}(x(t)+z(t)^2).$$

---

## Color scheme

The template is mostly in grayscale. For ease of navigation, however, links are underlined in slate blue. The same blue color is used for the template's favicon, and a lighter shade of slate blue is used for hovered buttons. 

It is easy to personalize the color used for links and buttons. The color is specified in the file `assets/css/core/theme-vars.css`. The code snippet specifying the color is:

```css
--darkcolor: #6a7ba2;
--lightcolor: #cbd1de;
```

The two shades of blue are specified by their hex code. Enter [other hex codes](https://www.colorhexa.com/) to modify your website's color scheme. Use the same hex codes to produce [a new favicon](https://favicon.io/favicon-generator/) with a different color to match your website's color scheme.

---

## Cover images

Cover images can be specified for all pages. The cover image will appear in lists on the website. It will also appear if a link to the page is used on social media. 

Let's look at the page for the first paper on the website, "Unusual Uses For Olive Oil".
A cover image for the page is specified at the top of the `index.md` file in the `content/papers/paper1/` folder: 

```yml
cover:
    image: "paper1.png"
    alt: "Some Uses For Olive Oil"
    relative: true
 ``` 

The cover image is `paper1.png`, found in the same folder as the `index.md` file. The image is in PNG format, which is the recommended format for cover images.

Cover images should be 1280 x 720 pixels. This size ensures that the cover image has a 16:9 aspect ratio (recommended for most social media), have a good resolution, while not being too large (100–300 KB is recommended). The image should also have some white padding around, to prevent important material from being cropped out.

To produce good cover images, [Image Magick](https://imagemagick.org) is a great software. It is free and open source and can be obtained on a Mac with Homebrew: `brew install imagemagick`. Once you have installed Image Magick, you can transform any image in PNG format to a cover image of the appropriate size with some padding:

```console
magick image.png -resize 1200x675 -gravity center -background white -extent 1280x720 image.png
```

---

## Redirects

It is easy to handle redirects on a Hugo website by using the `aliases` parameter within the page front matter. This feature allows you to define old URLs that should redirect to a new page. This is particularly useful when you change the URL structure or move content around in your website, and you want to ensure that visitors are redirected from the old URLs to the new one. This ensures that visitors using the old URLs still find the right content.

The template includes an example showing how to set up redirects using the `aliases` parameter. The redirects are set up in the `/courses/course1/index.md` file. In the preamble, the following snippet of code sets up redirects from old PDF files to the current course page:

```yml
aliases: 
    - /courses/course2/slides4.pdf
    - /courses/course2/slides1.pdf
    - /courses/course2/slides3.pdf
    - /courses/course2/slides2.pdf
    - /courses/course2/notes3.pdf
```

Hugo will then automatically generate the necessary redirect HTML pages during the build process. These HTML pages will be stored in the `public` folder. When a visitor navigates to any of the URLs listed in the aliases (such as `baseURL/courses/course2/slides4.pdf`), they will be redirected to the page where the alias is defined (`baseURL/courses/course1/`). 

This method is useful to manage redirects and ensure a seamless user experience when restructuring any part of your website. It is also useful to handle 404 issues since outdated links will automatically point to the correct content, preventing users from landing on the [404 error page](https://pascalmichaillat.org/hugo-website/404/).

--- 

## Testing the website on mobile devices

During development, it is possible to test your website on mobile devices—to check that everything is accessible and readable. Testing only requires to adjust the `hugo` command slightly.

+ Make sure that your laptop and phone are on the same wifi network, and get your laptop's IP address (say 192.168.1.50). This can be done by running `ipconfig getifaddr en0` in the terminal.
+ Once you have the IP address, run `hugo server --bind 0.0.0.0 --baseURL http://192.168.1.50:1313`.
+ On your phone's browser, go to `http://192.168.1.50:1313`.
+ This gives a true mobile rendering and is useful for final testing. As you modify the website source code on your computer, the modified website appears on your phone.


---

## Footer

The website has a footer, which contains a copyright notice and a "Powered by" notice. The footer can be customized by modifying the file `layouts/partials/footer.html`. It is possible to hide the footer by setting the parameter `hideFooter` to `true` in the `config.yml` file. 

---

## RSS feeds

In the background, Hugo automatically generates RSS feeds in XML format for your site. These feeds enable interested readers to subscribe to your content and be updated whenever you publish new content. The RSS feeds can be found in the `public` folder, and are typically available at `/index.xml` under the appropriate section.

For instance, on this website, the RSS feed for my research papers can be found at `https://pascalmichaillat.org/papers/index.xml`. The RSS feed for my design projects can be found at `https://pascalmichaillat.org/design/index.xml`. Hugo also produces RSS feeds for all keywords. On this website, the RSS feed for the keyword `business cycles` can be found at `https://pascalmichaillat.org/tags/business-cycles/index.xml`. 

The XML files can then be submitted to RSS readers, such as the [RSS app](https://rss.app), to [produce RSS feeds](https://rss.app/overview-feed-xml?feedId=44ZDQRZnqIktQJrt&feedXmlId=UaViYplhbFwE97Bd).

---

## Search

A search page can also be added to the website. To add a search  page, move the `search.md` file from the `archetypes` folder into the `content` folder. Then, add the following snippet at the end of the `config.yml` file so that search works properly:

```yml
outputs:
     home:
         - HTML
         - RSS
         - JSON
```

Finally, add the following snippet below `menu:main:` in the `config.yml` file to make the search page available from the menu:

```yml
- name: Search  
  url: search/  
  weight: 6
```

The search page will be available at `baseURL/search/`.

---

## Archetypes

The template comes with archetypes, stored in the `archetypes` folder. In Hugo, an archetype is a predefined content template that serves as a blueprint for creating new pages. Archetypes help streamline content creation by providing a consistent starting point with predefined metadata and content structure. There is an archetype for paper pages (`paper.md`) and an archetype for course pages (`course.md`).

To create a new webpage from an archetype, simply use the `hugo new` command in the terminal from the website directory. For example, to create a page for a new course, you can run:

```console
hugo new content/courses/my-new-teaching-material.md --kind course
```

Hugo will generate a new content file called `my-new-teaching-material.md` and place it the directory `content/courses/`, where all the courses are stored. Furthermore, Hugo will use the archetype `course.md`. Then, you can edit the content of the page by modifying the newly created file `my-new-teaching-material.md`. 

Similarly, to create a page for a new paper, you can run:

```console
hugo new content/papers/my-new-research-material.md --kind paper
```

Hugo will generate a new content file called `my-new-research-material.md` and place it the directory `content/papers/`, where all the papers are stored. Furthermore, Hugo will use the archetype `paper.md`.

---

## Public folder

In your local website repository, you will find a `public` folder. The folder is created when you run `hugo server` or `hugo`. The `hugo` commands process your content, templates, and other project files, and create a fully generated static website files that is ready to be deployed locally or online. The resulting output is placed in the `public` folder by default.

The `public` folder is not sent to the GitHub repository because it is not needed there (it is in the `.gitignore` file). During the GitHub Actions workflow, a fresh `public` folder is generated at build time by Hugo. That folder is then used ephemerally in the GitHub Actions runner. As a result, there is no `public` folder at all in the GitHub repository.

---

## Domain name

It is easy to use a custom domain name for the website. For instance, the domain name `https://pascalmichaillat.org/` is registered with [Squarespace](https://domains.squarespace.com). Once you have registered a domain, you need to [link it](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages) to your website. Make sure that the `baseURL` parameter in `config.yml` reflects the custom domain name. Make sure that the [page setting](https://github.com/pmichaillat/hugo-website/settings/pages) on GitHub also includes the domain name.

---

## Tips for job-market candidates

This template is designed for researchers at all levels, including students, postdocs, faculty members, and professional scientists. When preparing your website for the job market, it might make sense to adapt the website slightly. 

### Job-market status

To announce your job-market status, you can modify the subtitle on the landing page. You could for instance add 

```markdown
**In 2024/2025, I will be on the academic job market.**
```

to the text under `params:profileMode:subtitle` in the `config.yml` file.

You could also add more information, such as who your references are, how to contact them, which job-market meetings you will attend, and so on.

### Job-market paper and CV

I would also advise to place prominent links to your CV and job-market paper on the landing page. This can be easily achieved by adding the following code snippet below `profileMode:buttons:` in the `config.yml` file:

```yml
- name: Job-market paper
  url: jmp.pdf
- name: Curriculum vitae
  url: cv.pdf
```

This code snippet will add buttons for your job-market paper (`jmp.pdf`) and CV (`cv.pdf`) below the social icons on the homepage. The files `cv.pdf` and `jmp.pdf` must be placed in the `static` folder.