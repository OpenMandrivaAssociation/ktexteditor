%define major 5
%define libname %mklibname KF5Texteditor %{major}
%define devname %mklibname KF5Texteditor -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: ktexteditor5
Version: 5.111.0
Release: 1
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/ktexteditor-%{version}.tar.xz
Summary: Advanced embeddable text editor
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Script)
BuildRequires: pkgconfig(Qt5XmlPatterns)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(libgit2) >= 0.26.0
BuildRequires: pkgconfig(editorconfig)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5Archive)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5GuiAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Parts)
BuildRequires: cmake(KF5Sonnet)
BuildRequires: cmake(KF5XmlGui)
BuildRequires: cmake(KF5SyntaxHighlighting)
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt5-assistant

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
Requires: cmake(KF5Parts)

%description -n %{devname}
Development files for the KDE Frameworks 5 Texteditor library.

%package -n %{name}-devel-docs
Summary: Developer documentation for %{name} for use with Qt Assistant
Group: Documentation
Suggests: %{devname} = %{EVRD}

%description -n %{name}-devel-docs
Developer documentation for %{name} for use with Qt Assistant.

%prep
%autosetup -p1 -n ktexteditor-%{version}
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name}

%files -f %{name}.lang
%{_datadir}/qlogging-categories5/ktexteditor.*categories
%{_libdir}/qt5/plugins/kf5/parts/katepart.so
%{_datadir}/katepart5
%{_datadir}/kservices5/*
%{_datadir}/kservicetypes5/*
%{_datadir}/dbus-1/system.d/org.kde.ktexteditor.katetextbuffer.conf
%{_libdir}/libexec/kauth/kauth_ktexteditor_helper
%{_datadir}/dbus-1/system-services/org.kde.ktexteditor.katetextbuffer.service
%{_datadir}/polkit-1/actions/org.kde.ktexteditor.katetextbuffer.policy
%{_datadir}/kdevappwizard/templates/ktexteditor-plugin.tar.bz2

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5*
%{_libdir}/qt5/mkspecs/modules/*

%files -n %{name}-devel-docs
%{_docdir}/qt5/*.{tags,qch}
