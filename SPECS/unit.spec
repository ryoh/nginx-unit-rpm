%global         _hardened_build     1

%global         unit_user           unit
%global         unit_group          unit
%global         unit_uid            967
%global         unit_gid            967

%global         gopath              /usr/share/go/contrib

%bcond_without  perl
%bcond_without  python27
%bcond_without  python34
%bcond_without  python36
%bcond_without  php
%bcond_without  ruby
%bcond_without  nodejs
%bcond_without  go

%bcond_with     php56
%bcond_with     php70
%bcond_with     php71
%bcond_with     ruby23
%bcond_with     ruby24
%bcond_with     ruby25


Name:           unit
Version:        1.5
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


%if %{with nodejs}
BuildRequires:  nodejs npm
BuildRequires:  nodejs-devel node-gyp
Requires:       %{name} = %{version}
Requires:       nodejs npm
%endif

%description
NGINX Unit is a dynamic web and application server, designed to run applications in multiple languages. Unit is lightweight, polyglot, and dynamically configured via API. The design of the server allows reconfiguration of specific application parameters as needed by the engineering or operations.

%files
%defattr(-,root,root,-)
%doc CHANGES LICENSE NOTICE README
%attr(755,root,root) %{_sbindir}/unitd

%attr(700,root,root) %dir %{_sysconfdir}/unit
%attr(700,root,root) %dir %{_localstatedir}/log/unit
%attr(700,root,root) %dir %{_sharedstatedir}/unit
%attr(700,root,root) %dir %{_sharedstatedir}/unit/state
%attr(700,root,root) %dir %{_libdir}/unit/modules

%config(noreplace) %{_unitdir}/unit.service
%config(noreplace) %{_sysconfdir}/sysconfig/unit
%config(noreplace) %{_sysconfdir}/logrotate.d/unit
%config(noreplace) %{_tmpfilesdir}/unit.conf


%if %{with perl}
%package perl
Summary:        NGINX Unit perl module
BuildRequires:  perl-ExtUtils-Embed
Requires:       %{name} = %{version}

%description perl
%{summary}

%files perl
%{_libdir}/unit/modules/perl.unit.so
%endif


%if %{with python27}
%package python27
Summary:        NGINX Unit python 2.7 module
BuildRequires:  python-devel
Requires:       %{name} = %{version}
Requires:       python

%description python27
%{summary}

%files python27
%{_libdir}/unit/modules/python27.unit.so
%endif


%if %{with python34}
%package python34
Summary:        NGINX Unit python 3.4 module
BuildRequires:  python34-devel
Requires:       %{name} = %{version}
Requires:       python34

%description python34
%{summary}

%files python34
%{_libdir}/unit/modules/python34.unit.so
%endif


%if %{with python36}
%package python36
Summary:        NGINX Unit python 3.6 module
BuildRequires:  python36-devel
Requires:       %{name} = %{version}
Requires:       python36

%description python36
%{summary}

%files python36
%{_libdir}/unit/modules/python36.unit.so
%endif


%if %{with php}
%package php
Summary:        NGINX Unit PHP 5.4 module
BuildRequires:  php-devel php-embedded
Requires:       %{name} = %{version}
BuildRequires:  php-embedded

%description php
%{summary}

%files php
%{_libdir}/unit/modules/php.unit.so
%endif


%if %{with php56}
%package php56
Summary:        NGINX Unit PHP 5.6 module
AutoReq:        0
BuildRequires:  centos-release-scl
BuildRequires:  rh-php56-php-devel rh-php56-php-embedded
Requires:       %{name} = %{version}
Requires(pre):       centos-release-scl
Requires:       rh-php56-php-embedded

%description php56
%{summary}

%files php56
%{_libdir}/unit/modules/php56.unit.so
%endif


%if %{with php70}
%package php70
Summary:        NGINX Unit PHP 7.0 module
AutoReq:        0
BuildRequires:  centos-release-scl
BuildRequires:  rh-php70-php-devel rh-php70-php-embedded
Requires:       %{name} = %{version}
Requires:       centos-release-scl
Requires:       rh-php70-php-embedded

