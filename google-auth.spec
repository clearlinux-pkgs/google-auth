#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : google-auth
Version  : 1.11.0
Release  : 11
URL      : https://files.pythonhosted.org/packages/72/e1/b909fc8b72ff3e1664323fb9ab5ac712f242d3c15a2ab3ce846e64be6f35/google-auth-1.11.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/72/e1/b909fc8b72ff3e1664323fb9ab5ac712f242d3c15a2ab3ce846e64be6f35/google-auth-1.11.0.tar.gz
Summary  : Google Authentication Library
Group    : Development/Tools
License  : Apache-2.0
Requires: google-auth-license = %{version}-%{release}
Requires: google-auth-python = %{version}-%{release}
Requires: google-auth-python3 = %{version}-%{release}
Requires: cachetools
Requires: pyasn1-modules
Requires: rsa
Requires: setuptools
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : cachetools
BuildRequires : pyasn1-modules
BuildRequires : rsa
BuildRequires : setuptools
BuildRequires : six

%description
==========================
        
        |pypi|
        
        This library simplifies using Google's various server-to-server authentication
        mechanisms to access Google APIs.

%package license
Summary: license components for the google-auth package.
Group: Default

%description license
license components for the google-auth package.


%package python
Summary: python components for the google-auth package.
Group: Default
Requires: google-auth-python3 = %{version}-%{release}

%description python
python components for the google-auth package.


%package python3
Summary: python3 components for the google-auth package.
Group: Default
Requires: python3-core
Provides: pypi(google_auth)
Requires: pypi(cachetools)
Requires: pypi(pyasn1_modules)
Requires: pypi(rsa)
Requires: pypi(setuptools)
Requires: pypi(six)

%description python3
python3 components for the google-auth package.


%prep
%setup -q -n google-auth-1.11.0
cd %{_builddir}/google-auth-1.11.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583535473
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/google-auth
cp %{_builddir}/google-auth-1.11.0/LICENSE %{buildroot}/usr/share/package-licenses/google-auth/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/google-auth/7df059597099bb7dcf25d2a9aedfaf4465f72d8d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
