#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 3ngthrust
"""
import keyboard
import time

# References: https://en.wikipedia.org/wiki/Greek_alphabet (click on letters for unicode code)
#             https://www.sharelatex.com/learn/List_of_Greek_letters_and_math_symbols
#             https://github.com/boppreh/keyboard

unicode = True

unicode_dict = {'alpha': '03b1',
                'beta': '03b2',
                'gamma': '03b3',
                'delta': '03b4',
                'epsilon': '03b5',
                'theta': '03b8',
                'lambda': '03bb',
                'pi': '03c0',
                'rho': '03c1',
                'sigma': '03c3',
                'phi': '03c6',
                'psi': '03c8',
                'omega': '03c9',
                'Delta': '0394',
                'Phi': '03a6',
                'Omega': '03a9'
                }
                
tex_dict = {'alpha': r'\alpha',
            'beta': r'\beta',
            'gamma': r'\gamma',
            'delta': r'\delta',
            'epsilon': r'\varepsilon',
            'theta': r'\theta',
            'lambda': r'\lambda',
            'pi': r"\pi",
            'rho': r'\rho',
            'sigma': r'\sigma',
            'phi': r'\phi',
            'psi': r'\psi',
            'omega': r'\omega',
            'Delta': r'\Delta',
            'Phi': r'\Phi',
            'Omega': r'\Omega'
            }
     

def write_greek(char):
    if unicode:
        keyboard.send('backspace')
        keyboard.send('ctrl + shift + u') # Unicode input sequence for Linux (https://en.wikipedia.org/wiki/Unicode_input)
        keyboard.write(unicode_dict[char])
        keyboard.send('enter')
        
    else:
        keyboard.send('backspace')
        
        # Sending "\" with unicode it is buggy with keyboard.write and the more basic keyboard.send
        keyboard.send('ctrl + shift + u')
        time.sleep(0.1)
        keyboard.write('005c') # "\"
        keyboard.send('enter')
        
        
        for s in tex_dict[char][1:]: # String without the heading "\"
        
            # h i and j are buggy and therefore written with unicode
            if s == "h":
                keyboard.send('ctrl + shift + u')
                keyboard.write('0068') # "h"
                keyboard.send('enter')
                
            elif s == "i":
                keyboard.send('ctrl + shift + u')
                keyboard.write('0069') # "i"
                keyboard.send('enter')
                
            elif s == "j":
                keyboard.send('ctrl + shift + u')
                keyboard.write('006a') # "j"
                keyboard.send('enter')
                
            else:
                keyboard.write(s) # To write uppercase letters keyboard.write instead of keyboard.send has to be used
      
        
def switch_flag():
    keyboard.send('backspace') # Remove the written "l"
    
    global unicode
    unicode = not unicode

 
# Press "AltGr", "Shift" and 'l' one after another to change to Latex input.
keyboard.add_hotkey('alt gr, shift, l', switch_flag, trigger_on_release=True)

# Press 'AltGr' and afterwards the rspective key for small greek letters
keyboard.add_hotkey('alt gr, a', write_greek, args=['alpha'], trigger_on_release=True)
keyboard.add_hotkey('alt gr, b', write_greek, args=['beta'], trigger_on_release=True)
keyboard.add_hotkey('alt gr, g', write_greek, args=['gamma'], trigger_on_release=True)
keyboard.add_hotkey('alt gr, d', write_greek, args=['delta'], trigger_on_release=True)
keyboard.add_hotkey('alt gr, e', write_greek, args=['epsilon'], trigger_on_release=True)
keyboard.add_hotkey('alt gr, t', write_greek, args=['theta'], trigger_on_release=True)
keyboard.add_hotkey('alt gr, l', write_greek, args=['lambda'], trigger_on_release=True)
keyboard.add_hotkey('alt gr, p', write_greek, args=['pi'], trigger_on_release=True)
keyboard.add_hotkey('alt gr, r', write_greek, args=['roh'], trigger_on_release=True)
keyboard.add_hotkey('alt gr, s', write_greek, args=['sigma'], trigger_on_release=True)
keyboard.add_hotkey('alt gr, f', write_greek, args=['phi'], trigger_on_release=True)
keyboard.add_hotkey('alt gr, s', write_greek, args=['psi'], trigger_on_release=True)
keyboard.add_hotkey('alt gr, o', write_greek, args=['omega'], trigger_on_release=True)

# Press 'AltGr' and afterwards the rspective key in combination with "shift" for captial greek letters
keyboard.add_hotkey('alt gr, shift + d', write_greek, args=['Delta'], trigger_on_release=True)
keyboard.add_hotkey('alt gr, shift + f', write_greek, args=['Phi'], trigger_on_release=True)
keyboard.add_hotkey('alt gr, shift + o', write_greek, args=['Omega'], trigger_on_release=True)

keyboard.wait() # Runs forever until canceled with "Ctrl + C"
