#!%(context.build_env_exe)s -I

import os
import sys


os.environ['PYTHON_CROSSENV'] = "%(context.sentinel)d"

for name in ['_PYTHON_PROJECT_BASE', '_PYTHON_HOST_PLATFORM',
        '_PYTHON_SYSCONFIGDATA_NAME', 'PYTHONHOME', 'PYTHONPATH']:
    old = '_OLD_' + name
    if old not in os.environ and name in os.environ:
        os.environ[old] = os.environ[name]

os.environ['_PYTHON_PROJECT_BASE']=%(self.host_project_base)r
os.environ['_PYTHON_HOST_PLATFORM']=%(self.host_platform)r
os.environ['_PYTHON_SYSCONFIGDATA_NAME']=%(sysconfig_name)r
os.environ['PYTHONHOME']=%(self.host_home)r
oldpath = os.environ.get('PYTHONPATH')
newpath = os.pathsep.join([%(context.lib_path)r, %(stdlib)r])
if oldpath:
    path = os.pathsep.join([newpath, oldpath])
else:
    path = newpath

os.environ['PYTHONPATH'] = path

%(extra_envs)s

# This will fix up argv0 so that sys.executable will be correct
os.execv(%(context.build_env_exe)r, sys.argv)
