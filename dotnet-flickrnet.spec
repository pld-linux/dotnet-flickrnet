%include	/usr/lib/rpm/macros.mono
Summary:	.NET support for Flickr
Name:		dotnet-flickrnet
Version:	2.2.0
Release:	1
License:	MIT
Group:		Libraries
Source0:	FlickrNet2.2-Src-48055.zip
# Source0-md5:	534b3436762ce1bfb2568c9774340f0c
Source1:	flickrnet.pc
Patch0:		%{name}-assemblyinfo.patch
URL:		http://www.codeplex.com/FlickrNet
# FIXME: ugly workaround for broken patch handling in our CVS
BuildRequires:	dos2unix
BuildRequires:	mono-csharp >= 1.1.16.1
BuildRequires:	pkgconfig
BuildRequires:	unzip
ExcludeArch:	i386
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Flickr.Net API is a .Net Library for accessing the Flickr API.
Written entirely in C# it can be accessed from with any .Net language
in .Net Framework 1.1, .Net Framework 2.0, .Net Compact Framework 2.0
and Mono.

%prep
%setup -q -c -n FlickrNet
dos2unix FlickrNet/AssemblyInfo.cs
%patch0 -p1

%build
cd FlickrNet
gmcs -target:library -out:FlickrNet.dll -r:System.Web.dll *.cs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/pkgconfig/,%{_prefix}/lib/mono/flickrnet-%{version}}
install FlickrNet/FlickrNet.dll $RPM_BUILD_ROOT%{_prefix}/lib/mono/flickrnet-%{version}
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
sed -i "s/@VERSION@/%{version}/" $RPM_BUILD_ROOT%{_datadir}/pkgconfig/flickrnet.pc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_prefix}/lib/mono/flickrnet-%{version}
%{_prefix}/lib/mono/flickrnet-%{version}/*.dll
%{_datadir}/pkgconfig/flickrnet.pc
