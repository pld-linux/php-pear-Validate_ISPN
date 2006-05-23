%include	/usr/lib/rpm/macros.php
%define		_class		Validate
%define		_subclass	ISPN
%define		_status		alpha
%define		_pearname	Validate_ISPN

Summary:	%{_pearname} - validation class for ISPN (International Standard Product Numbers)
Summary(pl):	%{_pearname} - klasa sprawdzania poprawno¶ci ISPN (Internation Standard Product Numbers)
Name:		php-pear-%{_pearname}
Version:	0.6.0
Release:	1
License:	New BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	89d76b103dbc68aa2002fd793f319d7f
URL:		http://pear.php.net/package/Validate_ISPN/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.1.0
Requires:	php-pear
Requires:	php-pear-Validate >= 0.5.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Package containes ISPN (International Standard Product Numbers)
validations such as:
 - ISSN
 - ISBN
 - ISMN
 - ISRC (International Standard Recording Code)
 - EAN8
 - EAN13
 - EAN14
 - UCC12
 - SSCC

In PEAR status of this package is: %{_status}.

%description -l pl
Ten pakiet zawiera metody sprawdzania poprawno¶ci ISPN (Internation
Standard Product Numbers) takich jak:
 - ISSN
 - ISBN
 - ISMN
 - ISRC (International Standard Recording Code)
 - EAN8
 - EAN13
 - EAN14
 - UCC12
 - SSCC

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/%{_pearname}/LICENSE
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Validate/ISPN.php
