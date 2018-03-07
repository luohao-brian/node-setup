Name: node-setup
Summary: Tool for node setup
Version: 1.0.0
Release: 1.0%{?dist}
Source: %{name}-%{version}.tar.gz

Group: System Environment/Base
URL: https://github.com/luohao-brian/node-setup
License: GPLv2

%description
Tool for node setup.

%prep
%setup -q 

%build

%install
install -d -m 755 %{buildroot}/%{_unitdir}
install -d -m 755 %{buildroot}%{_sbindir}

# install ip*tables.h header files
install -m 755 node-setup %{buildroot}%{_sbindir}
# install systemd service files
install -c -m 644 node-setup.service %{buildroot}/%{_unitdir}

%post 
%systemd_post node-setup.service 

%preun 
%systemd_preun node-setup.service 

%postun 
%systemd_postun node-setup.service

%files 
%{_sbindir}/node-setup
%{_unitdir}/node-setup.service


%changelog
* Thu Sep 6 2018 Luo Hao - 1.0.0
- Initial setup
