#! /usr/bin/python
#
# Copyright (c) 2013-2014 The LearnByGame Project,Fofight Fong all rights reserved,
#
# coding=utf-8
#
# Python installer
#
# The file is the part of LearnByGame
#
"""
setup.py for installing LearnByGame

Usage:
   python setup.py install

Permission to use, modify, and distribute this software is given under the
terms of the GPL

NO WARRANTY IS EXPRESSED OR IMPLIED.  USE AT YOUR OWN RISK.

Version: 0.1

Date: 2013-2014-

"""

import platform
from __future__ import print_function
import sys
import os
from ez_setup import use_setuptools
from ctypes.util import find_library
from setuptools import setup, find_packages,Extension
import wifiphisher.common.constants as constants

# run installer with different platform
if platform.system() == "Linux":
	# Check user ID
	if os.getuid() != 0:
        print("Are you root? Please execute as root")
        exit()
    	
	try:
        	# if our command option is true then install stuff
        	if sys.argv[1] == "install":
            		installer = True
    	# if index is out of range then flag options
    	except IndexError:
        	print("** SET Dependency Installer **")
        	print("** Written by:Fofight**")
        	print("** Visit: https://www.github.com/Fofight/Learnbgame/LearnByGame **")
        	print("\nTo install: setup.py install")
    	# if user specified install then lets to the installation
    	if installer is True:
        	
		# if we trigger on sources.list then we know its ubuntu
        	if os.path.isfile("/etc/apt/sources.list"):
            		# force install of debian packages
            		subprocess.Popen("apt-get -y install "
                             "git apache2 python-requests libapache2-mod-php "
                             "python-pymssql build-essential python-pexpect "
                             "python-pefile python-crypto python-openssl", shell=True).wait()

        # If pacman.conf exists, we have a Arch based system
        elif os.path.isfile("/etc/pacman.conf"):
            subprocess.Popen("pacman -S --noconfirm --needed git python2 "
                             "python2-beautifulsoup3 python2-pexpect python2-crypto", shell=True).wait()

            subprocess.Popen("wget https://github.com/erocarrera/pefile/archive/master.zip", shell=True).wait()
            subprocess.Popen("unzip master.zip", shell=True).wait()
            subprocess.Popen("chmod a+x pefile-master/setup.py", shell=True).wait()
            subprocess.Popen("rm -rf pefile-master*", shell=True).wait()

        # if dnf.conf is there, we are dealing with a >= fedora 22 - added thanks to whoismath pr
        elif os.path.isfile("/etc/dnf/dnf.conf"):
            subprocess.Popen("dnf -y install git python-pexpect python-pefile python-crypto pyOpenSSL", shell=True).wait()

        # if sources.list or pacman.conf is not available then we're running
        # something offset
        else:
            print("[!] You're not running a Debian, Fedora or Arch variant. Installer not finished for this type of Linux distro.")
            print("[!] Install git, python-pexpect, python-crypto, python-openssl, python-pefile manually for all of SET dependancies.")
            sys.exit()

        if os.path.isdir("/usr/share/setoolkit"):
            print("[!] SET is already installed in /usr/share/setoolkit. Remove and start again.")
            sys.exit()

        if not os.path.isfile("/usr/bin/git"):
            print("[-] Install failed. GIT is not installed. SET will not continue.")
            print("[!] Install GIT and run the installer again.")
            sys.exit()

        print("[*] Copying SET into the /usr/share/setoolkit directory...")
        cwdpath = os.getcwd()
        subprocess.Popen("cd ..;cp -rf %s /usr/share/setoolkit" % cwdpath, shell=True).wait()
        print("[*] Installing setoolkit installer to /usr/bin/setoolkit...")
        subprocess.Popen("echo #!/bin/bash > /usr/bin/setoolkit", shell=True).wait()
        subprocess.Popen("echo cd /usr/share/setoolkit >> /usr/bin/setoolkit", shell=True).wait()
        subprocess.Popen("echo exec python2 setoolkit $@ >> /usr/bin/setoolkit", shell=True).wait()
        subprocess.Popen("cp /usr/share/setoolkit/seupdate /usr/bin/", shell=True).wait()
        subprocess.Popen("chmod +x /usr/bin/setoolkit", shell=True).wait()
        print("[*] We are now finished! To run SET, type setoolkit...")

