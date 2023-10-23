# APC-MINI-MK2-control-WLED

Control WLED with your APC MINI MK2 MIDI Controller

For it to work install the following libraries:
```python
   pip install python-rtmidi
```
```python
   pip install mido
```
```python
   pip install selenium
```    
1. Define the function of each button in buttons_functions.py (See coments)
2. Keep webdriver in C:/root or change line 7 in buttons_functions.py
3. Insert your controller board IP
4. Play

Optionally you can compile the tool to have an executable:
```python
   pyinstaller --console --onefile  main.py
```    
Inside the build folder
