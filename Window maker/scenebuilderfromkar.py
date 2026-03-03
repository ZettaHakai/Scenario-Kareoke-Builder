import re

def generate_scenario_calls(input_text,
                            prefix_txt1="scenario_text_0074",
                            prefix_txt2="scenario_text_0004",
                            wts_value="0x03",
                            output_file="generated_calls.c"):

    # Find all scenario_text_XXXX identifiers
    pattern = r"static\s+s16\s+(scenario_text_[0-9A-Fa-f]+)\[\]"
    matches = re.findall(pattern, input_text)

    if not matches:
        print("No scenario_text entries found.")
        return

    lines = []

    for name in matches:
        line = (
            f"        TXT, (s32)&{prefix_txt1}, "
            f"TXT, (s32)&{prefix_txt2}, "
            f"TXT, (s32)&{name}, "
            f"STW, (s32)&D_801C7740_1C8340, "
            f"WTS, {wts_value}, "
            f"ESR, (s32)&func_8003F460_40060,"
        )
        lines.append(line)

    # Write to file
    with open(output_file, "w") as f:
        for line in lines:
            f.write(line + "\n")

    print(f"Generated {len(lines)} scenario calls to {output_file}")


# ------------------ INPUT BLOCK ------------------

input_block = """
static s16 scenario_text_1500[] = { PCT_SPACE, CTR_EM_YELLOW, CHR_A, CTR_CLOSE_EM, CHR_a, PCT_COMMA, PCT_SPACE, CHR_I, CHR_M, CHR_P, CHR_A, CHR_C, CHR_T, PCT_EXCLAMATION, CTR_ENDLINE };

static s16 scenario_text_1501[] = { PCT_SPACE, CTR_EM_YELLOW, CHR_A, CHR_a, CTR_CLOSE_EM, PCT_COMMA, PCT_SPACE, CHR_I, CHR_M, CHR_P, CHR_A, CHR_C, CHR_T, PCT_EXCLAMATION, CTR_ENDLINE };

static s16 scenario_text_1502[] = { PCT_SPACE, CTR_EM_YELLOW, CHR_A, CHR_a, PCT_COMMA, PCT_SPACE, CHR_I, CTR_CLOSE_EM, CHR_M, CHR_P, CHR_A, CHR_C, CHR_T, PCT_EXCLAMATION, CTR_ENDLINE };

static s16 scenario_text_1503[] = { PCT_SPACE, CTR_EM_YELLOW, CHR_A, CHR_a, PCT_COMMA, PCT_SPACE, CHR_I, CHR_M, CTR_CLOSE_EM, CHR_P, CHR_A, CHR_C, CHR_T, PCT_EXCLAMATION, CTR_ENDLINE };

static s16 scenario_text_1504[] = { PCT_SPACE, CTR_EM_YELLOW, CHR_A, CHR_a, PCT_COMMA, PCT_SPACE, CHR_I, CHR_M, CHR_P, CTR_CLOSE_EM, CHR_A, CHR_C, CHR_T, PCT_EXCLAMATION, CTR_ENDLINE };

static s16 scenario_text_1505[] = { PCT_SPACE, CTR_EM_YELLOW, CHR_A, CHR_a, PCT_COMMA, PCT_SPACE, CHR_I, CHR_M, CHR_P, CHR_A, CTR_CLOSE_EM, CHR_C, CHR_T, PCT_EXCLAMATION, CTR_ENDLINE };

static s16 scenario_text_1506[] = { PCT_SPACE, CTR_EM_YELLOW, CHR_A, CHR_a, PCT_COMMA, PCT_SPACE, CHR_I, CHR_M, CHR_P, CHR_A, CHR_C, CTR_CLOSE_EM, CHR_T, PCT_EXCLAMATION, CTR_ENDLINE };

static s16 scenario_text_1507[] = { PCT_SPACE, CTR_EM_YELLOW, CHR_A, CHR_a, PCT_COMMA, PCT_SPACE, CHR_I, CHR_M, CHR_P, CHR_A, CHR_C, CHR_T, CTR_CLOSE_EM, PCT_EXCLAMATION, CTR_ENDLINE };



"""

generate_scenario_calls(input_block)