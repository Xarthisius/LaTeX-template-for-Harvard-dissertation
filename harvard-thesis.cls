% -------------------------------------------------------------------
%  @LaTeX-class-file{
%     filename        = "harvard-thesis.cls",
%     version         = "0.4",
%     date            = "4 April 2012",
%     codetable       = "ISO/ASCII",
%     keywords        = "LaTeX, harvard-thesis",
%     supported       = "send email to suchow@fas.harvard.edu",
%     docstring       = "A thesis class for a Harvard dissertation."
% --------------------------------------------------------------------

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{harvard-thesis}[2012/04/05 v0.4 Harvard University Thesis Class]
\LoadClass[12pt, oneside, a4paper]{book}


% Required packages
\RequirePackage{graphicx}
\RequirePackage{hyperref}
\hypersetup{
	linktocpage,
    colorlinks,
    citecolor=Crimson,
    filecolor=black,
    linkcolor=black,
    urlcolor=Crimson,
}

\RequirePackage[centertags]{amsmath}
\RequirePackage{amssymb}
\RequirePackage[numbers, comma, sort&compress]{natbib}
\RequirePackage[small, md, sc]{titlesec}
\RequirePackage[tight,nice]{units}
\RequirePackage{verbatim}

% colors
\RequirePackage{color}
\definecolor{Crimson}{rgb}{0.6471, 0.1098, 0.1882}

\RequirePackage{url}
\RequirePackage[titles]{tocloft}
\setcounter{tocdepth}{2}
\renewcommand{\cftchapfont}{\normalsize \scshape}

\renewcommand\bibname{Literatura}
\renewcommand\listfigurename{Spis rysunków}
%\raggedright

\RequirePackage{pdfsync} %do pdf synchronization [andy]

%\usepackage[closeFloats, noSeparatorLine]{fltpage} %use the custom modified fltpage package
\RequirePackage{afterpage}








\synctex=1 % turn synctex on automatically to sync between pdf viewer [andy]

%   list an entire bibliography entry inline. Useful for acknowledging when my paper was previously published
\RequirePackage{bibentry}
\nobibliography*

\RequirePackage{lettrine} % big letter at start of chapter
\RequirePackage[a4paper]{geometry}

\RequirePackage{fancyhdr}
\pagestyle{plain} % options: empty , plain , fancy
\RequirePackage[palatino]{quotchap}
\definecolor{chaptergrey}{rgb}{0.6,0,0}
\RequirePackage{titling}
\RequirePackage{setspace}
\RequirePackage{booktabs} % for much better looking tables
\RequirePackage[labelfont={sf,bf,small},textfont={sf,small},justification=RaggedRight,margin=0pt, figurewithin=section, tablewithin=section]{caption}
\onehalfspacing
\addtolength{\footnotesep}{\footnotesep}

%\raggedright

\parindent 12pt
\RequirePackage{mathspec}

% use Arno Pro instead of standard LaTeX fonts
\setmathsfont(Digits,Latin,Greek)[Numbers={OldStyle,Proportional}]{Arno Pro}
\setmathrm{Arno Pro}

\RequirePackage{fontspec,xltxtra,xunicode}
\defaultfontfeatures{Mapping=tex-text, Numbers=OldStyle}
\setromanfont[Mapping=tex-text,
			  Numbers=OldStyle,
			  Ligatures={Common},
			  SizeFeatures={%
		          {Size={-10}, Font=* Caption},
		          {Size={10-13.0}, Font=*},
		          {Size={13.01-19.9}, Font=* Subhead, Ligatures=Rare},
		       {Size={19.91-},Font=* Display, Ligatures=Rare}}]
			  {Arno Pro} %

%Set fonts for Mac Specific (Comment out on Windows XP)
%\setsansfont[Scale=MatchLowercase,Mapping=tex-text]{Helvetica Neue}
%\setmonofont[Scale=MatchLowercase]{Consolas}

% some definitions
\def\degreeyear#1{\gdef\@degreeyear{#1}}
\def\degreemonth#1{\gdef\@degreemonth{#1}}
\def\degree#1{\gdef\@degree{#1}}
\def\advisor#1{\gdef\@advisor{#1}}
\def\department#1{\gdef\@department{#1}}
\def\field#1{\gdef\@field{#1}}
\def\university#1{\gdef\@university{#1}}
\def\universitycity#1{\gdef\@universitycity{#1}}
\def\universitystate#1{\gdef\@universitystate{#1}}


\renewcommand{\maketitle}{
	\singlespacing
	\thispagestyle{empty}
	\vspace*{\fill} \vspace{150pt} \begin{center}
	\Huge \textcolor{Crimson}{\textit{\thetitle}} \normalsize \\ \sc \vspace{100pt}
	rozprawa doktorska \\
	\theauthor\\ przedłożona\\ Radzie \@department\\
	\vspace{12pt}
	in partial fulfillment of the requirements\\
	for the degree of\\ \@degree\\
	in the subject of\\ \@field\\
	\vspace{12pt}
	\@university\\ \@universitycity \@universitystate\\
	\@degreemonth\ \@degreeyear
	\end{center} \vspace*{\fill}
}

% You might also consider licensing your work under Creative Commons). See: http://creativecommons.org/weblog/entry/12824 for other PhD students who have released their work under creative commons.

