%define giturl git://github.com/camptocamp/mcollective-plugins.git
%define gitrev ec00a6d802
%define gituser camptocamp

%define plugindir %{_libexecdir}/mcollective/mcollective
%define agents augeasquery puppetd nettest service package filemgr nrpe process puppetca puppetral stomputil

Name            : mcollective-plugins
Version         : 0.0.1
Release         : 4.%{gitrev}
Summary         : Collection of plugins for Mcollective
Group           : Development/Libraries

#                 http://github.com/%{gituser}/%{name}/tarball/%{gitrev}
Source0         : %{gituser}-%{name}-%{gitrev}.tar.gz
URL             : http://projects.puppetlabs.com/projects/mcollective-plugins
Vendor          : Puppet Labs
License         : Apache License, Version 2
Packager        : Dan Carley <dan.carley@gmail.com>

BuildArch       : noarch
BuildRoot       : %{_tmppath}/%{name}-%{version}-root
Requires        : mcollective >= 1.1.0
BuildRequires   : git

%description
%{summary}.

%package all
Summary         : Skeleton package that pulls in all Mcollective plugins
Group           : Development/Libraries
Requires        : mcollective
Requires        : mcollective-plugins-augeasquery = %{version}
Requires        : mcollective-plugins-puppetd = %{version}
Requires        : mcollective-plugins-nettest = %{version}
Requires        : mcollective-plugins-service = %{version}
Requires        : mcollective-plugins-package = %{version}
Requires        : mcollective-plugins-filemgr = %{version}
Requires        : mcollective-plugins-nrpe = %{version}
Requires        : mcollective-plugins-process = %{version}
Requires        : mcollective-plugins-puppetca = %{version}
Requires        : mcollective-plugins-puppetral = %{version}
Requires        : mcollective-plugins-stomputil = %{version}
Requires        : mcollective-plugins-facter_facts = %{version}
Requires        : mcollective-plugins-registrationmeta = %{version}
Requires        : mcollective-plugins-actionpolicy = %{version}

%description all
%{summary}.

%package augeasquery
Summary         : Query Augeas
Group           : Development/Libraries
Requires        : mcollective

%description augeasquery
%{summary}.

%package puppetd
Summary         : Manage Puppet daemons
Group           : Development/Libraries
Requires        : mcollective

%description puppetd
%{summary}.

%package nettest
Summary         : Perform network reachability tests
Group           : Development/Libraries
Requires        : mcollective

%description nettest
%{summary}.

%package service
Summary         : Manage operating system service daemons
Group           : Development/Libraries
Requires        : mcollective

%description service
%{summary}.

%package package
Summary         : Manage operating system packages
Group           : Development/Libraries
Requires        : mcollective

%description package
%{summary}.

%package filemgr
Summary         : Manage files
Group           : Development/Libraries
Requires        : mcollective

%description filemgr
%{summary}.

%package nrpe
Summary         : Nagios remote plugin execution agent
Group           : Development/Libraries
Requires        : mcollective

%description nrpe
%{summary}.

%package process
Summary         : Process agent
Group           : Development/Libraries
Requires        : mcollective

%description process
%{summary}.

%package puppetca
Summary         : Manage Puppet Certificate Authority
Group           : Development/Libraries
Requires        : mcollective

%description puppetca
%{summary}.

%package puppetral
Summary         : Invoke Puppet providers
Group           : Development/Libraries
Requires        : mcollective

%description puppetral
%{summary}.

%package stomputil
Summary         : Stomp utility
Group           : Development/Libraries
Requires        : mcollective

%description stomputil
%{summary}.

%package facter_facts
Summary         : Use Facter as a fact source
Group           : Development/Libraries
Requires        : mcollective

%description facter_facts
%{summary}.

%package registrationmeta
Summary         : Collect metadata about registered nodes
Group           : Development/Libraries
Requires        : mcollective

%description registrationmeta
%{summary}.

%package actionpolicy
Summary         : Define policies for agent actions
Group           : Development/Libraries
Requires        : mcollective

%description actionpolicy
%{summary}.

%prep
%setup -n %{gituser}-%{name}-%{gitrev}

%build
# Make the locations of agents and applications consistent so that we can
# collect them up in a simple loop.
mv agent/service/agent/puppet-service.rb agent/service/agent/service.rb

