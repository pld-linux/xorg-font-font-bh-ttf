Summary:	bh-ttf font
Summary(pl):	Font bh-ttf
Name:		xorg-font-font-bh-ttf
Version:	0.99.1
Release:	0.1
License:	MIT
Group:		Fonts
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC3/font/font-bh-ttf-%{version}.tar.bz2
# Source0-md5:	98ba09761791c7ac31d9fd6baec66f04
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	fontconfig
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-util-util-macros
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/TTF
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
bh-ttf font.

%description -l pl
Font bh-ttf.

%prep
%setup -q -n font-bh-ttf-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-fontdir=%{_fontsdir}/TTF

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%{_fontsdir}/TTF/*.ttf
