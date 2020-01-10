# Copyright (c) 2000-2008, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%global section free

%global jspspec 2.1
%global major_version 6
%global minor_version 0
%global micro_version 24
%global packdname apache-tomcat-%{version}-src
%global servletspec 2.5
%global elspec 2.1
%global tcuid 91

# FHS 2.3 compliant tree structure - http://www.pathname.com/fhs/2.3/
%global basedir %{_var}/lib/%{name}
%global appdir %{basedir}/webapps
%global bindir %{_datadir}/%{name}/bin
%global confdir %{_sysconfdir}/%{name}
%global homedir %{_datadir}/%{name}
%global libdir %{_javadir}/%{name}
%global logdir %{_var}/log/%{name}
%global cachedir %{_var}/cache/%{name}
%global tempdir %{cachedir}/temp
%global workdir %{cachedir}/work
%global _initrddir %{_sysconfdir}/rc.d/init.d

Name: tomcat6
Epoch: 0
Version: %{major_version}.%{minor_version}.%{micro_version}
Release: 98%{?dist}
Summary: Apache Servlet/JSP Engine, RI for Servlet %{servletspec}/JSP %{jspspec} API

Group: Networking/Daemons
License: ASL 2.0
URL: http://tomcat.apache.org/
Source0: http://www.apache.org/dist/tomcat/tomcat-6/v%{version}/src/%{packdname}.tar.gz
Source1: %{name}-%{major_version}.%{minor_version}.conf
Source2: %{name}-%{major_version}.%{minor_version}.init
Source3: %{name}-%{major_version}.%{minor_version}.sysconfig
Source4: %{name}-%{major_version}.%{minor_version}.wrapper
Source5: %{name}-%{major_version}.%{minor_version}.logrotate
Source6: %{name}-%{major_version}.%{minor_version}-digest.script
Source7: %{name}-%{major_version}.%{minor_version}-tool-wrapper.script
Source8: servlet-api-OSGi-MANIFEST.MF
Source9: jsp-api-OSGi-MANIFEST.MF
Source10: %{name}-%{major_version}.%{minor_version}-log4j.properties
Source11: tomcat-juli-adapters.jar
Source12: tomcat-juli.jar
Patch0: %{name}-%{major_version}.%{minor_version}-bootstrap-MANIFEST.MF.patch
Patch1: %{name}-%{major_version}.%{minor_version}-tomcat-users-webapp.patch
Patch2: %{name}-%{major_version}.%{minor_version}-disable-setPerformancePreferences.patch
# WONTFIX
#Patch3: %{name}-%{major_version}.%{minor_version}.%{micro_version}-CVE-2010-1157.patch
Patch4: %{name}-%{major_version}.%{minor_version}.%{micro_version}-CVE-2010-2227.patch
Patch5: %{name}-%{major_version}.%{minor_version}-rhbz-674601.patch
Patch6: %{name}-6.0.24-CVE-2011-0534.patch
Patch7: %{name}-6.0.24-CVE-2010-3718.patch
Patch8: %{name}-6.0.24-CVE-2010-4172.patch
Patch9: %{name}-6.0.24-CVE-2011-0013.patch
Patch10: %{name}-6.0.24-rhbz698624.patch
Patch11: %{name}-6.0.24-rhbz697968.patch
# Slated for rhel-6.3
Patch12: %{name}-6.0.24-rhbz726169.patch
Patch13: %{name}-6.0.24-CVE-2011-3190-rhbz-738504.patch
Patch14: %{name}-6.0.24-CVE-2011-2204-rhbz-738504.patch
Patch15: %{name}-6.0.24-CVE-2011-2526-rhbz-738504.patch
Patch16: %{name}-6.0.24-CVE-2011-1184-rhbz-738504.patch
# Slated for rhel-6.3
Patch17: %{name}-6.0.24-rhbz-748813.patch
Patch18: %{name}-6.0.24-rhbz-783567.patch
Patch19: %{name}-6.0.24-CVE-2012-0022.patch
Patch20: %{name}-6.0.24-rhbz-847288.patch
Patch21: %{name}-6.0.24-rhbz-785954.patch
Patch22: %{name}-6.0.24-rhbz-857066.patch
Patch23: %{name}-6.0.24-CVE-2012-3439-rhbz-882011.patch
Patch24: %{name}-6.0.24-CVE-2012-4534-rhbz-883693.patch
Patch25: %{name}-6.0.24-CVE-2012-3546-rhbz-883706.patch
Patch26: %{name}-6.0.24-CVE-2013-2067-rhbz-962717.patch
Patch27: %{name}-6.0.24-CVE-2013-4322.patch
Patch28: %{name}-6.0.24-CVE-2013-4286.patch
Patch29: %{name}-6.0.24-CVE-2014-0050.patch
Patch30: %{name}-6.0.24-CVE-2014-0075.patch
Patch31: %{name}-6.0.24-CVE-2014-0099.patch
Patch32: %{name}-6.0.24-CVE-2014-0096.patch
Patch33: %{name}-6.0.24-CVE-2013-4590.patch
Patch34: %{name}-6.0.24-CVE-2014-0119.patch
Patch35: %{name}-6.0.24-CVE-2014-0227.patch
Patch36: %{name}-6.0.24-rhbz-1183252.patch
Patch37: %{name}-6.0.24-rhbz-1031327.patch
Patch38: %{name}-6.0.24-85-rhbz-1068689.patch
Patch39: %{name}-6.0.24-rhbz-1221877.patch
Patch40: %{name}-6.0.24-rhbz-1072484.patch
Patch41: %{name}-6.0.24-rhbz-1134600.patch
Patch42: %{name}-6.0.24-rhbz-1268352.patch
Patch43: %{name}-6.0.24-rhbz-1264559.patch
Patch44: %{name}-6.0.24-rhbz-1293290.patch
Patch45: %{name}-6.0.24-CVE-2015-5174.patch
Patch46: %{name}-6.0.24-CVE-2016-0706.patch
Patch47: %{name}-6.0.24-CVE-2016-0714.patch
Patch48: %{name}-6.0.24-CVE-2015-5345.patch
Patch49: %{name}-6.0.24-CVE-2016-5388.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch

