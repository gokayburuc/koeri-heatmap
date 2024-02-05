import pandas as pd

# Your existing DataFrame
data = {'Tarih': ['2024.01.03', '2024.01.03'],
        'Saat': ['21:48:33', '20:33:35'],
        'Enlem(N)': [37.7462, 40.4418],
        'Boylam(E)': [31.6310, 28.8985],
        'Derinlik(km)': [5.0, 8.0],
        'MD': ['-.-', '-.-'],
        'ML': [2.4, 1.4],
        'Mw': ['-.-', '-.-'],
        'Yer': ['GOLKASI-BEYSEHIR (KONYA)', 'GEMLIK KORFEZI (MARMARA DENIZI)'],
        'Çözüm Niteliği': ['İlksel', 'İlksel']}

df = pd.DataFrame(data)

# New data to append
new_data = {'Tarih': ['2024.01.03', '2024.01.03'],
            'Saat': ['18:00:00', '19:30:00'],
            'Enlem(N)': [35.1234, 39.5678],
            'Boylam(E)': [32.9876, 27.5432],
            'Derinlik(km)': [10.0, 12.5],
            'MD': ['-.-', '-.-'],
            'ML': [3.0, 2.5],
            'Mw': ['-.-', '-.-'],
            'Yer': ['NEW LOCATION 1', 'NEW LOCATION 2'],
            'Çözüm Niteliği': ['İlksel', 'İlksel']}

# Convert new data to a DataFrame
new_df = pd.DataFrame(new_data)

df = df._append(new_df, ignore_index=True)

# Print the resulting DataFrame
print(df)

