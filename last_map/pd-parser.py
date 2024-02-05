import pandas as pd

# Your data
data = """2024.01.03 21:48:33  37.7462   31.6310        5.0      -.-  2.4  -.-   GOLKASI-BEYSEHIR (KONYA)                          İlksel
2024.01.03 20:33:35  40.4418   28.8985        8.0      -.-  1.4  -.-   GEMLIK KORFEZI (MARMARA DENIZI)                   İlksel
2024.01.03 20:25:47  37.8265   36.4542        9.1      -.-  1.9  -.-   GEBEN-ANDIRIN (KAHRAMANMARAS)                     İlksel
2024.01.03 20:00:34  38.6838   37.9958        5.0      -.-  2.0  -.-   IPEKYOLU-HEKIMHAN (MALATYA)                       İlksel
2024.01.03 19:38:07  40.4108   28.8737       10.1      -.-  2.4  -.-   GEMLIK KORFEZI (MARMARA DENIZI)                   İlksel
2024.01.03 18:55:05  38.2988   37.1520        5.0      -.-  1.9  -.-   DOGAN-ELBISTAN (KAHRAMANMARAS)                    İlksel
2024.01.03 18:35:45  37.7362   37.0357        8.5      -.-  1.6  -.-   BAYDEMIRLI-(KAHRAMANMARAS)                        İlksel
2024.01.03 17:08:51  38.0932   36.6637        5.4      -.-  1.6  -.-   KARAOMER-GOKSUN (KAHRAMANMARAS)                   İlksel
2024.01.03 16:32:19  37.3907   36.8250        8.4      -.-  1.6  -.-   TURKOGLU (KAHRAMANMARAS)                          İlksel
2024.01.03 16:24:15  37.3080   42.3467        3.7      -.-  2.3  -.-   PINARONU-SILOPI (SIRNAK)                          İlksel"""

# Create a list of lines
lines = data.split('\n')

# Define column names
columns = ['Tarih', 'Saat', 'Enlem(N)', 'Boylam(E)', 'Derinlik(km)', 'MD',
           'ML', 'Mw', 'Yer', 'Çözüm Niteliği', 'Extra1', 'Extra2', 'Extra3']

# Create an empty DataFrame
df = pd.DataFrame(columns=columns)

# Iterate through each line and append to DataFrame
for line in lines:
    values = line.split()
    # Replace non-numeric characters in 'MD', 'ML', 'Mw' columns with NaN
    values[5:8] = [float(val.replace('-', 'NaN')) if val.replace('-', '').replace(
        '.', '').isdigit() else float('NaN') for val in values[5:8]]



    # FIXME: DataFrame object has no append
    df = df._append(pd.Series(values, index=columns), ignore_index=True)

# Print the resulting DataFrame
print(df)
