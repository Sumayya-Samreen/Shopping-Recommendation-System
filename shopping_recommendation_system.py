import pyttsx3
import random as r
import smtplib
import webbrowser

# --- DATA STRUCTURES ---
TV_list = []
mob_list = []
tele_dict = {}
mob_dict = {}
tv_adict = {}
tv_fdict = {}
mob_adict = {}
mob_fdict = {}

# --- CONFIGURATION ---
EMAIL_ADDRESS = "your_email@gmail.com"  # Replace with your Gmail
EMAIL_APP_PASSWORD = "your_app_password"  # Gmail App Password

# --- HELPER FUNCTIONS FOR OTP ---
def send_otp(email, otp):
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.ehlo()
        s.login(EMAIL_ADDRESS, EMAIL_APP_PASSWORD)
        s.sendmail(
            EMAIL_ADDRESS,
            email,
            f"Subject: OTP Verification\n\nYour OTP is: {otp}"
        )
        s.quit()
        return True
    except Exception:
        return False

def get_valid_email():
    while True:
        email = input("ENTER YOUR EMAIL TO CONTINUE SHOPPING: ")
        otp = ''.join([str(r.randint(1, 9)) for _ in range(4)])
        if send_otp(email, otp):
            print("OTP SENT SUCCESSFULLY!")
            return email, otp
        else:
            print("INVALID EMAIL OR SENDING FAILED! PLEASE ENTER A VALID EMAIL AGAIN.")

def validate_otp(actual_otp):
    while True:
        myotp = input("ENTER OTP RECEIVED VIA EMAIL: ")
        if myotp == actual_otp:
            print("OTP VALIDATION SUCCESSFUL!")
            return True
        else:
            print("INVALID OTP!")
            print("OPTIONS: 1. TRY AGAIN  2. RESEND OTP")
            choice = input("ENTER CHOICE: ")
            if choice == '1':
                continue
            elif choice == '2':
                return False
            else:
                print("INVALID CHOICE, TRY AGAIN.")

# --- HELPER FUNCTION FOR URL VALIDATION ---
def get_valid_url(prompt):
    while True:
        url = input(prompt)
        if url.startswith("http://") or url.startswith("https://"):
            return url
        else:
            print("INVALID URL! MUST START WITH http:// OR https://. TRY AGAIN.")

# --- ADMIN FUNCTION ---
def admin():
    while True:
        print("\nADMIN MENU")
        print("1. Add Items")
        print("2. Delete Items")
        print("0. Return to Main Menu")
        ch = input("ENTER CHOICE: ")
        if ch == '1':
            print("\nWHAT DO YOU WANT TO ADD? 1. TV  2. MOB")
            inner_ch = input("ENTER CHOICE: ")
            if inner_ch == '1':
                tv = input("ENTER TV NAME: ").upper()
                TV_list.append(tv)
                tvspec = input("ENTER TV SPEC: ").upper()
                tele_dict[tv] = tvspec
                aurl = get_valid_url("ENTER URL OF AMAZON PAGE: ")
                furl = get_valid_url("ENTER URL OF FLIPKART PAGE: ")
                tv_adict[tv] = aurl
                tv_fdict[tv] = furl
                print(f"\nTV {tv} ADDED SUCCESSFULLY!")
            elif inner_ch == '2':
                mob = input("ENTER MOBILE NAME: ").upper()
                mob_list.append(mob)
                mobspec = input("ENTER MOBILE SPEC: ").upper()
                mob_dict[mob] = mobspec
                aurl = get_valid_url("ENTER URL OF AMAZON PAGE: ")
                furl = get_valid_url("ENTER URL OF FLIPKART PAGE: ")
                mob_adict[mob] = aurl
                mob_fdict[mob] = furl
                print(f"\nMOBILE {mob} ADDED SUCCESSFULLY!")
            else:
                print("INVALID CHOICE!")
        elif ch == '2':
            print("\nWHAT DO YOU WANT TO DELETE? 1. TV  2. MOB")
            inner_ch = input("ENTER CHOICE: ")
            if inner_ch == '1':
                if not TV_list:
                    print("NO TV AVAILABLE TO DELETE.")
                    continue
                print("\nCURRENT TV LIST:")
                for idx, tv in enumerate(TV_list, 1):
                    print(f"{idx}. {tv}")
                choice_idx = input("ENTER THE NUMBER OF TV TO DELETE: ")
                if choice_idx.isdigit() and 1 <= int(choice_idx) <= len(TV_list):
                    tv_to_delete = TV_list[int(choice_idx)-1]
                    TV_list.remove(tv_to_delete)
                    del tele_dict[tv_to_delete]
                    del tv_adict[tv_to_delete]
                    del tv_fdict[tv_to_delete]
                    print(f"TV {tv_to_delete} DELETED SUCCESSFULLY!")
                else:
                    print("INVALID SELECTION.")
            elif inner_ch == '2':
                if not mob_list:
                    print("NO MOBILE AVAILABLE TO DELETE.")
                    continue
                print("\nCURRENT MOBILE LIST:")
                for idx, mob in enumerate(mob_list, 1):
                    print(f"{idx}. {mob}")
                choice_idx = input("ENTER THE NUMBER OF MOBILE TO DELETE: ")
                if choice_idx.isdigit() and 1 <= int(choice_idx) <= len(mob_list):
                    mob_to_delete = mob_list[int(choice_idx)-1]
                    mob_list.remove(mob_to_delete)
                    del mob_dict[mob_to_delete]
                    del mob_adict[mob_to_delete]
                    del mob_fdict[mob_to_delete]
                    print(f"MOBILE {mob_to_delete} DELETED SUCCESSFULLY!")
                else:
                    print("INVALID SELECTION.")
            else:
                print("INVALID CHOICE!")
        elif ch == '0':
            break
        else:
            print("INVALID CHOICE! TRY AGAIN.")

