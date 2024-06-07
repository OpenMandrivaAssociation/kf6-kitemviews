%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
%define major %(echo %{version} |cut -d. -f1-2)

%define libname %mklibname KF6ItemViews
%define devname %mklibname KF6ItemViews -d
#define git 20240217

Name: kf6-kitemviews
Version: 6.3.0
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/frameworks/kitemviews/-/archive/master/kitemviews-master.tar.bz2#/kitemviews-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/frameworks/%{major}/kitemviews-%{version}.tar.xz
%endif
Summary: Set of item views extending the Qt model-view framework
URL: https://invent.kde.org/frameworks/kitemviews
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
Requires: %{libname} = %{EVRD}

%description
Set of item views extending the Qt model-view framework

%package -n %{libname}
Summary: Set of item views extending the Qt model-view framework
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Set of item views extending the Qt model-view framework

%package -n %{libname}-designer
Summary: Qt Designer support for %{name} widgets
Group: System/Libraries
Requires: %{libname} = %{EVRD}
Supplements: qt6-qttools-designer

%description -n %{libname}-designer
Qt Designer support for %{name} widgets

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Set of item views extending the Qt model-view framework

%prep
%autosetup -p1 -n kitemviews-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-qt --with-html

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/kitemviews.*

%files -n %{devname}
%{_includedir}/KF6/KItemViews
%{_libdir}/cmake/KF6ItemViews
%{_qtdir}/doc/KF6ItemViews.*

%files -n %{libname}
%{_libdir}/libKF6ItemViews.so*

%files -n %{libname}-designer
%{_qtdir}/plugins/designer/kitemviews6widgets.so
