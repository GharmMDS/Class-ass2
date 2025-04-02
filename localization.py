
MESSAGES = {
    'en': {
        'select_language': "Select your language / Valitse kieli / Välj ditt språk / 言語を選択してください:",
        'invalid_choice': "Invalid choice. Please try again.",
        'prompt_num_items': "Enter the number of items to purchase:",
        'prompt_price': "Enter the price for item {}:",
        'prompt_quantity': "Enter the quantity for item {}:",
        'invalid_input': "Invalid input. Please enter a valid number.",
        'item_total': "Cost for item {}: {:.2f}",
        'total_cost_label': "Total cost of all items: {:.2f}"
    },
    'fi': {
        'select_language': "Valitse kieli:",
        'invalid_choice': "Virheellinen valinta. Yritä uudelleen.",
        'prompt_num_items': "Syötä ostettavien tuotteiden määrä:",
        'prompt_price': "Syötä tuotteen {} hinta:",
        'prompt_quantity': "Syötä tuotteen {} määrä:",
        'invalid_input': "Virheellinen syöte. Anna kelvollinen numero.",
        'item_total': "Tuotteen {} hinta: {:.2f}",
        'total_cost_label': "Kaikkien tuotteiden kokonaishinta: {:.2f}"
    },
    'sv': {
        'select_language': "Välj ditt språk:",
        'invalid_choice': "Ogiltigt val. Försök igen.",
        'prompt_num_items': "Ange antalet varor att köpa:",
        'prompt_price': "Ange priset för varan {}:",
        'prompt_quantity': "Ange mängden för varan {}:",
        'invalid_input': "Ogiltig inmatning. Ange ett giltigt nummer.",
        'item_total': "Kostnad för vara {}: {:.2f}",
        'total_cost_label': "Total kostnad för alla varor: {:.2f}"
    },
    'ja': {
        'select_language': "言語を選択してください:",
        'invalid_choice': "無効な選択です。もう一度お試しください。",
        'prompt_num_items': "購入する商品の数を入力してください:",
        'prompt_price': "商品{}の価格を入力してください:",
        'prompt_quantity': "商品{}の数量を入力してください:",
        'invalid_input': "無効な入力です。有効な数値を入力してください。",
        'item_total': "商品{}の費用: {:.2f}",
        'total_cost_label': "すべての商品の合計金額: {:.2f}"
    }
}

DEFAULT_LANG = 'en'

_current_lang = DEFAULT_LANG

def set_language(lang_code):
    """Sets the current language for messages."""
    global _current_lang
    if lang_code in MESSAGES:
        _current_lang = lang_code
    else:
        _current_lang = DEFAULT_LANG
        print(f"Warning: Language '{lang_code}' not found. Defaulting to '{DEFAULT_LANG}'.")

def get_message(key, *args):
    """Gets a translated message string."""
    lang_messages = MESSAGES.get(_current_lang, MESSAGES[DEFAULT_LANG])
    message_template = lang_messages.get(key, f"Missing translation for key: {key}")
    try:
        return message_template.format(*args)
    except (IndexError, KeyError):
        return message_template