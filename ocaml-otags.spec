Summary:	OCaml tags
Summary(pl):	Tagi dla OCamla
Name:		ocaml-otags
Version:	3.06.2
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://perso.wanadoo.fr/cuihtlauac.alvarado/otags-%{version}.tar.gz
Patch0:		%{name}-vi.patch
Vendor:		Cuihtlauac Alvardo <cuihtlauac.alvarado@francetelecom.com>
BuildRequires:	ocaml-camlp4 >= 3.05
%requires_eq	ocaml-camlp4
Obsoletes:	otags
Provides:	otags
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Program for making tags for Emacs and Vi, for OCaml source code.

%description -l pl
Program do tworzenia tag�w dla Emacsa i Vi do kodu �r�d�owego w OCamlu.

%prep
%setup -q -n otags-%{version}
%patch0 -p1

%build
# don't use %%configure
./configure --prefix %{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	INSTALLIBDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README HISTORY
%attr(755,root,root) %{_bindir}/*
%{_libdir}/ocaml/*