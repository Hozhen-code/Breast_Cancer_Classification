from __future__ import annotations
from pathlib import Path
import os

# 루트 탐색 기준 파일들 (있으면 루트로 간주)
_MARKERS = {".git", "requirements.txt", "pyproject.toml"}

def _find_project_root(start: Path | None = None) -> Path:
    """
    start 위치(기본: CWD)에서 위로 올라가며 프로젝트 루트를 찾는다.
    - 환경변수 PROJECT_ROOT가 설정되어 있으면 그걸 최우선으로 사용
    - .git / requirements.txt / pyproject.toml 등 마커 파일이 보이면 거기를 루트로 간주
    - 그래도 못 찾으면 현재 작업 디렉토리(Path.cwd())를 반환
    """
    env_root = os.getenv("PROJECT_ROOT")
    if env_root:
        return Path(env_root).resolve()

    cur = (start or Path.cwd()).resolve()
    for p in [cur, *cur.parents]:
        if any((p / m).exists() for m in _MARKERS):
            return p
    return cur  # fallback

def get_root(start: Path | None = None) -> Path:
    """프로젝트 루트 경로(Path) 반환"""
    return _find_project_root(start)

def get_data_dir(create: bool = True) -> Path:
    """루트 하위 data 디렉토리 경로. 없으면 create=True 시 생성."""
    p = get_root() / "data"
    if create:
        p.mkdir(parents=True, exist_ok=True)
    return p

def get_outputs_dir(create: bool = True) -> Path:
    """루트 하위 outputs 디렉토리 경로. 없으면 create=True 시 생성."""
    p = get_root() / "outputs"
    if create:
        p.mkdir(parents=True, exist_ok=True)
    return p

def get_data_path(*parts: str, create_parents: bool = False) -> Path:
    """
    data 하위 파일/폴더 경로를 안전하게 생성
    예) get_data_path("breast-cancer.csv")
    """
    p = get_data_dir(create=True).joinpath(*parts)
    if create_parents:
        p.parent.mkdir(parents=True, exist_ok=True)
    return p

def get_output_path(*parts: str, create_parents: bool = True) -> Path:
    """
    outputs 하위 파일 경로 생성 (기본적으로 상위 폴더 생성)
    예) get_output_path("figures", "roc_curve.png")
    """
    p = get_outputs_dir(create=True).joinpath(*parts)
    if create_parents:
        p.parent.mkdir(parents=True, exist_ok=True)
    return p
