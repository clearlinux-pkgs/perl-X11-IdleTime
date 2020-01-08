#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-X11-IdleTime
Version  : 0.09
Release  : 3
URL      : https://cpan.metacpan.org/authors/id/A/AW/AWENDT/X11-IdleTime-0.09.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/A/AW/AWENDT/X11-IdleTime-0.09.tar.gz
Summary  : Get the idle time of X11
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-X11-IdleTime-perl = %{version}-%{release}
Requires: perl(Inline)
BuildRequires : buildreq-cpan
BuildRequires : libX11
BuildRequires : libXScrnSaver-dev
BuildRequires : libXext-dev
BuildRequires : perl(Inline::C)
BuildRequires : perl(Inline::MakeMaker)
BuildRequires : perl(Parse::RecDescent)

%description
X11/IdleTime version 0.08
=========================
X11::IdleTime has one sub routine, GetIdleTime() which returns the number of seconds that X11 has been idle (no mouse or keyboard activity).

%package dev
Summary: dev components for the perl-X11-IdleTime package.
Group: Development
Provides: perl-X11-IdleTime-devel = %{version}-%{release}
Requires: perl-X11-IdleTime = %{version}-%{release}

%description dev
dev components for the perl-X11-IdleTime package.


%package perl
Summary: perl components for the perl-X11-IdleTime package.
Group: Default
Requires: perl-X11-IdleTime = %{version}-%{release}

%description perl
perl components for the perl-X11-IdleTime package.


%prep
%setup -q -n X11-IdleTime-0.09
cd %{_builddir}/X11-IdleTime-0.09

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/X11::IdleTime.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.1/x86_64-linux-thread-multi/X11/IdleTime.pm
/usr/lib/perl5/vendor_perl/5.30.1/x86_64-linux-thread-multi/auto/X11/IdleTime/IdleTime.so
