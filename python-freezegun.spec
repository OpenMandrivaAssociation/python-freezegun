%define module freezegun
%bcond_without test

Name:		python-freezegun
Version:	1.5.1
Release:	1
Summary:	Let your Python tests travel through time
Group:		Development/Python
License:	Apache-2.0
URL:		https://github.com/spulec/freezegun
Source0:	https://files.pythonhosted.org/packages/source/f/freezegun/%{module}-%{version}.tar.gz
# patch for python 3.13 datetimes test also fixes asserts in 3.11
# see for more:  https://github.com/spulec/freezegun/pull/550
Patch0:		freezegun-1.5.1-py13-datetimes-fix.patch
BuildArch:	noarch

BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(python-dateutil) >= 2.7
BuildRequires:	python%{pyver}dist(wheel)
%if %{with test}
BuildRequires:	python%{pyver}dist(pytest)
%endif

%description
FreezeGun: Let your Python tests travel through time FreezeGun is a library
that allows your Python tests to travel through time by mocking the datetime
module.Usage Once the decorator or context manager have been invoked, all calls
to datetime.datetime.now(), datetime.datetime.utcnow(), datetime.date.today(),
time.time(), time.localtime(), time.gmtime(), and time.strftime() will return
the...

%prep
%autosetup -n %{module}-%{version} -p1
# Remove bundled egg-info
rm -rf %{module}.egg-info

%build
%py3_build

%install
%py3_install

%if %{with test}
%check
pytest -v tests/
%endif

%files
%{python3_sitelib}/%{module}
%{python3_sitelib}/%{module}-%{version}.dist-info
%license LICENSE
%doc README.rst
