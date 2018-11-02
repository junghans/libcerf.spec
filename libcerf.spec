Name:		libcerf
Version:	1.9
Release:	2%{?dist}
Summary:        A library that provides complex error functions

License:        MIT
URL:            http://apps.jcns.fz-juelich.de/doku/sc/libcerf
Source0:        http://apps.jcns.fz-juelich.de/src/libcerf/%{name}-%{version}.tgz

BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  cmake
# Required to build the documentation
BuildRequires:  perl-podlators
BuildRequires:  perl-Pod-Html

%description
libcerf is a self-contained numeric library that provides an efficient
and accurate implementation of complex error functions, along with
Dawson, Faddeeva, and Voigt functions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup
# Force cmake to use the paths passed at configure time
sed -i -e 's|${destination}/lib|${LIB_INSTALL_DIR}|' lib/CMakeLists.txt
sed -i -e 's|CMAKE_INSTALL_PREFIX|SHARE_INSTALL_PREFIX|' man/CMakeLists.txt


%build
# libcerf does not build in place, that is why we create a build dir
mkdir build; cd build
%cmake ..
%make_build


%install
cd build
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%check
cd build
make test1


%files
%license COPYING
%doc README
%{_libdir}/*.so.1*

%files devel
%{_mandir}/man3/*
%{_includedir}/*
%{_libdir}/*.so


%changelog
* Fri Nov  2 2018 José Matos <jamatos@fedoraproject.org> - 1.9-2
- rebuild for all the supported releases

* Fri Oct 19 2018 José Matos <jamatos@fedoraproject.org> - 1.9-1
- update to 1.9

* Mon Oct 15 2018 José Matos <jamatos@fedoraproject.org> - 1.8-2
- add tests

* Sun Oct 14 2018 José Abílio Matos <jamatos@fedoraproject.org> - 1.8-1
- initial package
