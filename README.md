# Henrique Duarte — Personal CV / R&D Website

A complete Streamlit website inspired by modern AI/automation agency templates.

This fixed version renders the full page inside a Streamlit HTML component, so the HTML is interpreted correctly and will not appear as raw text on the page.

## Run locally

### Mac / Linux

```bash
cd henriqueduarte_conicorn_fixed_site
./run_localhost.sh
```

### Windows

```bat
cd henriqueduarte_conicorn_fixed_site
run_localhost.bat
```

### Manual

```bash
pip install -r requirements.txt
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

## Edit content

Open `app.py` and edit:

- `NAME`
- `EMAIL`
- `LINKEDIN`
- Text inside the HTML sections

## Assets

Images and the CV PDF are inside `assets/`.

Before publishing publicly, review the PDF to ensure you are comfortable with the personal information included in it.