BuildRequires: zip
BuildRequires: ant
BuildRequires: ant-trax
BuildRequires: xalan-j2
BuildRequires: ecj
BuildRequires: findutils
BuildRequires: jakarta-commons-collections
#BuildRequires: jakarta-commons-collections-tomcat5
BuildRequires: jakarta-commons-daemon
BuildRequires: jakarta-commons-logging
#BuildRequires: jakarta-commons-dbcp-tomcat5
#BuildRequires: jakarta-commons-pool-tomcat5
BuildRequires: jakarta-commons-dbcp
BuildRequires: jakarta-commons-pool
BuildRequires: jakarta-taglibs-standard
BuildRequires: java-devel >= 0:1.5.0
BuildRequires: jpackage-utils >= 0:1.7.0
BuildRequires: junit
BuildRequires: log4j
BuildRequires: mx4j
Requires(pre): shadow-utils
Requires(pre): shadow-utils
Requires: jakarta-commons-daemon
Requires: jakarta-commons-logging
Requires: jakarta-commons-collections
Requires: jakarta-commons-dbcp
Requires: jakarta-commons-pool
Requires: mx4j
Requires: java
Requires: procps
Requires: %{name}-lib = %{epoch}:%{version}-%{release}
Requires: log4j
Requires(post): log4j
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/chkconfig
# rhbz 782400
#Requires(post): redhat-lsb
#Requires(preun): redhat-lsb
Requires(post): /lib/lsb/init-functions
Requires(preun): /lib/lsb/init-functions
Requires(post): jpackage-utils
Requires(postun): jpackage-utils


%description
Tomcat is the servlet container that is used in the official Reference
Implementation for the Java Servlet and JavaServer Pages technologies.
The Java Servlet and JavaServer Pages specifications are developed by
Sun under the Java Community Process.

Tomcat is developed in an open and participatory environment and
released under the Apache Software License version 2.0. Tomcat is intended
to be a collaboration of the best-of-breed developers from around the world.

%package admin-webapps
Group: System Environment/Applications
Summary: The host-manager and manager web applications for Apache Tomcat
Requires: %{name} = %{epoch}:%{version}-%{release}

%description admin-webapps
The host-manager and manager web applications for Apache Tomcat.

%package docs-webapp
Group: System Environment/Applications
Summary: The docs web application for Apache Tomcat
Requires: %{name} = %{epoch}:%{version}-%{release}

%description docs-webapp
The docs web application for Apache Tomcat.

%package javadoc
Group: Documentation
Summary: Javadoc generated documentation for Apache Tomcat

%description javadoc
Javadoc generated documentation for Apache Tomcat.

%package jsp-%{jspspec}-api
Group: Internet/WWW/Dynamic Content
Summary: Apache Tomcat JSP API implementation classes
Provides: jsp = %{jspspec}
Provides: jsp21
Requires: %{name}-servlet-%{servletspec}-api = %{epoch}:%{version}-%{release}
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives

%description jsp-%{jspspec}-api
Apache Tomcat JSP API implementation classes.

%package el-%{elspec}-api
Summary: Expression Language v1.0 API
Group: Development/Libraries/Java
Provides: el_1_0_api = %{epoch}:%{version}-%{release}
Provides: el_api = %{elspec}
#Requires: %{name}-servlet-%{servletspec}-api = %{epoch}:%{version}-%{release}
#Requires %{name}-jsp-%{jspspec}-api = %{epoch}:%{version}-%{release}
Requires(preun): %{_sbindir}/update-alternatives
Requires(post): %{_sbindir}/update-alternatives

%description el-%{elspec}-api
Expression Language 1.0.

# %package log4j
#Group: Internet/WWW/Dynamic Content
#Summary: Log4J support for Apache Tomcat
#Requires: jakarta-commons-logging

# %description log4j
# Log4J support for Apache Tomcat

%package lib
Group: Development/Compilers
Summary: Libraries needed to run the Tomcat Web container
Requires: %{name}-jsp-%{jspspec}-api = %{epoch}:%{version}-%{release}
Requires: %{name}-servlet-%{servletspec}-api = %{epoch}:%{version}-%{release}
Requires: %{name}-el-%{elspec}-api = %{epoch}:%{version}-%{release}
Requires: mx4j
Requires: ecj
#Requires(post): jakarta-commons-collections-tomcat5
Requires: jakarta-commons-collections
Requires: jakarta-commons-dbcp
Requires: jakarta-commons-pool
Requires: log4j
Requires(preun): coreutils
# Removed log4j subpackage
Provides: %{name}-log4j = %{epoch}:%{version}-%{release}
Obsoletes: %{name}-log4j < %{epoch}:%{version}-%{release}

%description lib
Libraries needed to run the Tomcat Web container.

%package servlet-%{servletspec}-api
Group: Internet/WWW/Dynamic Content
Summary: Apache Tomcat Servlet API implementation classes
Provides: servlet = %{servletspec}
Provides: servlet6
Provides: servlet25
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives

%description servlet-%{servletspec}-api
Apache Tomcat Servlet API implementation classes.

%package webapps
Group: System Environment/Applications
Summary: The ROOT and examples web applications for Apache Tomcat
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires(post): jakarta-taglibs-standard >= 0:1.1

%description webapps
The ROOT and examples web applications for Apache Tomcat.

%prep
echo "Building on %{_arch}"
%ifarch ppc64 s390x ppc
echo "WARNING: Check generated webapp doc size!"
echo "Expect xslt to produce empty html files"
echo "on ppc64, ppc, and s390x"
#echo "using rhpkg build --target rhel-6.5-noarch-candidate"
#exit 1
%endif

%setup -q -c -T -a 0
# remove pre-built binaries and windows files
find . -type f \( -name "*.bat" -o -name "*.class" -o -name Thumbs.db -o -name "*.gz" -o \
          -name "*.jar" -o -name "*.war" -o -name "*.zip" \) | xargs -t %{__rm}
pushd %{packdname}
%patch0 -p0
%patch1 -p0
%patch2 -p0
#%patch3 -p0
%patch4 -p0
%patch5 -p0
%patch6 -p0
%patch7 -p0
%patch8 -p0
%patch9 -p0
%patch10 -p0
%patch11 -p0
%patch12 -p0
%patch13 -p0
%patch14 -p0
%patch15 -p0
%patch16 -p0
%patch17 -p0
%patch18 -p0
%patch19 -p0
%patch20 -p0
%patch21 -p0
%patch22 -p0
%patch23 -p0
%patch24 -p0
%patch25 -p0
%patch26 -p0
%patch27 -p0
%patch28 -p0
%patch29 -p0
%patch30 -p0
%patch31 -p0
%patch32 -p0
%patch33 -p0
%patch34 -p0
%patch35 -p0
%patch36 -p0
%patch37 -p0
%patch38 -p0
%patch39 -p0
%patch40 -p0
%patch41 -p0
%patch42 -p0
%patch43 -p0
%patch44 -p0
%patch45 -p0
%patch46 -p0
%patch47 -p0
%patch48 -p0
%patch49 -p0

%{__ln_s} $(build-classpath jakarta-taglibs-core) webapps/examples/WEB-INF/lib/jstl.jar
%{__ln_s} $(build-classpath jakarta-taglibs-standard) webapps/examples/WEB-INF/lib/standard.jar
%{__mkdir_p} tmp
pushd tmp
##%{jar} xf $(build-classpath commons-collections-tomcat5)
#%{jar} xf $(build-classpath commons-dbcp-tomcat5)
#%{jar} xf $(build-classpath commons-pool-tomcat5)
#%{jar} cf ../tomcat-dbcp.jar *
#popd
#%{__rm} -r tmp
popd

