# -*- coding: utf-8 -*-
import utils
import shutil
import os
import info

class subinfo(info.infoclass):
    def setTargets( self ):
        ver = "20111031"
        self.targets[ver] = "http://downloads.sourceforge.net/sourceforge/mingw-w64/mingw-w32-bin_i686-mingw_"+ver+"_sezero.zip"
        self.defaultTarget = ver
        
        
        self.targets["4.7.2"] = "http://downloads.sourceforge.net/sourceforge/mingwbuilds/%s-4.7.2-release-posix-sjlj-rev3.7z" % emergePlatform.buildArchitecture()
        self.targets["4.8.0-2"] = "http://downloads.sourceforge.net/sourceforge/mingwbuilds/x32-4.8.0-release-posix-sjlj-rev2.7z"

    def setDependencies( self ):
        self.buildDependencies['virtual/bin-base'] = 'default'

from Package.BinaryPackageBase import *

class Package(BinaryPackageBase):
    def __init__( self):
        self.subinfo = subinfo()
        self.subinfo.options.merge.ignoreBuildType = True
        BinaryPackageBase.__init__(self)

    def install(self):
        shutil.move( os.path.join( self.installDir() , "mingw32" ) , os.path.join( self.installDir(), "mingw" ) )
        if self.subinfo.buildTarget == "20111031":
            shutil.copy( os.path.join( self.installDir() , "mingw" , "bin" , "gmake.exe") , os.path.join( self.installDir() , "mingw" , "bin" , "mingw32-make.exe") )
            utils.applyPatch( self.imageDir(), os.path.join( self.packageDir(), "gcc_Exit.diff"), 0 )
        return True

if __name__ == '__main__':
    Package().execute()
