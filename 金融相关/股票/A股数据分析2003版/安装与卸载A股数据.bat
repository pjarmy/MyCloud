@echo off
echo. 
echo.
echo ������excel���׼���װ��ж�ع��ߡ�����
title ��excel���׼������� �ؼ���װ���֡�
echo. 
echo. 
:menu
echo ��ѡ��:
echo. 
echo    1 ����װ ��A�����ݡ����߲����
echo. 
echo    2 ��ж�� ��A�����ݡ����߲����
echo. 
echo    3 ���� ����
echo.
set /p select=������˵���Ӧ���ֺ�س�:  
if /i "%select%" == "1" goto ��װ
if /i "%select%" == "2" goto ж��
if /i "%select%" == "3" goto exit
goto menu
 
:��װ
cls

REG ADD "HKEY_CURRENT_USER\Software\Microsoft\Office\11.0\Excel\Security" /v "Level" /t REG_DWORD /d 1 /f
REG ADD "HKEY_CURRENT_USER\Software\Microsoft\Office\12.0\Excel\Security" /v "VBAWarnings" /t REG_DWORD /d 1 /f
REG ADD "HKEY_CURRENT_USER\Software\Microsoft\Office\14.0\Excel\Security" /v "VBAWarnings" /t REG_DWORD /d 1 /f
Cls
ECHO.
echo ***����װ�ɹ���***
 
goto exit
 
:ж��
cls

REG ADD "HKEY_CURRENT_USER\Software\Microsoft\Office\11.0\Excel\Security" /v "Level" /t REG_DWORD /d 2 /f
REG ADD "HKEY_CURRENT_USER\Software\Microsoft\Office\12.0\Excel\Security" /v "VBAWarnings" /t REG_DWORD /d 2 /f
REG ADD "HKEY_CURRENT_USER\Software\Microsoft\Office\14.0\Excel\Security" /v "VBAWarnings" /t REG_DWORD /d 2 /f
Cls
ECHO.
echo ***��ж�سɹ���***
 
goto exit
 
:exit
echo. 
echo. 
pause
exit 


