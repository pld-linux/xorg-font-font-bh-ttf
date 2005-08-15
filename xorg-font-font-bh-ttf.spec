# $Rev: 3199 $, $Date: 2005-08-15 12:17:57 $
#
Summary:	font-bh-ttf
Summary(pl):	font-bh-ttf
Name:		xorg-font-font-bh-ttf
Version:	0.99.0
Release:	0.01
License:	MIT
Group:		X11
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/font/font-bh-ttf-%{version}.tar.bz2
# Source0-md5:	ab5fe2f25544d820897b61b4b73efa9a
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-font-font-util
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/font-bh-ttf-%{version}-root-%(id -u -n)

%description
font-bh-ttf

%description -l pl
font-bh-ttf


%prep
%setup -q -n font-bh-ttf-%{version}


%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%{_libdir}/X11/fonts/TTF/*
