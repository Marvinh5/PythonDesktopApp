import sys
from cx_Freeze import setup, Executable

path_platforms = ( "C:\Python34\Lib\site-packages\PyQt5\plugins\platforms\qwindows.dll", "platforms\qwindows.dll",)

includes = ["PyQt5.QtCore","PyQt5.QtGui", "PyQt5.QtWidgets"]
includefiles = [path_platforms,"Auth.ui"]
excludes = []
packages = ["os"]
path = []

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
                     "includes":      includes, 
                     "include_files": includefiles,
                     "excludes":      excludes, 
                     "packages":      packages, 
                     "path":          path,
                     "include_msvcr": True
}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
exe = None
if sys.platform == "win32":
    exe = Executable(
      script="Authentication.py",
      initScript = None,
      base="Win32GUI",
      targetName="Auth.exe",
      compress = True,
      copyDependentFiles = True,
      appendScriptToExe = False,
      appendScriptToLibrary = False,
      icon = None
    )

setup(  
      name = "AuthForm",
      version = "0.1",
      author = 'Marvin',
      description = "Authentication Application!",
      options = {"build_exe": build_exe_options},
      executables = [exe]
)