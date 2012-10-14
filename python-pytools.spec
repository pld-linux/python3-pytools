#
# Conditional build:
%bcond_without	tests	# do not perform "setup.py test"
#
Summary:	A small collection of tools for Python
Summary(pl.UTF-8):	Mały zestaw narzędzi dla Pythona
Name:		python-pytools
Version:	2011.5
Release:	1
License:	MIT
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/p/pytools/pytools-%{version}.tar.gz
# Source0-md5:	90107519fee21eeb7e712afb2178a568
URL:		http://mathema.tician.de/software/pytools
BuildRequires:	python-devel
BuildRequires:	python-decorator >= 3.2.0
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-decorator >= 3.2.0
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
%{__python} setup.py build

%{?with_tests:%{__python} setup.py test}

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# change %{py_sitedir} to %{py_sitescriptdir} for 'noarch' packages!
#py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
#py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/pytools
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/pytools-%{version}-py*.egg-info
%endif
