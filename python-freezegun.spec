%define module freezegun
%bcond test 1

Name:		python-freezegun
Version:	1.5.5
Release:	1
Summary:	Let your Python tests travel through time
Group:		Development/Python
License:	Apache-2.0
URL:		https://github.com/spulec/freezegun
Source0:	https://files.pythonhosted.org/packages/source/f/%{module}/%{module}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch

BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
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
%py_build

%install
%py_install

%if %{with test}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitearch}:${PWD}"
pytest -v tests/
%endif

%files
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
%license LICENSE
%doc README.rst
