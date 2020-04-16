"""
CP1404/CP5632 Practical - Suggested Solution
Hexadecimal colour lookup
"""

COLOUR_TO_CODE = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7",
                "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc",
                "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378",
                "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6",
                "aquamarine4": "#458b74", "azure1": "#f0ffff",
                "azure2": "#e0eeee", "azure3": "#c1cdcd", "azure4": "#838b8b",
                "beige": "#f5f5dc", "bisque1": "#ffe4c4"}


def main():
    max_key_length = max([len(key) for key in COLOUR_TO_CODE.keys()])
    print("max key length:", max_key_length)
    for colour, code in COLOUR_TO_CODE.items():
        print("{:{col_width}} - {}".format(colour, code, col_width=max_key_length))


if __name__ == '__main__':
    main()
