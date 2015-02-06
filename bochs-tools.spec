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
URL: http://www.bablokb.de/%{name}/
BuildRoot: %{_tmppath}/%{name}-root
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

%clean
if test "/" != "$RPM_BUILD_ROOT"; then rm -rf $RPM_BUILD_ROOT; fi

%files
%defattr(-,root,root)
%doc ChangeLog COPYING NEWS README TODO
%{_bindir}/*
%{_mandir}/man1/*



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.6.4-6mdv2011.0
+ Revision: 616810
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 1.6.4-5mdv2010.0
+ Revision: 424665
- rebuild

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 1.6.4-4mdv2009.0
+ Revision: 240447
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Aug 15 2007 Pascal Terjan <pterjan@mandriva.org> 1.6.4-2mdv2008.0
+ Revision: 63812
- Add P0 to fix build on x86
- % Silence setup


* Wed Dec 07 2005 Lenny Cartier <lenny@mandriva.com> 1.6.4-2mdk
- rebuild

* Mon Apr 26 2004 Guillaume Bedot <guillaume.bedot@wanadoo.fr> 1.6.4-1mdk
- First package for Mandrakelinux inspired from the one in the sources...

