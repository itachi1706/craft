# -*- coding: utf-8 -*-
import utils
import os
import info
import emergePlatform
import compiler
import shutil

class subinfo(info.infoclass):
    def setTargets( self ):
        self.targets['49.1.1'] = 'http://download.icu-project.org/files/icu4c/49.1.1/icu4c-49_1_1-src.tgz'
        self.targetInstSrc['49.1.1'] = "icu\\source"
        self.targetDigests['49.1.1'] = 'f407d7e2808b76e3a6ca316aab896aef74bf6722'
        self.patchToApply[ '49.1.1' ] = [('icu-20120702.diff', 1)]
        if compiler.isMSVC2012():
            self.patchToApply[ '49.1.1' ].append(('msvc2011.diff', 1))
        self.defaultTarget = '49.1.1'

    def setDependencies( self ):
        self.buildDependencies['virtual/base'] = 'default'
        if compiler.isMinGW():
            self.buildDependencies['dev-util/msys'] = 'default'

from Package.CMakePackageBase import *

class PackageCMake(CMakePackageBase):
    def __init__( self, **args ):
        self.subinfo = subinfo()
        CMakePackageBase.__init__( self )

    def configure(self):
        return True

    def make(self):
        self.enterSourceDir()
        if self.buildType() == "Debug":
          bt = "Debug"
        else:
          bt = "Release"
        utils.system("msbuild /t:Rebuild %s /p:Configuration=%s" % (os.path.join(self.sourceDir(), "allinone", "allinone.sln" ), bt) )
        return True

    def install(self):
        utils.copyDir(os.path.join(self.sourceDir(), "..", "bin"), os.path.join(self.imageDir(), "bin"))
        utils.copyDir(os.path.join(self.sourceDir(), "..", "include"), os.path.join(self.imageDir(), "include"))
        utils.copyDir(os.path.join(self.sourceDir(), "..", "lib"), os.path.join(self.imageDir(), "lib"))
        return True

from Package.AutoToolsPackageBase import *

class PackageMSys(AutoToolsPackageBase):
    def __init__( self ):
        self.subinfo = subinfo()
        AutoToolsPackageBase.__init__(self)

    def install(self):
        if not AutoToolsPackageBase.install(self):
            return False
        files = os.listdir(os.path.join( self.installDir() , "lib" ))
        for dll in files:
            if dll.endswith(".dll"):
                utils.copyFile( os.path.join( self.installDir() , "lib" ,dll) , os.path.join( self.installDir(), "bin" ,dll) )
        return True

if compiler.isMinGW():
    class Package(PackageMSys):
        def __init__( self ):
            PackageMSys.__init__( self )
else:
    class Package(PackageCMake):
        def __init__( self ):
            PackageCMake.__init__( self )

if __name__ == '__main__':
      Package().execute()
