%define		_class		HTML
%define		_subclass	Select
%define		upstream_name	%{_class}_%{_subclass}_Common

%define		_requires_exceptions pear(HTML/Select/Common/UKCounty.php)\\|pear(HTML/Select/Common/USState.php)\\|pear(HTML/Select/Common/FRDepartements.php)\\|pear(HTML/Select/Common/Country.php)

Name:		php-pear-%{upstream_name}
Version:	1.1
Release:	%mkrel 11
Summary:	Small classes to handle common <select> lists
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/HTML_Select_Common/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
Obsoletes:	php-pear-HTML_Select
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Provides <select>lists for:
 - Country
 - UK counties
 - US States

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/%{_subclass}/Common/examples
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


