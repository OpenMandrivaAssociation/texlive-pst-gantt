Name:		texlive-pst-gantt
Version:	35832
Release:	1
Summary:	Draw GANTT charts with pstricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-gantt
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-gantt.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-gantt.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package uses PSTricks to draw GANTT charts, which are a
kind of bar chart that displays a project schedule. The package
requires the pstricks apparatus, of course.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/pst-gantt/pst-gantt.tex
%{_texmfdistdir}/tex/latex/pst-gantt/pst-gantt.sty
%doc %{_texmfdistdir}/doc/generic/pst-gantt/Changes
%doc %{_texmfdistdir}/doc/generic/pst-gantt/README
%doc %{_texmfdistdir}/doc/generic/pst-gantt/pst-gantt-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-gantt/pst-gantt-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-gantt/pst-gantt-doc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
