Name:           boxsafe
Version:        1.6.0.0-1
Release:        1%{?dist}
Summary:        boxsafe - hybrid storage solution provided by Cloudfort Inc
Source0:        https://gitlab.com/cloudfort_repo/boxsafe-release

BuildRequires:apache2, libapache2-mod-php7.0, mysql-server, php7.0-cli, php7.0-mysql, php-gd, php-curl, php-zip, php-dom, php-xml, mdadm, openssh-server, php-mbstring, rsync, monit

Requires:       bash 

%description    boxsafe - hybrid storage solution provided by Cloudfort Inc.

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%doc



%changelog
*Fri Mar23 2018 Qianqian Chen <qianqian.chen@cloudfortdata.com> -1.6.0.0-1
