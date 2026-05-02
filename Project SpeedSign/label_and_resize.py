import os
import shutil
from pathlib import Path

from PIL import Image, ImageOps
import matplotlib.pyplot as plt

# ====== SETTINGS ======
INPUT_DIR = Path("raw_images")          # put your unlabelled photos here
OUTPUT_DIR = Path("dataset")            # labelled + resized images end up here
IMAGE_SIZE = (224, 224)                 # common CNN size
COPY_INSTEAD_OF_MOVE = True             # True = keep originals, False = move originals away
SUPPORTED_EXTS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}

# Hotkeys -> class folder names
CLASS_MAP = {
    "1": "cigarette_used",
    "2": "cigarette_unused",
    "3": "snus_white_used",
    "4": "snus_white_unused",
    "5": "snus_black_used",
    "6": "snus_black_unused",
    "0": "reject_other",
}
# ======================


def ensure_dirs():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for class_name in CLASS_MAP.values():
        (OUTPUT_DIR / class_name).mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / "skipped").mkdir(parents=True, exist_ok=True)


def get_image_files(folder: Path):
    files = [p for p in folder.iterdir() if p.suffix.lower() in SUPPORTED_EXTS and p.is_file()]
    return sorted(files)


def unique_output_path(folder: Path, original_name: str):
    stem = Path(original_name).stem
    suffix = ".jpg"
    candidate = folder / f"{stem}{suffix}"
    i = 1
    while candidate.exists():
        candidate = folder / f"{stem}_{i}{suffix}"
        i += 1
    return candidate


def save_resized(image_path: Path, class_name: str):
    out_folder = OUTPUT_DIR / class_name
    out_path = unique_output_path(out_folder, image_path.name)

    with Image.open(image_path) as img:
        img = ImageOps.exif_transpose(img).convert("RGB")
        img = ImageOps.contain(img, IMAGE_SIZE)

        canvas = Image.new("RGB", IMAGE_SIZE, (255, 255, 255))
        x = (IMAGE_SIZE[0] - img.width) // 2
        y = (IMAGE_SIZE[1] - img.height) // 2
        canvas.paste(img, (x, y))
        canvas.save(out_path, quality=95)

    if not COPY_INSTEAD_OF_MOVE:
        image_path.unlink(missing_ok=True)

    return out_path


def mark_skipped(image_path: Path):
    skipped_folder = OUTPUT_DIR / "skipped"
    if COPY_INSTEAD_OF_MOVE:
        shutil.copy2(image_path, skipped_folder / image_path.name)
    else:
        shutil.move(str(image_path), skipped_folder / image_path.name)


def show_help():
    print("\nKeys:")
    for key, value in CLASS_MAP.items():
        print(f"  {key} -> {value}")
    print("  s -> skip")
    print("  q -> quit")
    print()


def label_images():
    ensure_dirs()
    files = get_image_files(INPUT_DIR)

    if not files:
        print(f"No images found in: {INPUT_DIR.resolve()}")
        print("Put your photos in that folder first.")
        return

    show_help()

    total = len(files)
    for idx, image_path in enumerate(files, start=1):
        print(f"[{idx}/{total}] {image_path.name}")

        with Image.open(image_path) as img:
            img = ImageOps.exif_transpose(img).convert("RGB")
            plt.figure(figsize=(8, 8))
            plt.imshow(img)
            plt.axis("off")
            plt.title(
                "1 cig_used | 2 cig_unused | 3 sw_used | 4 sw_unused | 5 sb_used | 6 sb_unused | 0 reject | s skip | q quit"
            )
            plt.show(block=False)

            choice = input("Label: ").strip().lower()
            plt.close("all")

        if choice == "q":
            print("Stopped.")
            return
        elif choice == "s":
            mark_skipped(image_path)
            print("Skipped.\n")
        elif choice in CLASS_MAP:
            saved_to = save_resized(image_path, CLASS_MAP[choice])
            print(f"Saved -> {saved_to}\n")
        else:
            print("Invalid key. Image not processed.\n")

    print("Done.")


if __name__ == "__main__":
    label_images()