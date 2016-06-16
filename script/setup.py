from distutils.core import setup

setup(name='Rest area',
      version='1.0',
      py_modules=['email_data','email_UI','facility',
                  'food', 'Information_service_station',
                  'local','mainUI','traffic','UI_Fome'
                  ],
      data_files = [('bitmaps',['main.png','main_2.png'])]
      )