%build
export CLASSPATH="$(build-classpath mx4j/mx4j-jmx.jar mx4j/mx4j-remote.jar)"
export OPT_JAR_LIST="ant/ant-trax xalan-j2"
#export CLASSPATH=$(build-classpath xalan-j2)
#export OPT_JAR_LIST="`%{__cat} %{_sysconfdir}/ant.d/trax` xalan-j2-serializer"
pushd %{packdname}
    # we don't care about the tarballs and we're going to replace
    # tomcat-dbcp.jar with jakarta-commons-{collections,dbcp,pool}-tomcat5.jar
    # so just create a dummy file for later removal
    touch HACK
    echo `javac -version` 2>&1
    # who needs a build.properties file anyway
    %{ant} -debug -Dbase.path="." \
        -Dbuild.compiler="modern" \
        -Dcommons-collections.jar="$(build-classpath commons-collections)" \
        -Dcommons-daemon.jar="$(build-classpath commons-daemon)" \
        -Dcommons-daemon.jsvc.tar.gz="HACK" \
        -Djasper-jdt.jar="$(build-classpath ecj)" \
        -Djdt.jar="$(build-classpath ecj)" \
        -Dtomcat-dbcp.jar="commons-dbcp.jar" \
        -Dtomcat-native.tar.gz="HACK" \
        -Dversion="%{version}" \
        -Dversion.build="%{micro_version}"
    # javadoc generation
    %{ant} -f dist.xml dist-prepare
    %{ant} -f dist.xml dist-source

    # This causes an error with sinjdoc. Move it out of the way for now
    mv java/org/apache/catalina/loader/WebappClassLoader.java ../
    rm -f output/dist/src/java/org/apache/catalina/loader/WebappClassLoader.java
    %{ant} -d -v -f dist.xml dist-javadoc
    cp ../WebappClassLoader.java java/org/apache/catalina/loader/
    mv ../WebappClassLoader.java output/dist/src/java/org/apache/catalina/loader/
    # remove some jars that we'll replace with symlinks later
    %{__rm} output/build/bin/commons-daemon.jar \
            output/build/lib/ecj.jar
    # remove the cruft we created
    %{__rm} output/build/bin/HACK \
            output/build/bin/tomcat-native.tar.gz 
#\
#            output/build/lib/HACK

popd
pushd %{packdname}/output/dist/src/webapps/docs/appdev/sample/src
%{__mkdir_p} ../web/WEB-INF/classes
%{javac} -cp ../../../../../../../../output/build/lib/servlet-api.jar -d ../web/WEB-INF/classes mypackage/Hello.java
pushd ../web
%{jar} cf ../../../../../../../../output/build/webapps/docs/appdev/sample/sample.war *
popd
popd

# inject OSGi manifests
mkdir -p META-INF
cp -p %{SOURCE8} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u %{packdname}/output/build/lib/servlet-api.jar META-INF/MANIFEST.MF
cp -p %{SOURCE9} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u %{packdname}/output/build/lib/jsp-api.jar META-INF/MANIFEST.MF

