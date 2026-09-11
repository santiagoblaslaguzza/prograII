from .store import NYPizzaStore, ChicagoPizzaStore

def main():
    ny = NYPizzaStore(); chi = ChicagoPizzaStore()

    for kind in ["cheese", "veggie", "clam", "pepperoni"]:
        p = ny.order_pizza(kind)
        print("Ethan ordered:", p)
        print()

    for kind in ["cheese", "veggie", "clam", "pepperoni"]:
        p = chi.order_pizza(kind)
        print("Joel ordered:", p)
        print()

if __name__ == "__main__":
    main()
