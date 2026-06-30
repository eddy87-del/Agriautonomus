# Installer files and build instructions for Agriautonomus

This directory contains two Inno Setup scripts and helper scripts to build Windows installer EXEs for the project.

Included files
- agri_app_installer.iss  — Inno Setup script that packages the PyInstaller EXE and supporting files into a traditional Windows installer.
- agri_docker_installer.iss — Inno Setup script that installs docker-compose.yml and a helper script that attempts to start the Docker stack.
- build_pyinstaller.bat — Batch script that creates a venv and builds main.py into a single EXE using PyInstaller (placed into dist\ by PyInstaller).
- build_inno.bat — Batch script that runs ISCC.exe on the .iss files to produce installer EXEs.
- docker_helper.ps1 — PowerShell helper that checks for Docker and runs docker compose to bring up the stack.

Prerequisites (for building installers)
- Windows machine to build installers (recommended)
- Python 3.8+ on PATH
- PyInstaller (build script will install it into venv)
- Inno Setup (to compile .iss files). Ensure ISCC.exe is on PATH.

Workflow (build App installer)
1. From repository root, run: installers\\build_pyinstaller.bat
   - This creates venv, installs requirements, and produces dist\\Agriautonomus.exe
2. After successful PyInstaller build, run: installers\\build_inno.bat
   - This runs ISCC to create the installer EXE(s).

Workflow (build Docker installer)
1. The Docker installer does not need PyInstaller output; it packages docker-compose.yml and deployment assets.
2. Run: installers\\build_inno.bat
3. Run the produced installer on the target machine. After installation, it will attempt to run PowerShell to check for Docker and bring up the stack.

Notes and recommendations
- The app installer expects the PyInstaller exe to exist at ../dist/Agriautonomus.exe relative to this installers directory. You can change the .iss if you prefer a different source path.
- To register the app to run as a Windows service you can either include nssm in the installer payload and call it postinstall, or use the built-in sc.exe to create a service if your exe supports running as a service. This is intentionally left out because service registration can be environment-specific.
- The Docker installer simply runs "docker compose up -d". If your compose file requires environment files or image builds, ensure the deployment/ directory includes them or adjust the docker_helper.ps1 accordingly.
- For offline installers, bundle all required binaries (PyInstaller exe, ai_models, frontend build, nssm.exe if needed) into the installers payload and update the .iss Files section to point to them.

If you'd like, I can:
- Add an NSSM-based service registration step and include NSSM in the installer payload (requires adding the binary).
- Modify the scripts to register the app as a service automatically.
- Create GitHub Actions workflow to build the PyInstaller exe and compile the Inno Setup installers on a Windows CI runner.

Which of those would you like me to add next?