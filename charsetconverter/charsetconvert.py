import sys

def utf8_to_utf16(input, output):
    with open(input, "r", encoding="utf-8") as f, open(output, 'wb') as converted:
        converted.write(f.read().encode('utf-16le'))

def utf16_to_utf8(input, output):
    with open(input, "rb") as f, open(output, "w", encoding="utf-8") as converted:
        converted.write(f.read().decode('utf-16le'))

if (len(sys.argv) != 4 or sys.argv[1] not in ("create", "extract")):
    print("Usage:")
    print("   python charsetconvert.py <command> <in_file> <out_file>")
    print("Commands:")
    print("   create   create character set text file")
    print("            example: python charsetconvert.py create SG_charset.txt mages_charset.bin")
    print("   extract  extract a character set from an existing .bin file")
    print("            example: python charsetconvert.py extract mages_charset_steam.bin steam_charset.txt")
    sys.exit(1)

if sys.argv[1] == "create":
    utf8_to_utf16(sys.argv[2], sys.argv[3])
elif sys.argv[1] == "extract":
    utf16_to_utf8(sys.argv[2], sys.argv[3]) 
