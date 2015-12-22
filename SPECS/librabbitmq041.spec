%define	_original_name librabbitmq

Name:      librabbitmq071
Summary:   Client library for AMQP
Version:   0.7.1
Release:   1%{?dist}
License:   MIT
Group:     System Environment/Libraries
URL:       https://github.com/alanxz/rabbitmq-c

Source0:   https://github.com/alanxz/rabbitmq-c/archive/rabbitmq-c-%{version}.tar.gz

BuildRequires: libtool
BuildRequires: python-simplejson
# For tools
BuildRequires: popt-devel
# For man page
BuildRequires: xmlto
Conflicts:     %{_original_name}


%description
This is a C-language AMQP client library for use with AMQP servers
speaking protocol versions 0-9-1.


%package devel
Summary:    Header files and development libraries for %{name}
Group:      Development/Libraries
Requires:   %{name}%{?_isa} = %{version}-%{release}
Conflicts:  %{_original_name}-devel

%description devel
This package contains the header files and development libraries
for %{name}.


%package tools
Summary:    Example tools built using the librabbitmq package
Group:      Development/Libraries
Requires:   %{name}%{?_isa} = %{version}
Conflicts:  %{_original_name}-tools

%description tools
This package contains example tools built using %{name}.

It provides:
amqp-consume        Consume messages from a queue on an AMQP server
amqp-declare-queue  Declare a queue on an AMQP server
amqp-delete-queue   Delete a queue from an AMQP server
amqp-get            Get a message from a queue on an AMQP server
amqp-publish        Publish a message on an AMQP server


%prep
%setup -q -n rabbitmq-c-%{version}

# Copy sources to be included in -devel docs.
cp -pr examples Examples


%build
autoreconf -i
%configure --enable-tools --enable-docs
make %{_smp_mflags}


%install
make install  DESTDIR="%{buildroot}"
rm %{buildroot}%{_libdir}/%{_original_name}.la


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%doc AUTHORS README.md THANKS TODO LICENSE-MIT
%{_libdir}/%{_original_name}.so.4*


%files devel
%doc Examples
%{_libdir}/%{_original_name}.so
%{_includedir}/amqp*
%{_libdir}/pkgconfig/librabbitmq.pc

%files tools
%{_bindir}/amqp-*
%doc %{_mandir}/man1/amqp-*.1*
%doc %{_mandir}/man7/librabbitmq-tools.7.gz


%changelog
* Tue Dec 12 2015 Ilya Otyutskiy <ilya.otyutskiy@icloud.com> - 0.7.1-1.vortex
- Update to 0.7.1.

* Tue Feb  4 2014 Ilya Otyutskiy <ilya.otyutskiy@icloud.com> - 0.4.1-1.vortex
- Update to 0.4.1.

* Thu Aug  1 2013 Remi Collet <remi@fedoraproject.org> - 0.3.0-1
- update to 0.3.0
- create sub-package for tools
- License is now MIT

* Sun Mar 11 2012 Remi Collet <remi@fedoraproject.org> - 0.1-0.2.hgfb6fca832fd2
- add %%check (per review comment)

* Sat Mar 10 2012 Remi Collet <remi@fedoraproject.org> - 0.1-0.1.hgfb6fca832fd2
- Initial RPM

