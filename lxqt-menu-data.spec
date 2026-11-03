%define major 0
%define devname %mklibname lxqt-menu-data -d

Name: lxqt-menu-data
Version: 2.5.0
Release: 1
Source0: https://github.com/lxqt/lxqt-menu-data/releases/download/%{version}/lxqt-menu-data-%{version}.tar.xz
Summary: Menu files for LXQt Panel, Configuration Center and PCManFM-Qt/libfm-qt
URL: https://github.com/lxqt/lxqt-menu-data
License: GPL
Group: System/Libraries
BuildSystem: cmake
BuildRequires: cmake(lxqt2-build-tools) >= 2.5.0
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6LinguistTools)
BuildArch: noarch

%description
Menu files for LXQt Panel, Configuration Center and PCManFM-Qt/libfm-qt

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{name} = %{EVRD}
# Fix misnamed package that somehow made it into abf
%if "%{_lib}" != "lib"
Obsoletes: liblxqt-menu-data-devel < %{EVRD}
%endif

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Menu files for LXQt Panel, Configuration Center and PCManFM-Qt/libfm-qt

%files
%{_sysconfdir}/xdg/menus/*
%{_datadir}/desktop-directories

%files -n %{devname}
%{_datadir}/cmake/*
