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
| [subsets](./questions/backtracking/medium/subsets.py) | backtracking | `medium` |
| [valid_parentheses](./questions/stack/easy/valid_parentheses.py) | stack | `easy` |
| [reverse_polish_notation](./questions/stack/medium/reverse_polish_notation.py) | stack | `medium` |
| [min_stack](./questions/stack/medium/min_stack.py) | stack | `medium` |
| [network_delay_time](./questions/advanced_graphs/medium/network_delay_time.py) | advanced_graphs | `medium` |
| [reverse_list](./questions/linked_list/easy/reverse_list.py) | linked_list | `easy` |
| [merge_linked_lists](./questions/linked_list/easy/merge_linked_lists.py) | linked_list | `easy` |
| [linked_list_cycle_detection](./questions/linked_list/easy/linked_list_cycle_detection.py) | linked_list | `easy` |
| [reorder_list](./questions/linked_list/medium/reorder_list.py) | linked_list | `medium` |
| [remove_nth_node_from_end](./questions/linked_list/medium/remove_nth_node_from_end.py) | linked_list | `medium` |
| [jump_game](./questions/greedy/medium/jump_game.py) | greedy | `medium` |
| [hand_of_straights](./questions/greedy/medium/hand_of_straights.py) | greedy | `medium` |
| [maximum_subarray](./questions/greedy/medium/maximum_subarray.py) | greedy | `medium` |
| [gas_station](./questions/greedy/medium/gas_station.py) | greedy | `medium` |
| [unique_paths](./questions/two_dimensional_dp/medium/unique_paths.py) | two_dimensional_dp | `medium` |
| [stocks](./questions/sliding_window/easy/stocks.py) | sliding_window | `easy` |
| [longest_repeating_character_replacement](./questions/sliding_window/medium/longest_repeating_character_replacement.py) | sliding_window | `medium` |
| [longest_substring_without_repeating_characters](./questions/sliding_window/medium/longest_substring_without_repeating_characters.py) | sliding_window | `medium` |
| [sub_tree_of_tree](./questions/trees/easy/sub_tree_of_tree.py) | trees | `easy` |
| [balanced_binary_tree](./questions/trees/easy/balanced_binary_tree.py) | trees | `easy` |
| [diameter_of_binary_tree](./questions/trees/easy/diameter_of_binary_tree.py) | trees | `easy` |
| [invert_tree](./questions/trees/easy/invert_tree.py) | trees | `easy` |
| [max_depth_binary_tree](./questions/trees/easy/max_depth_binary_tree.py) | trees | `easy` |
| [same_tree](./questions/trees/easy/same_tree.py) | trees | `easy` |
| [right_side_view_of_tree](./questions/trees/medium/right_side_view_of_tree.py) | trees | `medium` |
| [binary_tree_level_order_traversal](./questions/trees/medium/binary_tree_level_order_traversal.py) | trees | `medium` |
| [number_of_islands](./questions/graphs/medium/number_of_islands.py) | graphs | `medium` |
| [max_area_of_island](./questions/graphs/medium/max_area_of_island.py) | graphs | `medium` |
| [binary_search_recursive](./questions/binary_search/easy/binary_search_recursive.py) | binary_search | `easy` |
| [binary_search_interative](./questions/binary_search/easy/binary_search_interative.py) | binary_search | `easy` |
| [search_2D_matrix](./questions/binary_search/meduim/search_2D_matrix.py) | binary_search | `meduim` |
| [koko_eats_bananas](./questions/binary_search/meduim/koko_eats_bananas.py) | binary_search | `meduim` |
| [validpal](./questions/two_pointers/easy/validpal.py) | two_pointers | `easy` |
| [two_sum_II](./questions/two_pointers/medium/two_sum_II.py) | two_pointers | `medium` |
| [3Sum](./questions/two_pointers/medium/3Sum.py) | two_pointers | `medium` |
| [climbing_stairs](./questions/one_dimensional_dp/easy/climbing_stairs.py) | one_dimensional_dp | `easy` |
| [min_cost_climbing_stairs](./questions/one_dimensional_dp/easy/min_cost_climbing_stairs.py) | one_dimensional_dp | `easy` |
| [house_robber](./questions/one_dimensional_dp/medium/house_robber.py) | one_dimensional_dp | `medium` |
| [anagram](./questions/hashmap/easy/anagram.py) | hashmap | `easy` |
| [single_number](./questions/hashmap/easy/single_number.py) | hashmap | `easy` |
| [twosum](./questions/hashmap/easy/twosum.py) | hashmap | `easy` |
| [encode_and_decode](./questions/hashmap/medium/encode_and_decode.py) | hashmap | `medium` |
| [group_anagrams](./questions/hashmap/medium/group_anagrams.py) | hashmap | `medium` |
| [last_stone_weight](./questions/heaps/easy/last_stone_weight.py) | heaps | `easy` |
| [kth_largest](./questions/heaps/easy/kth_largest.py) | heaps | `easy` |
| [k_closest_points_to_orgin](./questions/heaps/medium/k_closest_points_to_orgin.py) | heaps | `medium` |
| [kth_largest_element_in_array](./questions/heaps/medium/kth_largest_element_in_array.py) | heaps | `medium` |
