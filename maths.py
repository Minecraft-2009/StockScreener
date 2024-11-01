stock_values = [1,2,3,4,5,6,7,8,10,11,8,7,7,7,7,8,9]

start_range = 0
end_range = 3

all_drop_ranges = []
index_of_ranges = []

# get ranges with proper drop
for range_length in range(2,5):
    start_range = 0
    end_range = range_length
    reached_end = False
    while not reached_end:
        section = stock_values[start_range:end_range]
        print(section)
        if section[-1] >= section[0]*0.5 and section[-1] < section[0]*0.75:
            all_drop_ranges.append([section, [start_range,end_range]])
        start_range +=1
        end_range += 1
        if end_range == len(stock_values)+1:
            reached_end = True
print("All:", all_drop_ranges)
print(stock_values[all_drop_ranges[1][1][0]])

unique_drop_ranges = []
partial_drop_ranges = []
# eliminate ranges part of larger ranges, exclude flat part
for test_drop_stats in all_drop_ranges:
    for other_drop_stats in all_drop_ranges:
        # if (other_drop_stats in partial_drop_ranges) or (other_drop_stats in unique_drop_ranges):
        #     pass
        if (test_drop_stats[1][0] >= other_drop_stats[1][0]) and (test_drop_stats[1][1] <= other_drop_stats[1][1]):
            partial_drop_ranges.append(test_drop_stats)
            if other_drop_stats not in partial_drop_ranges:
                unique_drop_ranges.append(other_drop_stats)
            if test_drop_stats in unique_drop_ranges:
                unique_drop_ranges.remove(test_drop_stats)
            if other_drop_stats in partial_drop_ranges:
                partial_drop_ranges.remove(other_drop_stats)
print("Unique:", unique_drop_ranges)
print("Partial:", partial_drop_ranges)
# remove flat from drop
# for drop_stats in unique_drop_ranges:
#     drop_range_values = drop_stats[0]
#     drop_flagged_as_flat = []
#     for num in range(2, len(drop_range_values)):
#         drop_flat_snippet = drop_range_values[-num:]
#         if drop_flat_snippet[-1] >= drop_flat_snippet[0]*0.97 and drop_flat_snippet[-1] <= drop_flat_snippet[0]*1.03:
#             drop_flagged_as_flat.append()
# get increase within X(=3) days; test for flat
meh_increase_ranges = []
for drop_stats in unique_drop_ranges:
    drop_end = drop_stats[1][1]
    rest_of_values = stock_values[drop_end:]
    for range_length in range(2,5):
        start_range = 0
        end_range = range_length
        reached_end = False
        while not reached_end:
            section = rest_of_values[start_range:end_range]
            print(section)
            if section == []:
                reached_end = True
                continue
            if section[-1] >= section[0]*1.1 :
                meh_increase_ranges.append([section, [start_range+drop_end,end_range+drop_end]])
            start_range +=1
            end_range += 1
            if end_range == len(rest_of_values)+1:
                reached_end = True
print("IncrBAD:", meh_increase_ranges)
all_increase_ranges = []
for pair in meh_increase_ranges:
    if pair[1][-1] > len(stock_values):
        pass
    else:
        all_increase_ranges.append(pair)
print("Incr:", all_increase_ranges)
unique_incr_ranges = []
partial_incr_ranges = []
# eliminate ranges part of larger ranges, exclude flat part
for test_incr_stats in all_increase_ranges:
    for other_incr_stats in all_increase_ranges:
        # if (other_drop_stats in partial_drop_ranges) or (other_drop_stats in unique_drop_ranges):
        #     pass
        if (test_incr_stats[1][0] >= other_incr_stats[1][0]) and (test_incr_stats[1][1] <= other_incr_stats[1][1]):
            partial_incr_ranges.append(test_incr_stats)
            if other_incr_stats not in partial_incr_ranges:
                unique_incr_ranges.append(other_incr_stats)
            if test_incr_stats in unique_incr_ranges:
                unique_incr_ranges.remove(test_incr_stats)
            if other_incr_stats in partial_incr_ranges:
                partial_incr_ranges.remove(other_incr_stats)
print("Unique:", unique_incr_ranges)
print("Partial:", partial_incr_ranges)

print("Drop:", unique_drop_ranges)
print("Incr:", unique_incr_ranges)

