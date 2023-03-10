\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{protokoll}[2020/10/28 Do not fail if gruppe not defined.]

\DeclareOption{twoside}{\PassOptionsToClass{twoside}{scrartcl}}

\DeclareOption*{\PackageError{protokoll}{Invalid option "\CurrentOption"}{Option "\CurrentOption" not recognized!}}

\ProcessOptions \relax

\LoadClass[12pt,a4paper]{scrartcl}

\RequirePackage[a4paper,inner=2.8cm,outer=3.5cm,top=1cm,bottom=1.2cm,includeheadfoot]{geometry}

\RequirePackage[T1]{fontenc}
\RequirePackage[utf8]{inputenc} 
\RequirePackage[ngerman]{babel}
\RequirePackage{graphicx}
\RequirePackage{icomma}
\RequirePackage{setspace}
\RequirePackage{hyperref}
\RequirePackage{siunitx}
\RequirePackage{helvet}
\RequirePackage{fancyhdr}
\RequirePackage{amssymb}
\RequirePackage{enumitem}
\RequirePackage{ifthen}

\newlist{checklist}{itemize}{1}
\setlist[checklist]{label=$\square$}

\renewcommand{\familydefault}{\sfdefault}

\pagenumbering{arabic}

\sisetup{separate-uncertainty}
\sisetup{locale=DE}

\setlength{\parindent}{0pt}
\setcapindent{0em}

\setcounter{secnumdepth}{0}

\newcommand{\versuchsgebiet}[1]{
  \newcommand{\@versuchsgebiet}{#1}
}

\newcommand{\gruppe}[1]{
  \newcommand{\@gruppe}{#1}
}

\newcommand{\@teilnehmer}{}
\newcommand{\@teilnehmerkurz}{}

\newcommand{\teilnehmer}[1]{
  \g@addto@macro\@teilnehmer{{\raggedright{}#1 \newline}}
  \g@addto@macro\@teilnehmerkurz{{#1 }}
}

\newcommand{\mitarbeit}[1]{
  \newcommand{\@mitarbeit}{#1}
}

\newcommand{\praktikum}[1]{
  \newcommand{\@praktikum}{#1}
}

\newenvironment{versuchsziele}{
  \addvspace{15mm}
  {\Large\textbf{Versuchsziele}}\par\nobreak\smallskip
}
{
  \par\bigskip
%  \pagebreak
%  \clearpage
}

\newcounter{aufgabe}[section]
\newenvironment{aufgabe}[1]{
  \refstepcounter{aufgabe}
  \addvspace{10mm}
  \noindent {\large\textbf{Aufgabe~\theaufgabe}
    \hspace{2mm} #1}\par\nobreak\smallskip
  \begin{itshape}
    \begin{small}
}
{
  \end{small}
\end{itshape}\medskip
}

\pagestyle{fancy}
\fancyhead{}
\fancyhead[LO,RE]{\@versuchsgebiet}
\fancyhead[LE,RO]{\@teilnehmerkurz}
\fancyfoot{}
\fancyfoot[LE,RO]{\thepage}

\hyphenation{Trig-ger-be-din-gung-en}

\AtBeginDocument{
  \thispagestyle{empty}

  {\raggedright{\huge\textbf{Physikalisches Grundpraktikum \@praktikum}}} \newline

   \begin{center}
    \begin{large}
      \textbf{Versuchsprotokoll: \@versuchsgebiet}\linebreak
    \end{large}
    \vspace{2mm}\newline
    \today
  \end{center}
  \vspace{5mm}


  \textbf{\@teilnehmer}
  \ifthenelse{\isundefined{\@mitarbeit}}{}{{\raggedright{}(\@mitarbeit)}\newline}\par
  \ifthenelse{\isundefined{\@gruppe}}{}{{\raggedright{}Gruppe \@gruppe}}
  \par\bigskip

  \renewcommand{\contentsname}{Versuchsliste}
  \tableofcontents
}

