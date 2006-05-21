#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	CGI
%define		pnam	kSession
Summary:	CGI::kSession - a session management module
Summary(pl):	CGI::kSession - zarz±dzanie sesjami
Name:		perl-CGI-kSession
Version:	0.5.3
Release:	3
License:	GPL
Vendor:		Marcin Krzyzanowski <krzak@linux.net.pl>
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1a80b88eb9a2fea5951a8fc55b514b1a
URL:		http://www.hakore.com/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-DB_File
BuildRequires:	perl-FreezeThaw
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module can be used anywhere you need sessions. As a session
management module, it uses files with a configurable lifetime to
handle your session data. For those of you familiar with PHP, you will
notice that the session syntax is a little bit similar.

%description -l pl
Ten modu³ mo¿e byæ u¿yty wszêdzie gdzie potrzebujesz sesji. U¿ywa
plików do przechowywania danych o sesji. Osoby które mia³y styczno¶æ z
jêzykiem PHP zauwa¿± ¿e sk³adnia jest podobna do stosowanej w PHP.

%prep
%setup -q -n %{pdir}-%{pnam}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO Changelog example*
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
