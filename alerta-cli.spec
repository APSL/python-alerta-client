%define name alerta-cli
%define version 1.0.0
%define release 1

Name: %{name}
Summary: Alerta command-line tool
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.gz
License: Apache License 2.0
Group: Utilities/System
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: x86_64
Vendor: Nick Satterly <nick.satterly@theguardian.com>
Url: https://github.com/alerta/python-alerta-cli
BuildRequires: python-devel, python-setuptools, python-pip, python-virtualenv

%description
Alerta is a monitoring framework that consolidates alerts
from multiple sources like syslog, SNMP, Nagios, Riemann,
Zabbix, and displays them on an alert console.

%prep
%setup

%build
/usr/bin/virtualenv --no-site-packages alerta
alerta/bin/pip install -r requirements.txt --upgrade
alerta/bin/python setup.py install --single-version-externally-managed --root=/
/usr/bin/virtualenv --relocatable alerta

%install
%__mkdir_p %{buildroot}/opt/alerta
cp -r %{_builddir}/%{name}-%{version}/alerta %{buildroot}/opt

%clean
rm -rf %{buildroot}

%files
/opt/alerta/*
%defattr(-,root,root)

%changelog
* Thu Mar 21 2013 Nick Satterly <nick.satterly@theguardian.com> - 1.0.0-1
- Package alerta relase 3.0 command-line tools
