@echo off
rem Set the PYTHONWARNINGS environment variable to ignore UserWarnings
set PYTHONWARNINGS=ignore::UserWarning:pkg_resources

call tts_stt_thesis\Scripts\activate.bat

IF %ERRORLEVEL% NEQ 0 (
    echo Failed to activate virtual environment. Exiting.
    pause
    exit /b %ERRORLEVEL%
)

rem Run your Python script
python main.py

rem You will likely want to remove 'pause' here if running truly silently
rem If your Python script has a GUI or writes to a log file, 'pause' is not needed.
rem pause