from pathlib import Path
import json
import re
import sys
from urllib.parse import unquote
from openapi_spec_validator import validate
root = Path(__file__).resolve().parents[1]
spec = json.loads((root / "docs/api/openapi-mvp.yaml").read_text(encoding="utf-8"))
validate(spec)
errors = []
for path in root.rglob("*.md"):
    if ".git" in path.parts:
        continue
    for match in re.finditer(r"\[[^\]]*\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
        target = match.group(1).split("#", 1)[0]
        if not target or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("//"):
            continue
        resolved = (path.parent / unquote(target)).resolve()
        if not resolved.is_relative_to(root) or not resolved.exists():
            errors.append(f"{path.relative_to(root)}: destino relativo inexistente")
if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"OpenAPI válido: {sum(len([m for m in methods if m in {'get','post','patch','delete','put'}]) for methods in spec['paths'].values())} operações; destinos de links relativos válidos.")

