; Inno Setup script to create a Windows installer for the Agriautonomus application
; Place this file in the installers/ directory and build with ISCC.exe
[Setup]
AppName=Agriautonomus
AppVersion=0.1
DefaultDirName={autopf}\Agriautonomus
DisableProgramGroupPage=yes
OutputBaseFilename=Agriautonomus_App_Installer
Compression=lzma2/ultra
SolidCompression=yes
ArchitecturesInstallIn64BitMode=x64

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
; Expect PyInstaller output to be in ../dist relative to this installers/ directory
Source: "..\\dist\\Agriautonomus.exe"; DestDir: "{app}"; Flags: ignoreversion
; Include schema and data
Source: "..\\schema.sql"; DestDir: "{app}\\data"; Flags: ignoreversion
; Include ai models directory if present
Source: "..\\ai_models\\*"; DestDir: "{app}\\ai_models"; Flags: ignoreversion recursesubdirs createallsubdirs
; Include optional frontend build if available
Source: "..\\frontend\\build\\*"; DestDir: "{app}\\frontend"; Flags: ignoreversion recursesubdirs createallsubdirs
; Include config and requirements files
Source: "..\\requirements*.txt"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Agriautonomus"; Filename: "{app}\\Agriautonomus.exe"
Name: "{commondesktop}\Agriautonomus"; Filename: "{app}\\Agriautonomus.exe"; Tasks: desktopicon

[Tasks]
Name: desktopicon; Description: "Create a &desktop icon"; GroupDescription: "Additional icons:"; Flags: unchecked

[Run]
; Offer to launch the application after install
Filename: "{app}\\Agriautonomus.exe"; Description: "Launch Agriautonomus"; Flags: nowait postinstall skipifsilent

; Note: To register the app as a Windows service automatically, include a helper (nssm) or rely on an included PowerShell script. See installers/README_INSTALLERS.md for options.
