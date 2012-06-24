Summary:	kFlickr - standalone Flickr.com uploader for KDE
Summary(pl):	kFlickr - samodzielne narz�dzie dla KDE do przesy�ania danych na Flickr.com
Name:		kflickr
Version:	0.6
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/kflickr/%{name}-%{version}.tar.bz2
# Source0-md5:	62a0d79e96c82454a19f2b563f2ebebf
Patch0:		%{name}-desktop.patch
URL:		http://kflickr.sourceforge.net/
BuildRequires:	kdelibs-devel >= 9:3.2
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
kFlickr is a standalone KDE application that allows for easy upload of
your favourite photos to your Flickr.com account. kFlickr provides the
following features:
- drag and drop from other applications (such as Konqueror and
  DigiKam)
- easy editing of your photo properties (title, description, privacy,
  tags)
- access to your Flickr.com list of tags
- support for more than one user
- image preview
- support for the new Flickr.com authentication
- batch editing of photos
- proxy server support
- support for JPG, PNG and (non-animated) GIF photo formats

%description -l pl
kFlickr to samodzielna aplikacja KDE pozwalaj�ca na �atwe przesy�anie
ulubionych zdj�� na konto Flickr.com. kFlickr daje nast�puj�ce
mo�liwo�ci:
- przeci�ganie z innych aplikacji (takich jak Konqueror czy DIgiKam)
- �atw� zmian� w�a�ciwo�ci zdj�� (tytu�u, opisu, danych prywatnych,
  znacznik�w)
- dost�p do listy znacznik�w Flickr.com
- obs�ug� wi�cej ni� jednego u�ytkownika
- podgl�d obraz�w
- obs�ug� nowego uwierzytelnienia Flickr.com
- wsadowe modyfikowanie zdj��
- obs�ug� serwera proxy
- obs�ug� format�w zdj�� JPG, PNG i (nie animowanego) GIF

%prep
%setup -q
%patch0 -p0

%build
%configure \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	kde_appsdir=%{_desktopdir}

mv -f $RPM_BUILD_ROOT%{_desktopdir}/Graphics/kflickr.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/kflickr
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_libdir}/kde3/*.la
%{_datadir}/apps/kflickr*
%{_iconsdir}/hicolor/*/*/*.png
%{_desktopdir}/*.desktop
%{_mandir}/man1/kflickr*
%{_datadir}/apps/konqueror/servicemenus/kflickr_servicemenu.desktop
%{_datadir}/services/kflickrpart.desktop
