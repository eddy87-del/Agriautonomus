@echo off
REM Build script to compile the Inno Setup installer(s).
REM Requires Inno Setup's ISCC.exe to be on PATH. Run from repository root.

set ISS_DIR=installers
if exist "%ISS_DIR%\\agri_app_installer.iss" (
    echo Building App installer...
    ISCC "%ISS_DIR%\\agri_app_installer.iss"
) else (
    echo Missing %ISS_DIR%\\agri_app_installer.iss
)

if exist "%ISS_DIR%\\agri_docker_installer.iss" (
    echo Building Docker installer...
    ISCC "%ISS_DIR%\\agri_docker_installer.iss"
) else (
    echo Missing %ISS_DIR%\\agri_docker_installer.iss
)

echo Done.
pause
