python3 get-pip.py
python3 -m pip install req.txt
schtasks.exe /create /tn Send-Auto-File /sc monthly  /st 00:00 /tr make
