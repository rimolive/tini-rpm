Name:           tini 
Version:        0.18.0
Release:        1%{?dist}
Summary:        Tini is the simplest init you could think of.

License:        MIT
URL:            https://github.com/krallin/tini
Source0:        https://github.com/krallin/tini/archive/v%{version}.tar.gz

BuildRequires:  cmake

%global debug_package %{nil} 

%description
A tiny but valid "init" for containers

%prep
%setup -q -n %{name}-%{version}

%build
%cmake
make

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%check
sh run_tests.sh

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%exclude %{_bindir}/%{name}-static

%changelog
* Wed Jul 18 2018 Ricardo Martinelli de Oliveira <ricardo.martinelli.oliveira@gmail.com>
- 0.18.0
- Initial version
