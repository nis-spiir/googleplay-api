from setuptools import setup
#from setuptools.command.build_py import build_py as _build
from distutils.command.build_py import build_py as _build_py

import os.path
import subprocess

PROTOC_EXEC = "protoc"

CURRENT_DIR = os.path.abspath( os.path.dirname( __file__ ) )

class ProtobufBuilder(_build_py):

    def run(self):
        # check if protobuf is installed
        try:
            exec_path = subprocess.check_output(["which", PROTOC_EXEC])[:-1]
        except subprocess.CalledProcessError:
            raise Exception("You should install protobuf compiler")

        print("Building protobuf file")
        subprocess.call([exec_path,
            "--proto_path=" + CURRENT_DIR,
            "--python_out=" + CURRENT_DIR + "/gpapi/",
            CURRENT_DIR + "/googleplay.proto"])
        _build_py.run(self)

setup(name='gpapi',
      version='0.4.5',
      description='Unofficial python api for google play',
      url='https://github.com/NoMore201/googleplay-api',
      author='NoMore201',
      author_email='domenico.iezzi.201@gmail.com',
      license='GPL3',
      packages=['gpapi'],
      package_data={
          'gpapi': [
              'config.py'
              'device.properties',
              'googleplay_pb2.py',
              'googleplay.py',
              'utils.py'
          ]},
      include_package_data=True,
      cmdclass={'build_py': ProtobufBuilder},
      install_requires=['cryptography>=2.2',
                        'protobuf>=3.5.2',
                        'requests'])
