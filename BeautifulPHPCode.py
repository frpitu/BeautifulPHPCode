__description__ = 'Make your code beautiful'
__author__ = 'frpitu'
__version__ = '1.0'
__date__ = '09/08/2024'

import requests

class BeautifulPHPCode:
      
  def transform(text):
    print("> Formatting code.. ", end="")
    data = {
      'data': text, 'indentation_style': 'k&r',
      'indent_with': 'spaces', 'indentation_size': '4',
      'ArrayNested': 'ArrayNested', 'EqualsAlign': '',
      'Fluent': 'Fluent', 'KeepEmptyLines': 'KeepEmptyLines',
      'ListClassFunction': '', 'Lowercase': 'Lowercase',
    }
      
    try: 
      text = requests.post('https://beautifytools.com/pb.php', data=data).text
      print("done")
    except:
      print("> There was an error formatting... using original")
