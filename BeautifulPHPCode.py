__description__ = 'Make your code beautiful'
__author__ = 'frpitu'
__version__ = '1.0'
__date__ = '09/08/2024'

"""

      __            _ 
    / _|_ __ _ __ (_) |_ _   
   | |_| '__| '_ \| | __| | | |
   |  _| |  | |_) | | |_| |_| |
   |_| |_|  | .__/|_|\__|\__,_|
            |_|
 * Copyrigth frpitu 2024 todos os direitos reservados
 * O projeto tem a lincensa GPL 2.0, caso você queira usar qualquer código está disponivel

"""

import requests

class BeautifulPHPCode:
  def transform(text):
    print("> Formatting code.. ", end="")
    data = {
      'data': self.source, 'indentation_style': 'k&r',
      'indent_with': 'spaces', 'indentation_size': '4',
      'ArrayNested': 'ArrayNested', 'EqualsAlign': '',
      'Fluent': 'Fluent', 'KeepEmptyLines': 'KeepEmptyLines',
      'ListClassFunction': '', 'Lowercase': 'Lowercase',
    }
      
    try: 
      self.source = requests.post('https://beautifytools.com/pb.php', data=data).text
      print("done")
    except:
      print("\n[+] there was an error formatting... using original")
