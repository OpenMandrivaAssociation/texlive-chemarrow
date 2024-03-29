Name:		texlive-chemarrow
Version:	17146
Release:	2
Summary:	Arrows for use in chemistry
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chemarrow
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemarrow.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemarrow.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemarrow.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This bundle consists of a font (available as metafont source,
metapost source, and generated type 1 versions), and a package
to use it. The arrows in the font are designed to look more
like those in chemistry text-books than do Knuth's originals.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/chemarrow/arrow.afm
%{_texmfdistdir}/fonts/map/dvips/chemarrow/chemarrow.map
%{_texmfdistdir}/fonts/source/public/chemarrow/arrow.mf
%{_texmfdistdir}/fonts/tfm/public/chemarrow/arrow.tfm
%{_texmfdistdir}/fonts/type1/public/chemarrow/arrow.inf
%{_texmfdistdir}/fonts/type1/public/chemarrow/arrow.pfb
%{_texmfdistdir}/fonts/type1/public/chemarrow/arrow.pfm
%{_texmfdistdir}/tex/latex/chemarrow/chemarrow.sty
%doc %{_texmfdistdir}/doc/fonts/chemarrow/Liesmich.txt
%doc %{_texmfdistdir}/doc/fonts/chemarrow/README
%doc %{_texmfdistdir}/doc/fonts/chemarrow/arrow.Mac.sit.hqx
%doc %{_texmfdistdir}/doc/fonts/chemarrow/chemarrow-de.pdf
%doc %{_texmfdistdir}/doc/fonts/chemarrow/chemarrow-de.tex
%doc %{_texmfdistdir}/doc/fonts/chemarrow/chemarrow.pdf
%doc %{_texmfdistdir}/doc/fonts/chemarrow/chemarrow.tex
%doc %{_texmfdistdir}/doc/fonts/chemarrow/testchem.tex
#- source
%doc %{_texmfdistdir}/source/fonts/chemarrow/Arrow.vfb
%doc %{_texmfdistdir}/source/fonts/chemarrow/arrow.mp

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
