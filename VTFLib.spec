Name:       VTFLib
Version:    {{{ git_dir_version }}}
Release:    1%{?dist}
Summary:    Linux port of VTFLib 

License:    GPLv2.1
URL:        https://github.com/panzi/VTFLib
VCS:        {{{ git_dir_vcs }}}
Source:     {{{ git_dir_pack }}}

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: g++

# Disable debug packages
%define debug_package %{nil}

%description
Linux port of Nem's VTFLib http://nemesis.thewavelength.net/index.php?p=40

%package devel
Summary:     Devel package for Linux port of VTFLib

%description devel
%{summary}.

%prep
{{{ git_dir_setup_macro }}}

%build
%cmake -DUSE_LIBTXC_DXTN=OFF -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install
cp %{buildroot}%{_libdir}/pkgconfig/VTFLib13.pc %{buildroot}%{_libdir}/pkgconfig/VTFLib.pc

%files
%license LGPL.txt
%doc README.md
%{_libdir}/libVTFLib*.so
%{_libdir}/pkgconfig/VTFLib*.pc

%files devel
%{_includedir}/VTFLib*