\newcommand{\copyrightpage}{
	\newpage \thispagestyle{empty} \vspace*{\fill}
	\sc \noindent \copyright~\textit{\@degreeyear \hspace{3pt}~- \theauthor} \\
	\noindent All rights reserved.
	\vspace*{\fill} \newpage \rm
}

\newcommand{\abstractpage}{
	\newpage
	\pagenumbering{roman}
	\setcounter{page}{3}
	\pagestyle{fancy}
	\lhead{Dissertation advisor: \@advisor} \rhead{\@author}
	\renewcommand{\headrulewidth}{0.0pt}
	\begin{center}
	\vspace*{1pt}
	\Large \textcolor{Crimson}{\textit{\@title}} \normalsize\\
	\vspace*{15pt}
	\sc Abstract \\ \rm
	\end{center}
	\doublespace %Harvard registrar requests that abstract is double spaced
	\input{frontmatter/abstract}
	\doublespace %Harvard registrar requests that abstract is double spaced
	\newpage \lhead{} \rhead{}
	\cfoot{\thepage}
	\onehalfspacing
}

\newcommand{\dedicationpage}{
	\pagestyle{fancy}
	\newpage \thispagestyle{fancy} \vspace*{\fill}
	\sc \noindent \input{frontmatter/dedication}
	\vspace*{\fill} \newpage \rm
	}

% the list of authors
\newcommand{\authorlist}{
	\pagestyle{fancy}
	\newpage
	\thispagestyle{fancy}
	\chapter*{Author List}
	\noindent \input{frontmatter/authorlist}
	\newpage \rm
	}

% the acknowledgments page
\newcommand{\acknowledgments}{
	\chapter*{Acknowledgments}
	\noindent
	\input{frontmatter/thanks}
	\vspace*{\fill}
	\newpage
	\setcounter{page}{1}
	\pagenumbering{arabic}}

