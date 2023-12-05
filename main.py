print('START import')
from application.salary import calculate_salary
from application.db.people import get_employees
from pytube import YouTube
from datetime import datetime

print('import DONE')


def main():
    calculate_salary()
    get_employees()
    link = input('Вставьте ссылку на видео: ')
    yt = YouTube(link)
    print(f'Скчиваем ролик - {yt.title}')
    ys = yt.streams.get_highest_resolution()
    ys.download()
    return f'Done in {datetime.now()}'


if __name__ == '__main__':
    print(main())