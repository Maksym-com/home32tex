import gspread
from oauth2client.service_account import ServiceAccountCredentials
import matplotlib.pyplot as plt
import pandas as pd

# Встановіть підключення до Google Sheets.

scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
client = gspread.authorize(creds)
 
# Відкрийте Google таблицю
sheet = client.open('GoITeens17').sheet1

# Отримайте дані з таблиці
data = sheet.get_all_values()


# Дані для першої діаграми
x1 = [row[0] for row in data[1:]]
y1 = [int(row[1]) for row in data[1:]]

# Дані для другої діаграми
x2 = [row[0] for row in data[1:]]
y2 = [int(row[2]) for row in data[1:]]

df = pd.DataFrame({'Хоббі і навчання (години)': 'Місяці',
                   'Навчання': [x1, y1],
                   'Хоббі': [x2, y2]})

# Створення об'єктів підграфіків та графіка
fig, (ax1, ax2) = plt.subplots(1, 2)

# Побудова першої діаграми
ax1.bar(x1, y1, color='violet')
ax1.set_title('Хоббі (години)')
ax1.set_xlabel('Місяці')
ax1.set_ylabel('Години')

# Побудова другої діаграми
ax2.bar(x2, y2, color='green')
ax2.set_title('Навчання (години)')
ax2.set_xlabel('Місяці')
ax2.set_ylabel('Години')

# Показати графік
plt.tight_layout()  # Для кращого розміщення підписів осей
plt.show()

