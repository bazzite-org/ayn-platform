%if 0%{?fedora}
%global debug_package %{nil}
%endif

Name:     ayn-platform
Version:  {{{ git_dir_version }}}
Release:  1%{?dist}
Summary:  Linux drivers for AYN x86 handhelds
License:  GPLv3
URL:      https://github.com/KyleGospo/ayn-platform

Source:   %{url}/archive/refs/heads/main.tar.gz

Provides: %{name}-kmod-common = %{version}
Requires: %{name}-kmod >= %{version}

BuildRequires: systemd-rpm-macros

%description
Linux drivers for AYN x86 handhelds providing a hwmon interface for pwm fan control and temperature sensors, as well as RGB control.

%prep
%setup -q -c %{name}-main

%files
%doc %{name}-main/README.md
%license %{name}-main/LICENSE

%changelog
{{{ git_dir_changelog }}}
