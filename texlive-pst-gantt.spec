# revision 17206
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-gantt
# catalog-date 2010-02-24 21:46:55 +0100
# catalog-license lppl
# catalog-version 0.21
Name:		texlive-pst-gantt
Version:	0.21
Release:	3
Summary:	Draw GANTT charts with pstricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-gantt
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-gantt.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-gantt.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-gantt.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package draws GANTT charts, which are a kind of bar chart
that displays a project schedule. The package requires the
pstricks apparatus, of course.

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
#- source
%doc %{_texmfdistdir}/source/generic/pst-gantt/Makefile

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.21-2
+ Revision: 755309
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.21-1
+ Revision: 719354
- texlive-pst-gantt
- texlive-pst-gantt
- texlive-pst-gantt
- texlive-pst-gantt

