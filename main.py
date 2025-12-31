ъ#!/usr/bin/env python3

import sys
from pathlib import Path
from detector import detect_type
from handlers import get_handler
from validator import validate_input, validate_output

def main():
    if len(sys.argv) < 3:
        print("usage: python main.py <input> <output>", file=sys.stderr)
        sys.exit(1)
    
    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    
    if not validate_input(input_path):
        sys.exit(1)
    
    if not validate_output(output_path):
        sys.exit(1)
    
    file_type = detect_type(input_path)
    handler = get_handler(file_type)
    
    if not handler:
        print(f"unsupported type: {file_type}", file=sys.stderr)
        sys.exit(1)
    
    try:
        handler.convert(input_path, output_path)
    except Exception as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()