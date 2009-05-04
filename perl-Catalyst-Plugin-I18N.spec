%define module	Catalyst-Plugin-I18N
%define name	perl-%{module}
%define version 0.09
%define release %mkrel 1

Summary:	I18N for Catalyst
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%module/
Source:     http://www.cpan.org/modules/by-module/Catalyst/%{module}-%{version}.tar.gz
BuildRequires:	perl(Catalyst) >= 2.99
BuildRequires:	perl(I18N::LangTags::Detect)
BuildRequires:	perl(Locale::Maketext::Lexicon)
BuildRequires:	perl(Locale::Maketext::Simple)
BuildRequires:	perl(MRO::Compat)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
Supports mo/po files and Maketext classes under your applications I18N
namespace.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor --skipdeps
%__make

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/*/*
%{perl_vendorlib}/Catalyst/Plugin/*


