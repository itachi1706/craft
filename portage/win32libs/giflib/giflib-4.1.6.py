import shutil
import info
from Package.CMakePackageBase import *

class subinfo(info.infoclass):
    def setTargets( self ):
        for ver in ['4.1.6', '5.0.4']:
            self.targets[ver] = 'http://downloads.sourceforge.net/sourceforge/giflib/giflib-' + ver + '.tar.bz2'
            self.targetInstSrc[ver] = 'giflib-' + ver
        self.targetDigests['5.0.4'] = 'af3fdf84e2b9ac5c18e7102835a92e2066c7c9f1'
        self.patchToApply['4.1.6'] = ("giflib-4.1.6-20100327.diff", 1)
        self.patchToApply['5.0.4'] = [("giflib-5.0.4-20130202.diff", 1)]
        self.shortDescription = "GIF file manipulation library (utilities and docs)"
        self.defaultTarget = '4.1.6'

    def setDependencies( self ):
        self.buildDependencies['virtual/base'] = 'default'
        self.dependencies['win32libs/zlib'] = 'default'

class Package(CMakePackageBase):
    def __init__( self, **args ):
        self.subinfo = subinfo()
        CMakePackageBase.__init__( self )
        self.subinfo.options.package.packageName = 'giflib'
        self.subinfo.options.configure.defines = "-DBUILD_utils=OFF"


if __name__ == '__main__':
    Package().execute()
