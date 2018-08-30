@echo off
echo. 
echo.
echo ——【excel软标准表格安装、卸载工具】——
title 【excel软标准表格工作室 控件安装助手】
echo. 
echo. 
:menu
echo 请选择:
echo. 
echo    1 【安装 “A股数据”工具插件】
echo. 
echo    2 【卸载 “A股数据”工具插件】
echo. 
echo    3 【退 出】
echo.
set /p select=请输入菜单对应数字后回车:  
if /i "%select%" == "1" goto 安装
if /i "%select%" == "2" goto 卸载
if /i "%select%" == "3" goto exit
goto menu
 
:安装
cls

REG ADD "HKEY_CURRENT_USER\Software\Microsoft\Office\11.0\Excel\Security" /v "Level" /t REG_DWORD /d 1 /f
REG ADD "HKEY_CURRENT_USER\Software\Microsoft\Office\12.0\Excel\Security" /v "VBAWarnings" /t REG_DWORD /d 1 /f
REG ADD "HKEY_CURRENT_USER\Software\Microsoft\Office\14.0\Excel\Security" /v "VBAWarnings" /t REG_DWORD /d 1 /f
Cls
ECHO.
echo ***　安装成功　***
 
goto exit
 
:卸载
cls

REG ADD "HKEY_CURRENT_USER\Software\Microsoft\Office\11.0\Excel\Security" /v "Level" /t REG_DWORD /d 2 /f
REG ADD "HKEY_CURRENT_USER\Software\Microsoft\Office\12.0\Excel\Security" /v "VBAWarnings" /t REG_DWORD /d 2 /f
REG ADD "HKEY_CURRENT_USER\Software\Microsoft\Office\14.0\Excel\Security" /v "VBAWarnings" /t REG_DWORD /d 2 /f
Cls
ECHO.
echo ***　卸载成功　***
 
goto exit
 
:exit
echo. 
echo. 
pause
exit 


