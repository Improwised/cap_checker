# cap_checker
Capslock Notifier for Garuda Linux

This aims at creating capslock indicator for starlabs laptop.
- It is not working for gnome and terminal
- Service is failing, have to check that

Do not forgot to omit venv at the end, because, the program will be running at system level, so system should contain those packages with same versions.

## Steps

1. Clone the repository in home directory
```
git clone git@github.com:Improwised/cap_checker.git
cd cap_checker

2. Install python-tk
```
sudo pacman -S tk=tk-8.6.14-4
```

3. Create a python venv
```
python -m venv venv
```

4. Activate venv
```
source venv/bin/activate
```

5. Install requirements
```
pip install -r requirements.txt
```

6. Currently creating a service and it is in progress
