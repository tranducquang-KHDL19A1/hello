"""Start the existing AI02 Streamlit interface on Render."""
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent

def main():
    os.chdir(ROOT)
    from inference_bridge import discover_models
    models = discover_models(ROOT / "model")
    if not models:
        raise SystemExit("Missing trained checkpoint in model/. Upload an AI02 .pth or .joblib before deploying.")
    if any(m["kind"] == "classic" for m in models) and not (ROOT / "src" / "predict.py").is_file():
        print("Warning: src/predict.py is missing; Baseline/SVM will not work.", flush=True)
    port = str(int(os.environ.get("PORT", "8501")))
    os.execv(sys.executable, [sys.executable, "-m", "streamlit", "run",
        str(ROOT / "app.py"), "--server.address=0.0.0.0",
        "--server.port=" + port, "--server.headless=true"])

if __name__ == "__main__":
    main()
