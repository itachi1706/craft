import info

class subinfo(info.infoclass):
    def setTargets( self ):
        """ """
        self.targets['5.1.36-3'] = """
http://downloads.sourceforge.net/kde-windows/mysql-server-5.1.36-3-bin.tar.bz2
http://downloads.sourceforge.net/kde-windows/mysql-server-5.1.36-3-lib.tar.bz2
"""
        self.targetDigests['5.1.36-3'] = ['75a2dd72879bc71ea80c2b06e90d37792d80782d',
                                          'b94d2fbb213d6f5244e402977dacd10605657d4a']
        self.targetInstSrc['5.1.36-3'] = ""
        self.defaultTarget = '5.1.36-3'

    def setDependencies( self ):
        """ """
        self.hardDependencies['gnuwin32/wget'] = 'default'
        
from Package.BinaryPackageBase import *

class Package(BinaryPackageBase):
    def __init__( self ):
        self.subinfo = subinfo()
        BinaryPackageBase.__init__( self )
      
            

if __name__ == '__main__':
    Package().execute()
