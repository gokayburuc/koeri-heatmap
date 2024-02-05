import csv


def clean_data(csv_filename):
    data = []

    try:
        with open(csv_filename, "r") as rf:
            reader = csv.reader(rf)
            for row in reader:
                raw_data = [float(row[1]), float(row[2]), float(row[3])]
                data.append(raw_data)
                print(raw_data)
    except FileNotFoundError:
        print(f"File '{csv_filename}' not found.")
    except (ValueError, IndexError) as e:
        print(f"Error processing data: {e}")

    return data


# Example usage:
cleaned_data = clean_data("map_data.csv")
print(cleaned_data)
