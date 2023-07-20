## Greedy Algorithm

# huffman coding is huffman coding is a lossless data compression algorithm 
# that uses a greedy algorithm to construct a prefix code for a given set of symbols.


from collections import Counter, namedtuple

def huffman_encoding(data):
    """"
    Generates a Huffman encoded string of the input data
    """""
    # create a frequency counter for the data
    freq_counter = Counter(data)
    # create a namedtuple for the huffman tree nodes
    HuffmanNode = namedtuple("HuffmanNode", ["char", "freq"])
    # Create a priority queue for the Huffman tree
    priority_queue = PriorityQueue()
    # Add all characters to the priority queue
    for char, freq in freq_counter.items():
        priority_queue.put(HuffmanNode(char,freq))

    # Combine nodes until only the root node remains
    while priority_queue.qsize() >1:
        left_node = priority_queue.get()
        right_node = priority_queue.get()
        combined_freq = left_node.freq + right_node.freq
        combined_node = HuffmanNode(None, combined_freq)
        priority_queue.put(combined_node)

    # Generate the Huffman code for each character 
    huffman_code = {}
    generate_code(priority_queue.get(), "", huffman_code)

    # Encode the input data 
    encoded_data = ""
    for char in data:
        encoded_data += huffman_code[char]
    return encoded_data, huffman_code

print(huffman_encoding("aaaaaabbbccc"))



