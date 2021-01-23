---
title: (정리) LaTex
layout: post 
---

### About this doc 

- 이번장에서는 레이텍에 관련된 셋팅을 다룬다. 

- 쿡북형태 

--- 

### LaTex 
```
\documentclass[12pt,oneside,english]{book}
\usepackage{babel}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{color}
\definecolor{marron}{RGB}{60,30,10}
\definecolor{darkblue}{RGB}{0,0,80}
\definecolor{lightblue}{RGB}{80,80,80}
\definecolor{darkgreen}{RGB}{0,80,0}
\definecolor{darkgray}{RGB}{0,80,0}
\definecolor{darkred}{RGB}{80,0,0}
\definecolor{shadecolor}{rgb}{0.97,0.97,0.97}
\usepackage[demo]{graphicx}
\usepackage{wallpaper}
\usepackage{wrapfig,booktabs}

\usepackage{fancyhdr}
\usepackage{lettrine}
\input Acorn.fd
\newcommand*\initfamily{\usefont{U}{Acorn}{xl}{n}}

\usepackage{geometry}
\geometry{
tmargin=5cm, 
bmargin=3cm, 
lmargin=1cm, 
rmargin=1cm,
headheight=1.5cm,
headsep=0.8cm,
footskip=0.5cm}

\renewcommand{\familydefault}{pplj} 
\usepackage[
final,
stretch=10,
protrusion=true,
tracking=true,
spacing=on,
kerning=on,
expansion=true]{microtype}

%\setlength{\parskip}{1.5ex plus 0.2ex minus 0.2ex}


\usepackage{fourier-orns}
\newcommand{\dash}{\vspace{2em}\noindent \textcolor{darkgray}{\hrulefill~ \raisebox{-2.5pt}[10pt][10pt]{\leafright \decofourleft \decothreeleft  \aldineright \decotwo \floweroneleft \decoone   \floweroneright \decotwo \aldineleft\decothreeright \decofourright \leafleft} ~  \hrulefill \\ \vspace{2em}}}
\newcommand{\rdash}{\noindent \textcolor{darkgray}{ \raisebox{-1.9pt}[10pt][10pt]{\leafright} \hrulefill \raisebox{-1.9pt}[10pt][10pt]{\leafright \decofourleft \decothreeleft  \aldineright \decotwo \floweroneleft \decoone}}}
% \newcommand{\ldash}{\textcolor{darkgray}{\raisebox{-1.9pt}[10pt][10pt]{\decoone \floweroneright \decotwo \aldineleft \decothreeright \decofourright \leafleft} \hrulefill \raisebox{-1.9pt}[10pt][10pt]{\leafleft}}}


\fancyhf{}

\renewcommand{\chaptermark}[1]{\markboth{#1}{}}
\renewcommand{\sectionmark}[1]{\markright{#1}}

\newcommand{\estcab}[1]{\itshape\textcolor{marron}{\nouppercase #1}}

\fancyhead[LO]{\estcab{\rightmark}} 
\fancyhead[RO]{\estcab{\leftmark}}
\fancyhead[RO]{\bf\nouppercase{ \leftmark}}
\fancyfoot[RO]{ \leafNE  ~~ \bf \thepage}

\newenvironment{Section}[1]
{\section{\vspace{0ex}#1}}
{\vspace{12pt}\centering ------- \decofourleft\decofourright ------- \par}

\usepackage{lipsum}
\setlength{\parindent}{1em} % Sangría española
\pagestyle{fancy}

\renewcommand{\footnoterule}{\noindent\textcolor{marron}{\decosix \raisebox{2.9pt}{\line(1,0){100}} \lefthand} \vspace{.5em} }
\usepackage[hang,splitrule]{footmisc}
\addtolength{\footskip}{0.5cm}
\setlength{\footnotemargin}{0.3cm}
\setlength{\footnotesep}{0.4cm} 

\usepackage{chngcntr}
\counterwithout{figure}{chapter}
\counterwithout{table}{chapter}

\usepackage{kotex}
\usepackage{amsthm} 
\usepackage{amsmath} 
\usepackage{amsfonts}
\usepackage{enumerate} 
\usepackage{cite}
\usepackage{graphics} 
\usepackage{graphicx,lscape} 
\usepackage{subcaption}
\usepackage{algpseudocode}
\usepackage{algorithm}
\usepackage{titlesec}
\usepackage{cite, url}
\usepackage{amssymb}

\def\ck{\paragraph{\large$\bullet$}\large}
\def\goal{\paragraph{\large(목표)}\large}
\def\observe{\paragraph{\large(관찰)}\large}
\def\assume{\paragraph{\large(가정)}\large}
\def\summary{\paragraph{\large(요약)}\large}
\def\EX{\paragraph{\large(예제)}\large}
\def\guess{\paragraph{\large(추측)}\large}
\def\thus{\paragraph{\large(결론)}\large}
\def\prob{\paragraph{\large(문제)}\large}
\def\sol{\paragraph{\large(해결)}\large}
\def\dfn{\paragraph{\large(정의)}\large}
\def\thm{\paragraph{\large(정리)}\large}
\def\lem{\paragraph{\large(레마)}\large}
\def\promise{\paragraph{\large(약속)}\large}
\def\property{\paragraph{\large(특징)}\large}
\def\note{\paragraph{\large\textit{\underline{note:}}}\large}
\def\ex{\paragraph{\large\textit{example:}}\large}

\def\one{\paragraph{\large(1)}\large}
\def\two{\paragraph{\large(2)}\large}
\def\three{\paragraph{\large(3)}\large}
\def\four{\paragraph{\large(4)}\large}
\def\five{\paragraph{\large(5)}\large}
\def\six{\paragraph{\large(6)}\large}
\def\seven{\paragraph{\large(7)}\large}
\def\eight{\paragraph{\large(8)}\large}
\def\nine{\paragraph{\large(9)}\large}
\def\ten{\paragraph{\large(10)}\large}

\newcommand{\bld}[1]{\mbox{\boldmath $#1$}}

\DeclareMathOperator*{\argmin}{arg\,min} 
\DeclareMathOperator*{\argmax}{arg\,max} 

\usepackage{titlesec}
\titleformat*{\section}{\LARGE\bfseries}
\titleformat*{\subsection}{\Large\bfseries}
\titleformat*{\subsubsection}{\large\bfseries}
\titleformat*{\paragraph}{\large\bfseries}
\titleformat*{\subparagraph}{\large\bfseries}

\begin{document}
\title{Title}
\maketitle
\chapter{chap}
\section{sec}
\begin{thebibliography}{9} 
\bibitem{Choi2018} Choi, G., Oh, H. S., \& Kim, D. (2018). Enhancement of variational mode decomposition with missing values. Signal Processing, 142, 75-86.
\end{thebibliography}
\end{document}
```

### LaTex in R markdown 

```
---
title: "title"
author: "최규빈"
date: "12/31/2020"
header-includes:
- \usepackage{kotex}
- \usepackage{caption}
- \usepackage{amsthm} 
- \usepackage{amsmath, amsfonts, amssymb} 
- \usepackage{enumerate} 
- \usepackage{cite}
- \usepackage{algpseudocode}
- \usepackage{algorithm}
- \usepackage{indentfirst}
- \usepackage{bm}
- \DeclareMathOperator*{\argmin}{arg\,min}
- \DeclareMathOperator*{\argmax}{arg\,max}
- \usepackage{booktabs}
- \usepackage{animate}
- \usepackage{algpseudocode}
- \usepackage{algorithm}
- \usepackage{amsthm}
- \usepackage{graphicx,lscape}
- \usepackage{subcaption}
- \usepackage{xcolor}
- \linespread{2}
fontsize: 15pt
output: pdf_document
---
```