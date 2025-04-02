import localization 

def get_numeric_input(prompt_key, *args):
    """Gets numeric input (float or int) from the user with validation."""
    while True:
        try:
            value_str = input(localization.get_message(prompt_key, *args) + " ")
            value = float(value_str) 
            if value < 0:
                print(localization.get_message('invalid_input') + " (Cannot be negative)")
                continue
            return int(value) if value.is_integer() else value
        except ValueError:
            print(localization.get_message('invalid_input'))
        except KeyboardInterrupt:
            print("\nExiting.")
            exit()

def calculate_total(items):
    """Calculates the total cost given a list of (price, quantity) tuples."""
    total_cost = 0.0
    for price, quantity in items:
        total_cost += price * quantity
    return total_cost

def select_language():
    """Prompts the user to select a language."""
    print("1: English")
    print("2: Suomi (Finnish)")
    print("3: Svenska (Swedish)")
    print("4: 日本語 (Japanese)")

    prompt = localization.MESSAGES['en']['select_language']

    while True:
        try:
            choice = input(prompt + " ")
            choice_int = int(choice)
            if choice_int == 1:
                return 'en'
            elif choice_int == 2:
                return 'fi'
            elif choice_int == 3:
                return 'sv'
            elif choice_int == 4:
                return 'ja'
            else:
                print(localization.MESSAGES['en']['invalid_choice'])
        except ValueError:
            print(localization.MESSAGES['en']['invalid_choice'])
        except KeyboardInterrupt:
            print("\nExiting.")
            exit()


def main():
    """Main function to run the shopping cart application."""
    selected_lang = select_language()
    localization.set_language(selected_lang)

    num_items = 0
    while num_items <= 0:
         num_items_input = get_numeric_input('prompt_num_items')
         if isinstance(num_items_input, int) and num_items_input > 0:
             num_items = num_items_input
         else:
             print(localization.get_message('invalid_input') + " (Must be a positive whole number)")


    items_data = []
    print("-" * 20)

    for i in range(1, num_items + 1):
        price = -1.0
        while price < 0:
            price = get_numeric_input('prompt_price', i)
            if price < 0:
                 print(localization.get_message('invalid_input') + " (Price cannot be negative)")


        quantity = 0
        while quantity <= 0:
             quantity_input = get_numeric_input('prompt_quantity', i)
             if isinstance(quantity_input, int) and quantity_input > 0:
                 quantity = quantity_input
             else:
                 print(localization.get_message('invalid_input') + " (Quantity must be a positive whole number)")

        items_data.append((price, quantity))
        item_total = price * quantity
        print(localization.get_message('item_total', i, item_total))
        print("-" * 10)

    total_cart_cost = calculate_total(items_data)
    print("-" * 20)
    print(localization.get_message('total_cost_label', total_cart_cost))
    print("-" * 20) 


if __name__ == "__main__":
    main()