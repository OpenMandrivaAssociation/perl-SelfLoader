
%define realname   SelfLoader
%define version    1.17
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Automatic function loader (using __DATA__)
Source:     http://www.cpan.org/modules/by-module//%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel


BuildArch: noarch

%description
This module tells its users that functions in the FOOBAR package are to be
autoloaded from after the '__DATA__' token. See also the
perlsub/"Autoloading" manpage.

The __DATA__ token
    The '__DATA__' token tells the perl compiler that the perl code for
    compilation is finished. Everything after the '__DATA__' token is
    available for reading via the filehandle FOOBAR::DATA, where FOOBAR is
    the name of the current package when the '__DATA__' token is reached.
    This works just the same as '__END__' does in package 'main', but for
    other modules data after '__END__' is not automatically retrievable,
    whereas data after '__DATA__' is. The '__DATA__' token is not
    recognized in versions of perl prior to 5.001m.

    Note that it is possible to have '__DATA__' tokens in the same package
    in multiple files, and that the last '__DATA__' token in a given
    package that is encountered by the compiler is the one accessible by
    the filehandle. This also applies to '__END__' and main, i.e. if the
    'main' program has an '__END__', but a module 'require'd (_not_ 'use'd)
    by that program has a 'package main;' declaration followed by an
    ''__DATA__'', then the 'DATA' filehandle is set to access the data
    after the '__DATA__' in the module, _not_ the data after the '__END__'
    token in the 'main' program, since the compiler encounters the
    'require'd file later.

%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


