Name:           tini 
Version:        0.18.0
Release:        1%{?dist}
Summary:        ok

License:        MIT
URL:            https://github.com/krallin/tini
Source0:        https://github.com/krallin/tini/archive/v%{version}.tar.gz

BuildRequires:  cmake

%description
A tiny but valid "init" for containers

%prep
%setup -q -n %{name}-%{version}


%build
export CFLAGS="-DPR_SET_CHILD_SUBREAPER=36 -DPR_GET_CHILD_SUBREAPER=37"
cmake . && make

%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%license add-license-file-here
%doc add-docs-here



%changelog
* Wed Jul 18 2018 Ricardo Martinelli de Oliveira <ricardo.martinelli.oliveira@gmail.com>
- Initial version
