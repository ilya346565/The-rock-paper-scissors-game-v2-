import random
import os
import re


def check_play_status():
  valid_responses = ['Да', 'Нет']
  while True:
      try:
          response = input('Вы хотите сыграть еще раз? (Да или нет): ')
          if response.lower() not in valid_responses:
              raise ValueError('Только "да" или "Нет"')

          if response.lower() == 'Да':
              return True
          else:
              os.system('cls' if os.name == 'nt' else 'clear')
              print('Спасибо за игру!')
              exit()

      except ValueError as err:
          print(err)


def play_rps():
   play = True
   while play:
       os.system('cls' if os.name == 'nt' else 'clear')
       print('')
       print('Камень, ножницы, бумага - Короче говоря!')

       user_choice = input('Выбери свое оружие'
                           ' [R]Камень, [P]Бумага, или [S]Ножницы: ')

       if not re.match("[SsRrPp]", user_choice):
           print('Пожалуйста, выберите букву:')
           print('[R]Камень, [P]Бумага, или [S]Ножницы')
           continue

       print(f'Ты выбрал: {user_choice}')

       choices = ['R', 'P', 'S']
       opp_choice = random.choice(choices)

       print(f'I chose: {opp_choice}')

       if opp_choice == user_choice.upper():
           print('Завязывай!')
           play = check_play_status()
       elif opp_choice == 'R' and user_choice.upper() == 'S':
           print('Камень бьет ножницы, я выигрываю!')
           play = check_play_status()
       elif opp_choice == 'S' and user_choice.upper() == 'P':
           print('Ножницы бьют бумагу! Я победил!')
           play = check_play_status()
       elif opp_choice == 'P' and user_choice.upper() == 'R':
           print('Бумага бьет камень, я выигрываю!')
           play = check_play_status()
       else:
           print('Ты победилY!\n')
           play = check_play_status()


if __name__ == '__main__':
   play_rps()