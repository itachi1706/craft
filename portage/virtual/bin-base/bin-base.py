import info


class subinfo(info.infoclass):
    def setTargets( self ):
        self.targets['0.2'] = ""
        self.defaultTarget = '0.2'

    def setDependencies( self ):
        self.buildDependencies['gnuwin32/wget'] = 'default'
        self.buildDependencies['dev-util/7zip'] = 'default'
        self.buildDependencies['dev-util/shimgen'] = 'default'
        self.buildDependencies['gnuwin32/patch'] = 'default'
        self.runtimeDependencies['libs/craft'] = 'default'

from Package.VirtualPackageBase import *
from Source.SourceBase import *

class Package(VirtualPackageBase):
    def __init__(self):
        VirtualPackageBase.__init__(self)

