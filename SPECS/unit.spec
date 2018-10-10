%global         _hardened_build     1

%global         unit_user           unit
%global         unit_group          unit
%global         unit_uid            967
%global         unit_gid            967

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
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  openssl-devel
Requires:       openssl

%description
NGINX Unit is a dynamic web and application server, designed to run applications in multiple languages. Unit is lightweight, polyglot, and dynamically configured via API. The design of the server allows reconfiguration of specific application parameters as needed by the engineering or operations.


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

%make_build


%install
[[ -d %{buildroot} ]] && rm -rf "%{buildroot}"
%{__mkdir} -p "%{buildroot}"
%make_install


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
#%systemd_post unit.service
case $1 in
  1)
  : install
  ;;
  2)
  : update
  ;;
esac

%preun
#%systemd_pre unit.service
case $1 in
  0)
  : uninstall
  ;;
  1)
  : update
  ;;
esac

%postun
#%systemd_postun unit.service
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


%files
%defattr(-,root,root,-)
%doc CHANGES LICENSE NOTICE README
%{_sbindir}/unitd


%changelog
* Wed Oct 10 2018 Ryoh Kawai <kawairyoh@gmail.com> - 1.4-1%{?dist}
- initial create