# --- CUSTOMER FUNCTION ---
def customer():
    name = input("\nWELCOME, PLEASE ENTER YOUR NAME: ").upper()
    print(f"HELLO {name}! WELCOME TO OUR PRODUCT RECOMMENDATION SERVICES!!")

    # Text-to-Speech
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 130)
    engine.setProperty('voice', voices[1].id)
    def speak(audio):
        engine.say(audio)
        engine.runAndWait()
    speak(f"HELLO {name}! WELCOME TO OUR PRODUCT RECOMMENDATION SERVICES!!")

    while True:
        print("\nWHAT ARE YOU LOOKING FOR?")
        print("1. Television")
        print("2. Mobile")
        print("0. BACK TO MAIN MENU")
        ch = input("ENTER CHOICE: ")

        if ch == '1' and TV_list:
            while True:
                print("\nLIST OF AVAILABLE TVS:")
                for idx, tv in enumerate(TV_list, 1):
                    print(f"{idx}. {tv}")
                choice_idx = input("ENTER THE NUMBER OF TV YOU WANT TO BUY: ")
                if choice_idx.isdigit() and 1 <= int(choice_idx) <= len(TV_list):
                    mytv = TV_list[int(choice_idx)-1]
                    break
                print("INVALID SELECTION. TRY AGAIN.")

            print("\nSPECIFICATIONS:")
            print(tele_dict[mytv])

            # EMAIL + OTP FLOW
            email, otp = get_valid_email()
            while not validate_otp(otp):
                otp = ''.join([str(r.randint(1, 9)) for _ in range(4)])
                if send_otp(email, otp):
                    print("NEW OTP SENT SUCCESSFULLY!")
                else:
                    print("INVALID EMAIL OR SENDING FAILED! PLEASE ENTER A VALID EMAIL AGAIN.")
                    email, otp = get_valid_email()

            speak("OTP VALIDATION SUCCESSFUL!")
            while True:
                print("WOULD YOU LIKE TO CONTINUE SHOPPING WITH: 1. AMAZON  2. FLIPKART")
                ch2 = input("ENTER CHOICE: ")
                if ch2 == '1':
                    webbrowser.open(tv_adict[mytv])
                    break
                elif ch2 == '2':
                    webbrowser.open(tv_fdict[mytv])
                    break
                else:
                    print("INVALID CHOICE! ENTER 1 OR 2.")

        elif ch == '2' and mob_list:
            while True:
                print("\nLIST OF AVAILABLE MOBILES:")
                for idx, mob in enumerate(mob_list, 1):
                    print(f"{idx}. {mob}")
                choice_idx = input("ENTER THE NUMBER OF MOBILE YOU WANT TO BUY: ")
                if choice_idx.isdigit() and 1 <= int(choice_idx) <= len(mob_list):
                    mymob = mob_list[int(choice_idx)-1]
                    break
                print("INVALID SELECTION. TRY AGAIN.")

            print("\nSPECIFICATIONS:")
            print(mob_dict[mymob])

            # EMAIL + OTP FLOW
            email, otp = get_valid_email()
            while not validate_otp(otp):
                otp = ''.join([str(r.randint(1, 9)) for _ in range(4)])
                if send_otp(email, otp):
                    print("NEW OTP SENT SUCCESSFULLY!")
                else:
                    print("INVALID EMAIL OR SENDING FAILED! PLEASE ENTER A VALID EMAIL AGAIN.")
                    email, otp = get_valid_email()

            speak("OTP VALIDATION SUCCESSFUL!")
            while True:
                print("WOULD YOU LIKE TO CONTINUE SHOPPING WITH: 1. AMAZON  2. FLIPKART")
                ch2 = input("ENTER CHOICE: ")
                if ch2 == '1':
                    webbrowser.open(mob_adict[mymob])
                    break
                elif ch2 == '2':
                    webbrowser.open(mob_fdict[mymob])
                    break
                else:
                    print("INVALID CHOICE! ENTER 1 OR 2.")

        elif ch == '0':
            break
        else:
            print("INVALID CHOICE OR NO PRODUCTS AVAILABLE. TRY AGAIN.")

# --- MAIN LOOP ---
while True:
    print("\nMAIN MENU:")
    print("1. CUSTOMER")
    print("2. ADMINISTRATOR")
    print("0. EXIT")
    choice = input("ENTER CHOICE: ")
    if choice == '1':
        customer()
    elif choice == '2':
        admin()
    elif choice == '0':
        print("THANK YOU FOR USING OUR SERVICE!")
        break
    else:
        print("INVALID CHOICE! TRY AGAIN.")
