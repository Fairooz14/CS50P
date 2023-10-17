import datetime
import ephem

# Function 1: Get the current date
def get_current_date():
    return datetime.date.today()

# Function 2: Calculate the lunar phase for a given date
def calculate_lunar_phase_for_date(date):
    moon = ephem.Moon(date)
    phase = int(moon.phase / 100 * 4)
    return phase

# Function 3: Display the lunar phase
def display_lunar_phase(phase):
    phases = ["New Moon", "First Quarter", "Full Moon", "Last Quarter"]
    return phases[phase]

# Function 4: Main function to run the Lunar Phase Tracker
def main():
    date = get_current_date()
    phase = calculate_lunar_phase_for_date(date)
    phase_name = display_lunar_phase(phase)
    print(f"On {date}, the Moon is in the {phase_name} phase.")

if __name__ == "__main__":
    main()
