import heapq

def parse_file(file_in):
    data = []
    with open(file_in, 'r') as file:
        for line in file:
            space_idx = line.find(' ')
            code = int(line[:space_idx])
            content = line[space_idx + 1:].strip()  # Strip any leading/trailing whitespace
            data.append((code, content))  # Store as tuple
    return data

def decode(message_file):
    org_data = parse_file(message_file)
    for i in range(len(org_data)):
        heapq.heapify(rg_data[:i+1])
    decode_list = []

    #traserve
    idx = 0
    while idx < len(org_data):
        _, content = org_data[idx]  
        decode_list.append(content)
        right_child = idx * 2 + 2
        if right_child < len(org_data):
            idx = right_child
        else:
            break

    
    print(' '.join(decode_list))

decode("coding_qual_input.txt")