Summary:	Compute MD5 message digests on an arbitrary number of files
Summary(pl.UTF-8):   Obliczanie skrótów MD5 dla dowolnej liczby plików
Name:		md5deep
Version:	1.12
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/md5deep/%{name}-%{version}.tar.gz
# Source0-md5:	a86d2d2b25b8dfd4cee7a130ef388b28
Patch0:		%{name}-Makefile.patch
URL:		http://md5deep.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
md5deep is a cross-platform program to compute MD5 message digests on
an arbitrary number of files. The program is known to run on Windows,
Linux, FreeBSD, OS X, Solaris, and should run on most other platforms.
md5deep is similar to the md5sum program found in the GNU Coreutils
package, but has the following additional features:
- Recursive operation - md5deep is able to recursive examine an entire
  directory tree. That is, compute the MD5 for every file in a directory
  and for every file in every subdirectory.
- Time estimation - md5deep can produce a time estimate when it's
  processing very large files.
- Comparison mode - md5deep can accept a list of known hashes and
  compare them to a set of input files. The program can display either
  those input files that match the list of known hashes or those that do
  not match.

%description -l pl.UTF-8
md5deep to wieloplatformowy program do obliczania skrótów MD5 dla
dowolnej liczby plików. Program działa pod Windows, Linuksem, FreeBSD,
OS X, Solarisem i powinien działać na większości innych platform.
md5deep jest podobny do programu md5sum z pakietu GNU Coreutils, ale
ma następujące dodatkowe możliwości:
- praca rekurencyjna - md5deep może rekurencyjnie sprawdzać całe
  drzewo katalogów, obliczając MD5 dla każdego pliku w katalogu oraz dla
  każdego pliku we wszystkich jego podkatalogach;
- szacowanie czasu - md5deep może pokazywać oszacowania czasu trwania
  operacji przy przetwarzaniu bardzo dużych plików;
- tryb porównywania - md5deep może dostać listę znanych skrótów i
  porównywać je ze zbiorem plików wejściowych; program może wypisać te
  pliki, które pasują do listy znanych skrótów lub te, które nie pasują.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	LDFLAGS="%{rpmldflags}" \
	OURCC="%{__cc}" \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
