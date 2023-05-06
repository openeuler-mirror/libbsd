Name:           libbsd
Version:        0.10.0
Release:        2
Summary:        Library providing BSD-compatible functions for portability
URL:            http://libbsd.freedesktop.org/
License:        BSD and ISC and Copyright only and Public Domain

Source0:        http://libbsd.freedesktop.org/releases/libbsd-%{version}.tar.xz
# Use symver attribute for symbol versioning
Patch1:         %{name}-symver.patch
Patch2:         fix-clang.patch

BuildRequires:  gcc
BuildRequires:  autoconf automake libtool
BuildRequires:  make

%description
libbsd provides useful functions commonly found on BSD systems, and
lacking on others like GNU systems, thus making it easier to port
projects with strong BSD origins, without needing to embed the same
code over and over again on each project.

%package devel
Summary:        Development files for libbsd
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for the libbsd library.

%package ctor-static
Summary:        Development files for libbsd
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description ctor-static
The libbsd-ctor static library is required if setproctitle() is to be used
when libbsd is loaded via dlopen() from a threaded program.  This can be
configured using "pkg-config --libs libbsd-ctor".

%prep
%setup -q

%patch1 -p1 -b .symver
%patch2 -p1

%build
autoreconf -fiv
%configure
%make_build V=1

%check
%make_build check V=1

%install
%make_install V=1


rm %{buildroot}%{_libdir}/%{name}.a
rm %{buildroot}%{_libdir}/%{name}.la
rm %{buildroot}%{_mandir}/man3/explicit_bzero.3bsd


%ldconfig_scriptlets

%files
%license COPYING
%doc README TODO ChangeLog
%{_libdir}/%{name}.so.*

%files devel
%{_mandir}/man3/*.3bsd.*
%{_mandir}/man7/%{name}.7.*
%{_includedir}/bsd
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/%{name}-overlay.pc

%files ctor-static
%{_libdir}/%{name}-ctor.a
%{_libdir}/pkgconfig/%{name}-ctor.pc

%changelog
* Sat May 06 2023 yoo <sunyuechi@iscas.ac.cn> - 0.10.0-2
- fix clang build error

* Fri Jul 15 2022 misaka00251 <misaka00251@misakanet.cn> - 0.10.0-1
- Init package (Thanks to fedora team)
