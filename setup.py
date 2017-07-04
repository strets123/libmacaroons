from setuptools import setup, Extension
from Cython.Distutils import build_ext

NAME = "macaroons"
VERSION = "0.1"
DESCR = "A small template project that shows how to wrap C/C++ code into python using Cython"
URL = "http://www.google.com"
REQUIRES = [ 'cython']

AUTHOR = "Tristan A. Hearn"
EMAIL = "tristanhearn@gmail.com"

LICENSE = "Apache 2.0"

SRC_DIR = ""
PACKAGES = [NAME]

data = [ SRC_DIR + item for item in [  "bindings/python/macaroons.pyx",  "macaroons.c", "base64.c",
"explicit_bzero.c",
"packet.c",
"port.c",
"sha256.c",
"shim.c",
"slice.c",
"timingsafe_bcmp.c",
"tweetnacl.c",
"v1.c",
"v2.c",
"varint.c"]]


ext_1 = Extension( "macaroons", data,
                  libraries=[],
                  include_dirs=["."])


EXTENSIONS = [ext_1]

if __name__ == "__main__":
    setup(install_requires=REQUIRES,
          packages=PACKAGES,
          package_dir={ 'macaroons': ''},
          zip_safe=False,
          name=NAME,
          version=VERSION,
          description=DESCR,
          author=AUTHOR,
          author_email=EMAIL,
          url=URL,
          license=LICENSE,
          cmdclass={"build_ext": build_ext},
          ext_modules=EXTENSIONS
          )
