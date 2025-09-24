#建立一個名為check_password_streth的函式，接受一個password字串
#規則1.檢查密碼長度是否大於等於8，如果是，分數+1
#規則2.檢查密碼是否包含至少一個數字，如果是，分數+1
#規則3.檢查密碼是否包含至少一個大寫字母，如果是，分數+1
#規則3.檢查密碼是否包含至少一個小寫字母，如果是，分數+1
#規則5.檢查密碼是否包含至少一個特殊字元，如果是，分數+1
#最後根據總分傳回強度等級，0-2分為"弱"，3-4分為"中"，5分為"強"
def check_password_strength(password):
    score = 0
    
    # 規則1: 檢查密碼長度是否大於等於8
    if len(password) >= 8:
        score += 1
    
    # 規則2: 檢查密碼是否包含至少一個數字
    if any(char.isdigit() for char in password):
        score += 1
    
    # 規則3: 檢查密碼是否包含至少一個大寫字母
    if any(char.isupper() for char in password):
        score += 1
    
    # 規則4: 檢查密碼是否包含至少一個小寫字母
    if any(char.islower() for char in password):
        score += 1
    
    # 規則5: 檢查密碼是否包含至少一個特殊字元
    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
    if any(char in special_characters for char in password):
        score += 1
    
    # 根據總分傳回強度等級
    if score <= 2:
        return "弱"
    elif score <= 4:
        return "中"
    else:
        return "強"
    
# 測試函式
print(check_password_strength("Password123"))          
