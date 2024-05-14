import sqlalchemy
import os

from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Book, Stock, Shop, Sale



login = os.getenv("login")

DSN = login
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

a_1 = Publisher(name="Джек Лондон")
a_2 = Publisher(name="Теодор Драйзер")
a_3 = Publisher(name="Андрей Константинов")

t_1 = Book(title="Мартин Иден", publisher= a_1)
t_2 = Book(title="Морской волк", publisher= a_1)
t_3 = Book(title="Финансист", publisher= a_2)
t_4 = Book(title="Титан", publisher= a_2)
t_5 = Book(title="Адвокат", publisher= a_3)
t_6 = Book(title="Судья", publisher= a_3)

sh_1 = Shop(name="Буквоед")
sh_2 = Shop(name="Лабиринт")

st_1 = Stock(book=t_1, shop=sh_1, count=100)
st_2 = Stock(book=t_2, shop=sh_1, count=150)
st_3 = Stock(book=t_3, shop=sh_1, count=100)
st_4 = Stock(book=t_4, shop=sh_1, count=150)
st_5 = Stock(book=t_5, shop=sh_2, count=200)
st_6 = Stock(book=t_6, shop=sh_2, count=200)

sa_1 = Sale(price=500, date_sale="09-05-2024", stock=st_1, count=1)
sa_2 = Sale(price=500, date_sale="10-05-2024", stock=st_2, count=2)
sa_3 = Sale(price=777, date_sale="24-04-2024", stock=st_3, count=3)
sa_4 = Sale(price=450, date_sale="08-05-2024", stock=st_4, count=1)
sa_5 = Sale(price=400, date_sale="09-09-2023", stock=st_5, count=2)
sa_6 = Sale(price=400, date_sale="29-09-2023", stock=st_6, count=1)

session.add_all([a_1, a_2, a_3, t_1, t_2, t_3, t_4, t_5, t_6, sh_1, sh_2, st_1, st_2, st_3, st_4, st_5, st_6,
                 sa_1, sa_2, sa_3, sa_4, sa_5, sa_6])
session.commit()

def get_shops(find):
    sub = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).select_from(Shop).\
        join(Stock).\
        join(Book).\
        join(Publisher).\
        join(Sale)
    if find.isdigit():
        all_query = sub.filter(Publisher.id == finds).all()
    else:
        all_query = sub.filter(Publisher.name == finds).all()
    for book, shop, price, sale in all_query:
        print(f"{book: <20} | {shop: <10} | {price: <6} | {sale}")

if __name__ == "__main__":
    finds = input("Введите, пожалуйста, имя или идентификатор автора: ")
    get_shops(finds)

session.close()








