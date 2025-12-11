# TEST DATA - Do not modify
creator_name = "DigitalDreamer"
current_followers = 4567
starting_followers = 2100
days_tracked = 45
milestone_increment = 1000

# YOUR CODE BELOW THIS LINE
# Calculate follower statistics and milestone progress

# Calculate milestone progress
current_milestone = current_followers // milestone_increment
progress_in_milestone = current_followers % milestone_increment

# Calculate growth statistics
total_gained = current_followers - starting_followers
daily_average = int(round(total_gained // days_tracked, 0))

# Calculate projections
days_to_milestone = int(round((milestone_increment - progress_in_milestone) / daily_average, 0))
weekly_growth = daily_average * 7

# Display results with f-strings
print(f'''Creator: {creator_name}
Current Milestone: {current_milestone}
Progress in Milestone: {progress_in_milestone} followers 
Total Growth: {total_gained} followers
Daily Average: {daily_average} followers
Days to Next Milestone: {days_to_milestone} days
Weekly Growth Projection: {weekly_growth} followers''')
