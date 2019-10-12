#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : redis
Version  : 3.3.10
Release  : 44
URL      : https://files.pythonhosted.org/packages/e9/dd/fcc1003fa83da521fdfa2f41515209ef15d2246f96d0d1ddaaa564a950b3/redis-3.3.10.tar.gz
Source0  : https://files.pythonhosted.org/packages/e9/dd/fcc1003fa83da521fdfa2f41515209ef15d2246f96d0d1ddaaa564a950b3/redis-3.3.10.tar.gz
Summary  : Python client for Redis key-value store
Group    : Development/Tools
License  : MIT
Requires: redis-license = %{version}-%{release}
Requires: redis-python = %{version}-%{release}
Requires: redis-python3 = %{version}-%{release}
Requires: hiredis
BuildRequires : buildreq-distutils3
BuildRequires : hiredis

%description
========
        
        The Python interface to the Redis key-value store.

%package license
Summary: license components for the redis package.
Group: Default

%description license
license components for the redis package.


%package python
Summary: python components for the redis package.
Group: Default
Requires: redis-python3 = %{version}-%{release}

%description python
python components for the redis package.


%package python3
Summary: python3 components for the redis package.
Group: Default
Requires: python3-core

%description python3
python3 components for the redis package.


%prep
%setup -q -n redis-3.3.10

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1570924661
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/redis
cp %{_builddir}/redis-3.3.10/LICENSE %{buildroot}/usr/share/package-licenses/redis/a4b61fde3ceaed3091f9f7ac886713a60beef947
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/redis/a4b61fde3ceaed3091f9f7ac886713a60beef947

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