%description php70
%{summary}

%files php70
%{_libdir}/unit/modules/php70.unit.so
%endif


%if %{with php71}
%package php71
Summary:        NGINX Unit PHP 7.1 module
AutoReq:        0
BuildRequires:  centos-release-scl
BuildRequires:  rh-php71-php-devel rh-php71-php-embedded
Requires:       %{name} = %{version}
Requires:       centos-release-scl
Requires:       rh-php71-php-embedded

%description php71
%{summary}

%files php71
%{_libdir}/unit/modules/php71.unit.so
%endif


%if %{with ruby}
%package ruby
Summary:        NGINX Unit Ruby 2.0 module
BuildRequires:  ruby-devel
Requires:       %{name} = %{version}
Requires:       rubygem-rack

%description ruby
%{summary}

%files ruby
%{_libdir}/unit/modules/ruby.unit.so
%endif


%if %{with ruby23}
%package ruby23
Summary:        NGINX Unit Ruby 2.3 module
BuildRequires:  centos-release-scl
BuildRequires:  rh-ruby23-ruby-devel
Requires:       %{name} = %{version}
Requires:       centos-release-scl
Requires:       rh-ruby23-ruby

%description ruby23
%{summary}

%files ruby23
%{_libdir}/unit/modules/ruby23.unit.so
%endif


%if %{with ruby24}
%package ruby24
Summary:        NGINX Unit Ruby 2.4 module
BuildRequires:  centos-release-scl
BuildRequires:  rh-ruby24-ruby-devel
Requires:       %{name} = %{version}
Requires:       centos-release-scl
Requires:       rh-ruby24-ruby

%description ruby24
%{summary}

%files ruby24
%{_libdir}/unit/modules/ruby24.unit.so
%endif


%if %{with ruby25}
%package ruby25
Summary:        NGINX Unit Ruby 2.5 module
BuildRequires:  centos-release-scl
BuildRequires:  rh-ruby25-ruby-devel
Requires:       %{name} = %{version}
Requires:       centos-release-scl
Requires:       rh-ruby25-ruby

%description ruby25
%{summary}

%files ruby25
%{_libdir}/unit/modules/ruby25.unit.so
%endif


%if %{with go}
%package go
Summary:        NGINX Unit Go module
BuildRequires:  golang
Requires:       %{name} = %{version}
Requires:       golang

%description go
%{summary}

