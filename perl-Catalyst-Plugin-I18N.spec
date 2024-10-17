%define upstream_name	 Catalyst-Plugin-I18N
%define upstream_version 0.10

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	I18N for Catalyst
License:	GPL
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%upstream_name/
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst) >= 2.99
BuildRequires:	perl(I18N::LangTags::Detect)
BuildRequires:	perl(Locale::Maketext::Lexicon)
BuildRequires:	perl(Locale::Maketext::Simple) >= 0.190.0
BuildRequires:	perl(MRO::Compat)

BuildArch:	noarch
Requires:	perl(Locale::Maketext::Lexicon)

%description
Supports mo/po files and Maketext classes under your applications I18N
namespace.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor --skipdeps
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/*/*
%{perl_vendorlib}/Catalyst/Plugin/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.100.0-2mdv2011.0
+ Revision: 680739
- mass rebuild

* Fri Jul 16 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-1mdv2011.0
+ Revision: 554344
- adding min version in buildrequires:
- update to 0.10

* Wed Dec 02 2009 Jérôme Quelin <jquelin@mandriva.org> 0.90.0-1mdv2010.1
+ Revision: 472691
- adding missing requires:

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.90.0-1mdv2010.0
+ Revision: 406263
- rebuild using %%perl_convert_version

* Mon May 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-1mdv2010.0
+ Revision: 371665
- update to new version 0.09

* Sun Aug 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-1mdv2009.0
+ Revision: 270335
- update to new version 0.08

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.07-3mdv2009.0
+ Revision: 255560
- rebuild

* Tue Jan 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-1mdv2008.1
+ Revision: 152980
- update to new version 0.07
- update to new version 0.07

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Jul 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdv2008.0
+ Revision: 55684
- update to new version 0.06


* Sat Mar 12 2005 Scott Karns <scott@karnstech.com> 0.05-1mdk
- First Mdv package

