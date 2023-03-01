Summary:	Bigelow & Holmes Luxi font in TrueType format
Summary(pl.UTF-8):	Font Bigelow & Holmes Luxi w formacie TrueType
Name:		xorg-font-font-bh-ttf
Version:	1.0.4
Release:	1
License:	distributable if unmodified
Group:		Fonts
Source0:	https://xorg.freedesktop.org/releases/individual/font/font-bh-ttf-%{version}.tar.xz
# Source0-md5:	063bfa1456c8a68208bf96a33f472bb1
Patch0:		fontconfig-2.10.patch
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	fontconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-font-font-util >= 1.2
BuildRequires:	xorg-util-util-macros >= 1.20
BuildRequires:	xz
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/TTF
Requires:	fontconfig >= 1:2.10.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bigelow & Holmes Luxi font in TrueType format.

%description -l pl.UTF-8
Font Bigelow & Holmes Luxi w formacie TrueType.

%prep
%setup -q -n font-bh-ttf-%{version}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
%if "%{_gnu}" != "-gnux32"
	--build=%{_host} \
	--host=%{_host} \
%endif
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
%doc COPYING ChangeLog README.md
%{_fontsdir}/TTF/luxi*.ttf
%{_datadir}/fontconfig/conf.avail/42-luxi-mono.conf
%config(noreplace,missingok) %verify(not link md5 mtime size) /etc/fonts/conf.d/42-luxi-mono.conf
