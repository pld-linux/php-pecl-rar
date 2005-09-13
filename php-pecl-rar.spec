%define		_modname	rar
%define		_status		alpha

Summary:	%{_modname} - read rar archives
Summary(pl):	%{_modname} - odczyt archiwów rar
Name:		php-pecl-%{_modname}
Version:	0.2
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	9d79f80d11a9deb915219a41850c5071
URL:		http://pecl.php.net/package/rar/
BuildRequires:	php-devel
Requires:	php-common
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php
%define		extensionsdir	%{_libdir}/php

%description
Rar is a powerful and effective archiver, which was created by Eugene
Roshal and became rather popular quite fast. This extension gives you
possibility to read Rar archives.

In PECL status of this extension is: %{_status}.

%description -l pl
Rar to potê¿ny i wydajny archiwizator. Zosta³ stworzony przez Eugene
Roshala i szybko zdoby³ popularno¶æ. Z pomoc± tego rozszerzenia
mo¿liwy jest odczyt archiwów Rar.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{extensionsdir}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/php-module-install install %{_modname} %{_sysconfdir}/php-cgi.ini

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove %{_modname} %{_sysconfdir}/php-cgi.ini
fi

%files
%defattr(644,root,root,755)
%doc %{_modname}-%{version}/CREDITS
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
