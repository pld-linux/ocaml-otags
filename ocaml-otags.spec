Summary:	OCaml tags
Summary(pl):	OCaml tags
Name:		ocaml-otags
Version:	3.04.3
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://www.multimania.com/moninjf/Ocaml/otags-%{version}.tar.gz
Patch0:		%{name}-vi.patch
URL:		http://www.multimania.com/moninjf/Ocaml/
BuildRequires:	ocaml-camlp4 >= 3.04-2
%requires_eq	ocaml-camlp4
Obsoletes:	otags
Provides:	otags
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Program for making tags for Emacs and Vi, for OCaml source code.

%description -l pl
Program do robienia tagów dla Emacsa i Vi do kodu ¼ród³owego w OCamlu.

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

gzip -9nf README HISTORY

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_libdir}/ocaml/*
