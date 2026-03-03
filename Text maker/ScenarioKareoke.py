# Python 3.x

def generate_sliding_arrays_close_only(base_line_str, start_id=0x1500,
                                       emphasis="CTR_EM_YELLOW",
                                       close="CTR_CLOSE_EM"):
    arrays = {}
    output_id = start_id

    # Split single wrapped string into tokens
    base_line = base_line_str.split(",")

    # Strip whitespace
    base_line = [token.strip() for token in base_line]

    # Find first CHR_ token
    first_letter_index = next(
        (i for i, v in enumerate(base_line) if v.startswith("CHR_")),
        None
    )

    if first_letter_index is None:
        return arrays

    for i, val in enumerate(base_line):
        if not val.startswith("CHR_"):
            continue

        line = base_line.copy()

        # Insert closing emphasis after current letter
        line.insert(i + 1, close)

        # Insert opening emphasis at first letter
        line.insert(first_letter_index, emphasis)

        array_name = f"scenario_text_{output_id:04X}"
        arrays[array_name] = line
        output_id += 1

    return arrays


def write_arrays_to_file(arrays, filename="scenario_arrays.c"):
    with open(filename, "w") as f:
        for name, content in arrays.items():
            line_str = ", ".join(content)
            f.write(f"static s16 {name}[] = {{ {line_str} }};\n\n")
    print(f"Written {len(arrays)} arrays to {filename}")


# ---------------- vvvv Quote Area vvvv----------------

base_line = """

PCT_SPACE,CHR_A,CHR_a,PCT_COMMA,PCT_SPACE,CHR_I,CHR_M,CHR_P,CHR_A,CHR_C,CHR_T,PCT_EXCLAMATION,CTR_ENDLINE

"""

arrays = generate_sliding_arrays_close_only(base_line, start_id=0x1500)
write_arrays_to_file(arrays, filename="scenario_arrays.c")