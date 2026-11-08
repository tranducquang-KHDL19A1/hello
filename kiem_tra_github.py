"""Report large upload candidates without modifying any files."""
from pathlib import Path
ROOT = Path(__file__).resolve().parent
SKIP = {'.venv', 'venv', '.git', '__pycache__', 'data'}
if __name__ == '__main__':
    count = 0
    for path in sorted(ROOT.rglob('*')):
        rel = path.relative_to(ROOT)
        if any(part in SKIP for part in rel.parts) or not path.is_file():
            continue
        size = path.stat().st_size / (1024 * 1024)
        if size > 25:
            count += 1
            method = 'Git LFS' if size > 100 else 'Git (khong tai qua trinh duyet)'
            print(f'{size:.2f} MiB | {rel} | {method}')
    if not count:
        print('Khong co file vuot 25 MiB trong cac thu muc da kiem tra.')
