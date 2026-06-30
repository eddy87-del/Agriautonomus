; Inno Setup script to create a Windows installer that deploys Docker Compose stack for Agriautonomus
; This installer will place docker-compose.yml and helper scripts on the machine and attempt to start the stack after install.

[Setup]
AppName=Agriautonomus Docker Stack
AppVersion=0.1
DefaultDirName={autopf}\Agriautonomus\docker
DisableProgramGroupPage=yes
OutputBaseFilename=Agriautonomus_Docker_Installer
Compression=lzma2/ultra
SolidCompression=yes
ArchitecturesInstallIn64BitMode=x64

[Files]
; Copy the repository Docker Compose definitions and any needed assets into the install dir
Source: "..\\docker-compose.yml"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\\deployment\\*"; DestDir: "{app}\\deployment"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "docker_helper.ps1"; DestDir: "{app}\\tools"; Flags: ignoreversion

[Icons]
Name: "{group}\Agriautonomus Docker"; Filename: "{app}\\docker-compose.yml"

[Run]
; Run the Docker helper PowerShell script after installation to attempt to start the stack
Filename: "powershell.exe"; Parameters: "-ExecutionPolicy Bypass -NoProfile -File \"{app}\\tools\\docker_helper.ps1\""; Flags: runasoriginaluser shellexec skipifsilent

; The helper will check for Docker and guide the user to install Docker Desktop if missing.
