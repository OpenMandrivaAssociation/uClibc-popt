%define _provides_exceptions libpopt.so.0\\|devel(libpopt)
%define _requires_exceptions devel(/lib/libNoVersion)

%define realname popt

%define	major 1
%define	libname %{name}%{major}

%define basedir %{_prefix}/%{_target_cpu}-linux-uclibc
%define _sysconfdir %{basedir}/etc
%define _mandir %{basedir}/usr/share/man
%define _bindir %{basedir}/usr/bin
%define _sbindir %{basedir}/usr/sbin
%define _libdir %{basedir}/usr/lib
%define _docdir %{basedir}/usr/share/doc
%define _includedir %{basedir}/usr/include
%define _lib %{basedir}/lib

Summary:	A C library for parsing command line parameters
Name:		uClibc-%{realname}
Version:	1.6.3
Release:	%mkrel 4
License:	BSD
Group:		System/Libraries
URL:		http://www.ltsp.org/
Source0:	http://ltsp.org/tarballs/%{realname}.tar.bz2
BuildRequires:	uClibc uClibc-devel uClibc-static-devel

%description
Popt is a C library for parsing command line parameters.  Popt was
heavily influenced by the getopt() and getopt_long() functions, but it
improves on them by allowing more powerful argument expansion.  Popt
can parse arbitrary argv[] style arrays and automatically set
variables based on command line arguments.  Popt allows command line
arguments to be aliased via configuration files and includes utility
functions for parsing arbitrary strings into argv[] arrays using
shell-like rules.

%package -n	%{libname}
Summary:	The popt compression and decompression library
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release} 
Requires:	uClibc

%description -n	%{libname}
Popt is a C library for parsing command line parameters.  Popt was
heavily influenced by the getopt() and getopt_long() functions, but it
improves on them by allowing more powerful argument expansion.  Popt
can parse arbitrary argv[] style arrays and automatically set
variables based on command line arguments.  Popt allows command line
arguments to be aliased via configuration files and includes utility
functions for parsing arbitrary strings into argv[] arrays using
shell-like rules.


%package -n	%{libname}-devel
Summary:	Header files and libraries for developing apps which will use popt
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release} 
Requires:	uClibc-devel uClibc-static-devel

%description -n	%{libname}-devel
Popt is a C library for parsing command line parameters.  Popt was
heavily influenced by the getopt() and getopt_long() functions, but it
improves on them by allowing more powerful argument expansion.  Popt
can parse arbitrary argv[] style arrays and automatically set
variables based on command line arguments.  Popt allows command line
arguments to be aliased via configuration files and includes utility
functions for parsing arbitrary strings into argv[] arrays using
shell-like rules.

Install popt-devel if you're a C programmer and you'd like to use its
capabilities.

%prep

%setup -q -n %{realname}

%build
rm -f rm config.cache

uclibc ./configure --libdir=%{_libdir} --mandir=%{_mandir} --includedir=%{_includedir} --disable-nls

%install
rm -rf %{buildroot}

export DONT_STRIP=1

uclibc make DESTDIR=%{buildroot} install 

%post -n %{libname} -p %{basedir}/sbin/ldconfig

%postun -n %{libname} -p %{basedir}/sbin/ldconfig

%clean
rm -fr %{buildroot}

%files -n %{libname}
%defattr(-, root, root)
%doc README
%{_libdir}/libpopt.so.0*

%files -n %{libname}-devel
%defattr(-, root, root)
%doc README CHANGES COPYING
%{_libdir}/*a
%{_libdir}/*.so
%{_includedir}/*
%{_mandir}/*/*


