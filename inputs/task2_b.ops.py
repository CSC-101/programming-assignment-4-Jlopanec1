# Step 1: Filter counties where the Bachelor's Degree or Higher percentage is greater than 40%
filter-gt:Income.Persons Below Poverty Level:40.0

# Step 2: Print how many counties were filtered
print "Filter: Education.Bachelor's Degree or Higher gt 40.0 (xyz entries)"

# Step 3: For each filtered county, print the percentage of the population below the poverty level
for each county in filtered_counties:
    print(f"County Name: {county['name']}")
    print(f"  Percentage of Population Below Poverty Level: {county['poverty_pct']}%")