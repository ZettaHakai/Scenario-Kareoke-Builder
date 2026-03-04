import re

input_file = "input.c"
output_file = "scenario_file_labeled.c"

# Read input file
with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Find last yellow letter for each scenario_text array
yellow_last = {}
array_pattern = re.compile(r"static s16 (scenario_text_[0-9A-F]+)\[\]\s*=\s*\{(.*?)\};", re.DOTALL)
chr_pattern = re.compile(r"CHR_([A-Za-z0-9])")

for line_idx, line in enumerate(lines):
    if "static s16 scenario_text_" in line:
        array_block = line
        i = line_idx + 1
        while "};" not in array_block and i < len(lines):
            array_block += lines[i]
            i += 1
        m = array_pattern.search(array_block)
        if m:
            array_name = m.group(1)
            body = m.group(2)
            yellow_block = re.search(r"CTR_EM_YELLOW(.*?)(CTR_CLOSE_EM)", body, re.DOTALL)
            if yellow_block:
                letters = chr_pattern.findall(yellow_block.group(1))
                if letters:
                    last_letter = letters[-1]
                    yellow_last[array_name] = last_letter
                    # Only add comment if it does not already exist
                    if not re.search(rf";\s*//{last_letter}", array_block):
                        array_block = re.sub(r"\};\s*$", f"}}; //{last_letter}\n", array_block, flags=re.MULTILINE)
                        lines[line_idx:i] = [array_block]

# Add comment to TXT lines referencing the arrays
for idx, line in enumerate(lines):
    txt_match = re.search(r"TXT,\s*\(s32\)&.*?,\s*\(s32\)&(scenario_text_[0-9A-F]+)", line)
    if txt_match:
        array_name = txt_match.group(1)
        if array_name in yellow_last:
            last_letter = yellow_last[array_name]
            # Only append if not already present
            if f"//{last_letter}" not in line:
                lines[idx] = line.rstrip() + f" //{last_letter}\n"

# Write output
with open(output_file, "w", encoding="utf-8") as f:
    f.writelines(lines)

print(f"Labels applied. Output written to {output_file}")