from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='1',
      description='Sort files in the directory',
      url='https://github.com/PotapovALeksey/education/tree/main/hw-6',
      author='Alex Potapov',
      author_email='alexpotapov@example.com',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={ 'console_scripts': ['clean-folder = clean_folder.main:clean_folder'] }
)