% An environment for paragraph-style section
\providecommand\newthought[1]{%
   \addvspace{1.0\baselineskip plus 0.5ex minus 0.2ex}%
   \noindent\textsc{#1}}

\let\jnl@style=\rmfamily
\def\ref@jnl#1{{\jnl@style#1}}%
\newcommand\aj{\ref@jnl{AJ}}%
          % Astronomical Journal
\newcommand\actaa{\ref@jnl{Acta Astron.}}%
  % Acta Astronomica
\newcommand\araa{\ref@jnl{ARA\&A}}%
          % Annual Review of Astron and Astrophys
\newcommand\apj{\ref@jnl{ApJ}}%
          % Astrophysical Journal
\newcommand\apjl{\ref@jnl{ApJ}}%
          % Astrophysical Journal, Letters
\newcommand\apjs{\ref@jnl{ApJS}}%
          % Astrophysical Journal, Supplement
\newcommand\ao{\ref@jnl{Appl.~Opt.}}%
          % Applied Optics
\newcommand\apss{\ref@jnl{Ap\&SS}}%
          % Astrophysics and Space Science
\newcommand\aap{\ref@jnl{A\&A}}%
          % Astronomy and Astrophysics
\newcommand\aapr{\ref@jnl{A\&A~Rev.}}%
          % Astronomy and Astrophysics Reviews
\newcommand\aaps{\ref@jnl{A\&AS}}%
          % Astronomy and Astrophysics, Supplement
\newcommand\azh{\ref@jnl{AZh}}%
          % Astronomicheskii Zhurnal
\newcommand\baas{\ref@jnl{BAAS}}%
          % Bulletin of the AAS
\newcommand\caa{\ref@jnl{Chinese Astron. Astrophys.}}%
  % Chinese Astronomy and Astrophysics
\newcommand\cjaa{\ref@jnl{Chinese J. Astron. Astrophys.}}%
  % Chinese Journal of Astronomy and Astrophysics
\newcommand\icarus{\ref@jnl{Icarus}}%
  % Icarus
\newcommand\jcap{\ref@jnl{J. Cosmology Astropart. Phys.}}%
  % Journal of Cosmology and Astroparticle Physics
\newcommand\jrasc{\ref@jnl{JRASC}}%
          % Journal of the RAS of Canada
\newcommand\memras{\ref@jnl{MmRAS}}%
          % Memoirs of the RAS
\newcommand\mnras{\ref@jnl{MNRAS}}%
          % Monthly Notices of the RAS
\newcommand\na{\ref@jnl{New A}}%
  % New Astronomy
\newcommand\nar{\ref@jnl{New A Rev.}}%
  % New Astronomy Review
\newcommand\pra{\ref@jnl{Phys.~Rev.~A}}%
          % Physical Review A: General Physics
\newcommand\prb{\ref@jnl{Phys.~Rev.~B}}%
          % Physical Review B: Solid State
\newcommand\prc{\ref@jnl{Phys.~Rev.~C}}%
          % Physical Review C
\newcommand\prd{\ref@jnl{Phys.~Rev.~D}}%
          % Physical Review D
\newcommand\pre{\ref@jnl{Phys.~Rev.~E}}%
          % Physical Review E
\newcommand\prl{\ref@jnl{Phys.~Rev.~Lett.}}%
          % Physical Review Letters
\newcommand\pasa{\ref@jnl{PASA}}%
  % Publications of the Astron. Soc. of Australia
\newcommand\pasp{\ref@jnl{PASP}}%
          % Publications of the ASP
\newcommand\pasj{\ref@jnl{PASJ}}%
          % Publications of the ASJ
\newcommand\qjras{\ref@jnl{QJRAS}}%
          % Quarterly Journal of the RAS
\newcommand\rmxaa{\ref@jnl{Rev. Mexicana Astron. Astrofis.}}%
  % Revista Mexicana de Astronomia y Astrofisica
\newcommand\skytel{\ref@jnl{S\&T}}%
          % Sky and Telescope
\newcommand\solphys{\ref@jnl{Sol.~Phys.}}%
          % Solar Physics
\newcommand\sovast{\ref@jnl{Soviet~Ast.}}%
          % Soviet Astronomy
\newcommand\ssr{\ref@jnl{Space~Sci.~Rev.}}%
          % Space Science Reviews
\newcommand\zap{\ref@jnl{ZAp}}%
          % Zeitschrift fuer Astrophysik
\newcommand\nat{\ref@jnl{Nature}}%
          % Nature
\newcommand\iaucirc{\ref@jnl{IAU~Circ.}}%
          % IAU Cirulars
\newcommand\aplett{\ref@jnl{Astrophys.~Lett.}}%
          % Astrophysics Letters and Communications
\newcommand\apspr{\ref@jnl{Astrophys.~Space~Phys.~Res.}}%
          % Astrophysics Space Physics Research
\newcommand\bain{\ref@jnl{Bull.~Astron.~Inst.~Netherlands}}%
          % Bulletin Astronomical Institute of the Netherlands
\newcommand\fcp{\ref@jnl{Fund.~Cosmic~Phys.}}%
          % Fundamental Cosmic Physics
\newcommand\gca{\ref@jnl{Geochim.~Cosmochim.~Acta}}%
          % Geochimica Cosmochimica Acta
\newcommand\grl{\ref@jnl{Geophys.~Res.~Lett.}}%
          % Geophysics Research Letters
\newcommand\jcp{\ref@jnl{J.~Chem.~Phys.}}%
          % Journal of Chemical Physics
\newcommand\jgr{\ref@jnl{J.~Geophys.~Res.}}%
          % Journal of Geophysical Research
\newcommand\jqsrt{\ref@jnl{J.~Quant.~Spec.~Radiat.~Transf.}}%
          % Journal of Quantitiative Spectroscopy and Radiative Trasfer
\newcommand\memsai{\ref@jnl{Mem.~Soc.~Astron.~Italiana}}%
          % Mem. Societa Astronomica Italiana
\newcommand\nphysa{\ref@jnl{Nucl.~Phys.~A}}%
          % Nuclear Physics A
\newcommand\physrep{\ref@jnl{Phys.~Rep.}}%
          % Physics Reports
\newcommand\physscr{\ref@jnl{Phys.~Scr}}%
          % Physica Scripta
\newcommand\planss{\ref@jnl{Planet.~Space~Sci.}}%
          % Planetary Space Science
\newcommand\procspie{\ref@jnl{Proc.~SPIE}}%
          % Proceedings of the SPIE
\let\astap=\aap
\let\apjlett=\apjl
\let\apjsupp=\apjs
\let\applopt=\ao
\newcommand\phn{\phantom{0}}%
\newcommand\phd{\phantom{.}}%
\newcommand\phs{\phantom{$-$}}%
\newcommand\phm[1]{\phantom{#1}}%
\let\la=\lesssim            % For Springer A&A compliance...
\let\ga=\gtrsim
\newcommand\sq{\mbox{\rlap{$\sqcap$}$\sqcup$}}%
\newcommand\arcdeg{\mbox{$^\circ$}}%
\newcommand\arcmin{\mbox{$^\prime$}}%
\newcommand\arcsec{\mbox{$^{\prime\prime}$}}%
\newcommand\fd{\mbox{$.\!\!^{\mathrm d}$}}%
\newcommand\fh{\mbox{$.\!\!^{\mathrm h}$}}%
\newcommand\fm{\mbox{$.\!\!^{\mathrm m}$}}%
\newcommand\fs{\mbox{$.\!\!^{\mathrm s}$}}%
\newcommand\fdg{\mbox{$.\!\!^\circ$}}%
\newcommand\farcm@mss{\mbox{$.\mkern-4mu^\prime$}}%
\let\farcm\farcm@mss
\newcommand\farcs@mss{\mbox{$.\!\!^{\prime\prime}$}}%
\let\farcs\farcs@mss
\newcommand\fp{\mbox{$.\!\!^{\scriptscriptstyle\mathrm p}$}}%
\newcommand\micron{\mbox{$\mu$m}}%
\def\farcm@apj{%
 \mbox{.\kern -0.7ex\raisebox{.9ex}{\scriptsize$\prime$}}%
}%
\def\farcs@apj{%
 \mbox{%
  \kern  0.13ex.%
  \kern -0.95ex\raisebox{.9ex}{\scriptsize$\prime\prime$}%
  \kern -0.1ex%
 }%
}%
\newcommand\case[2]{\mbox{$\frac{#1}{#2}$}}%
\newcommand\slantfrac{\case}%
\newcommand\onehalf{\slantfrac{1}{2}}%
\newcommand\onethird{\slantfrac{1}{3}}%
\newcommand\twothirds{\slantfrac{2}{3}}%
\newcommand\onequarter{\slantfrac{1}{4}}%
\newcommand\threequarters{\slantfrac{3}{4}}%
\newcommand\ubvr{\mbox{$U\!BV\!R$}}%% UBVR system
\newcommand\ub{\mbox{$U\!-\!B$}}%   % U-B
\newcommand\bv{\mbox{$B\!-\!V$}}%   % B-V
\newcommand\vr{\mbox{$V\!-\!R$}}%   % V-R
\newcommand\ur{\mbox{$U\!-\!R$}}%   % U-R
\newcommand\ion[2]{#1$\;${\small\rmfamily\@Roman{#2}}\relax}%
\newcommand\nodata{ ~$\cdots$~ }%
\newcommand\diameter{\ooalign{\hfil/\hfil\crcr\mathhexbox20D}}%
\newcommand\degr{\arcdeg}%
\newcommand\Sun{\sun}% Sun symbol, "S"
\newcommand\Sol{\sun}%
\newcommand\sun{\odot}%
\newcommand\Mercury{\astro{\char1}}% Mercury symbol, "1"
\newcommand\Venus{\astro{\char2}}% Venus symbol, "2"
\newcommand\Earth{\earth}% Earth symbol, "3"
\newcommand\Terra{\earth}%
\newcommand\earth{\oplus}%
\newcommand\Mars{\astro{\char4}}% Mars symbol, "4"
\newcommand\Jupiter{\astro{\char5}}% Jupiter symbol, "5"
\newcommand\Saturn{\astro{\char6}}% Saturn symbol, "6"
\newcommand\Uranus{\astro{\char7}}% Uranus symbol, "7"
\newcommand\Neptune{\astro{\char8}}% Neptune symbol, "8"
\newcommand\Pluto{\astro{\char9}}% Pluo symbol, "9"
\newcommand\Moon{\astro{\char10}}% Moon symbol, "M"
\newcommand\Luna{\Moon}%
\newcommand\Aries{\astro{\char11}}%
\newcommand\VEq{\Aries}% vernal equinox (Aries)
\newcommand\Taurus{\astro{\char12}}%
\newcommand\Gemini{\astro{\char13}}%
\newcommand\Cancer{\astro{\char14}}%
\newcommand\Leo{\astro{\char15}}%
\newcommand\Virgo{\astro{\char16}}%
\newcommand\Libra{\astro{\char17}}%
\newcommand\AEq{\Libra}% autumnal equinox (Libra)
\newcommand\Scorpius{\astro{\char18}}%
\newcommand\Sagittarius{\astro{\char19}}%
\newcommand\Capricornus{\astro{\char20}}%
\newcommand\Aquarius{\astro{\char21}}%
\newcommand\Pisces{\astro{\char22}}%
\newcommand\mref[1]{(\ref{#1})}%
\def\Msun{\hbox{$\mathrm{\thinspace M_{\odot}}$}}
\def\Mearth{\hbox{$\mathrm{\thinspace M_{\oplus}}$}}
\def\Rsun{\hbox{$\mathrm{\thinspace R_{\odot}}$}}
\def\Lsun{\hbox{$\mathrm{\thinspace L_{\odot}}$}}
\def\g{\hbox{$\thinspace\textrm{g}$}}
\def\pc{\hbox{$\thinspace\textrm{pc}$}}
\def\AU{\hbox{$\thinspace\textrm{AU}$}}
\def\cm{\hbox{$\thinspace\textrm{cm}$}}
\def\km{\hbox{$\thinspace\textrm{km}$}}
\def\m{\hbox{$\thinspace\textrm{m}$}}
\def\mum{\hbox{$\thinspace\mu\textrm{m}$}}
\def\s{\hbox{$\thinspace\textrm{s}$}}
\def\K{\hbox{$\thinspace\textrm{K}$}}
\def\yr{\hbox{$\thinspace\textrm{lat}$}}
\def\Myr{\hbox{$\thinspace\textrm{Myr}$}}
\def\mH{\hbox{$m_{\textrm{H}}$}}
\DeclareMathAlphabet\EuRoman{U}{eur}{m}{n}
\SetMathAlphabet\EuRoman{bold}{U}{eur}{b}{n}
\newcommand{\eurom}{\EuRoman}
\newcommand{\yt}{{\texttt{yt}}}