#mkdir agent/package/agent
mv agent/package/agent/puppet-package.rb agent/package/agent/package.rb
#mv agent/package/package.ddl agent/package/agent/

#mkdir agent/puppetca/agent
#mv agent/puppetca/*.* agent/puppetca/agent

#mkdir agent/puppetral/agent
#mv agent/puppetral/*.* agent/puppetral/agent

%install
rm -rf %{buildroot}

# Agents and applications.
install -d -m 755 %{buildroot}%{plugindir}
install -d -m 755 %{buildroot}%{plugindir}/agent
install -d -m 755 %{buildroot}%{plugindir}/application
for agent_name in %{agents}; do
    install agent/${agent_name}/agent/*.* %{buildroot}%{plugindir}/agent
    if [ -f agent/${agent_name}/application/*.* ]; then
        install agent/${agent_name}/application/*.* %{buildroot}%{plugindir}/application
    fi
done

# Fact plugins.
install -d -m 755 %{buildroot}%{plugindir}/facts
install facts/facter/facter_facts.rb %{buildroot}%{plugindir}/facts/

# Registrations plugins.
install -d -m 755 %{buildroot}%{plugindir}/registration
install registration/meta.rb %{buildroot}%{plugindir}/registration/

# Utils.
install -d -m 755 %{buildroot}%{plugindir}/util
install simplerpc_authorization/action_policy/actionpolicy.rb %{buildroot}%{plugindir}/util/

%clean
rm -rf %{buildroot}

%files all

%files augeasquery
%defattr(-,root,root)
%{plugindir}/agent/augeasquery.rb
%{plugindir}/agent/augeasquery.ddl
%{plugindir}/application/augeas.rb

%files puppetd
%defattr(-,root,root)
%{plugindir}/agent/puppetd.rb
%{plugindir}/agent/puppetd.ddl
%{plugindir}/application/puppetd.rb

%files nettest
%defattr(-,root,root)
%{plugindir}/agent/nettest.rb
%{plugindir}/agent/nettest.ddl
%{plugindir}/application/nettest.rb

%files service
%defattr(-,root,root)
%{plugindir}/agent/service.rb
%{plugindir}/agent/service.ddl
%{plugindir}/application/service.rb

%files package
%defattr(-,root,root)
%{plugindir}/agent/package.rb
%{plugindir}/agent/package.ddl
%{plugindir}/application/package.rb

%files filemgr
%defattr(-,root,root)
%{plugindir}/agent/filemgr.rb
%{plugindir}/agent/filemgr.ddl
%{plugindir}/application/filemgr.rb

%files nrpe
%defattr(-,root,root)
%{plugindir}/agent/nrpe.rb
%{plugindir}/agent/nrpe.ddl
%{plugindir}/application/nrpe.rb

%files process
%defattr(-,root,root)
%{plugindir}/agent/process.rb
%{plugindir}/agent/process.ddl
#%{plugindir}/application/pgrep.rb

%files puppetca
%defattr(-,root,root)
%{plugindir}/agent/puppetca.rb
%{plugindir}/agent/puppetca.ddl

%files puppetral
%defattr(-,root,root)
%{plugindir}/agent/puppetral.rb
%{plugindir}/agent/puppetral.ddl

%files stomputil
%defattr(-,root,root)
%{plugindir}/agent/stomputil.rb
%{plugindir}/agent/stomputil.ddl

%files facter_facts
%defattr(-,root,root)
%{plugindir}/facts/facter_facts.rb

%files registrationmeta
%defattr(-,root,root)
%{plugindir}/registration/meta.rb

%files actionpolicy
%defattr(-,root,root)
%{plugindir}/util/actionpolicy.rb

%changelog
* Wed Jun 01 2011 Dan Carley <dan.carley@gmail.com> 0.0.1-3
- Add NRPE plugin.
- Bump repo revision.

* Tue May 10 2011 Dan Carley <dan.carley@gmail.com> 0.0.1-2
- Rename facter_facts plugin.
- Include registrationmeta and actionpolicy.

* Tue May 3 2011 Dan Carley <dan.carley@gmail.com> 0.0.1-1
- Bundle official Mcollective plugins.
