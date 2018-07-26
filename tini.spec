Name:           tini 
Version:        0.18.0
Release:        1%{?dist}
Summary:        ok

License:        MIT
URL:            https://github.com/krallin/tini
Source0:        https://github.com/krallin/tini/archive/v%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  glibc-static
BuildRequires:  gcc

%global debug_package %{nil} 

%description
A tiny but valid "init" for containers

%prep
%setup -q -n %{name}-%{version}

%build
export CC=$(which gcc)
export CFLAGS="-DPR_SET_CHILD_SUBREAPER=36 -DPR_GET_CHILD_SUBREAPER=37"
cmake . && make

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
%doc README.md LICENSE
/usr/local/bin/%{name}
/usr/local/bin/%{name}-static

%changelog
* Wed Jul 18 2018 Ricardo Martinelli de Oliveira <ricardo.martinelli.oliveira@gmail.com>
- Initial version
