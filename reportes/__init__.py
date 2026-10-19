import importlib.util
import sys
from pathlib import Path

ruta = Path(__file__).resolve().parent.parent / "reportes.py"
spec = importlib.util.spec_from_file_location("modulo_reportes", ruta)
reportes = importlib.util.module_from_spec(spec)
sys.modules["modulo_reportes"] = reportes
spec.loader.exec_module(reportes)

sys.modules["reportes"] = reportes
