@echo off

MODE COM9:38400,N,8,1 >NUL

:loop

set totalMem=
set availableMem=
set usedMem=

for /f "tokens=4" %%a in ('systeminfo ^| findstr Physical') do if defined totalMem (set availableMem=%%a) else (set totalMem=%%a)

set totalMem=%totalMem:,=%
set availableMem=%availableMem:,=%
set /a usedMem=totalMem-availableMem
wmic cpu get loadpercentage

set /p x="%totalMem%P%usedMem%P%cpuUsage%PLine1PLine2PLine3PE" <nul >\\.\COM9
ping 192.0.2.2 -n 1 -w 1000 > nul

goto loop