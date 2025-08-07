import re
import os
from dotenv import load_dotenv
from collections import Counter
from statistics import mean, median, variance
import psycopg2
from bs4 import BeautifulSoup
import random

load_dotenv()


with open('bincom_colors.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

rows = soup.find_all('tr')[1:]
all_colors = []

for row in rows:
    colors_text = row.find_all('td')[1].text
    colors = [c.strip().upper() for c in colors_text.split(',')]
    all_colors.extend(colors)

color_corrections = {'BLEW': 'BLUE', 'ARSH': 'ASH'}
all_colors = [color_corrections.get(c, c) for c in all_colors]

color_counts = Counter(all_colors)
colors_sorted = sorted(color_counts.items(), key=lambda x: x[1], reverse=True)

# 1. Mean color
mean_color = colors_sorted[0][0]

# 2. Most worn color
most_worn_color = mean_color

# 3. Median color
sorted_colors = sorted(all_colors)
mid = len(sorted_colors) // 2
if len(sorted_colors) % 2 == 0:
    median_color = sorted_colors[mid - 1]
else:
    median_color = sorted_colors[mid]

# 4. Variance of color frequencies
freq_values = list(color_counts.values())
color_variance = variance(freq_values)

# 5. Probability of RED
prob_red = all_colors.count('RED') / len(all_colors)

# 6. Save to PostgreSQL
def save_to_postgres(color_counts):
    try:
        conn = psycopg2.connect(
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT')
        )
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS color_frequency (
                id SERIAL PRIMARY KEY,
                color VARCHAR(20),
                frequency INT
            );
        """)
        cursor.execute("DELETE FROM color_frequency")

        for color, freq in color_counts.items():
            cursor.execute("INSERT INTO color_frequency (color, frequency) VALUES (%s, %s);", (color, freq))

        conn.commit()
        cursor.close()
        conn.close()
        print("Saved to PostgreSQL successfully.")
    except Exception as e:
        print("PostgreSQL error:", e)

# 7. Recursive search
def recursive_search(lst, target, index=0):
    if index >= len(lst):
        return -1
    if lst[index] == target:
        return index
    return recursive_search(lst, target, index + 1)

# 8. Generate 4-digit binary and convert to decimal
def binary_to_decimal():
    binary = ''.join(random.choice(['0', '1']) for _ in range(4))
    decimal = int(binary, 2)
    print(f"Generated binary: {binary} -> Decimal: {decimal}")
    return binary, decimal

# 9. Sum first 50 Fibonacci numbers
def sum_fibonacci(n=50):
    fibs = [0, 1]
    while len(fibs) < n:
        fibs.append(fibs[-1] + fibs[-2])
    return sum(fibs[:n])

# TESTS
print("\n===== BINCOM COLOR ANALYSIS =====")
print("Mean color:", mean_color)
print("Most worn color:", most_worn_color)
print("Median color:", median_color)
print("Variance of color frequencies:", round(color_variance, 2))
print("Probability of picking RED:", round(prob_red, 3))

save_to_postgres(color_counts)

sample_list = [3, 7, 9, 12, 15, 21]
target = 12
result_index = recursive_search(sample_list, target)
print(f"\nRecursive search: {target} found at index {result_index}" if result_index != -1 else "Not found")

binary_to_decimal()

print("Sum of first 50 Fibonacci numbers:", sum_fibonacci())
