import build_data
import sys


class DemographicsProcessor:
    def __init__(self, data):
        # Assuming the data is already provided in a list of dictionaries.
        self.data = data
        self.filtered_data = self.data

    def display(self):
        """Display the filtered counties in a readable format"""
        if not self.filtered_data:
            print("No data available to display.")
            return
        for county in self.filtered_data:
            print(f"County: {county['County']}, State: {county['State']}, Population: {county['2014 Population']}")

    def filter_state(self, state):
        """Filter counties by state abbreviation"""
        self.filtered_data = [county for county in self.data if county['State'] == state]
        print(f"Filter: state == {state} ({len(self.filtered_data)} entries)")

    def filter_gt(self, field, value):
        """Filter counties where the value of the field is greater than the specified number"""
        self.filtered_data = [county for county in self.filtered_data if float(county[field]) > value]
        print(f"Filter: {field} gt {value} ({len(self.filtered_data)} entries)")

    def filter_lt(self, field, value):
        """Filter counties where the value of the field is less than the specified number"""
        self.filtered_data = [county for county in self.filtered_data if float(county[field]) < value]
        print(f"Filter: {field} lt {value} ({len(self.filtered_data)} entries)")

    def population_total(self):
        """Compute and print the total population across all counties"""
        total_pop = sum(int(county['2014 Population']) for county in self.filtered_data)
        print(f"2014 population: {total_pop}")

    def population_field(self, field):
        """Compute the total population for a specified field (percentage of population)"""
        total_pop = sum(float(county['2014 Population']) * float(county[field]) / 100 for county in self.filtered_data)
        print(f"2014 {field} population: {total_pop}")

    def percent_field(self, field):
        """Compute the percentage of the total population for a specified field"""
        total_pop = sum(float(county['2014 Population']) for county in self.filtered_data)
        field_pop = sum(float(county['2014 Population']) * float(county[field]) / 100 for county in self.filtered_data)
        percent = (field_pop / total_pop) * 100
        print(f"2014 {field} percentage: {percent:.2f}")

    def process_operations(self, operations_file):
        """Process the operations file"""
        try:
            with open(operations_file, 'r') as f:
                for line_num, line in enumerate(f, start=1):
                    line = line.strip()
                    if not line:
                        continue  # Skip empty lines

                    try:
                        parts = line.split(':')
                        operation = parts[0]

                        if operation == "display":
                            self.display()
                        elif operation == "filter-state":
                            self.filter_state(parts[1])
                        elif operation == "filter-gt":
                            self.filter_gt(parts[1], float(parts[2]))
                        elif operation == "filter-lt":
                            self.filter_lt(parts[1], float(parts[2]))
                        elif operation == "population-total":
                            self.population_total()
                        elif operation == "population":
                            self.population_field(parts[1])
                        elif operation == "percent":
                            self.percent_field(parts[1])
                        else:
                            print(f"Error: Unknown operation at line {line_num}")
                    except IndexError:
                        print(f"Error: Malformed operation at line {line_num}")
                    except ValueError as e:
                        print(f"Error: Invalid value in operation at line {line_num}: {e}")
        except FileNotFoundError:
            print(f"Error: The operations file could not be found.")
            sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: No operations file specified.")
        sys.exit(1)

    # Example data, replace with actual data from the source.
    demo_data = [
        {'County': 'Alameda', 'State': 'CA', '2014 Population': '1500000',
         'Education.Bachelor\'s Degree or Higher': '40', 'Income.Persons Below Poverty Level': '15'},
        {'County': 'Orange', 'State': 'CA', '2014 Population': '3000000',
         'Education.Bachelor\'s Degree or Higher': '60', 'Income.Persons Below Poverty Level': '10'},
        {'County': 'Miami-Dade', 'State': 'FL', '2014 Population': '2800000',
         'Education.Bachelor\'s Degree or Higher': '30', 'Income.Persons Below Poverty Level': '22'},
        {'County': 'Harris', 'State': 'TX', '2014 Population': '4500000',
         'Education.Bachelor\'s Degree or Higher': '50', 'Income.Persons Below Poverty Level': '18'}
    ]

    operations_file = sys.argv[1]

    processor = DemographicsProcessor(demo_data)
    processor.process_operations(operations_file)
