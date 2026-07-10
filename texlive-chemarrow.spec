%global tl_name chemarrow
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.9
Release:	%{tl_revision}.1
Summary:	Arrows for use in chemistry
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/chemarrow
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chemarrow.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chemarrow.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chemarrow.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This bundle consists of a font (available as Metafont source, MetaPost
source, and generated type 1 versions), and a package to use it. The
arrows in the font are designed to look more like those in chemistry
text-books than do Knuth's originals.

