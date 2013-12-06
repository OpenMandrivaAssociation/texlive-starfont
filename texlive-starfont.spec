# revision 19982
# category Package
# catalog-ctan /fonts/ps-type1/starfont
# catalog-date 2010-09-30 00:35:45 +0200
# catalog-license pd
# catalog-version 1.2
Name:		texlive-starfont
Version:	1.2
Release:	4
Summary:	The StarFont Sans astrological font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/ps-type1/starfont
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/starfont.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/starfont.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2-2
+ Revision: 756168
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.2-1
+ Revision: 719578
- texlive-starfont
- texlive-starfont
- texlive-starfont
- texlive-starfont

