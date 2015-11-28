#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
%bcond_without	tests	# do not perform "setup.py test"
#
Summary:	A small collection of tools for Python 2
Summary(pl.UTF-8):	Mały zestaw narzędzi dla Pythona 2
Name:		python-pytools
Version:	2014.3.5
Release:	4
License:	MIT
Group:		Development/Languages/Python
#Source0Download: https://pypi.python.org/pypi/pytools
Source0:	https://pypi.python.org/packages/source/p/pytools/pytools-%{version}.tar.gz
# Source0-md5:	7f8e9d6a88090a601e96a9ee095d3512
URL:		http://mathema.tician.de/software/pytools
%if %{with python2}
BuildRequires:	python-appdirs >= 1.4.0
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	python-decorator >= 3.2.0
BuildRequires:	python-distribute
BuildRequires:	python-six
%endif
%if %{with python3}
BuildRequires:	python3-appdirs >= 1.4.0
BuildRequires:	python3-devel >= 1:3.3
BuildRequires:	python3-decorator >= 3.2.0
BuildRequires:	python3-distribute
BuildRequires:	python3-six
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.612
Requires:	python-appdirs >= 1.4.0
Requires:	python-decorator >= 3.2.0
Requires:	python-six
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pytools is a big bag of things that are "missing" from the Python
standard library. This is mainly a dependency of Andreas Kloeckner's
other software packages, and is probably of little interest to you
unless you use those.

%description -l pl.UTF-8
Pytools to pojemnik na elementy "brakującyce" w standardowej
bibliotece Pythona. Jest to głównie zależność innych pakietów
oprogramowania Andreasa Kloecknera, w pozostałych przypadkach pewnie
mało interesująca.

%package -n python3-pytools
Summary:	A small collection of tools for Python 3
Summary(pl.UTF-8):	Mały zestaw narzędzi dla Pythona 3
Group:		Development/Languages/Python
Requires:	python3-appdirs >= 1.4.0
Requires:	python3-decorator >= 3.2.0
Requires:	python3-six

%description -n python3-pytools
Pytools is a big bag of things that are "missing" from the Python
standard library. This is mainly a dependency of Andreas Kloeckner's
other software packages, and is probably of little interest to you
unless you use those.

%description -n python3-pytools -l pl.UTF-8
Pytools to pojemnik na elementy "brakującyce" w standardowej
bibliotece Pythona. Jest to głównie zależność innych pakietów
oprogramowania Andreasa Kloecknera, w pozostałych przypadkach pewnie
mało interesująca.

%prep
%setup -q -n pytools-%{version}

%build
%if %{with python2}
%py_build \
	--build-base build-2 %{?with_tests:test}
%endif

%if %{with python3}
%py3_build \
	--build-base build-3 %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_build \
		--build-base build-2 \
	install \
		--skip-build \
		--optimize=2 \
		--root=$RPM_BUILD_ROOT

%py_postclean
%endif

%if %{with python3}
%py3_build \
		--build-base build-3 \
	install \
		--skip-build \
		--optimize=2 \
		--root=$RPM_BUILD_ROOT
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/pytools
%{py_sitescriptdir}/pytools-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pytools
%defattr(644,root,root,755)
%doc README
%{py3_sitescriptdir}/pytools
%{py3_sitescriptdir}/pytools-%{version}-py*.egg-info
%endif