%files go
%{gopath}/src/nginx/unit/ldflags-lrt.go
%{gopath}/src/nginx/unit/port.go
%{gopath}/src/nginx/unit/request.go
%{gopath}/src/nginx/unit/response.go
%{gopath}/src/nginx/unit/unit.go
%{gopath}/src/nginx/unit/nxt_application.h
%{gopath}/src/nginx/unit/nxt_array.h
%{gopath}/src/nginx/unit/nxt_atomic.h
%{gopath}/src/nginx/unit/nxt_auto_config.h
%{gopath}/src/nginx/unit/nxt_buf.h
%{gopath}/src/nginx/unit/nxt_buf_filter.h
%{gopath}/src/nginx/unit/nxt_buf_pool.h
%{gopath}/src/nginx/unit/nxt_cache.h
%{gopath}/src/nginx/unit/nxt_cert.h
%{gopath}/src/nginx/unit/nxt_cgo_lib.c
%{gopath}/src/nginx/unit/nxt_cgo_lib.h
%{gopath}/src/nginx/unit/nxt_clang.h
%{gopath}/src/nginx/unit/nxt_conf.h
%{gopath}/src/nginx/unit/nxt_conn.h
%{gopath}/src/nginx/unit/nxt_djb_hash.h
%{gopath}/src/nginx/unit/nxt_dyld.h
%{gopath}/src/nginx/unit/nxt_errno.h
%{gopath}/src/nginx/unit/nxt_event_engine.h
%{gopath}/src/nginx/unit/nxt_fastcgi_source.h
%{gopath}/src/nginx/unit/nxt_fd_event.h
%{gopath}/src/nginx/unit/nxt_fiber.h
%{gopath}/src/nginx/unit/nxt_file.h
%{gopath}/src/nginx/unit/nxt_file_event.h
%{gopath}/src/nginx/unit/nxt_file_name.h
%{gopath}/src/nginx/unit/nxt_hash.h
%{gopath}/src/nginx/unit/nxt_http.h
%{gopath}/src/nginx/unit/nxt_http_parse.h
%{gopath}/src/nginx/unit/nxt_http_source.h
%{gopath}/src/nginx/unit/nxt_job.h
%{gopath}/src/nginx/unit/nxt_job_file.h
%{gopath}/src/nginx/unit/nxt_job_resolve.h
%{gopath}/src/nginx/unit/nxt_list.h
%{gopath}/src/nginx/unit/nxt_listen_socket.h
%{gopath}/src/nginx/unit/nxt_log.h
%{gopath}/src/nginx/unit/nxt_log_moderation.h
%{gopath}/src/nginx/unit/nxt_lvlhsh.c
%{gopath}/src/nginx/unit/nxt_lvlhsh.h
%{gopath}/src/nginx/unit/nxt_main.h
%{gopath}/src/nginx/unit/nxt_main_process.h
%{gopath}/src/nginx/unit/nxt_malloc.h
%{gopath}/src/nginx/unit/nxt_mem_map.h
%{gopath}/src/nginx/unit/nxt_mem_pool_cleanup.h
%{gopath}/src/nginx/unit/nxt_mem_zone.h
%{gopath}/src/nginx/unit/nxt_mp.h
%{gopath}/src/nginx/unit/nxt_murmur_hash.c
%{gopath}/src/nginx/unit/nxt_murmur_hash.h
%{gopath}/src/nginx/unit/nxt_parse.h
%{gopath}/src/nginx/unit/nxt_port.h
%{gopath}/src/nginx/unit/nxt_port_hash.h
%{gopath}/src/nginx/unit/nxt_port_memory.h
%{gopath}/src/nginx/unit/nxt_port_memory_int.h
%{gopath}/src/nginx/unit/nxt_port_rpc.h
%{gopath}/src/nginx/unit/nxt_process.h
%{gopath}/src/nginx/unit/nxt_process_type.h
%{gopath}/src/nginx/unit/nxt_queue.h
%{gopath}/src/nginx/unit/nxt_random.h
%{gopath}/src/nginx/unit/nxt_rbtree.h
%{gopath}/src/nginx/unit/nxt_recvbuf.h
%{gopath}/src/nginx/unit/nxt_router.h
%{gopath}/src/nginx/unit/nxt_runtime.h
%{gopath}/src/nginx/unit/nxt_semaphore.h
%{gopath}/src/nginx/unit/nxt_sendbuf.h
%{gopath}/src/nginx/unit/nxt_service.h
%{gopath}/src/nginx/unit/nxt_signal.h
%{gopath}/src/nginx/unit/nxt_sockaddr.h
%{gopath}/src/nginx/unit/nxt_socket.h
%{gopath}/src/nginx/unit/nxt_sort.h
%{gopath}/src/nginx/unit/nxt_source.h
%{gopath}/src/nginx/unit/nxt_spinlock.h
%{gopath}/src/nginx/unit/nxt_sprintf.h
%{gopath}/src/nginx/unit/nxt_stream_source.h
%{gopath}/src/nginx/unit/nxt_string.h
%{gopath}/src/nginx/unit/nxt_test_build.h
%{gopath}/src/nginx/unit/nxt_thread.h
%{gopath}/src/nginx/unit/nxt_thread_id.h
%{gopath}/src/nginx/unit/nxt_thread_log.h
%{gopath}/src/nginx/unit/nxt_thread_pool.h
%{gopath}/src/nginx/unit/nxt_thread_time.h
%{gopath}/src/nginx/unit/nxt_time.h
%{gopath}/src/nginx/unit/nxt_timer.h
%{gopath}/src/nginx/unit/nxt_tls.h
%{gopath}/src/nginx/unit/nxt_types.h
%{gopath}/src/nginx/unit/nxt_unicode_lowcase.h
%{gopath}/src/nginx/unit/nxt_unicode_macosx_lowcase.h
%{gopath}/src/nginx/unit/nxt_unit.c
%{gopath}/src/nginx/unit/nxt_unit.h
%{gopath}/src/nginx/unit/nxt_unit_field.h
%{gopath}/src/nginx/unit/nxt_unit_request.h
%{gopath}/src/nginx/unit/nxt_unit_response.h
%{gopath}/src/nginx/unit/nxt_unit_sptr.h
%{gopath}/src/nginx/unit/nxt_unit_typedefs.h
%{gopath}/src/nginx/unit/nxt_unix.h
%{gopath}/src/nginx/unit/nxt_upstream.h
%{gopath}/src/nginx/unit/nxt_upstream_source.h
%{gopath}/src/nginx/unit/nxt_utf8.h
%{gopath}/src/nginx/unit/nxt_vector.h
%{gopath}/src/nginx/unit/nxt_work_queue.h
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
  --config=%{_bindir}/php-config \
  --lib-path=%{_libdir} \
