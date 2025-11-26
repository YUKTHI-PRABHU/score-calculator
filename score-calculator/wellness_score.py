import pandas as pd

def calculate_wellness_score(row):
    # Normalize scales
    sleep_score = min((row['sleep_hours'] / 8) * 100, 100)
    steps_score = min((row['steps'] / 10000) * 100, 100)
    mood_score = (row['mood'] / 5) * 100
    
    # Weighted score
    wellness = (0.4 * sleep_score) + (0.35 * steps_score) + (0.25 * mood_score)
    return round(wellness, 2)

def main():
    df = pd.read_csv('wellness_data.csv')
    df['Wellness Score'] = df.apply(calculate_wellness_score, axis=1)
    print(df)
    df.to_csv('wellness_output.csv', index=False)
    print("\n✔️ Wellness scores saved to wellness_output.csv")

if __name__ == "__main__":
    main()
