@ECHO OFF

MODE COM9:9600,N,8,1 >NUL

:loop

set totalMem=
set availableMem=
set usedMem=
REM You need to make a loop
for /f "tokens=4" %%a in ('systeminfo ^| findstr Physical') do if defined totalMem (set availableMem=%%a) else (set totalMem=%%a)
set totalMem=%totalMem:,=%
set availableMem=%availableMem:,=%
set /a usedMem=totalMem-availableMem
Echo Total Memory: %totalMem%
Echo Used Memory: %usedMem%
set /p x="Mem: %usedMem% " <nul >\\.\COM9

ping 192.0.2.2 -n 1 -w 1000 > nul
goto loop