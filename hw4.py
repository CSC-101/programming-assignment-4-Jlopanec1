import build_data
import sys
# Function to load the demographics data from a local text file


full_data = build_data.get_data()

def display(operation):
    try:
        with open("filename") as operation:
            for county in full_data:
                print(f"County: {county.county}")
                print(f"  - Education (Bachelor's Degree or Higher): {county.education}%")
                print(f"  - Education (High School or Higher): {county.education}%")
            # Display Ethnicities
                print("  - Ethnicities:")
            for ethnicity, percentage in county.ethnicities.items():
                print(f"    - {ethnicity}: {percentage}%")
            # Display Income Information
                print(f"  - Income (Persons Below Poverty Level): {county.income}%")
                print("=" * 50)
    if not full_data:
        print("No data available to display.")
        return


        

def filter_by_state(state: str) -> list:
    list_state = []
    for county in full_data:
        if county.state == state:
            list_state.append(county)
    print(f"Filter: {state}, ({len(list_state)} entries)")
    return list_state


def filter_greater_by_field_number(demographics: list[full_data], field:str, num: int) -> list:
    def filter_gt(collection, field:dict, number):
        # Filter the collection based on the condition
        filtered_collection = [entry for entry in collection if entry[field] > number]

        # Print the result message with the number of remaining entries
        print(f"Filter: {field} gt {number} ({len(filtered_collection)} entries)")

        # Return the filtered collection
        return filtered_collection


def filter_lesser_by_field_number(demographics: list[full_data], field:str, num: int) -> list:
    list_less = []
    for county in full_data:
        if {field} < num:
            list_less.append(county)
    print(f"Filter: {field} ls {num} ({len(list_less)} entries)")
    return list_less

def population_total(county_demographics: list[full_data]) -> float:
    if  full_data is None:
        return 0
    total = 0
    for county in full_data:
        total += county.population["2014 Population"]
    return total

def population_field(county_demographics: list[full_data], field) -> float:
    total_sub_population = 0.0

    for county in full_data:
        if field in county.field_values:
            field_value = county.field_values[field]
            sub_population = county.population * (field_value / 100)
            total_sub_population += sub_population


def percent_field(demographics: list[full_data], field: str) -> float:
    total_sub_population = 0.0
    total_population = 0.0

    for county in full_data:
        if field in county:
            field_value = county.field
            sub_population = county.population * (field_value / 100)
            total_sub_population += sub_population
            total_population += county.population
    # If total population is zero, avoid division by zero
    if total_population == 0:
        print(f"2014 {field} percentage: 0.00")
        return 0.0
    # Calculate the percentage
    percentage = (total_sub_population / total_population) * 100
    # Print the result in the required format
    print(f"2014 {field} percentage: {percentage:.2f}")
    return percentage

