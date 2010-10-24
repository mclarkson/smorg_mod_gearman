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
Patch1: log_location.patch
Patch1: chkconfig.patch
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
install -D -m 755 mod_gearman.o ${RPM_BUILD_ROOT}%_libdir/mod_gearman/neb/mod_gearman.o
install -D -m 755 mod_gearman_worker ${RPM_BUILD_ROOT}%_bindir/mod_gearman_worker
install -D -m 755 etc/mod_gearman.conf ${RPM_BUILD_ROOT}%_sysconfdir/mod_gearman.conf
install -D -m 755 worker/initscript ${RPM_BUILD_ROOT}%_sysconfdir/init.d/mod_gearman_worker
install -D -m 755 gearman_top ${RPM_BUILD_ROOT}%_bindir/gearman_top
# send_gearman is like send_nsca
install -D -m 755 send_gearman ${RPM_BUILD_ROOT}%_bindir/send_gearman
# check_gearman is a nagios check but useful on its own any way
install -D -m 755 check_gearman ${RPM_BUILD_ROOT}%_bindir/check_gearman

%clean
#%{__rm} -rf %{buildroot}

%files
%{_libdir}/mod_gearman/neb/mod_gearman.o
%{_bindir}/mod_gearman_worker
%{_bindir}/gearman_top
%{_bindir}/send_gearman
%{_bindir}/check_gearman
%{_sysconfdir}/mod_gearman.conf
%{_sysconfdir}/init.d/mod_gearman_worker

%post
/sbin/chkconfig --add mod_gearman_worker

%changelog
* Sat Oct 23 2010 Mark Clarkson  <ext-mark.clarkson@nokia.com> - 0.1-1
- Initial package
