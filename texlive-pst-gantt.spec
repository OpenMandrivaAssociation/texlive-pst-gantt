%global tl_name pst-gantt
%global tl_revision 35832

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.22a
Release:	%{tl_revision}.1
Summary:	Draw GANTT charts with PSTricks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-gantt
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-gantt.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-gantt.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package uses PSTricks to draw GANTT charts, which are a kind of bar
chart that displays a project schedule. The package requires the
pstricks apparatus, of course.

