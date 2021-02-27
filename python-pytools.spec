#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
%bcond_without	tests	# do not perform "setup.py test"
#
%define		pypi_name	pytools
Summary:	A small collection of tools for Python 2
Summary(pl.UTF-8):	Mały zestaw narzędzi dla Pythona 2
Name:		python-pytools
Version:	2018.5.2
Release:	3
License:	MIT
Group:		Development/Languages/Python
#Source0Download: https://pypi.python.org/simple/pytools/
Source0:	https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	50217f663eb30a1e5d248cc6defd0cf6
URL:		http://mathema.tician.de/software/pytools
%if %{with python2}
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-appdirs >= 1.4.0
BuildRequires:	python-decorator >= 3.2.0
BuildRequires:	python-numpy >= 1.6.0
BuildRequires:	python-pytest
BuildRequires:	python-six >= 1.8.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.3
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-appdirs >= 1.4.0
BuildRequires:	python3-decorator >= 3.2.0
BuildRequires:	python3-numpy >= 1.6.0
BuildRequires:	python3-pytest
BuildRequires:	python3-six >= 1.8.0
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
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
%py_build

%{?with_tests:PYTHONPATH=$(pwd) %{__python} -m pytest test}
%endif

%if %{with python3}
%py3_build

%{?with_tests:PYTHONPATH=$(pwd) %{__python3} -m pytest test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/pytools
%{py_sitescriptdir}/pytools-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pytools
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/pytools
%{py3_sitescriptdir}/pytools-%{version}-py*.egg-info
%endif