%install
%{__rm} -rf $RPM_BUILD_ROOT
# build initial path structure
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_bindir}
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_sbindir}
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_javadocdir}/%{name}
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_initrddir}
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{appdir}
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{bindir}
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{confdir}
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{confdir}/Catalina/localhost
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{libdir}
%{__install} -d -m 0775 ${RPM_BUILD_ROOT}%{logdir}
/bin/touch ${RPM_BUILD_ROOT}%{logdir}/catalina.out
%{__install} -d -m 0775 ${RPM_BUILD_ROOT}%{homedir}
%{__install} -d -m 0775 ${RPM_BUILD_ROOT}%{tempdir}
%{__install} -d -m 0775 ${RPM_BUILD_ROOT}%{workdir}
# move things into place
pushd %{packdname}/output/build
    %{__cp} -a bin/*.{jar,xml} ${RPM_BUILD_ROOT}%{bindir}
    %{__cp} %{SOURCE10} conf/log4j.properties
    %{__cp} -a conf/*.{policy,properties,xml} ${RPM_BUILD_ROOT}%{confdir}
    %{__cp} -a lib/*.jar ${RPM_BUILD_ROOT}%{libdir}
    %{__cp} -a webapps/* ${RPM_BUILD_ROOT}%{appdir}
popd
# javadoc
pushd %{packdname}/output/dist/webapps
    %{__cp} -a docs/api/* ${RPM_BUILD_ROOT}%{_javadocdir}/%{name}
popd
%{__sed} -e "s|\@\@\@TCHOME\@\@\@|%{homedir}|g" \
         -e "s|\@\@\@TCTEMP\@\@\@|%{tempdir}|g" \
         -e "s|\@\@\@LIBDIR\@\@\@|%{_libdir}|g" %{SOURCE1} \
    > ${RPM_BUILD_ROOT}%{confdir}/%{name}.conf
%{__sed} -e "s|\@\@\@TCHOME\@\@\@|%{homedir}|g" \
         -e "s|\@\@\@TCTEMP\@\@\@|%{tempdir}|g" \
         -e "s|\@\@\@LIBDIR\@\@\@|%{_libdir}|g" %{SOURCE3} \
    > ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/%{name}
%{__install} -m 0644 %{SOURCE2} \
    ${RPM_BUILD_ROOT}%{_initrddir}/%{name}
%{__install} -m 0644 %{SOURCE4} \
    ${RPM_BUILD_ROOT}%{_sbindir}/%{name}
%{__ln_s} %{name} ${RPM_BUILD_ROOT}%{_sbindir}/d%{name}
%{__sed} -e "s|\@\@\@TCLOG\@\@\@|%{logdir}|g" %{SOURCE5} \
    > ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d/%{name}
%{__sed} -e "s|\@\@\@TCHOME\@\@\@|%{homedir}|g" \
         -e "s|\@\@\@TCTEMP\@\@\@|%{tempdir}|g" \
         -e "s|\@\@\@LIBDIR\@\@\@|%{_libdir}|g" %{SOURCE6} \
    > ${RPM_BUILD_ROOT}%{_bindir}/%{name}-digest
%{__sed} -e "s|\@\@\@TCHOME\@\@\@|%{homedir}|g" \
         -e "s|\@\@\@TCTEMP\@\@\@|%{tempdir}|g" \
         -e "s|\@\@\@LIBDIR\@\@\@|%{_libdir}|g" %{SOURCE7} \
    > ${RPM_BUILD_ROOT}%{_bindir}/%{name}-tool-wrapper
# create jsp and servlet API symlinks
pushd ${RPM_BUILD_ROOT}%{_javadir}
    %{__mv} %{name}/jsp-api.jar %{name}-jsp-%{jspspec}-api-%{version}.jar
    %{__mv} %{name}/servlet-api.jar \
        %{name}-servlet-%{servletspec}-api-%{version}.jar
    %{__mv} %{name}/el-api.jar %{name}-el-%{elspec}-api-%{version}.jar
    %{__ln_s} %{name}-jsp-%{jspspec}-api-%{version}.jar \
        %{name}-jsp-%{jspspec}-api.jar
    %{__ln_s} %{name}-servlet-%{servletspec}-api-%{version}.jar \
        %{name}-servlet-%{servletspec}-api.jar
    %{__ln_s} %{name}-el-%{elspec}-api-%{version}.jar %{name}-el-%{elspec}-api.jar
popd

pushd %{packdname}/output/build
   %{_bindir}/build-jar-repository lib commons-collections \
   commons-dbcp commons-pool ecj mx4j/mx4j-jmx.jar  mx4j/mx4j-remote.jar 2>&1
   %{_bindir}/build-jar-repository -p webapps/examples/WEB-INF/lib \
   taglibs-core.jar taglibs-standard.jar 2>&1
popd

pushd ${RPM_BUILD_ROOT}%{libdir}
    # fix up jars to include version number
    for i in *.jar; do
        j="$(echo $i | %{__sed} -e 's,\.jar$,,')"
        %{__mv} ${j}.jar ${j}-%{version}.jar
        %{__ln_s} ${j}-%{version}.jar ${j}.jar
    done
    # symlink JSP and servlet API jars
    %{__ln_s} ../%{name}-jsp-%{jspspec}-api-%{version}.jar .
    %{__ln_s} ../%{name}-servlet-%{servletspec}-api-%{version}.jar .
    %{__ln_s} ../%{name}-el-%{elspec}-api-%{version}.jar .

#    %{__rm} tomcat-dbcp.jar
#    %{__cp} -p $(build-classpath commons-collections) .
#   %{__cp} -p $(build-classpath log4j) .
    %{__ln_s} $(build-classpath commons-collections) commons-collections.jar
    %{__ln_s} $(build-classpath log4j) log4j.jar
    %{__ln_s} $(build-classpath commons-dbcp) .
    %{__ln_s} $(build-classpath commons-pool) .
    %{__ln_s} $(build-classpath ecj) jasper-jdt.jar
    %{__ln_s} $(build-classpath mx4j/mx4j-jmx) .
    %{__ln_s} $(build-classpath mx4j/mx4j-remote) .
#   copy extras
    %{__mkdir} extras
    pushd extras
    %{__cp} -p %{SOURCE11} .
    %{__cp} -p %{SOURCE12} .
    popd
popd
pushd ${RPM_BUILD_ROOT}%{bindir}
    # fix up jars to include version number
    for i in *.jar; do
        j="$(echo $i | %{__sed} -e 's,\.jar$,,')"
        %{__mv} ${j}.jar ${j}-%{version}.jar
        %{__ln_s} ${j}-%{version}.jar ${j}.jar
    done
popd
# symlink to the FHS locations where we've installed things
pushd ${RPM_BUILD_ROOT}%{homedir}
    %{__ln_s} %{appdir} webapps
    %{__ln_s} %{confdir} conf
    %{__ln_s} %{libdir} lib
    %{__ln_s} %{logdir} logs
    %{__ln_s} %{tempdir} temp
    %{__ln_s} %{workdir} work
popd

# install sample webapp
%{__mkdir_p} ${RPM_BUILD_ROOT}%{appdir}/sample
pushd ${RPM_BUILD_ROOT}%{appdir}/sample
%{jar} xf ${RPM_BUILD_ROOT}%{appdir}/docs/appdev/sample/sample.war
popd
%{__rm} ${RPM_BUILD_ROOT}%{appdir}/docs/appdev/sample/sample.war

# rhbz 661244 - missing tomcat6-juli link
pushd ${RPM_BUILD_ROOT}%{libdir}
%{__ln_s} %{bindir}/tomcat-juli.jar .
popd

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%pre
# add the tomcat user and group
%{_sbindir}/groupadd -g %{tcuid} -r tomcat 2>/dev/null || :
%{_sbindir}/useradd -c "Apache Tomcat" -u %{tcuid} -g tomcat \
    -s /sbin/nologin -r -d %{homedir} tomcat 2>/dev/null || :

%post
# install but don't activate
/sbin/chkconfig --add %{name}

%post jsp-%{jspspec}-api
%{_sbindir}/update-alternatives --install %{_javadir}/jsp.jar jsp \
    %{_javadir}/%{name}-jsp-%{jspspec}-api.jar 20100

%post servlet-%{servletspec}-api
%{_sbindir}/update-alternatives --install %{_javadir}/servlet.jar servlet \
    %{_javadir}/%{name}-servlet-%{servletspec}-api.jar 20500

%post el-%{elspec}-api
%{_sbindir}/update-alternatives --install %{_javadir}/elspec.jar elspec \
        %{_javadir}/%{name}-el-%{elspec}-api.jar 20250
%preun
# clean tempdir and workdir on removal or upgrade
%{__rm} -rf %{workdir}/* %{tempdir}/*
if [ "$1" = "0" ]; then
    %{_initrddir}/%{name} stop >/dev/null 2>&1
    /sbin/chkconfig --del %{name}
fi

%postun jsp-%{jspspec}-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove jsp \
        %{_javadir}/%{name}-jsp-%{jspspec}-api.jar
fi

%postun servlet-%{servletspec}-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove servlet \
        %{_javadir}/%{name}-servlet-%{servletspec}-api.jar
fi

%postun el-%{elspec}-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove elspec \
        %{_javadir}/%{name}-el-%{elspec}-api.jar
fi

%files
%defattr(0664,root,tomcat,0755)
%doc %{packdname}/{LICENSE,NOTICE,RELEASE*}
%attr(0755,root,root) %{_bindir}/%{name}-digest
%attr(0755,root,root) %{_bindir}/%{name}-tool-wrapper
%attr(0755,root,root) %{_sbindir}/d%{name}
%attr(0755,root,root) %{_sbindir}/%{name}
%attr(0755,tomcat,root) %dir %{logdir}
%attr(0644,tomcat,tomcat) %verify(not size md5 mtime) %{logdir}/catalina.out
%attr(0755,root,root) %{_initrddir}/%{name}
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%attr(0755,root,tomcat) %dir %{basedir}

%defattr(0644,root,tomcat,0775)
%attr(0775,root,tomcat) %dir %{appdir}
%attr(0755,root,tomcat) %dir %{confdir}
%attr(0775,root,tomcat) %{confdir}/Catalina
%attr(0775,root,tomcat) %dir %{confdir}/Catalina/localhost
%config(noreplace) %{confdir}/%{name}.conf
%config(noreplace) %{confdir}/*.policy
%config(noreplace) %{confdir}/*.properties
%config(noreplace) %{confdir}/context.xml
%config(noreplace) %{confdir}/server.xml
%attr(0640,root,tomcat) %config(noreplace) %{confdir}/tomcat-users.xml
%config(noreplace) %{confdir}/web.xml
%attr(0775,root,tomcat) %dir %{cachedir}
%attr(0775,root,tomcat) %dir %{tempdir}
%attr(0775,root,tomcat) %dir %{workdir}
%dir %{homedir}
%{bindir}/bootstrap-%{version}.jar
%{bindir}/bootstrap.jar
%{bindir}/catalina-tasks.xml
%{bindir}/tomcat-juli-%{version}.jar
%{bindir}/tomcat-juli.jar
%attr(0775,root,tomcat) %{homedir}/conf
%{homedir}/lib
%{homedir}/temp
%{homedir}/webapps
%{homedir}/work
%{homedir}/logs

%files admin-webapps
%defattr(0644,root,tomcat,0775)
%{appdir}/host-manager
%{appdir}/manager
%config(noreplace) %{appdir}/manager/WEB-INF/web.xml
%config(noreplace) %{appdir}/host-manager/WEB-INF/web.xml

%files docs-webapp
%defattr(0644,root,tomcat,0755)
%{appdir}/docs

%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}

%files jsp-%{jspspec}-api
%defattr(0644,root,root,0755)
%{_javadir}/%{name}-jsp-%{jspspec}-api-%{version}.jar
%{_javadir}/%{name}-jsp-%{jspspec}-api.jar

%files lib
%defattr(0644,root,root,0755)
%{libdir}

%files servlet-%{servletspec}-api
%defattr(0644,root,root,0755)
%{_javadir}/%{name}-servlet-%{servletspec}-api-%{version}.jar
%{_javadir}/%{name}-servlet-%{servletspec}-api.jar

%files el-%{elspec}-api
%defattr(0655,root,root,0755)
%{_javadir}/%{name}-el-%{elspec}-api-%{version}.jar
%{_javadir}/%{name}-el-%{elspec}-api.jar
%{_javadir}/%{name}/%{name}-el-%{elspec}-api-%{version}.jar

%files webapps
%defattr(0644,tomcat,tomcat,0755)
%{appdir}/ROOT
%{appdir}/examples
%{appdir}/sample
#%{appdir}/host-manager
#%{appdir}/manager

%changelog
* Tue Aug 23 2016 Coty Sutherland <csutherl@redhat.com> 0:6.0.24-98
- Resolves: rhbz#1362210 CVE-2016-5388 Tomcat: CGI sets environmental variable based on user supplied Proxy request header
- Resolves: rhbz#1368119

* Mon Aug 15 2016 Coty Sutherland <csutherl@redhat.com> 0:6.0.24-97
- Resolves: rhbz#1367051 CVE-2015-5174 URL Normalization issue
- Resolves: rhbz#1367054 CVE-2016-0706 Security Manager bypass via StatusManagerServlet
- Resolves: rhbz#1367058 CVE-2016-0714 Security Manager bypass via persistence mechanisms
- Resolves: rhbz#1367054 CVE-2015-5345 Directory disclosure

* Tue Jul 19 2016 Coty Sutherland <csutherl@redhat.com> 0:6.0.24-96
- Resolves: rhbz#1357123 rpm -V tomcat6 fails due on /var/log/tomcat6/catalina.out

* Mon Feb 8 2016 Coty Sutherland <csutherl@redhat.com> 0:6.0.24-95
- Related: rhbz#1084426 Reverting to prevent Satellite installation issues mentioned in rhbz-1302761

* Fri Jan 08 2016 Coty Sutherland <csutherl@redhat.com> 0:6.0.24-92
- Resolves: rhbz#1293290 CVE-2014-7810 tomcat6 security manager bypass via EL expressions

* Mon Dec 21 2015 Coty Sutherland <csutherl@redhat.com> 0:6.0.24-91
- Resolves: rhbz#886653 Tomcat6 files should be owned by user / group tomcat

* Mon Dec 21 2015 Coty Sutherland <csutherl@redhat.com> 0:6.0.24-91
- Resolves: rhbz#1155509 tomcat6 packages are arch dependent

* Mon Dec 14 2015 Coty Sutherland <csutherl@redhat.com> 0:6.0.24-91
- Resolves: rhbz#1264559 Correct behaviour of ResourceBundleELResolver.

* Mon Dec 14 2015 Coty Sutherland <csutherl@redhat.com> 0:6.0.24-91
- Resolves: rhbz#1268352 Resolving NIO connector memory leak.

* Thu Dec 10 2015 Coty Sutherland <csutherl@redhat.com> 0:6.0.24-91
- Resolves: rhbz#1134600 Resolve STRICT_SERVLET_COMPLIANCE issues.

* Wed Dec 09 2015 Coty Sutherland <csutherl@redhat.com> 0:6.0.24-91
- Resolves: rhbz#1072484 Resolve fix translation problem affecting IBM JDK.

* Thu Oct 29 2015 Coty Sutherland <csutherl@redhat.com> 0:6.0.24-91
- Resolves: rhbz#1221877 Add support for disableURLRewriting.

* Fri May 15 2015 David Knox <dknox@redhat.com> 0:6.0.24-90
- Related: rhbz#1042811 left over test value in the conf

* Fri May 15 2015 David Knox <dknox@redhat.com> 0:6.0.24-89
- Resolves: rhbz#1042811 tomcat6 service restarts will cause a 
- duplicated command-line arguments

* Thu Mar 26 2015 David Knox <dknox@redhat.com> 0:6.0.24-88
- Related: rhbz#1022061 changed in init file. Remove test
- in function stop for result after initial command to
- stop.

* Wed Feb 25 2015 David Knox <dknox@redhat.com> 0:6.0.24-87
- Resolves: rhbz#1128396 NPE in chunked encoding.
- Regenerated patches for 4322 and 0227

* Wed Feb 25 2015 David Knox <dknox@redhat.com> 0:6.0.24-86
- Resolves: rhbz#1068689 Add option to disable log rotation
- in FileHandler

* Wed Feb 25 2015 David Knox <dknox@redhat.com> 0:6.0.24-85
- Resolves: CVE-2014-0227 Limited DoS in chunked transfer

* Mon Feb 23 2015 David Knox <dknox@redhat.com> 0:6.0.24-84
- Resolves: rhbz#1022061 Tomcat init script needs to be adjusted to kill tomcat
- if stop is unsuccessful 

* Thu Feb 19 2015 David Knox <dknox@redhat.com> 0:6.0.24-83
- Resolves: rhbz#1054817 Mark Tomcat Manager web.xml as 
- config in spec

* Thu Feb 19 2015 David Knox <dknox@redhat.com> 0:6.0.24-82
- Resolves: rhbz#1031327 Backport apache 50072 blank responses

* Mon Feb 2 2015 David Knox <dknox@redhat.com> 0:6.0.24-81
- Resolves: rhbz#1183252 Tomcat breaks in serving large files
- greater than 1.7 mb and under high load and high threading

* Tue Sep 16 2014 David Knox <dknox@redhat.com> 0:6.0.24-80
- Related: CVE-2013-4590  - remove xml schema names javaee_5,
- javaee_web_services_1_2, and javaee_web_services_1_2_client
- from descriptor.DigesterFactory initialization. These
- schema definitions are not relevant to 6.0.24 as the version
- of their spec did not exist at the time.
- Resolves: rhbz#1140855 - request parameter truncated


* Fri Sep 12 2014 David Knox <dknox@redhat.com> 0:6.0.24-79
- Related: rhbz#1140301 - have to bump the nvr to be greater
- than 6.5.z

* Tue Sep 9 2014 David Knox <dknox@redhat.com> 0:6.0.24-69
- Resolves: rhbz#1140301 - reverse changes of 845786.
- Rebuilding for compose.

* Fri Jul 31 2014 David Knox <dknox@redhat.com> 0:6.0.24-68
- Resolves: CVE-2013-4590
- Resolves: CVE-2014-0119

* Mon Jul 7 2014 David Knox <dknox@redhat.com> 0:6.0.24-67
- Related: CVE-2014-0075 incomplete

* Wed Jul 2 2014 David Knox <dknox@redhat.com> 0:6.0.24-66
- Related: CVE-2014-0050 
- Related: CVE-2013-4322

* Fri Jun 20 2014 David Knox <dknox@redhat.com> 0:6,0.24-65
- Resolves: CVE-2014-0099
- Resolves: CVE-2014-0096
- Resolves: CVE-2014-0075

* Wed Jun 4 2014 David Knox <dknox@redhat.com> 0:6.0.24-64
- Resolves: CVE-2014-0050

* Mon Apr 7 2014 David Knox <dknox@redhat.com> 0:6.0.24-63
- Resolves: CVE-2013-4322 CVE-2013-4286. Branched from
- rhel-6.5

* Wed Sep 11 2013 David Knox <dknox@redhat.com> 0:6.0.24-62
- Related: rhbz 915447 Introduced a space char in TOMCAT_GROUP

* Tue Sep 10 2013 David Knox <dknox@redhat.com> 0:6.0.24-61
- Related: rhbz 915447 Typo in conf and sysconf

* Thu Sep 5 2013 David Knox <dknox@redhat.com> 0:6.0.24-60
- Related: rhbz 915447 can't start with group other than tomcat
- changes in init script. Added TOMCAT_GROUP to sysconfig and
- tomcat6.conf. Also changed default to the group that user
- tomcat belongs.

* Tue Sep 3 2013 David Knox <dknox@redhat.com> 0:6.0.24-59
- Related: CVE-2012-3439 Digest Authentication. Fixed typo
- in the patch file.

* Mon Aug 26 2013 David Knox <dknox@redhat.com> 0:6.0.24-58
- Resolves: CVE-2012-3439
- Resolves: CVE-2012-4534
- Resolves: CVE-2012-3546
- Increment build number to exceed 6_4 build number. Demanded
- by rpmdiff

* Wed Aug 7 2013 David Knox <dknox@redhat.com> 0:6.0.24-54
- Resolves: rhbz 845786 webapps-docs contained empty files. 
- Build will fail of architectures ppc s390x ppc64. Use
- target rhel-6.5-noarch-candidate
- Resolves: rhbz 915447 can't start with group other than tomcat
- changes in init script
- Resolves: rhbz 950647 Error in checkpidfile of init script
- Resolves: rhbz 977685 Full implementation of juli and juli
- adapters. Jars placed in new extras directory
- Resolves: 960225 Status script does not return proper PID

* Tue Jun 11 2013 David Knox <dknox@redhat.com> 0:6.0.24-53
- Resolves: CVE-2013-2067 session fixation

* Wed May 16 2013 David Knox <dknox@redhat.com> 0:6.0.24-52
- Related: rhbz#955977 CVE-2013-1976

* Wed May 16 2013 David Knox <dknox@redhat.com> 0:6.0.24-51
- Related: rhbz#955977 CVE-2013-1976 Changed location of 
- TOMCAT_LOG to /var/log where only root can write to it. Touching
- TOMCAT_LOG is no longer necessary

* Tue Apr 30 2013 David Knox <dknox@redhat.com> 0:6.0.24-50
- Resolves: rhbz#955977 CVE-2013-1976 Improper TOMCAT_LOG management in
- init script

* Wed Jan 16 2013 David Knox <dknox@redhat.com> 0:6.0.24-49
- Related: rhbz 576540
- Javadoc is not being generated correctly by the build

* Tue Dec 11 2012 David Knox <dknox@redhat.com> 0:6.0.24-48
- Resolves: rhbz 576540 - regression init script in the 
- wrong place. Changed _initrddir definition herein to point to the 
- right place.

* Thu Nov 8 2012 David Knox <dknox@redhat.com> 0:6.0.24-47
- Resolves: rhbz 857066 apache bz 48843 ArrayIndexOutofBounds

* Tue Oct 2 2012 David Knox <dknox@redhat.com> 0:6.0.24-46
- Resolves: rhbz 847288 classloader deadlock compiler JSPs
- Resolves: rhbz 785954 HTML filtering needed
- Resolves: rhbz 798617 init gives incorrect status 

* Tue May 22 2012 David Knox <dknox@redhat.com> 0:6.0.24-45
- Resolves: rhbz 757632 regression

* Thu Mar 29 2012 David Knox <dknox@redhat.com> 0:6.0.24-44
- Resolves: CVE-2012-0022 regression. Change made to patch.

* Tue Mar 13 2012 David Knox <dknox@redhat.com> 0:6.0.24-43
- Resolves: rhbz# 802396. Changes made to init script.

* Thu Mar 1 2012 David Knox <dknox@redhat.com> 0:6.0.24-42
- Resolves cve-2012-0022 (2011-4858) rhbz 783728

* Mon Jan 23 2012 David Knox <dknox@redhat.com> 0:6.0.24-41
- Resolves: rhbz 782400 - remove redhat-lsb dependency
- Resolves: rhbz 726169 (783407) - Unable to compile class for JSP
- Resolves: rhbz 783567 - tag attributes parsing throws exception

* Wed Jan 5 2012 David Knox <dknox@redhat.com> 0:6.0.24-39
- Resolves: rhbz 757632 - version arg results in CNFException
- changes made to initscript.

* Tue Oct 25 2011 David Knox <dknox@redhat.com> 0:6.0.24-38
- resolves: rhbz 748813 NPE w/no data in chunked POST request
-  Not included in 6.2. Slated for 6.3

* Mon Sep 26 2011 David Knox <dknox@redhat.com> 0:6.0.24-37
- resolves: cve-2011-3190 rhbz 738504
- resolves: cve-2011-2204 rhbz 738504
- resolves: cve-2011-2526 rhbz 738504
- resolves: cve-2011-1184 rhbz 738504
- resolves: rhbz 698624 - revisited

* Mon Aug 29 2011 David Knox <dknox@redhat.com> 0:6.0.24-36
- resolves: rhbz 726169 - jsp1.1 regression exception
- Not included in 6.2 slated for 6.3

* Mon Jun 06 2011 David Knox <dknox@redhat.com> 0:6.0.24-35
- resolves: rhbz 687968 - tomcat6 broken when LANG="fr_FR"

* Tue May 02 2011 David Knox <dknox@redhat.com> 0:6.0.24-34
- resolves: rhbz 701759 - hardcoded catalina.out 
- Not included in 6.2 slated for 6.3

* Thu Apr 28 2011 David Knox <dknox@redhat.com> 0:6.0.24-33
- resolves: rhbz 695284 - multiple instances logging fiasco

* Thu Apr 28 2011 David Knox <dknox@redhat.com> 0:6.0.24-32
- Resolves: rhbz 698624 - inet4address can't be cast to String

* Thu Apr 28 2011 David Knox <dknox@redhat.com> 0:6.0.24-31
- Resolves: rhbz 656403 - cve-2010-4172 jsp syntax error

* Mon Apr 18 2011 David Knox <dknox@redhat.com> 0:6.0.24-30
- Resolves: rhbz#697504 initscript logging location

* Wed Apr 13 2011 David Knox <dknox@redhat.com> 0:6.0.24-29
- Resolves: rhbz#656403, rhbz#675926, rhbz#676011
- CVE-2010-4172, CVE-2010-3718, CVE-2011-0013, CVE-2010-4476,
- CVE-2011-0534
 
* Tue Apr 12 2011 David Knox <dknox@redhat.com> 0:6.0.24-28
- Resovles  rhbz#695284 - wrapper logs to different locations
- CVE-2010-4172, CVE-2011-0013, CVE-2010-3718 commented out 
- until needed. 

* Thu Mar 17 2011 David Knox <dknox@redhat.com> 0:6.0.24-27
- naming-factory-dbcp missing fix in tomcat6.conf
- Add Obsoletes for log4j

* Mon Mar 14 2011 David Knox <dknox@redhat.com> 0:6.0.24-26
- Add log4j to package lib. Corrected typo in log4 Provides
- epock versus epoch

* Wed Mar 09 2011 David Knox <dknox@redhat.com> 0:6.0.24-25
- Installed permissions do not allow tomcat to start
- incrementing NVR so yum won't get confused with the zstream

* Fri Mar 04 2011 David Knox <dknox@redhat.com> 0:6.0.24-23
- Resolves: rhbz 678671 - useradd sets shell to nologin
- dangling symlink for log4j. Added it as R: and R(post)

* Fri Feb 17 2011 David Knox <dknox@redhat.com> 0:6.0.24-21
- Resolves: 678671 - tomcat user requires login shell

* Thu Feb 17 2011 David Knox <dknox@redhat.com> 0:6.0.24-20
- Resolves: rhbz#636997 Additionally created instances of tomcat
- are broken

* Tue Feb 8 2011 David Knox <dknox@redhat.com> 0:6.0.24-19
- Resolves: CVE-2011-0534 rhbz# 675926

* Wed Dec 8 2010 David Knox <dknox@redhat.com> 0:6.0.24-18
- Resolves: rhbz# 661244 missing tomcat6-juli link
- Fixed symlinks to commons-collections and log4j in libdir
- Removed log4j package

* Tue Oct 26 2010 David Knox <dknox@redhat.com> 0:6.0.24-17
- Replacing commons-xxxx-tomcat5 with jakarta-commons-xxxx

* Wed Sep 29 2010 David Knox <dknox@redhat.com> 0:6.0.24-16
- Resolves: rhbz#636997 - Additionally created instances of tomcat are
- broken

* Fri Aug 13 2010 David Knox <dknox@redhat.com> 0:6.0.24-15
- Resolves: rhbz#617501 CVE-2010-2227

* Wed Aug 4 2010 David Knox <dknox@redhat.com> 0:6.0.24-14
- Added 2227 patch

* Mon Jul 12 2010 David Knox <dknox@redhat.com> 0:6.0.24-13
- fixed servlet-api typo

* Thu Jul 1 2010 David Knox <dknox@redhat.com> 0:6.0.24-12
- Resolves: rhbz#584699. A respin was required to fix post and
- postun for el. Updated EL-spec to 2.1 from 1.0. Tomcat6 uses 
- elspec 2.1

* Tue Jun 29 2010 David Knox <dknox@redhat.com> 0:6.0.24-11
- Resolves: rhbz#584699 initscript collected problems LSB
- compliant. Not complete yet. Return values are correct and 
- usage function has been implemented. 

* Thu Jun 23 2010 David Knox <dknox@redhat.com> 0:6.0.24-10
- Resolves: rhbz#606822 CVE-2010-1157

* Thu May 20 2010 David Knox <dknox@redhat.com> 0:6.0.24-9
- Resolves: rhbz#582037 Revert to Java 1.5. Also fixed Error
- deploying web application.

* Thu May 20 2010 David Knox <dknox@redhat.com> 0:6.0.24-8
- Resolves: rhbz#584699 - and two other bugs along with
- various spec flaws fixed. 

* Mon May 17 2010 David Knox <dknox@redhat.com> 0:6.0.24-7
- Build and run using gcj 1.5. Spec refactored. JSP examples
- are working. 

* Wed Apr 21 2010 David Knox <dknox@redhat.com> 0:6.0.24-6
- Patched spec file to avoid sinjdoc issue

* Wed Apr 21 2010 David Knox <dknox@redhat.com> 0:6.0.24-5
- Adding patch for setPerformancePrefernces

* Tue Apr 13 2010 david knox <dknox@redhat.com> 0:6.0.24-4
- increment build number

* Tue Apr 13 2010 David Knox <dknox@redhat.com> 0:6.0.24-3
- Removed prerun lib and post WEB-INF/lib. Moved build-jar-repos to
- after the installs. Added Requires and BuildRequires for jakarta-
- commons-{dbcp,pool,collections}-tomcat5 and ecj. Changed define macro to
- global.

* Tue Apr 13 2010 David Knox <dknox@redhat.com> 0:6.0.24-2
- Revert: Revert JDK/Java Requires and BuildRequires to version 1.5 versus 1.6


* Mon Mar 1 2010 Alexander Kurtakov <akurtako@redhat.com> 0:6.0.24-1
- Update to 6.0.24.

* Tue Dec 22 2009 Alexander Kurtakov <akurtako@redhat.com> 0:6.0.20-2
- Drop file requires on /usr/share/java/ecj.jar.

* Mon Nov 9 2009 Alexander Kurtakov <akurtako@redhat.com> 0:6.0.20-1
- Update to 6.0.20. Fixes CVE-2009-0033,CVE-2009-0580. 

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:6.0.18-10.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 1 2009 Alexander Kurtakov <akurtako@redhat.com> 0:6.0.18-9.2
- Add OSGi manifest for servlet-api.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:6.0.18-9.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 02 2008 David Walluck <dwalluck@redhat.com> 0:6.0.18-8.1
- build for Fedora

* Tue Dec 02 2008 David Walluck <dwalluck@redhat.com> 0:6.0.18-8
- fix directory ownership

* Thu Nov 13 2008 David Walluck <dwalluck@redhat.com> 0:6.0.18-7
- add Requires for update-alternatives

* Tue Oct 07 2008 David Walluck <dwalluck@redhat.com> 0:6.0.18-6
- use lsb_release instead of lsb-release to get the distributor

* Tue Oct 07 2008 David Walluck <dwalluck@redhat.com> 0:6.0.18-5
- fix initscript messages on Mandriva Linux
- fix help message in initscript

* Wed Oct 01 2008 David Walluck <dwalluck@redhat.com> 0:6.0.18-4
- redefine %%_initrddir for FHS-compliance
- make initscript LSB-complaint

* Fri Sep 26 2008 David Walluck <dwalluck@redhat.com> 0:6.0.18-3
- fix status in initscript

* Thu Sep 25 2008 David Walluck <dwalluck@redhat.com> 0:6.0.18-2
- remove initscripts and /sbin/service requirement
- call initscript directly without using /sbin/service
- require /sbin/chkconfig instead of chkconfig
- remove chkconfig requirement from packages that don't require it

* Tue Aug 26 2008 David Walluck <dwalluck@redhat.com> 0:6.0.18-1
- 6.0.18
- Resolves: CVE-2008-1232, CVE-2008-1947, CVE-2008-2370, CVE-2008-2938
- fix definition of java.security.policy with d%%{name} start-security
- don't pass $CATALINA_OPTS with d%%{name} stop
- redefine tempdir and workdir for tmpwatch workaround
- change eclipse-ecj references to ecj

* Thu Jul 10 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0:6.0.16-1.8
- drop repotag

* Fri Apr 04 2008 David Walluck <dwalluck@redhat.com> 0:6.0.16-1jpp.7.fc9
- version jsp and servlet Provides with their spec versions
- remove Obsoletes/Provides for servletapi6 package as it can co-exist
- check for java-functions existence in wrapper script
- move d%%{name} to %%{name} and create symlink for d%%{name}
- improve status function in initscript
- change license to ASL 2.0 again as per Fedora guidelines

* Mon Mar 24 2008 David Walluck <dwalluck@redhat.com> 0:6.0.16-1jpp.6.fc9
- remove Requires: tomcat-native
- put back original JPackage Group (except javadoc) and License tags
- add Provides for jsp and servlet
- use ant macro
- build and install sample webapp
- call /sbin/service to stop service on uninstall
- remove references to $RPM_BUILD_DIR
- use copy instead of move to fix short-circuit install build
- remove prebuilt sample.war
- remove Thumbs.db files
- add Requires: java >= 0:1.6.0

* Mon Mar 24 2008 David Walluck <dwalluck@redhat.com> 0:6.0.16-1jpp.6.fc9
- remove Requires: tomcat-native
- put back original JPackage Group (except javadoc) and License tags
- add Provides for jsp and servlet
- use ant macro
- build and install sample webapp
- call /sbin/service to stop service on uninstall
- remove references to $RPM_BUILD_DIR
- use copy instead of move to fix short-circuit install build
- remove prebuilt sample.war
- remove Thumbs.db files
- add Requires: java >= 0:1.6.0

* Wed Mar 19 2008 David Walluck <dwalluck@redhat.com> 0:6.0.16-1jpp.5.fc9
- explicitly unset CLASSPATH
- explicitly set OPT_JAR_LIST to include ant/ant-trax

* Tue Mar 18 2008 David Walluck <dwalluck@redhat.com> 0:6.0.16-1jpp.4.fc9
- remove BuildRequires: sed
- remove specific references to icedtea

* Mon Mar 17 2008 David Walluck <dwalluck@redhat.com> 0:6.0.16-1jpp.3.fc9
- add digest and tool-wrapper scripts
- Requires: tomcat-native

* Fri Mar 7 2008 David Walluck <dwalluck@redhat.com> 0:6.0.16-1jpp.2.fc9
- use %%{_var} for appdir instead of /srv
- use ${JAVACMD} for java executable in wrapper script
- use built-in status function in initscript where possible
- add missing require on procps for status function
- fix java.library.path setting in %%{_sysconfdir}/sysconfig/%%{name}
- add patch to document webapps in %%{_sysconfdir}/%%{name}/tomcat-users.xml
- remove %%{appdir}/ROOT/admin
- move %%{_bindir}/d%%{name} to %%{_sbindir}/d%%{name}

* Mon Mar 3 2008 David Walluck <dwalluck@redhat.com> 0:6.0.16-1jpp.1.fc9
- use %%{_initrddir} macro instead of %%{_sysconfdir}/init.d (rhbz #153187)
- fix java.library.path setting in %%{name}.conf (rhbz #253605)
- fix incorrect initscript output (rhbz #380921)
- update initscript (rhbz #247077)
- add logrotate support
- fix strange-permission
- fix %%prep
- replace /var with %%{_var}
- replace %%{_localstatedir} with %%{_var}
- use %%{logdir} where possible
- call build-jar-repository with full path in scriptlets
- remove file-based requires
- build with icedtea and set as the default JAVA_HOME in %%{name}.conf
- fix non-standard-group
- change ecj references to eclipse-ecj
- change Apache Software License 2.0 to ASL 2.0 for rpmlint

* Fri Feb  8 2008 Jason Corley <jason.corley@gmail.com> - 0:6.0.16-1jpp
- update to 6.0.16

* Sun Dec  2 2007 Jason Corley <jason.corley@gmail.com> - 0:6.0.14-2jpp
- add /etc/tomcat6/Catalina/localhost (Alexander Kurtakov)

* Tue Aug 14 2007 Jason Corley <jason.corley@gmail.com> 0:6.0.14-1jpp
- first JPackage release
