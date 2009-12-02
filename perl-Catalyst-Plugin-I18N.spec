%define upstream_name	 Catalyst-Plugin-I18N
%define upstream_version 0.09

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	I18N for Catalyst
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%upstream_name/
Source0:    http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Catalyst) >= 2.99
BuildRequires:	perl(I18N::LangTags::Detect)
BuildRequires:	perl(Locale::Maketext::Lexicon)
BuildRequires:	perl(Locale::Maketext::Simple)
BuildRequires:	perl(MRO::Compat)

BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

Requires:	perl(Locale::Maketext::Lexicon)

%description
Supports mo/po files and Maketext classes under your applications I18N
namespace.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor --skipdeps
%make

%check
%make test

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
