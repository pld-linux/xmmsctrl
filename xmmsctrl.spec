
Summary:	command line control utiity for xmms
Summary(pl):	tekstowe narzêdzie steruj±ce programem xmms
Name:		xmmsctrl
Version:	1.8
Release:	1
URL:		http://www.docs.uu.se/~adavid
Source0:	http://user.it.uu.se/~adavid/utils/%{name}-%{version}.tar.gz
# Source0-md5:	0774f3e61cfc89c1fd3f0526c48b35db
License:	GPL
Group:		Applications/Multimedia
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	xmms-devel

%description
xmmsctrl is a small utility to control xmms from the command line. Its
goal is to be used coupled with sh to test xmms state and perform an
appropriate action, e.g. if playing then pause else play. The interest
of this is to bind keys in a window manager to have control over xmms
with keys that do play/next/pause, prev, control sound...

%description -l pl
xmmsctrl jest ma³ym narzêdziem pozwalaj±cym kontrolowaæ xmmsa z poziomu
wiersza poleceñ. Jego zadaniem jest sprzê¿enie z xmmsem w celu sprawdzenia
jego stanu oraz przygotowania odpowiedniej akcji typu "play" czy "pause".

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install xmmsctrl $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README HELP samples
%attr(755,root,root) %{_bindir}/xmmsctrl
