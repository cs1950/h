from heapq import heappush, heappop, heapify
from collections import defaultdict
import time 

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(freq_map):
    priority_queue = [HuffmanNode(char, freq) for char, freq in freq_map.items()]
    
    heapify(priority_queue)

    while len(priority_queue) > 1:
        left_node = heappop(priority_queue)
        right_node = heappop(priority_queue)

        merged_node = HuffmanNode(None, left_node.freq + right_node.freq)
        merged_node.left = left_node
        merged_node.right = right_node

        heappush(priority_queue, merged_node)

    return priority_queue[0]


def generate_huffman_codes(root, current_code="", huffman_codes={}):
    if root is None:
        return

    if root.char is not None:
        huffman_codes[root.char] = current_code
        return

    generate_huffman_codes(root.left, current_code + "0", huffman_codes)
    generate_huffman_codes(root.right, current_code + "1", huffman_codes)


def huffman_encoding(text):
    if text=="":
        return "", {}

    freq_map = defaultdict(int)
    for char in text:
        freq_map[char] += 1

    huffman_tree = build_huffman_tree(freq_map)
    huffman_codes = {}
    generate_huffman_codes(huffman_tree, "", huffman_codes)

    encoded_text = "".join(huffman_codes[char] for char in text)
    return encoded_text, huffman_codes

if __name__ == "__main__":
    input_text = input("Enter Message: ")
    start_time = time.time()
    encoded_text, huffman_codes = huffman_encoding(input_text)
    end_time = time.time()
    print(f"Time:{(end_time-start_time):.6f} seconds\n")
    print(f"Encoded text: {encoded_text}\n")
    print("Huffman Codes:\n")
    for char, code in huffman_codes.items():
        print(f"{char}: {code}")

