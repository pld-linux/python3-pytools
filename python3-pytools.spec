#
# Conditional build:
%bcond_without	tests	# do not perform "setup.py test"
#
%define		pypi_name	pytools
Summary:	A small collection of tools for Python 2
Summary(pl.UTF-8):	Mały zestaw narzędzi dla Pythona 2
Name:		python3-pytools
Version:	2025.1.2
Release:	2
License:	MIT
Group:		Development/Languages/Python
#Source0Download: https://pypi.python.org/simple/pytools/
Source0:	https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	8b55ccb53ebd25b08b631e476ab2bb25
URL:		http://mathema.tician.de/software/pytools
BuildRequires:	python3-devel >= 1:3.3
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-appdirs >= 1.4.0
BuildRequires:	python3-decorator >= 3.2.0
BuildRequires:	python3-numpy >= 1.6.0
BuildRequires:	python3-pytest
BuildRequires:	python3-six >= 1.8.0
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-appdirs >= 1.4.0
Requires:	python3-decorator >= 3.2.0
Requires:	python3-six
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

%prep
%setup -q -n pytools-%{version}

%build
%py3_build_pyproject

%if %{with tests}
%{__python3} -m zipfile -e build-3/*.whl build-3-test
# use explicit plugins list for reliable builds (delete PYTEST_PLUGINS if empty)
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS= \
%{__python3} -m pytest -o pythonpath="$PWD/build-3-test" pytools
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/pytools
%{py3_sitescriptdir}/pytools-%{version}.dist-info
