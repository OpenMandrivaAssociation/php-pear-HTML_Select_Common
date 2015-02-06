%define		_class		HTML
%define		_subclass	Select
%define		upstream_name	%{_class}_%{_subclass}_Common

Name:		php-pear-%{upstream_name}
Version:	1.2.0
Release:	5
Summary:	Small classes to handle common <select> lists
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/HTML_Select_Common/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
Obsoletes:	php-pear-HTML_Select
BuildArch:	noarch
BuildRequires:	php-pear

%description
Provides <select>lists for:
 - Country
 - UK counties
 - US States

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

chmod 644 %{upstream_name}-%{version}/examples/*

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/examples
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml




%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-3mdv2012.0
+ Revision: 742003
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-2
+ Revision: 679354
- mass rebuild

* Wed Dec 29 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-1mdv2011.0
+ Revision: 625892
- 1.2.0

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1-12mdv2011.0
+ Revision: 613680
- the mass rebuild of 2010.1 packages

* Sat Dec 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.1-11mdv2010.1
+ Revision: 477883
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.1-10mdv2010.0
+ Revision: 441179
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.1-9mdv2009.1
+ Revision: 322121
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.1-8mdv2009.0
+ Revision: 236880
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.1-7mdv2007.0
+ Revision: 81670
- Import php-pear-HTML_Select_Common

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.1-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1-1mdk
- initial Mandriva package (PLD import)

