# Copyright 2016 Mario Graff (https://github.com/mgraffg)

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from setuptools import setup


setup(
    name="b4msa",
    description="""Baselines for Multilingual Sentiment Analysis""",
    # long_description=long_desc,
    # version=version,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        'Programming Language :: Python :: 3',
        "Topic :: Scientific/Engineering :: Artificial Intelligence"],
    # url='https://github.com/mgraffg/EvoDAG',
    # author="Mario Graff",
    # author_email="mgraffg@ieee.org",
    # cmdclass={"build_ext": build_ext, "clean": Clean},
    # ext_modules=ext_modules,
    # packages=['EvoDAG', 'EvoDAG/tests'],
    # include_package_data=True,
    # zip_safe=False,
    # package_data={'': ['*.pxd']},
    # install_requires=['cython >= 0.19.2', 'numpy >= 1.6.2'],
    # entry_points={
    #     'console_scripts': ['EvoDAG=EvoDAG.command_line:main'],
    # }
)
