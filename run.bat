@echo off

echo Activating Conda environment...
call conda activate kakauto

echo Starting ftp.py...
start cmd /k python "ftp.py"
pause

echo Starting master.py...
start cmd /k python "master.py"
pause

:run_slave
echo Starting slave.py...
start cmd /k python "slave.py"
echo Press Enter to run slave.py again, or Ctrl+C to exit.
pause
goto run_slave