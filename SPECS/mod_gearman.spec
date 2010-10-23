Summary: Mod Gearman Nagios NEB module
Name: mod_gearman
Version: 0.6
Release: 1
License: BSD
Group: System Environment/Libraries
BuildRequires: gcc-c++
URL: http://labs.consol.de/lang/de/nagios/mod-gearman/

Packager: Mark Clarkson <ext-mark.clarkson@nokia.com>

#Source: http://launchpad.net/gearmand/trunk/%{version}/+download/gearmand-%{version}.tar.gz
Source: mod_gearman-0.6.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Mod Gearman is a new way of distributing active Nagios checks across your network. It consists of two parts: There is a NEB module which resides in the Nagios core and adds servicechecks, hostchecks and eventhandler to a Gearman queue. There can be multiple equal gearman servers. The counterpart is one or more worker clients for the checks itself. They can be bound to host and servicegroups.

%prep
%setup -q

%configure

%build
%{__make} %{_smp_mflags}

%install
[ "$RPM_BUILD_ROOT" != "/" ] && %{__rm} -rf %{buildroot}
#%{__make} install  DESTDIR="%{buildroot}" AM_INSTALL_PROGRAM_FLAGS=""
install -m 755 mod_gearman.o ${RPM_BUILD_ROOT}%_libdir/mod_gearman/neb/mod_gearman.o

%clean
%{__rm} -rf %{buildroot}

%files
%{_libdir}/mod_gearman/neb/mod_gearman.o

%changelog
* Sat Oct 23 2010 Mark Clarkson  <ext-mark.clarkson@nokia.com> - 0.1-1
- Initial package
