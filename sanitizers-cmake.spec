Summary:	CMake module to enable sanitizers for binary targets
Name:		sanitizers-cmake
Version:	20241103
Release:	1
License:	MIT
Group:		Libraries
Source0:	https://github.com/arsenm/sanitizers-cmake/archive/master/%{name}-%{version}.tar.gz
# Source0-md5:	ef8f79e8241546fd36c4c6f94b09d511
URL:		https://github.com/arsenm/sanitizers-cmake/
BuildRequires:	cmake
Requires:	cmake
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CMake module to enable sanitizers for binary targets.

%prep
%setup -q -n %{name}-master

%build


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/cmake/Sanitizers

cp -p cmake/* $RPM_BUILD_ROOT%{_datadir}/cmake/Sanitizers

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%dir %{_datadir}/cmake/Sanitizers
%{_datadir}/cmake/Sanitizers/*.cmake
%attr(755, root, root) %{_datadir}/cmake/Sanitizers/asan-wrapper
