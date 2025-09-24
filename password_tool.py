import random
import string
import sys

def check_password_strength(password):
    """
    檢查密碼強度，根據五項規則給分，回傳"弱"、"中"或"強"。
    規則：
      1. 長度>=8
      2. 含數字
      3. 含大寫字母
      4. 含小寫字母
      5. 含特殊字元
    """
    score = 0
    if len(password) >= 8:
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.islower() for char in password):
        score += 1
    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
    if any(char in special_characters for char in password):
        score += 1
    if score <= 2:
        return "弱"
    elif score <= 4:
        return "中"
    else:
        return "強"

def generate_strong_password(length=12):
    """
    產生一組強密碼，預設長度12，必含大寫、小寫、數字、特殊字元。
    """
    if length < 8:
        raise ValueError("密碼長度至少需8位")
    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
    all_chars = string.ascii_letters + string.digits + special_characters
    # 確保每種型態至少一個
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(special_characters)
    ]
    # 剩餘長度隨機填充
    password += [random.choice(all_chars) for _ in range(length - 4)]
    random.shuffle(password)
    return ''.join(password)

if __name__ == '__main__':
    """
    從命令列取得密碼參數，若有則檢查強度，否則產生並印出一組強密碼。
    """
    if len(sys.argv) > 1:
        pwd = sys.argv[1]
        print(f'密碼: {pwd}')
        print(f'強度: {check_password_strength(pwd)}')
    else:
        new_pwd = generate_strong_password()
        print(f'產生的強密碼: {new_pwd}')
