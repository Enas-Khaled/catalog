from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item

engine = create_engine('sqlite:///categoryitem.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and category a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# item for category1
category1 = Category(name="Frist Category")

session.add(category1)
session.commit()


Item1 = Item(name="sandwich loaves", description="sandwich loaves",
                     price="$2.99", section="Bakery", category=category1)

session.add(Item1)
session.commit()

Item2 = Item(name="cheeses", description="cheeses",
                     price="$5.50", section="Dairy", category=category1)

session.add(Item2)
session.commit()

Item3 = Item(name="fruits", description="fruits",
                     price="$3.99", section="Produce", category=category1)

session.add(Item3)
session.commit()

Item4 = Item(name="eggs", description="eggs",
                     price="$7.99", section="Dairy", category=category1)

session.add(Item4)
session.commit()

Item5 = Item(name="coffee", description="coffee",
                     price="$1.99", section="Beverages", category=category1)

session.add(Item5)
session.commit()

Item6 = Item(name="Iced Tea", description="with Lemon",
                     price="$.99", section="Beverages", category=category1)

session.add(Item6)
session.commit()

Item7 = Item(name="milk", description="milk",
                     price="$3.49", section="Dairy", category=category1)

session.add(Item7)
session.commit()

Item8 = Item(name="yogurt", description="yogurt",
                     price="$5.99", section="Dairy", category=category1)

session.add(Item8)
session.commit()


# item for category2
category2 = Category(name="category2")

session.add(category2)
session.commit()


Item1 = Item(name="butter", description="butter",
                     price="$7.99", section="Dairy", category=category2)

session.add(Item1)
session.commit()

Item2 = Item(
    name="butter", description="butter", price="$25", section="Dairy", category=category2)

session.add(Item2)
session.commit()

Item3 = Item(name="dinner rolls", description="dinner rolls",
                     price="", section="Bakery", category=category2)

session.add(Item3)
session.commit()

Item4 = Item(name="soda", description="soda",
                     price="", section="Beverages", category=category2)

session.add(Item4)
session.commit()

Item5 = Item(name="vegetables", description="vegetables",
                     price="", section="Produce", category=category2)

session.add(Item5)
session.commit()

Item6 = Item(
    name="tea", description="tea", price="", section="Beverages", category=category2)

session.add(Item6)
session.commit()


# item category3
category1 = Category(name="category3")

session.add(category1)
session.commit()


Item1 = Item(name="bagels", description="bagels",
                     price="", section="Bakery", category=category1)

session.add(Item1)
session.commit()

Item2 = Item(name="yogurt", description="yogurt",
                     price="", section="Dairy", category=category1)

session.add(Item2)
session.commit()

Item3 = Item(name="item3", description="item des",
                     price="", section="", category=category1)

session.add(Item3)
session.commit()

Item4 = Item(name="item4", description="item des",
                     price="", section="", category=category1)

session.add(Item4)
session.commit()


# item for category
category1 = Category(name="category4")

session.add(category1)
session.commit()


Item1 = Item(name="item1", description="item des",
                     price="", section="", category=category1)

session.add(Item1)
session.commit()

Item2 = Item(name="item2", description="item des",
                     price="", section="", category=category1)

session.add(Item2)
session.commit()

Item3 = Item(name="item3",
                     description="item des", price="", section="", category=category1)

session.add(Item3)
session.commit()

Item4 = Item(name="item4",
                     description="item des", price="", section="", category=category1)

session.add(Item4)
session.commit()

Item5 = Item(name="item5", description="item des",
                     price="", section="", category=category1)

session.add(Item5)
session.commit()


# item for category5
category1 = Category(name="category5")

session.add(category1)
session.commit()


Item1 = Item(name="item1", description="item des",
                     price="", section="", category=category1)

session.add(Item1)
session.commit()

Item2 = Item(name="item2", description="item des",
                     price="", section="", category=category1)

session.add(Item2)
session.commit()

Item3 = Item(name="item3", description="",
                     price="", section="", category=category1)

session.add(Item3)
session.commit()

Item4 = Item(name="item 4",
                     description="", price="", section="", category=category1)

session.add(Item4)
session.commit()

Item5 = Item(name="item5", description="item des",
                     price="", section="", category=category1)

session.add(Item5)
session.commit()


# item for item
category1 = Category(name="category6")

session.add(category1)
session.commit()


Item1 = Item(name="item1", description="item des",
                     price="", section="", category=category1)

session.add(Item1)
session.commit()

Item2 = Item(name="item2", description="item des",
                     price="", section="", category=category1)

session.add(Item2)
session.commit()

Item3 = Item(name="item3", description="item des",
                     price="", section="", category=category1)

session.add(Item3)
session.commit()

Item4 = Item(name="item4",
                     description="", price="", section="", category=category1)

session.add(Item4)
session.commit()


# item for category
category1 = Category(name="category6 ")

session.add(category1)
session.commit()

Item9 = Item(name="item9", description=" item des",
                     price="$8.99", section="Dairy", category=category1)

session.add(Item9)
session.commit()


Item1 = Item(name="item1", description="item des",
                     price="", section="", category=category1)

session.add(Item1)
session.commit()

Item2 = Item(name="item2", description="item des",
                     price="", section="", category=category1)

session.add(Item2)
session.commit()

Item3 = Item(name="item3",
                     description="item des", price="", section="", category=category1)

session.add(Item3)
session.commit()

Item4 = Item(name="item4", description="item 4",
                     price="", section="", category=category1)

session.add(Item4)
session.commit()


# item for category
category1 = Category(name="category8 ")

session.add(category1)
session.commit()


Item1 = Item(name="item 1",
                     description="item des", price="", section="", category=category1)

session.add(Item1)
session.commit()

Item2 = Item(name="item", description="item des ",
                     price="",section="", category=category1)

session.add(Item2)
session.commit()

print "added items!"
