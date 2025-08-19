def main():
    name = input("Your name? ").strip()
    house = input("Your house? ").strip()

    patronus = get_patronus(name)

    print(f"Hello, {name} from {house}")
    print("Your patronus is", patronus)


def get_patronus(name):
    if name == "Harry":
        return "🐎"
    elif name == "Ron":
        return "🦁"
    elif name == "Hermione":
        return "🦈"
    else:
        return "🪄"

        
if __name__ == "__main__":
    main()