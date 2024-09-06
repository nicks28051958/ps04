import wikipediaapi
import sys

# Инициализация Wikipedia API с правильным User-Agent
wiki_wiki = wikipediaapi.Wikipedia(language='ru',
                                   user_agent='MyWikipediaApp/1.0 (https://example.com/myapp; myemail@example.com)')


def print_intro():
    print("Добро пожаловать в Wikipedia-поиск!")
    print("Вы можете искать статьи, просматривать связанные страницы или выходить из программы.")


def search_wikipedia():
    query = input("Введите запрос для поиска на Википедии: ")
    page = wiki_wiki.page(query)

    if page.exists():
        print(f"Вы нашли статью: {page.title}\n")
        action_menu(page)
    else:
        print(f"Статья по запросу '{query}' не найдена.")
        search_wikipedia()


def action_menu(page):
    while True:
        print("\nВыберите действие:")
        print("1. Просмотреть параграфы статьи")
        print("2. Перейти на одну из связанных страниц")
        print("3. Выйти из программы")
        choice = input("Введите номер действия: ")

        if choice == "1":
            display_paragraphs(page)
        elif choice == "2":
            display_links(page)
        elif choice == "3":
            print("Выход из программы.")
            sys.exit()
        else:
            print("Неверный выбор, попробуйте снова.")


def display_paragraphs(page):
    print("\nСодержание статьи:")
    print(page.summary)  # Вывод краткого содержания статьи


def display_links(page):
    print("\nСвязанные страницы:")
    links = page.links
    if not links:
        print("Нет связанных страниц.")
        return

    for i, title in enumerate(links.keys(), 1):
        print(f"{i}. {title}")

    link_choice = input("Введите номер связанной страницы для перехода или '0' для возврата: ")
    if link_choice.isdigit():
        link_choice = int(link_choice)
        if 1 <= link_choice <= len(links):
            selected_link = list(links.keys())[link_choice - 1]
            new_page = wiki_wiki.page(selected_link)
            action_menu(new_page)
        elif link_choice == 0:
            return
        else:
            print("Неверный выбор, попробуйте снова.")
    else:
        print("Введите числовое значение.")


if __name__ == "__main__":
    print_intro()
    search_wikipedia()

