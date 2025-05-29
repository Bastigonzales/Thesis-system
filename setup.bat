@echo off
REM This batch file runs your Python setup script.

REM --- Configuration ---
REM Set the name of your Python setup script
SET PYTHON_SETUP_SCRIPT=setup_env.py

REM --- Script Start ---
echo.
echo Attempting to run the Python setup script: %PYTHON_SETUP_SCRIPT%
echo.

REM Check if the Python script exists
IF NOT EXIST "%PYTHON_SETUP_SCRIPT%" (
    echo Error: The Python script '%PYTHON_SETUP_SCRIPT%' was not found in the current directory.
    echo Please ensure '%PYTHON_SETUP_SCRIPT%' is in the same directory as this batch script, or provide the full path.
    pause
    EXIT /B 1
)

REM Run the Python script
REM Make sure 'python' is in your system's PATH, or provide the full path to your Python executable.
python "%PYTHON_SETUP_SCRIPT%"

REM Check the exit status of the Python script
IF %ERRORLEVEL% NEQ 0 (
    echo.
    echo The Python setup script '%PYTHON_SETUP_SCRIPT%' encountered an error.
    pause
    EXIT /B %ERRORLEVEL%
) ELSE (
    echo.
    echo The Python setup script '%PYTHON_SETUP_SCRIPT%' completed successfully.
)

echo.
echo Batch script finished.
echo.
pause