%global         _hardened_build     1

%global         unit_user           unit
%global         unit_group          unit
%global         unit_uid            967
%global         unit_gid            967

%bcond_without  perl
%bcond_without  python27
%bcond_without  python34
%bcond_without  python36
%bcond_without  php
%bcond_without  ruby

Name:           unit
Version:        1.4
Release:        1%{?dist}
Summary:        A dynamic web and application server.

Group:          System Environment/Daemons
License:        ASL 2.0
URL:            https://unit.nginx.org/
Source0:        https://github.com/nginx/unit/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source10:       unit.service
Source11:       unit.sysconfig
Source12:       unit.logrotate
Source13:       unit.tmpfiles
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%systemd_requires
BuildRequires:  openssl-devel
Requires:       openssl

%description
NGINX Unit is a dynamic web and application server, designed to run applications in multiple languages. Unit is lightweight, polyglot, and dynamically configured via API. The design of the server allows reconfiguration of specific application parameters as needed by the engineering or operations.

%files
%defattr(-,root,root,-)
%doc CHANGES LICENSE NOTICE README
%attr(755,root,root) %{_sbindir}/unitd

%attr(700,root,root) %dir %{_sysconfdir}/unit
%attr(700,root,root) %dir %{_localstatedir}/log/unit

%config(noreplace) %{_unitdir}/unit.service
%config(noreplace) %{_sysconfdir}/sysconfig/unit
%config(noreplace) %{_sysconfdir}/logrotate.d/unit
%config(noreplace) %{_tmpfilesdir}/unit.conf


%if %{with perl}
%package perl
Summary:        NGINX Unit perl module
BuildRequires:  perl-ExtUtils-Embed

%description perl
%{summary}

%files perl
%{_libdir}/unit/modules/perl.unit.so
%endif


%if %{with python27}
%package python27
Summary:        NGINX Unit python 2.7 module
BuildRequires:  python-devel

%description python27
%{summary}

%files python27
%{_libdir}/unit/modules/python27.unit.so
%endif


%if %{with python34}
%package python34
Summary:        NGINX Unit python 3.4 module
BuildRequires:  python34-devel

%description python34
%{summary}

%files python34
%{_libdir}/unit/modules/python34.unit.so
%endif


%if %{with python36}
%package python36
Summary:        NGINX Unit python 3.6 module
BuildRequires:  python36-devel

%description python36
%{summary}

%files python36
%{_libdir}/unit/modules/python36.unit.so
%endif


%if %{with php}
%package php
Summary:        NGINX Unit PHP 5.4 module
BuildRequires:  php-devel php-embedded

%description php
%{summary}

%files php
%{_libdir}/unit/modules/php.unit.so
%endif


%if %{with ruby}
%package ruby
Summary:        NGINX Unit Ruby 2.0 module
BuildRequires:  ruby-devel

%description ruby
%{summary}

%files ruby
%{_libdir}/unit/modules/ruby.unit.so
%endif


%prep
%setup -q


%build
CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS ; 
LDFLAGS="${LDFLAGS:-%__global_ldflags}"; export LDFLAGS; 

./configure \
  --cc-opt="${CFLAGS}" \
  --ld-opt="${LDFLAGS}" \
  --prefix=%{_prefix} \
  --bindir=%{_bindir} \
  --sbindir=%{_sbindir} \
  --modules=%{_libdir}/unit/modules \
  --state=%{_sharedstatedir}/unit/state \
  --pid=%{_rundir}/unit/unit.pid \
  --log=%{_localstatedir}/log/unit/unit.log \
  --control=unix:%{_rundir}/unit/control.unit.sock \
  --user=%{unit_user} \
  --group=%{unit_group} \
  --openssl \

%if %{with perl}
./configure perl \
  --module=perl \
  --perl=%{__perl} \
%endif

%if %{with python27}
./configure python \
  --module=python27 \
  --config=python2.7-config \
  --lib-path=%{_libdir}/libpython2.7.so \
%endif

%if %{with python34}
./configure python \
  --module=python34 \
  --config=python3.4-config \
  --lib-path=%{_libdir}/libpython3.4m.so \
%endif

%if %{with python36}
./configure python \
  --module=python36 \
  --config=python3.6-config \
  --lib-path=%{_libdir}/libpython3.6m.so \
%endif

%if %{with php}
./configure php \
  --module=php \
  --lib-path=%{_libdir}/libphp5.so \
%endif

%if %{with ruby}
./configure ruby \
  --module=ruby \
  --ruby=%{_bindir}/ruby \
%endif

%make_build all


%install
[[ -d %{buildroot} ]] && rm -rf "%{buildroot}"
%{__mkdir} -p "%{buildroot}"
%make_install all

# systemd service
%{__install} -D -p -m 0400 %{SOURCE10} %{buildroot}%{_unitdir}/unit.service
%{__install} -D -p -m 0400 %{SOURCE11} %{buildroot}%{_sysconfdir}/sysconfig/unit

# log
%{__install} -d -m 0755 %{buildroot}%{_localstatedir}/log/unit
%{__install} -D -p -m 0400 %{SOURCE12} %{buildroot}%{_sysconfdir}/logrotate.d/unit

# pid/socket dir
%{__install} -d -m 0700 %{buildroot}%{_rundir}/unit
%{__install} -D -p -m 0400 %{SOURCE13} %{buildroot}%{_tmpfilesdir}/unit.conf

# config files
%{__install} -d -m 0700 %{buildroot}%{_sysconfdir}/unit


# For Ruby
export QA_RPATHS=1


%clean
rm -rf "%{buildroot}"


%pre
case $1 in
  1)
  : install
  getent group %{unit_group} >/dev/null 2>&1 \
    || groupadd -r -g %{unit_gid} %{unit_group} \
    || groupadd -r %{unit_group}

  getent passwd %{unit_user} >/dev/null 2>&1 \
    || useradd -r -g %{unit_group} -u %{unit_uid} %{unit_user} \
    || useradd -r -g %{unit_group} %{unit_user}
  ;;
  2)
  : update
  ;;
esac

%post
%systemd_post unit.service
%tmpfiles_create unit.conf
case $1 in
  1)
  : install
  ;;
  2)
  : update
  ;;
esac

%preun
%systemd_pre unit.service
case $1 in
  0)
  : uninstall
  ;;
  1)
  : update
  ;;
esac

%postun
%systemd_postun unit.service
case $1 in
  0)
  : uninstall
  getent passwd %{unit_user} >/dev/null 2>&1 \
    && userdel %{unit_user} >/dev/null 2>&1 ||:

  getent group %{unit_group} >/dev/null 2>&1 \
    && groupdel %{unit_group} >/dev/null 2>&1 ||:
  ;;
  1)
  : update
  ;;
esac


%changelog
* Wed Oct 10 2018 Ryoh Kawai <kawairyoh@gmail.com> - 1.4-1%{?dist}
- initial create
