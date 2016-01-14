%{?scl:%scl_package perl-Module-Pluggable}
%{!?scl:%global pkg_name %{name}}

%global cpan_version 5.1
Name:           %{?scl_prefix}perl-Module-Pluggable
# Epoch to compete with perl.spec
Epoch:          1
# Keep two digit decimal part
Version:        %{cpan_version}0
Release:        1.sc1%{?dist}
Summary:        Automatically give your module the ability to have plugins
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Module-Pluggable/
Source0:        http://www.cpan.org/authors/id/S/SI/SIMONW/Module-Pluggable-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl(FindBin)
BuildRequires:  %{?scl_prefix}perl(Module::Build)
BuildRequires:  %{?scl_prefix}perl(strict)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(base)
BuildRequires:  %{?scl_prefix}perl(Carp)
%if 0%(perl -e 'print $] > 5.017')
BuildRequires:  %{?scl_prefix}perl(deprecate)
%endif
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(File::Basename)
BuildRequires:  %{?scl_prefix}perl(File::Find)
BuildRequires:  %{?scl_prefix}perl(File::Spec::Functions) >= 3.00
BuildRequires:  %{?scl_prefix}perl(if)
BuildRequires:  %{?scl_prefix}perl(vars)
# Tests:
BuildRequires:  %{?scl_prefix}perl(Data::Dumper)
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.62
BuildRequires:  %{?scl_prefix}perl(warnings)
# Optional tests:
# App::FatPacker not yet packaged
#%%if !%%{defined perl_bootstrap}
#BuildRequires:  perl(App::FatPacker) >= 0.10.0
#BuildRequires:  perl(Cwd)
#BuildRequires:  perl(File::Copy)
#BuildRequires:  perl(File::Path)
#BuildRequires:  perl(File::Temp)
#%%endif
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})
Requires:       %{?scl_prefix}perl(File::Spec::Functions) >= 3.00
%if 0%(perl -e 'print $] > 5.017')
Requires:       %{?scl_prefix}perl(deprecate)
%endif

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^%{?scl_prefix}perl\\(File::Spec::Functions\\)$

%if ( 0%{?rhel} && 0%{?rhel} < 7 )
%filter_from_requires /perl(File::Spec::Functions)\s*$/d
%filter_setup
%endif

%description
This package provides a simple but, hopefully, extensible way of having
'plugins' for your module. Essentially all it does is export a method into
your name space that looks through a search path for .pm files and turn those
into class names. Optionally it instantiates those classes for you.

%prep
%setup -q -n Module-Pluggable-%{cpan_version}
find -type f -exec chmod -x {} +

%build
%{?scl:scl enable %{scl} "}
perl Build.PL installdirs=vendor
%{?scl:"}
%{?scl:scl enable %{scl} "}
./Build
%{?scl:"}

%install
%{?scl:scl enable %{scl} "}
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{?scl:"}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} "}
./Build test
%{?scl:"}

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Jan 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.10-1
- 5.1 bump
- Resolves: rhbz#1059119

* Tue Nov 19 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1:4.80-1
- 4.8 bump

* Mon May 20 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1:4.7-1
- 4.7 bump

* Mon Feb 18 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1:4.6-1
- SCL package - initial import

