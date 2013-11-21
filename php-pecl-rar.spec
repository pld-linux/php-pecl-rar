%define		php_name	php%{?php_suffix}
%define		modname	rar
%define		status		stable
Summary:	%{modname} - read rar archives
Summary(pl.UTF-8):	%{modname} - odczyt archiwów rar
Name:		%{php_name}-pecl-%{modname}
Version:	3.0.2
Release:	1
License:	PHP 3.01
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
# Source0-md5:	3015ec07e0a42d2f365abed2fa3c0f6e
URL:		http://pecl.php.net/package/rar/
BuildRequires:	libstdc++-devel
BuildRequires:	%{php_name}-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.650
%{?requires_php_extension}
Requires:	php(core) >= 5.0.4
Obsoletes:	php-pear-%{modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rar is a powerful and effective archiver, which was created by Eugene
Roshal and became rather popular quite fast. This extension gives you
possibility to read Rar archives.

In PECL status of this extension is: %{status}.

%description -l pl.UTF-8
Rar to potężny i wydajny archiwizator. Został stworzony przez Eugene
Roshala i szybko zdobył popularność. Z pomocą tego rozszerzenia
możliwy jest odczyt archiwów Rar.

To rozszerzenie ma w PECL status: %{status}.

%prep
%setup -qc
mv %{modname}-%{version}*/* .

%build
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}
install -p modules/%{modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{modname}.ini
; Enable %{modname} extension module
extension=%{modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%doc CREDITS README
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{modname}.so