if platform.system() == 'Darwin':
    subprocess.Popen("easy_install pexpect pycrypto pyopenssl pefile", shell=True).wait()
       
if platform.system() not in  ["Linux", "Darwin"]:
    print("[!] Sorry this installer is not designed for any other system other "
          "than Linux and Mac. Please install the Python dependencies manually.")



"""
This module tries to install all the required software.
"""
def get_dnsmasq():
    """
    Try to install dnsmasq on host machine if not present

    :return: None
    :rtype: None
    """

    if not os.path.isfile("/usr/sbin/dnsmasq"):
        install = raw_input(("[" + constants.T + "*" + constants.W + "] dnsmasq not found " +
                             "in /usr/sbin/dnsmasq, " + "install now? [y/n] "))

        if install == "y":
            if os.path.isfile("/usr/bin/pacman"):
                os.system("pacman -S dnsmasq")
            elif os.path.isfile("/usr/bin/yum"):
                os.system("yum install dnsmasq")
            else:
                os.system("apt-get -y install dnsmasq")
        else:
            sys.exit(("[" + constants.R + "-" + constants.W + "] dnsmasq " +
                      "not found in /usr/sbin/dnsmasq"))

    if not os.path.isfile("/usr/sbin/dnsmasq"):
        dnsmasq_message = ("\n[" + constants.R + "-" + constants.W +
                           "] Unable to install the \'dnsmasq\' package!\n" + "[" + constants.T +
                           "*" + constants.W + "] This process requires a persistent internet " +
                           "connection!\nPlease follow the link below to configure your " +
                           "sources.list\n" + constants.B + "http://docs.kali.org/general-use/" +
                           "kali-linux-sources-list-repositories\n" + constants.W + "[" +
                           constants.G + "+" + constants.W + "] Run apt-get update for changes " +
                           "to take effect.\n" + "[" + constants.G + "+" + constants.W + "] " +
                           "Rerun the script to install dnsmasq.\n[" + constants.R + "!" +
                           constants.W + "] Closing")

        sys.exit(dnsmasq_message)


def get_hostapd():
    """
    Try to install hostapd on host system if not present

    :return: None
    :rtype: None
    """

    if not os.path.isfile("/usr/sbin/hostapd"):
        install = raw_input(("[" + constants.T + "*" + constants.W + "] hostapd not found in " +
                             "/usr/sbin/hostapd, install now? [y/n] "))

        if install == "y":
            if os.path.isfile("/usr/bin/pacman"):
                os.system("pacman -S hostapd")
            elif os.path.isfile("/usr/bin/yum"):
                os.system("yum install hostapd")
            else:
                os.system("apt-get -y install hostapd")
        else:
            sys.exit(("[" + constants.R + "-" + constants.W + "] hostapd not found in " +
                      "/usr/sbin/hostapd"))

    if not os.path.isfile("/usr/sbin/hostapd"):
        hostapd_message = ("\n[" + constants.R + "-" + constants.W + "] Unable to install the " +
                           "\'hostapd\' package!\n[" + constants.T + "*" + constants.W + "] " +
                           "This process requires a persistent internet connection!\nPlease " +
                           "follow the link below to configure your sources.list\n" + constants.B +
                           "http://docs.kali.org/general-use/kali-linux-sources-list-" +
                           "repositories\n" + constants.W + "[" + constants.G + "+" + constants.W +
                           "] Run apt-get update for changes to take effect.\n[" + constants.G +
                           "+" + constants.W + "] Rerun the script to install hostapd.\n[" +
                           constants.R + "!" + constants.W + "] Closing")

        sys.exit(hostapd_message)


def get_libdbus():
    """
    Try to install the libdbus
    return: None
    retype: None
    """

    # install the libdbus-1
    if not find_library("dbus-1"):
        install = raw_input(("[" + constants.T + "*" + constants.W + "] libdbus-1 not found " +
                             "install now? [y/n] "))

        if install == "y":
            if os.path.isfile("/usr/bin/apt-get"):
                os.system("apt-get -y install libdbus-1-dev")
            else:
                sys.exit(("[" + constants.R + "-" + constants.W + "] libdbus-1 not found. "
                          "Please install libdbus-1 (i.e. using your package manager)"))
        else:
            sys.exit(("[" + constants.R + "-" + constants.W + "] libdbus-1 not found. "
                      "Please install libdbus-1 (i.e. using your package manager)"))

    # install the dbus-glib-1
    if not find_library("dbus-glib-1"):
        install = raw_input(("[" + constants.T + "*" + constants.W + "] dbus-glib-1 "
                             "not found install now? [y/n] "))

        if install == "y":
            if os.path.isfile("/usr/bin/apt-get"):
                os.system("apt-get -y install libdbus-glib-1-dev")
            else:
                sys.exit(("[" + constants.R + "-" + constants.W + "] libdbus-glib-1 not found. "
                          "Please install libdbus-glib-1 (i.e. using your package manager)"))
        else:
            sys.exit(("[" + constants.R + "-" + constants.W + "] libdbus-glib-1 not found. "
                      "Please install libdbus-glib-1 (i.e. using your package manager)"))

