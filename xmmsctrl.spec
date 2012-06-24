# TODO: optflags
Summary:	Command line control utiity for XMMS
Summary(pl):	Dzia�aj�ce z linii polece� narz�dzie steruj�ce programem XMMS
Name:		xmmsctrl
Version:	1.8
Release:	1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://user.it.uu.se/~adavid/utils/%{name}-%{version}.tar.gz
# Source0-md5:	0774f3e61cfc89c1fd3f0526c48b35db
URL:		http://www.docs.uu.se/~adavid
BuildRequires:	xmms-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xmmsctrl is a small utility to control XMMS from the command line. Its
goal is to be used coupled with sh to test XMMS state and perform an
appropriate action, e.g. if playing then pause else play. The interest
of this is to bind keys in a window manager to have control over XMMS
with keys that do play/next/pause, prev, control sound...

%description -l pl
xmmsctrl jest ma�ym narz�dziem pozwalaj�cym sterowa� XMMS-em z poziomu
wiersza polece�. Jego zadaniem jest sprz�enie z XMMS-em w celu
sprawdzenia jego stanu oraz wykonania odpowiedniej akcji, na przyk�ad
w��czenie pauzy, je�li trwa odtwarzanie, a w przeciwnym wypadku
w��czenie odtwarzania. Program mo�e mie� zastosowanie przy
przypisywaniu klawiszy w zarz�dcy okien do sterowania XMMS-em.

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
