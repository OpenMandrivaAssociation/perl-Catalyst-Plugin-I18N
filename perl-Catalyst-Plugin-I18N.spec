%define module	Catalyst-Plugin-I18N
%define name	perl-%{module}
%define version 0.06
%define release %mkrel 1

Summary:	I18N for Catalyst
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Perl
Requires:	perl
URL:		http://search.cpan.org/dist/%module/
Source:		%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%else
BuildRequires:	perl
%endif
BuildRequires:	perl(Catalyst) >= 2.99
BuildRequires:	perl(I18N::LangTags::Detect)
BuildRequires:	perl(Locale::Maketext::Lexicon)
BuildRequires:	perl(Locale::Maketext::Simple)
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch

%description
Supports mo/po files and Maketext classes under your applications I18N
namespace.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%__make

%check
%__make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/*/*
%{perl_vendorlib}/Catalyst/Plugin/*


