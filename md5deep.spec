Summary:	Compute MD5 message digests on an arbitrary number of files
Summary(pl):	Obliczanie skrótów MD5 dla dowolnej liczby plików
Name:		md5deep
Version:	0.16
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://md5deep.sourceforge.net/%{name}-%{version}.tar.gz
# Source0-md5:	a07715c3344524da1270e9eb39f9b9e1
URL:		http://md5deep.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
md5deep is a cross-platform program to compute MD5 message digests on
an arbitrary number of files. The program is known to run on Windows,
Linux, FreeBSD, OS X, Solaris, and should run on most other platforms.
md5deep is similar to the md5sum program found in the GNU Coreutils
package, but has the following additional features:
- Recursive operation - md5deep is able to recursive examine an entire
  directory tree. That is, compute the MD5 for every file in a
  directory and for every file in every subdirectory.
- Time estimation - md5deep can produce a time estimate when it's
  processing very large files.
- Comparison mode - md5deep can accept a list of known hashes and
  compare them to a set of input files. The program can display either
  those input files that match the list of known hashes or those that
  do not match.

%description -l pl
md5deep to wieloplatformowy program do obliczania skrótów MD5 dla
dowolnej liczby plików. Program dzia³a pod Windows, Linuksem, FreeBSD,
OS X, Solarisem i powinien dzia³aæ na wiêkszo¶ci innych platform.
md5deep jest podobny do programu md5sum z pakietu GNU Coreutils, ale
ma nastêpuj±ce dodatkowe mo¿liwo¶ci:
- praca rekurencyjna - md5deep mo¿e rekurencyjnie sprawdzaæ ca³e 
  drzewo katalogów, obliczaj±c MD5 dla ka¿dego pliku w katalogu oraz
  dla ka¿dego pliku we wszystkich jego podkatalogach;
- szacowanie czasu - md5deep mo¿e pokazywaæ oszacowania czasu trwania
  operacji przy przetwarzaniu bardzo du¿ych plików;
- tryb porównywania - md5deep mo¿e dostaæ listê znanych skrótów i
  porównywaæ je ze zbiorem plików wej¶ciowych; program mo¿e wypisaæ te
  pliki, które pasuj± do listy znanych skrótów lub te, które nie
  pasuj±.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc} %{rpmcflags} -D__LINUX -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install md5deep $RPM_BUILD_ROOT%{_bindir}
install md5deep.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO
%attr(755,root,root) %{_bindir}/md5deep
%{_mandir}/man1/*
