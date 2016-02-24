%define major 5
%define libname %mklibname KF5Texteditor %{major}
%define devname %mklibname KF5Texteditor -d
%define debug_package %{nil}
%define _disable_lto 1
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: ktexteditor
Version: 5.19.0
Release: 1
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/ktexteditor-%{version}.tar.xz
Summary: Advanced embeddable text editor
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Script)
BuildRequires: pkgconfig(Qt5XmlPatterns)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(libgit2)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5Archive)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5GuiAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Parts)
BuildRequires: cmake(KF5Sonnet)
BuildRequires: cmake(KF5XmlGui)
Requires: %{libname} = %{EVRD}
%rename ktexteditor5

%description
Advanced embeddable text editor.

%package -n %{libname}
Summary: Advanced embeddable text editor
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Advanced embeddable text editor.

%package -n %{devname}
Summary: Development files for the KDE Frameworks 5 Texteditor library
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files for the KDE Frameworks 5 Texteditor library.

%prep
%setup -qn ktexteditor-%{version}
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name}5

%files -f %{name}5.lang
%{_libdir}/qt5/plugins/kf5/parts/katepart.so
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
%{_libdir}/qt5/mkspecs/modules/*
