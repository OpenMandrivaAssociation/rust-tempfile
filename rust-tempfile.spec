# Generated by rust2rpm 10
%bcond_without check
%global debug_package %{nil}

%global crate tempfile

Name:           rust-%{crate}
Version:        3.1.0
Release:        3%{?dist}
Summary:        Library for managing temporary files and directories

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/tempfile
Source:         %{crates_source}
# Initial patched metadata
# * No Windows
# * No Redox
Patch0:         tempfile-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Library for managing temporary files and directories.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md NEWS
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 06 11:33:46 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.1.0-1
- Update to 3.1.0

* Sun Jun 30 11:50:43 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.0.9-1
- Update to 3.0.9

* Thu Jun 20 00:15:25 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.0.8-3
- Regenerate

* Sun Jun 09 21:57:26 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.0.8-2
- Regenerate

* Fri May 31 2019 Josh Stone <jistone@redhat.com> - 3.0.8-1
- Update to 3.0.8

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.0.7-1
- Update to 3.0.7

* Sun Feb 10 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.0.6-1
- Update to 3.0.6

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 03 2018 Josh Stone <jistone@redhat.com> - 3.0.5-1
- Update to 3.0.5

* Sat Oct 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.0.4-2
- Adapt to new packaging

* Thu Sep 20 2018 Josh Stone <jistone@redhat.com> - 3.0.4-1
- Update to 3.0.4

* Wed Jul 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.0.3-1
- Update to 3.0.3

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.0.2-1
- Update to 3.0.2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.2.0-3
- Rebuild for rust-packaging v5

* Sun Dec 31 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.2.0-2
- Bump rand to 0.4

* Sat Nov 04 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.2.0-1
- Update to 2.2.0

* Thu Jun 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproejct.org> - 2.1.5-4
- Drop rustc_version BR

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.5-3
- Port to use rust-packaging

* Sun Feb 26 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.5-2
- Rebuild

* Sun Feb 26 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.5-1
- Initial package
