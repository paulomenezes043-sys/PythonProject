from cx_Freeze import setup, Executable


executable =  [Executable('main.py')]
setup(
    name='Projeto aulas',
    version='1.0',
    description ='Mountain Shooter app',
    options={'build_exe': {'packages':['pygame']}},
    executables=executable)