def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    print(arguments)
    for arg in arguments:
        print(arg)
    print(keywords)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           kfff="ddd",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


def display_info(first, second, *extras, category, detail, **options):
    print("First argument:", first)
    print("Second argument:", second)
    print("Extra positional args:", extras)
    print("Keyword options:", options)

# Example usage
display_info(
    10,
    20,
    30, 40, 50,
    category="Books",
    detail="Fiction",
    author="Orwell",
    year=1949
)