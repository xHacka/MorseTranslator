from multiprocessing.sharedctypes import Value


def morse_code_encode(text):
    return "".join([morse[letter] + " " for letter in text.upper()])


def morse_code_decode(code):
    decoded = ""
    words = [word.split() for word in code.replace("/", "|").split('|')]
    keys, values = zip(*morse.items())
    for word in words:
        for letter in word:
            try:
                decoded += keys[values.index(letter)]
            except ValueError:
                decoded += "\u2591"
        decoded += ' '

    return decoded
  

if __name__ == '__main__':
    morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
             'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-',
             'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
             'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
             '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..',
             '-': '-....-', '/': '-..-.', ':': '---...', "'": '.----.', '_': '..--.-', ')': '-.--.-', ';': '-.-.-',
             '(': '-.--.', '=': '-...-', '@': '.--.-.', ' ': '|'}
    
    print(f"""
        \r{"-"*40}
        \r[*] Simple Morse Code Encode/Decoder
        \r[1] Encode {" ":{7}}[2] Decode
        \r[0] Example{" ":{7}}[q] Quit 
        \r{"-"*40}
        """.strip())
    
    while True: 
        action = input("\nEnter Action: ").lower()
        if action in ('0', 'example'):
            text = "This Is An Example Text"
            encoded = morse_code_encode(text)
            decoded = morse_code_decode(encoded)
            print(f"Example: {text}\nEncoded: {encoded}\nDecoded: {decoded}")
        elif action in ('1', 'encode'):
            text = input("Text To Encode:\n> ")
            print("> " + morse_code_encode(text))
        elif action in ('2', 'decode'):
            text = input("Text To Decode:\n> ")
            print("> " + morse_code_decode(text))
        elif action in ('q', 'quit', 'exit'):
            exit() 