%endif

%if %{with php56}
./configure php \
  --module=php56 \
  --config=/opt/rh/rh-php56/root/bin/php-config \
  --lib-path=/opt/rh/rh-php56/root%{_libdir} \
%endif

%if %{with php70}
./configure php \
  --module=php70 \
  --config=/opt/rh/rh-php70/root/bin/php-config \
  --lib-path=/opt/rh/rh-php70/root%{_libdir} \
%endif

%if %{with php71}
./configure php \
  --module=php71 \
  --config=/opt/rh/rh-php71/root/bin/php-config \
  --lib-path=/opt/rh/rh-php71/root%{_libdir} \
%endif

%if %{with ruby}
./configure ruby \
  --module=ruby \
  --ruby=%{_bindir}/ruby \
%endif

%if %{with ruby23}
source /opt/rh/rh-ruby23/enable
./configure ruby \
  --module=ruby23 \
  --ruby=/opt/rh/rh-ruby23/root/bin/ruby \
%endif

%if %{with ruby24}
source /opt/rh/rh-ruby24/enable
./configure ruby \
  --module=ruby24 \
  --ruby=/opt/rh/rh-ruby24/root/bin/ruby \
%endif

%if %{with ruby25}
source /opt/rh/rh-ruby25/enable
./configure ruby \
  --module=ruby25 \
  --ruby=/opt/rh/rh-ruby25/root/bin/ruby \
%endif

%if %{with go}
./configure go \
  --go=%{_bindir}/go \
  --go-path=%{gopath} \
%endif

%if %{with nodejs}
./configure nodejs \
  --node=%{_bindir}/node \
  --npm=%{_bindir}/npm \
  --node-gyp=%{_bindir}/node-gyp \
%endif

%make_build


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
export QA_RPATHS=3


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
* Mon Oct 29 2018 Ryoh Kawai <kawairyoh@gmail.com> - 1.5-2%{?dist}
- Add Node.JS
* Mon Oct 29 2018 Ryoh Kawai <kawairyoh@gmail.com> - 1.5-1%{?dist}
- Bump up 1.5
* Fri Oct 19 2018 Ryoh Kawai <kawairyoh@gmail.com> - 1.4-2%{?dist}
- Add PHP 5.6/7.0/7.1 modules  (from scl package)
- Add Ruby 2.3/2.4/2.5 modules (from scl package)
* Wed Oct 10 2018 Ryoh Kawai <kawairyoh@gmail.com> - 1.4-1%{?dist}
- initial create
