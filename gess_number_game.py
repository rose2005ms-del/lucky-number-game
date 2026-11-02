import random


def get_guess():
    while True:
        try:
            guess = int(input("حدس تو: "))

            if 1 <= guess <= 100:
                return guess
            else:
                print("عدد باید بین 1 تا 100 باشد!")

        except ValueError:
            print("لطفاً فقط عدد وارد کن!")


def give_hint(guess, secret_number):
    difference = abs(guess - secret_number)

    if guess < secret_number:
        direction = "عدد مخفی بزرگ تر است."
    else:
        direction = "عدد مخفی کوچک تر است."

    if difference <= 5:
        message = "خیلی نزدیک شدی!"
    elif difference <= 15:
        message = "فاصله زیادی نداری!"
    else:
        message = "هنوز خیلی فاصله داری!"

    print(direction)
    print(message)


def show_rank(attempts):
    ranks = {
        1: "نمونه ای!",
        2: "بسیار خوب!",
        3: "خوب!",
        4: "قبول!",
        5: "با شانس بردی!"
    }

    print("رتبه نهایی:", ranks[attempts])


def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 5

    print("\n" + "=" * 35)
    print("       مرحله جدید Lucky Number")
    print("=" * 35)
    print("یک عدد بین 1 تا 100 انتخاب شده است.")
    print("برای پیدا کردن آن 5 فرصت داری.")

    while attempts < max_attempts:

        print("\nتلاش", attempts + 1, "از", max_attempts)
        print("فرصت باقی مانده:", max_attempts - attempts)

        guess = get_guess()

        attempts += 1

        if guess == secret_number:
            print("\nآفرین! عدد مخفی را پیدا کردی.")
            print("تعداد تلاش های تو:", attempts)
            show_rank(attempts)
            return

        give_hint(guess, secret_number)

    print("\nفرصت هایت تمام شد!")
    print("عدد مخفی این بود:", secret_number)
    print("این بار شانس با تو یار نبود!")


def main():
    print("=" * 35)
    print("          LUCKY NUMBER")
    print("       بازی حدس اعداد")
    print("=" * 35)

    while True:
        play_game()

        answer = input(
            "\nآیا برای یک بازی جدید آماده ای؟ (بله/خیر): "
        ).strip().lower()

        if answer not in ["بله", "yes", "y"]:
            print("\nممنون که Lucky Number را بازی کردی!")
            print("تا بازی بعدی، خداحافظ!")
            break


main()