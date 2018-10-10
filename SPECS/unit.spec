Name:           unit
Version:        1.4
Release:        1%{?dist}
Summary:        A dynamic web and application server.

Group:          System Environment/Daemons
License:        ASL 2.0
URL:            https://unit.nginx.org/
Source0:        https://github.com/nginx/unit/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#BuildRequires:  
#Requires:       

%description
NGINX Unit is a dynamic web and application server, designed to run applications in multiple languages. Unit is lightweight, polyglot, and dynamically configured via API. The design of the server allows reconfiguration of specific application parameters as needed by the engineering or operations.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc



%changelog
* Wed Oct 10 2018 Ryoh Kawai <kawairyoh@gmail.com> - 1.4-1%{?dist}
- initial create
