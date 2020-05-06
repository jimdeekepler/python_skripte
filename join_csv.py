from __future__ import print_function

def join_lines(lines, pick_column, num_lines, primary_key_columns=[0, 1]):
    last_ids = []
    item_columns = []
    for line in lines.split('\n'):
        columns = line.split()
        if columns == []:
            continue
        if len(last_ids) == 0:
                for pk_col in primary_key_columns:
                    # print(pk_col)
                    # print(columns[pk_col])
                    last_ids.append(columns[pk_col])
        else:
            for i in range(len(primary_key_columns)):
                if last_ids[i] != columns[primary_key_columns[i]]:
                    # start a new line
                    last_ids = []
                    item_columns = []
                    break
        if (len(last_ids)) != 0:
            # join lines
            item_columns.append(columns[pick_column])
            if len(item_columns) == num_lines:
                output = ""
                for last_id in last_ids:
                    output += last_id + "\t"
                for item in item_columns:
                    output += item + "\t"
                print(output)

        # print(columns)


example_input = """
1	2	3	4	5	6
1	2	5	7	9	9
1	2	7	8	9	9
"""

join_lines(example_input, 3, 3)
join_lines(example_input, 4, 3)

