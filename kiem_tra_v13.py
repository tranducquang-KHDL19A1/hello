"""Check actual imports and deployment prerequisites; never load checkpoints."""
from pathlib import Path
import importlib
import sys
ROOT = Path(__file__).resolve().parent

def main():
    print('AI02 V13 | Project:', ROOT, '| Python:', sys.version.split()[0])
    missing = []
    for module in ('streamlit', 'PIL', 'numpy', 'scipy', 'sklearn', 'skimage', 'matplotlib', 'joblib', 'torch', 'torchvision'):
        try:
            loaded = importlib.import_module(module)
            print('[OK]', module, getattr(loaded, '__version__', ''))
        except Exception as exc:
            missing.append(module)
            print('[LOI]', module, type(exc).__name__, str(exc))
    for name in ('app.py', 'requirements.txt', 'inference_bridge.py', 'cnn_utils.py', 'recycling_advice.py', 'multiview_inference.py', 'ui_v10_utils.py'):
        ok = (ROOT / name).is_file()
        print('[OK]' if ok else '[THIEU]', name)
        if not ok: missing.append(name)
    from inference_bridge import discover_models
    models = [m for m in discover_models(ROOT / 'model') if len(m['paths']) == 1]
    print('Checkpoint duoc ung dung nhan dien:', [m['paths'][0].name for m in models])
    if not models:
        missing.append('checkpoint')
        print('[THIEU] Can chep checkpoint that vao model/; khong tu tao file rong.')
    if any(m['kind'] == 'classic' for m in models):
        try:
            importlib.import_module('src.predict')
            print('[OK] src.predict')
        except Exception as exc:
            missing.append('src.predict')
            print('[LOI] Baseline/SVM:', type(exc).__name__, str(exc))
    if not (ROOT / 'src' / 'quality.py').is_file():
        print('[LUU Y] Thieu src/quality.py: chua the huan luyen lai CNN.')
    print('Kiem tra nay khong xac minh checkpoint nap duoc hay do chinh xac.')
    print('Mo web: http://localhost:8501')
    return 1 if missing else 0

if __name__ == '__main__':
    raise SystemExit(main())
