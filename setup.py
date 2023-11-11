from distutils.core import setup

setup(name='dsss_homework_2',
      version='1.0',
      description='Math game and unit tests',
      author='Larua González Ruiz',
      url='https://github.com/Lauragonzalezruiz1/dsss_homework_2',
      packages=['math_quiz'],
      scripts=[
        'math_quiz/math_quiz.py',
        'math_quiz/tests_math_quiz.py'
    ]
     )
