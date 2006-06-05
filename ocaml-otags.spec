Summary:	OCaml tags
Summary(pl):	Tagi dla OCamla
Name:		ocaml-otags
Version:	3.08.0.1
Release:	6
License:	GPL
Group:		Development/Tools
Source0:	http://perso.rd.francetelecom.fr/alvarado/soft/otags-%{version}.tar.gz
# Source0-md5:	180f0a70e4da8864cbf35fd3022e63db
Vendor:		Cuihtlauac Alvardo <cuihtlauac.alvarado@francetelecom.com>
BuildRequires:	ocaml-camlp4 >= 3.07
%requires_eq	ocaml-camlp4
Obsoletes:	otags
Provides:	otags
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Program for making tags for Emacs and Vi, for OCaml source code.

%description -l pl
Program do tworzenia tagów dla Emacsa i Vi do kodu ¼ród³owego w OCamlu.

%prep
%setup -q -n otags-%{version}

%build
sed -i -e s:/usr/local/:/usr/:g -e s:/lib/:/%{_lib}/:g Makefile.depend
# don't use %%configure
./configure --prefix %{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	INSTALLLIBDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README HISTORY
%attr(755,root,root) %{_bindir}/*
%{_libdir}/ocaml/*
