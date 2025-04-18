%define major 0
%define devname %mklibname lxqt-menu-data -d

Name: lxqt-menu-data
Version: 2.2.0
Release: 1
Source0: https://github.com/lxqt/lxqt-menu-data/archive/%{version}/%{name}-%{version}.tar.gz
Summary: Menu files for LXQt Panel, Configuration Center and PCManFM-Qt/libfm-qt
URL: https://github.com/lxqt/lxqt-menu-data
License: GPL
Group: System/Libraries
BuildRequires: cmake ninja
BuildRequires: cmake(lxqt2-build-tools)
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

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Menu files for LXQt Panel, Configuration Center and PCManFM-Qt/libfm-qt

%prep
%autosetup -p1
%cmake \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_sysconfdir}/xdg/menus/*
%{_datadir}/desktop-directories

%files -n %{devname}
%{_datadir}/cmake/*
