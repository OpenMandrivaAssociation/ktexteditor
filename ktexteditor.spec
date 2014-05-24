%define major 5
%define libname %mklibname KF5Texteditor %{major}
%define devname %mklibname KF5Texteditor -d
%define debug_package %{nil}

Name: ktexteditor5
Version: 4.99.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/unstable/frameworks/%{version}/ktexteditor-%{version}.tar.xz
Summary: Advanced embeddable text editor
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5)
BuildRequires: cmake(KF5Archive)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5GuiAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Parts)
BuildRequires: cmake(KF5Sonnet)
BuildRequires: ninja
Requires: %{libname} = %{EVRD}

%description
Advanced embeddable text editor

%package -n %{libname}
Summary: Advanced embeddable text editor
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Advanced embeddable text editor

%package -n %{devname}
Summary: Development files for the KDE Frameworks 5 Texteditor library
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files for the KDE Frameworks 5 Texteditor library

%prep
%setup -qn ktexteditor-%{version}
%cmake -G Ninja

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install %{?_smp_mflags}

%files
%{_libdir}/plugins/katepart.so
%{_sysconfdir}/xdg/kate*
%{_datadir}/katepart
%{_datadir}/katepart5
%{_datadir}/kservices5/*
%{_datadir}/kservicetypes5/*

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5*
%{_prefix}/mkspecs/*