# check the dbus related libraries first
get_libdbus()

# setup settings
NAME = "LearnByGame"
AUTHOR = "FofightFong"
maintainer= "Fofight"
maintainer_email=""
AUTHOR_EMAIL = "ffofight@gmail.com"
URL = "https://github.com/Fofight/Learnbgame/LearnByGame"
download_url = ""
DESCRIPTION = "when,what,where,who,why,How?--The world,you are here.0 and 1 or...Learn by game!"
long_description =""
LICENSE = "F"
NAMESPACE_PACKAGES=[],
KEYWORDS = ["Fofight", "Fong", "Learnbgame", "LearnByGame","Free","Future"]
PACKAGES = find_packages(exclude=["", ""])#?
INCLUDE_PACKAGE_DATA = True
VERSION = "0.1"
ZIP_SAFE=False,
PLATFORMS = ["any"],
platforms="Unix, Windows (mingw|cygwin), Mac OSX",
CLASSIFIERS = ["Development Status :: 5 - Production/Stable",
      	       "Development Status :: 3 - Alpha",
               "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
               "Natural Language :: English", 
               "Programming Language :: Python",
	       "Programming Language :: C/C++",
	       "Programming Language :: Perl",
	       "Programming Language :: Lisp",
	       "Programming Language :: Java",
	       "Programming Language :: Fortran",
               "Topic :: Security",
               "Topic :: Internet :: WWW/HTTPS :: WSGI :: Application",
               "Topic :: Software Development :: Libraries :: Python Modules",
               "Topic :: Scientific/Engineering",
               "Topic :: Software Development :: Code Generators",
	       "Topic :: System :: Networking",
               "Environment :: Win32 (MS Windows)",
               "Environment :: X11 Applications",
	       "Operating System :: OS Independent",
               "Operating System :: Microsoft :: Windows",
               "Operating System :: POSIX",
               "Operating System :: MacOS",
	       "Intended Audience :: End Users/Desktop",
               "Intended Audience :: System Administrators",
	       "Intended Audience :: Developers",
               "Intended Audience :: Science/Research",
               "Intended Audience :: Information Technology"]
ENTRY_POINTS = {"console_scripts": ["Fong : run"]}
INSTALL_REQUIRES = []
test_suite =[]
ext_modules = ""
extras_require = ""
cmdclass = {}
TESTS_REQUIRE=[],


# run setup
setup(name=NAME, author=AUTHOR, author_email=AUTHOR_EMAIL, description=DESCRIPTION,
      license=LICENSE, keywords=KEYWORDS, packages=PACKAGES,namespace_packages=NAMESPACE_PACKAGES,
      include_package_data=INCLUDE_PACKAGE_DATA, version=VERSION, entry_points=ENTRY_POINTS,
      install_requires=INSTALL_REQUIRES, classifiers=CLASSIFIERS, 
      url=URL,tests_require=TESTS_REQUIRE,zip_safe=ZIP_SAFE,platforms=PLATFORMS)

# Get hostapd or dnsmasq if needed
get_hostapd()
get_dnsmasq()

print()
print("		     __	")
print("		    |  |")
print("  ((.))	    |  |   _	  __		")    
print(r"    |       |  |  / \    /  \ 		")  
print(r"   /_\      |  | |___|   |   | 		| | \__ \ | | |  __/ |   ")
print(r"  /___\     |  | |       \   |   	_|_|___/_| |_|\___|_|   ")
print(r" /     \    |  | |_____|  \__|_    _       | |                                ")
print("             |  ------             |_|                                ")
print("             |________|                                                  ")


if __name__ == '__main__':
    print('This is the wrong setup.py file to run')




