# LC100: 100 Days of Leetcode

For my last summer before I'm a senior at BC, I've set out to challenge myself with practicing at least one LeetCode question every day for 100 days straight. The goal here is consistency and gradual improvement in my problem-solving skills.

## Progress Heatmap
![sebas's progress xD)](./auto_assets/plot.png)


The heat map above tracks my daily progress. I consider a day a win so long as I push a solution -- whether I nailed the problem or just put forth a genuine effort.

### A day gets credited when I either:

1. Submit a solution to a new problem
2. Modify/improve an existing solution

The heatmap is made using this janky seaborn wrapper called july -- currently the main repo has a ton of bugs. I've forked and cleaned up a lot of them: you can find that here: [sebas-july](https://github.com/SebPuchi/july)

## Integrity & Automation 

To keep myself accountable, I've set up a github actions bot to automatically monitor my progress. Every night at midnight ET, the server examines my git commit history to detect if I've made any updates to ./questions

If activity is detected, I get credit for that day. The idea here is that git history never lies and I can't go back and change things even if I wanted to. 

The automation script that I cooked up handles most of the heavy lifting

[update_status.py](./update_status.py) does the following every night:

1. Automatically generates the progress heat map
2. Updates this README with my current progress
3. Maintains the completed questions table below

## Notes
Once I feel comfortable with a completed question, I write up solutions notes and add it it to my ongoing latex file

<p align="center">
  <a href="./notex.pdf">
    <img src="./auto_assets/notes.png" width="750">
  </a>
</p>

## Completed Questions
| Question | Category | Difficulty |
|:-----------------------------|:---------|:------------|
| [palindromic_substrings](./questions/one_dimensional_dp/medium/palindromic_substrings.py) | one_dimensional_dp | `medium` |
| [decode_ways](./questions/one_dimensional_dp/medium/decode_ways.py) | one_dimensional_dp | `medium` |
| [house_robber](./questions/one_dimensional_dp/medium/house_robber.py) | one_dimensional_dp | `medium` |
| [house_robber_II](./questions/one_dimensional_dp/medium/house_robber_II.py) | one_dimensional_dp | `medium` |
| [longest_palindromic_substring](./questions/one_dimensional_dp/medium/longest_palindromic_substring.py) | one_dimensional_dp | `medium` |
| [coin_change](./questions/one_dimensional_dp/medium/coin_change.py) | one_dimensional_dp | `medium` |
| [min_cost_climbing_stairs](./questions/one_dimensional_dp/easy/min_cost_climbing_stairs.py) | one_dimensional_dp | `easy` |
| [climbing_stairs](./questions/one_dimensional_dp/easy/climbing_stairs.py) | one_dimensional_dp | `easy` |
| [daily_temperatures](./questions/stack/medium/daily_temperatures.py) | stack | `medium` |
| [min_stack](./questions/stack/medium/min_stack.py) | stack | `medium` |
| [reverse_polish_notation](./questions/stack/medium/reverse_polish_notation.py) | stack | `medium` |
| [remove_all_adjacent_duplicates_in_string](./questions/stack/easy/remove_all_adjacent_duplicates_in_string.py) | stack | `easy` |
| [valid_parentheses](./questions/stack/easy/valid_parentheses.py) | stack | `easy` |
| [maximum_subarray](./questions/greedy/medium/maximum_subarray.py) | greedy | `medium` |
| [jump_game](./questions/greedy/medium/jump_game.py) | greedy | `medium` |
| [gas_station](./questions/greedy/medium/gas_station.py) | greedy | `medium` |
| [hand_of_straights](./questions/greedy/medium/hand_of_straights.py) | greedy | `medium` |
| [copy_linked_list_with_random_pointer](./questions/linked_list/medium/copy_linked_list_with_random_pointer.py) | linked_list | `medium` |
| [remove_nth_node_from_end](./questions/linked_list/medium/remove_nth_node_from_end.py) | linked_list | `medium` |
| [add_two_numbers](./questions/linked_list/medium/add_two_numbers.py) | linked_list | `medium` |
| [sort_list](./questions/linked_list/medium/sort_list.py) | linked_list | `medium` |
| [find_duplicate_number](./questions/linked_list/medium/find_duplicate_number.py) | linked_list | `medium` |
| [reorder_list](./questions/linked_list/medium/reorder_list.py) | linked_list | `medium` |
| [reverse_list](./questions/linked_list/easy/reverse_list.py) | linked_list | `easy` |
| [linked_list_cycle_detection](./questions/linked_list/easy/linked_list_cycle_detection.py) | linked_list | `easy` |
| [merge_linked_lists](./questions/linked_list/easy/merge_linked_lists.py) | linked_list | `easy` |
| [merge_k_sorted_linked_lists](./questions/linked_list/hard/merge_k_sorted_linked_lists.py) | linked_list | `hard` |
| [longest_repeating_character_replacement](./questions/sliding_window/medium/longest_repeating_character_replacement.py) | sliding_window | `medium` |
| [longest_substring_without_repeating_characters](./questions/sliding_window/medium/longest_substring_without_repeating_characters.py) | sliding_window | `medium` |
| [permutation_in_string](./questions/sliding_window/medium/permutation_in_string.py) | sliding_window | `medium` |
| [stocks](./questions/sliding_window/easy/stocks.py) | sliding_window | `easy` |
| [valid_sudoku](./questions/hashmap/medium/valid_sudoku.py) | hashmap | `medium` |
| [product_of_array_except_self](./questions/hashmap/medium/product_of_array_except_self.py) | hashmap | `medium` |
| [encode_and_decode](./questions/hashmap/medium/encode_and_decode.py) | hashmap | `medium` |
| [group_anagrams](./questions/hashmap/medium/group_anagrams.py) | hashmap | `medium` |
| [twosum](./questions/hashmap/easy/twosum.py) | hashmap | `easy` |
| [single_number](./questions/hashmap/easy/single_number.py) | hashmap | `easy` |
| [happy_number](./questions/hashmap/easy/happy_number.py) | hashmap | `easy` |
| [anagram](./questions/hashmap/easy/anagram.py) | hashmap | `easy` |
| [implement_trie_prefix_tree](./questions/tries/medium/implement_trie_prefix_tree.py) | tries | `medium` |
| [unique_paths](./questions/two_dimensional_dp/medium/unique_paths.py) | two_dimensional_dp | `medium` |
| [longest_common_subsequence](./questions/two_dimensional_dp/medium/longest_common_subsequence.py) | two_dimensional_dp | `medium` |
| [binary_search_interative](./questions/binary_search/easy/binary_search_interative.py) | binary_search | `easy` |
| [binary_search_recursive](./questions/binary_search/easy/binary_search_recursive.py) | binary_search | `easy` |
| [find_min_in_rotated_sorted_array](./questions/binary_search/meduim/find_min_in_rotated_sorted_array.py) | binary_search | `meduim` |
| [koko_eats_bananas](./questions/binary_search/meduim/koko_eats_bananas.py) | binary_search | `meduim` |
| [search_rotated_sorted_array](./questions/binary_search/meduim/search_rotated_sorted_array.py) | binary_search | `meduim` |
| [search_2D_matrix_II](./questions/binary_search/meduim/search_2D_matrix_II.py) | binary_search | `meduim` |
| [search_2D_matrix](./questions/binary_search/meduim/search_2D_matrix.py) | binary_search | `meduim` |
| [meeting_rooms_II](./questions/intervals/medium/meeting_rooms_II.py) | intervals | `medium` |
| [insert_interval](./questions/intervals/medium/insert_interval.py) | intervals | `medium` |
| [merge_intervals](./questions/intervals/medium/merge_intervals.py) | intervals | `medium` |
| [non_overlapping_intervals](./questions/intervals/medium/non_overlapping_intervals.py) | intervals | `medium` |
| [meeting_rooms](./questions/intervals/easy/meeting_rooms.py) | intervals | `easy` |
| [merge_two_2d_arrays_by_summing_values](./questions/intervals/easy/merge_two_2d_arrays_by_summing_values.py) | intervals | `easy` |
| [longest_consecutive_sequence](./questions/two_pointers/medium/longest_consecutive_sequence.py) | two_pointers | `medium` |
| [3Sum](./questions/two_pointers/medium/3Sum.py) | two_pointers | `medium` |
| [squares_of_a_sorted_array](./questions/two_pointers/medium/squares_of_a_sorted_array.py) | two_pointers | `medium` |
| [container_with_most_water](./questions/two_pointers/medium/container_with_most_water.py) | two_pointers | `medium` |
| [two_sum_II](./questions/two_pointers/medium/two_sum_II.py) | two_pointers | `medium` |
| [validpal](./questions/two_pointers/easy/validpal.py) | two_pointers | `easy` |
| [valid_pal_II](./questions/two_pointers/easy/valid_pal_II.py) | two_pointers | `easy` |
| [course_schedule](./questions/graphs/medium/course_schedule.py) | graphs | `medium` |
| [pacific_atlantic_water_flow](./questions/graphs/medium/pacific_atlantic_water_flow.py) | graphs | `medium` |
| [max_area_of_island](./questions/graphs/medium/max_area_of_island.py) | graphs | `medium` |
| [graph_valid_tree](./questions/graphs/medium/graph_valid_tree.py) | graphs | `medium` |
| [clone_graph](./questions/graphs/medium/clone_graph.py) | graphs | `medium` |
| [surrounded_regions](./questions/graphs/medium/surrounded_regions.py) | graphs | `medium` |
| [graph_count_connected_components](./questions/graphs/medium/graph_count_connected_components.py) | graphs | `medium` |
| [rotten_oranges](./questions/graphs/medium/rotten_oranges.py) | graphs | `medium` |
| [Islands_and_treasures](./questions/graphs/medium/Islands_and_treasures.py) | graphs | `medium` |
| [number_of_islands](./questions/graphs/medium/number_of_islands.py) | graphs | `medium` |
| [alien_dictonary](./questions/graphs/hard/alien_dictonary.py) | graphs | `hard` |
| [word_search](./questions/backtracking/medium/word_search.py) | backtracking | `medium` |
| [combination_sum](./questions/backtracking/medium/combination_sum.py) | backtracking | `medium` |
| [subsets](./questions/backtracking/medium/subsets.py) | backtracking | `medium` |
| [task_schedular](./questions/heaps/medium/task_schedular.py) | heaps | `medium` |
| [kth_largest_element_in_array](./questions/heaps/medium/kth_largest_element_in_array.py) | heaps | `medium` |
| [k_closest_points_to_orgin](./questions/heaps/medium/k_closest_points_to_orgin.py) | heaps | `medium` |
| [last_stone_weight](./questions/heaps/easy/last_stone_weight.py) | heaps | `easy` |
| [kth_largest](./questions/heaps/easy/kth_largest.py) | heaps | `easy` |
| [validate_binary_search_tree](./questions/trees/medium/validate_binary_search_tree.py) | trees | `medium` |
| [kth_smallest_int_in_bst](./questions/trees/medium/kth_smallest_int_in_bst.py) | trees | `medium` |
| [right_side_view_of_tree](./questions/trees/medium/right_side_view_of_tree.py) | trees | `medium` |
| [longest_common_ancestor_in_binary_search_tree](./questions/trees/medium/longest_common_ancestor_in_binary_search_tree.py) | trees | `medium` |
| [binary_tree_level_order_traversal](./questions/trees/medium/binary_tree_level_order_traversal.py) | trees | `medium` |
| [count_good_nodes_in_tree](./questions/trees/medium/count_good_nodes_in_tree.py) | trees | `medium` |
| [construct_binary_tree_from_preorder_and_inorder_traversal](./questions/trees/medium/construct_binary_tree_from_preorder_and_inorder_traversal.py) | trees | `medium` |
| [same_tree](./questions/trees/easy/same_tree.py) | trees | `easy` |
| [diameter_of_binary_tree](./questions/trees/easy/diameter_of_binary_tree.py) | trees | `easy` |
| [invert_tree](./questions/trees/easy/invert_tree.py) | trees | `easy` |
| [max_depth_binary_tree](./questions/trees/easy/max_depth_binary_tree.py) | trees | `easy` |
| [balanced_binary_tree](./questions/trees/easy/balanced_binary_tree.py) | trees | `easy` |
| [sub_tree_of_tree](./questions/trees/easy/sub_tree_of_tree.py) | trees | `easy` |
| [binary_tree_maximum_path_sum](./questions/trees/hard/binary_tree_maximum_path_sum.py) | trees | `hard` |
| [serialize_and_deserialize_binary_tree](./questions/trees/hard/serialize_and_deserialize_binary_tree.py) | trees | `hard` |
| [set_matrix_zeros](./questions/math_geometry/medium/set_matrix_zeros.py) | math_geometry | `medium` |
| [rotate_image](./questions/math_geometry/medium/rotate_image.py) | math_geometry | `medium` |
| [spiral_matrix](./questions/math_geometry/medium/spiral_matrix.py) | math_geometry | `medium` |
| [plus_one](./questions/math_geometry/easy/plus_one.py) | math_geometry | `easy` |
| [network_delay_time](./questions/advanced_graphs/medium/network_delay_time.py) | advanced_graphs | `medium` |
