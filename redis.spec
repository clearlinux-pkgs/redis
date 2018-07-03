#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : redis
Version  : 2.10.6
Release  : 34
URL      : https://pypi.debian.net/redis/redis-2.10.6.tar.gz
Source0  : https://pypi.debian.net/redis/redis-2.10.6.tar.gz
Summary  : Python client for Redis key-value store
Group    : Development/Tools
License  : MIT
Requires: redis-python3
Requires: redis-python
BuildRequires : pbr
BuildRequires : pip

BuildRequires : python3-dev
BuildRequires : setuptools

%description
========
        
        The Python interface to the Redis key-value store.

%package python
Summary: python components for the redis package.
Group: Default
Requires: redis-python3

%description python
python components for the redis package.


%package python3
Summary: python3 components for the redis package.
Group: Default
Requires: python3-core

%description python3
python3 components for the redis package.


%prep
%setup -q -n redis-2.10.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523566748
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
