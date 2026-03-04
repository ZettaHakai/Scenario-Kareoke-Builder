import re

windows_file = "windows.c"        # file with original 18 STW timings
scenario_file = "scenario_text.c" # file with letters broken into TXT windows
output_file = "scenario_adjusted.c"

# Regex
stw_pattern = re.compile(r'STW\s*,\s*\(s32\)&D_801C7740_1C8340\s*,\s*WTS\s*,\s*(0x[0-9A-Fa-f]+)')
txt_pattern = re.compile(r'TXT\s*,\s*\(s32\)&scenario_text_[0-9A-Fa-f]+')

# -------- Step 1: Read original window timings --------
with open(windows_file, "r") as f:
    original_timings = [int(m.group(1), 16) for line in f
                        if (m := stw_pattern.search(line))]

if not original_timings:
    raise ValueError("No STW timings found in windows file.")

# -------- Step 2: Read scenario TXT lines --------
with open(scenario_file, "r") as f:
    scenario_lines = f.readlines()

# Extract all TXT lines with their indices
txt_indices = [i for i, line in enumerate(scenario_lines) if txt_pattern.search(line)]
num_txt = len(txt_indices)

# -------- Step 3: Distribute original timings across TXT lines --------
num_windows = len(original_timings)
# Total letters per original window (roughly equal)
# e.g., if 320 letters over 18 windows, letters_per_window = [17,17,18,...]
letters_per_window = []
quotient, remainder = divmod(num_txt, num_windows)
for i in range(num_windows):
    letters_per_window.append(quotient + (1 if i < remainder else 0))

# Assign timings
assigned_timings = []
for window_idx, count in enumerate(letters_per_window):
    timing = original_timings[window_idx]
    per_letter = timing // count
    assigned_timings.extend([per_letter]*count)

if len(assigned_timings) != num_txt:
    raise ValueError("Timing allocation mismatch!")

# -------- Step 4: Write adjusted scenario --------
adjusted_lines = scenario_lines.copy()
for idx, line_idx in enumerate(txt_indices):
    # find the next STW line after this TXT, replace timing
    # easier: insert STW before this TXT
    adjusted_lines[line_idx] = re.sub(
        r'STW\s*,\s*\(s32\)&D_801C7740_1C8340\s*,\s*WTS\s*,\s*0x[0-9A-Fa-f]+',
        f'STW, (s32)&D_801C7740_1C8340, WTS, 0x{assigned_timings[idx]:X}',
        scenario_lines[line_idx]
    )

with open(output_file, "w") as f:
    f.writelines(adjusted_lines)

print(f"Adjusted scenario written to {output_file} ({num_txt} letters updated)")
