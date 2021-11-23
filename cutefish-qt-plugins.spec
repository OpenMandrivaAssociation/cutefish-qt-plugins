%define oname qt-plugins

Name:           cutefish-qt-plugins
Version:        0.5
Release:        1
Summary:        Qt platform theme plugin, unified style.
License:        GPL-3.0-or-later
Group:          System/GUI
URL:            https://github.com/cutefishos/qt-plugins
Source:         https://github.com/cutefishos/qt-plugins/archive/refs/tags/%{version}/%{oname}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5ThemeSupport)
BuildRequires:  cmake(ECM)
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5XdgIconLoader)
BuildRequires:  pkgconfig(dbusmenu-qt5)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-ewmh)

%description
Unify Qt application style of CutefishOS.

%prep
%autosetup -n %{oname}-%{version} -p1

%build
%cmake
%make_build

%install
%make_install -C build

%files
%license LICENSE
%doc README.md
%{_libdir}/qt5/platformthemes/libcutefishplatformtheme.so
%{_libdir}/qt5//styles/libcutefishstyle.so
