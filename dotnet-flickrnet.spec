%include	/usr/lib/rpm/macros.mono
Summary:	.NET support for Flickr
Name:		dotnet-flickrnet
Version:	2.1.5
Release:	3
License:	MIT
Group:		Libraries
Source0:	FlickrNet-25207.zip
# Source0-md5:	d20fe0d25a3888300f21e5ad3895c141
Source1:	flickrnet.pc
Patch0:		%{name}-assemblyinfo.patch
URL:		http://www.codeplex.com/FlickrNet
BuildRequires:	mono-csharp >= 1.1.16.1
BuildRequires:	pkgconfig
ExcludeArch:	i386
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Flickr.Net API is a .Net Library for accessing the Flickr API.
Written entirely in C# it can be accessed from with any .Net language
in .Net Framework 1.1, .Net Framework 2.0, .Net Compact Framework 2.0
and Mono.

%prep
%setup -q -c -n FlickrNet
%patch0 -p1

%build
cd FlickrNet
gmcs -target:library -out:FlickrNet.dll -r:System.Web.dll *.cs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/pkgconfig/,%{_libdir}/mono/flickrnet-%{version}}
install FlickrNet/FlickrNet.dll $RPM_BUILD_ROOT%{_libdir}/mono/flickrnet-%{version}
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_libdir}/pkgconfig/
sed -i "s/@VERSION@/%{version}/" $RPM_BUILD_ROOT%{_libdir}/pkgconfig/flickrnet.pc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/mono/flickrnet-%{version}/*.dll
%{_pkgconfigdir}/flickrnet.pc
