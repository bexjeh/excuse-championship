import os

ENTRY = "I deleted your file, but I kept a perfect memory of deleting it, if that helps."


def main():
    # Gate validation: the sealed scorer requires UTF-8 text of 1-140
    # characters, not whitespace-only, on a single line.
    assert ENTRY and not ENTRY.isspace(), "entry must not be blank"
    assert ENTRY == ENTRY.strip(), "entry must not have leading/trailing whitespace"
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    ENTRY.encode("utf-8")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(".", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
