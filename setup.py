from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext as _build_ext
from Cython.Build import cythonize


class build_ext(_build_ext):
    """Builds RVO2 before our module."""

    def run(self):
        # Build RVO2
        import os
        import os.path
        import subprocess

        build_dir = os.path.abspath('build/RVO2')
        if not os.path.exists(build_dir):
            os.makedirs(build_dir)
            subprocess.check_call(['cmake', '../..', '-DCMAKE_CXX_FLAGS=-fPIC'],
                                  cwd=build_dir)
        subprocess.check_call(['make', '-j8'], cwd=build_dir)

        super().run()


extensions = [
    Extension('rvo2', ['src/*.pyx'],
              include_dirs=['src'],
              libraries=['RVO'],
              library_dirs=['build/RVO2/src'],
              extra_compile_args=['-fPIC']),
]

setup(
    name="pyrvo2",
    ext_modules=cythonize(extensions),
    cmdclass={'build_ext': build_ext},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Games/Entertainment :: Simulation',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
