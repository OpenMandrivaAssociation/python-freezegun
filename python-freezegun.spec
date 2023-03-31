# Created by pyp2rpm-3.3.5
%global pypi_name freezegun

Name:           python-%{pypi_name}
Version:        1.0.0
Release:        2
Summary:        Let your Python tests travel through time
Group:          Development/Python
License:        Apache 2.0
URL:            https://github.com/spulec/freezegun
Source0:        %{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(python-dateutil) >= 2.7
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)

%description
FreezeGun: Let your Python tests travel through time FreezeGun is a library
that allows your Python tests to travel through time by mocking the datetime
module.Usage Once the decorator or context manager have been invoked, all calls
to datetime.datetime.now(), datetime.datetime.utcnow(), datetime.date.today(),
time.time(), time.localtime(), time.gmtime(), and time.strftime() will return
the...

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
