Summary:	Autodesk FBX SDK library
Summary(pl.UTF-8):	Biblioteka Autodesk FBX SDK
Name:		fbxsdk
Version:	2020.0.1
Release:	0.1
License:	proprietary
Group:		Libraries
#Source0Download: https://www.autodesk.com/developer-network/platform-technologies/fbx-sdk-2020-0
Source0:	https://www.autodesk.com/content/dam/autodesk/www/adn/fbx/2020-0-1/fbx202001_fbxsdk_linux.tar.gz
# NoSource0-md5:	4771622b5a55fcbf9ff26a140e2e110d
NoSource:	0
URL:		https://www.autodesk.com/developer-network/platform-technologies/fbx-sdk-2020-0
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The FBX SDK is a C++ software development kit (SDK) that lets you
import and export 3D scenes using the Autodesk FBX file format. The
FBX SDK reads FBX files created with FiLMBOX version 2.5 and later and
writes FBX files compatible with MotionBuilder version 6.0 and up. 

%description -l pl.UTF-8
FBX SDK to pakiet programistyczny C++ (SDK), pozwalający importować i
eksportować sceny 3D z użyciem formatu plików Autodesk FBX. FBX SDK
czyta pliki FBX utworzone przy użyciu programu FiLMBOX w wersji 2.5 i
późniejszych, a zapisuje pliki FBX zgodne z programem MotionBuilder w
wersji 6.0 i nowszych.

%package devel
Summary:	Header files for FBX SDK library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki FBX SDK
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel >= 6:4.8

%description devel
Header files for FBX SDK library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki FBX SDK.

%package static
Summary:	Static FBX SDK library
Summary(pl.UTF-8):	Statyczna biblioteka FBX SDK
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static FBX SDK library.

%description static -l pl.UTF-8
Statyczna biblioteka FBX SDK.

%prep
%setup -q -c

# offset of gzip stream (0x1F 0x8B magic) in executable (after installer code)
GZ_START=515852
# offset of tar archive in decompressed stream (after license text)
TAR_START=180222
# then decompressed data begin with license text, then TAR archive
tail -c +$((GZ_START + 1)) fbx202001_fbxsdk_linux | zcat | tail -c +$((TAR_START + 1)) - | tar xf -

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

cp -pr include/fbxsdk* $RPM_BUILD_ROOT%{_includedir}

%ifarch %{ix86}
install lib/gcc/x86/release/lib* $RPM_BUILD_ROOT%{_libdir}
%endif
%ifarch %{x8664}
install lib/gcc/x64/release/lib* $RPM_BUILD_ROOT%{_libdir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc FBX_SDK_Online_Documentation.html License.txt
%attr(755,root,root) %{_libdir}/libfbxsdk.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/fbxsdk.h
%{_includedir}/fbxsdk

%files static
%defattr(644,root,root,755)
%{_libdir}/libfbxsdk.a
