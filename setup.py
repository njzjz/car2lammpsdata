"""Use 'pip install .' to install."""


from setuptools import find_packages, setup

if __name__ == '__main__':

    setup(name='car2lammpsdata',
          description='car2lammpsdata',
          version='0.0.3',
          keywords="car2lammpsdata",
          url='https://github.com/njzjz/car2lammpsdata',
          author='Jinzhe Zeng',
          author_email='jzzeng@stu.ecnu.edu.cn',
          packages=find_packages(),
          python_requires='~=3.3',
          install_requires=[
              'ase',
          ],
          entry_points={
              'console_scripts': [
                  'car2lammpsdata=car2lammpsdata.car2lammpsdata:_commandline',
              ]
          },
          use_scm_version=True,
          classifiers=[
              "Natural Language :: English",
              "Operating System :: POSIX :: Linux",
              "Operating System :: Microsoft :: Windows",
              "Programming Language :: Python :: 3.6",
              "Programming Language :: Python :: 3.7",
              "Topic :: Scientific/Engineering :: Chemistry",
              "Topic :: Software Development :: Libraries :: Python Modules",
              "Topic :: Software Development :: Version Control :: Git",
          ],
          zip_safe=True,
          )
