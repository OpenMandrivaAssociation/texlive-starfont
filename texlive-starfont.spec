Name:		texlive-starfont
Version:	19982
Release:	2
Summary:	The StarFont Sans astrological font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/ps-type1/starfont
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/starfont.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/starfont.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package contains StarFontSans and StarFontSerif, two
public-domain astrological fonts designed by Anthony I.P. Owen,
and the appropriate macros to use them with TeX and LaTeX. The
fonts are supplied in the original TrueType Format and as
PostScript font files.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/starfont/starfont.afm
%{_texmfdistdir}/fonts/afm/public/starfont/strfnser.afm
%{_texmfdistdir}/fonts/map/dvips/starfont/starfont.map
%{_texmfdistdir}/fonts/tfm/public/starfont/fstr8x.tfm
%{_texmfdistdir}/fonts/tfm/public/starfont/fsts8x.tfm
%{_texmfdistdir}/fonts/type1/public/starfont/starfont.pfb
%{_texmfdistdir}/fonts/type1/public/starfont/strfnser.pfb
%{_texmfdistdir}/tex/latex/starfont/starfont.sty
%doc %{_texmfdistdir}/doc/fonts/starfont/COPYING
%doc %{_texmfdistdir}/doc/fonts/starfont/Makefile
%doc %{_texmfdistdir}/doc/fonts/starfont/README
%doc %{_texmfdistdir}/doc/fonts/starfont/STRFNSAN.TTF
%doc %{_texmfdistdir}/doc/fonts/starfont/STRFNSER.TTF
%doc %{_texmfdistdir}/doc/fonts/starfont/starfont.pdf
%doc %{_texmfdistdir}/doc/fonts/starfont/starfont.tex
%doc %{_texmfdistdir}/doc/fonts/starfont/table.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
