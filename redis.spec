#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : redis
Version  : 2.10.5
Release  : 12
URL      : https://pypi.python.org/packages/source/r/redis/redis-2.10.5.tar.gz
Source0  : https://pypi.python.org/packages/source/r/redis/redis-2.10.5.tar.gz
Summary  : Python client for Redis key-value store
Group    : Development/Tools
License  : MIT
Requires: redis-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
redis-py
========
The Python interface to the Redis key-value store.
.. image:: https://secure.travis-ci.org/andymccurdy/redis-py.png?branch=master
:target: http://travis-ci.org/andymccurdy/redis-py

%package python
Summary: python components for the redis package.
Group: Default

%description python
python components for the redis package.


%prep
%setup -q -n redis-2.10.5

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
