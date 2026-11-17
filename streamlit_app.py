"""Klimatperspektiv – klimatpåverkan per DeSO i Malmö i fem perspektiv (kartlager) för översiktsplaneringen:
markens klimatvärde, nyexploatering, transport och mobilitet, energi och cirkularitet, 2024–2050.

Starta lokalt:                 python -m streamlit run streamlit_app.py
Streamlit Community Cloud:     huvudfil streamlit_app.py
Beräkningen körs i webbläsaren (app/model.js). Streamlit bäddar in koden och underlaget i en fristående HTML-sida.
"""
from __future__ import annotations

import io
import json
import re
import zipfile
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SHELL = "app/shell.html"
MARKER = re.compile(r"\{\{([^}]+)\}\}")
DATAFILER = ("data/grund_deso.json", "data/kol_deso.json", "data/utbyggnad_op2023.json", "data/deso_2025_malmo.geojson",
             "data/land_malmo_osm.json", "data/metadata.json", "data/kallkontroll.json", "data/stadsutveckling.json", "data/metodtext.json")


def _embed(name: str, text: str) -> str:
    text = text.strip()
    if name.endswith((".json", ".geojson")):
        json.loads(text)  # validera
        return text.replace("<", "\\u003c")
    if name.endswith(".js"):
        return re.sub(r"</script", r"<\\/script", text, flags=re.IGNORECASE)
    if name.endswith(".css"):
        return re.sub(r"</style", r"<\\/style", text, flags=re.IGNORECASE)
    return text


def _signature() -> tuple:
    files = [*sorted((ROOT / "app").glob("*")), *sorted((ROOT / "data").glob("*"))]
    return tuple((str(p), p.stat().st_mtime_ns, p.stat().st_size) for p in files if p.is_file())


@lru_cache(maxsize=2)
def _assemble_cached(signature: tuple) -> str:
    del signature
    return assemble()


def assemble() -> str:
    """Bygg en fristående HTML-sida med all kod och allt underlag inbäddat."""
    shell = (ROOT / SHELL).read_text(encoding="utf-8")
    meta = json.loads((ROOT / "data/metadata.json").read_text(encoding="utf-8"))

    def sub(match: re.Match) -> str:
        name = match[1]
        if name == "byggdatum":
            return meta.get("byggdatum", "")
        if ".." in name.split("/") or not (name.startswith("app/") or name.startswith("data/")):
            raise ValueError("Otillåten sökväg i mallen: " + name)
        return _embed(name, (ROOT / name).read_text(encoding="utf-8"))

    html = MARKER.sub(sub, shell)
    if re.search(r"\{\{(?:app|data)/[^}]*\}\}", html):
        raise ValueError("Mallen innehåller platshållare som inte kunde fyllas.")
    return html


def page_html() -> str:
    return _assemble_cached(_signature())


def data_zip() -> bytes:
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        for name in DATAFILER:
            z.write(ROOT / name, name)
    return buf.getvalue()


def main() -> None:
    import streamlit as st
    import streamlit.components.v1 as components

    st.set_page_config(page_title="Klimatperspektiv · Malmö ÖP", page_icon="🗺️", layout="wide", initial_sidebar_state="collapsed")
    st.markdown("""<style>
[data-testid="stHeader"], [data-testid="stSidebar"], footer {display:none;}
.block-container {padding:0 !important;max-width:100% !important;}
[data-testid="stMainBlockContainer"] {padding:0 !important;}
iframe {border:0;}
.st-key-kp_rad {padding: 6px 16px 2px 16px; background: #f5f5ef;}
</style>""", unsafe_allow_html=True)
    try:
        html = page_html()
    except (OSError, ValueError, KeyError) as error:
        st.error("Klimatperspektiv kunde inte läsa underlaget. Kontrollera mapparna app/ och data/.")
        st.caption(str(error))
        return
    with st.container(key="kp_rad"):
        c1, c2, c3 = st.columns([3, 1, 1], vertical_alignment="center")
        c1.markdown("**Klimatperspektiv · Malmö_ÖP** – fem kartlager för översiktsplaneringen. Beräkningen körs i din webbläsare.")
        c2.download_button("Underlag · ZIP", data_zip(), "klimatperspektiv_underlag.zip", "application/zip", use_container_width=True)
        c3.download_button("Fristående sida · HTML", html.encode("utf-8"), "klimatperspektiv_malmo.html", "text/html", use_container_width=True,
                           help="Hela modellen i en fil. Öppnas i webbläsaren utan internet (bakgrundskartan kräver internet).")
    components.html(html, height=1080, scrolling=True)


if __name__ == "__main__":
    main()
