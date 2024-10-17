%define debug_package	%{nil}
%define name		bochs-tools
%define shortname	bochstools
%define version		1.6.4
%define release		7

Name:		%{name}
Version:	%{version}
Release:	%{release}
Source: http://www.bablokb.de/%{name}/%{shortname}-%{version}.tar.bz2
Patch0:		bochstools-1.6.4-_syscall5.patch
License: GPL
URL: https://www.bablokb.de/%{name}/
Group: Emulators
Summary: Manipulates Bochs disk-images

%description
Bochs-Tools are a collection of scripts and programs to be used together with
the Bochs-emulator. The main goal was to provide a Unix-like interface to the
emulator and to enable access to Bochs disk-images from outside of Bochs.

The tools were developed under Linux. They might also work on other
operating-systems. Feedback on this issue is appreciated. 

%prep
%setup -q -n %{shortname}-%{version}
%patch0 -p6 -b .syscall5

%build
make -C src VERSION="%{version}"

%install
make UID=0 DESTDIR="$RPM_BUILD_ROOT" PREFIX="%{_prefix}" BINDIR="%{_bindir}" \
    MANDIR="%{_mandir}" CFLAGS="$RPM_OPT_FLAGS" bins install


%files
%doc ChangeLog COPYING NEWS README TODO
%{_bindir}/*
%{_mandir}/man1/*
