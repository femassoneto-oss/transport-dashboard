# Transport Dashboard

## Overview
This project reads the Excel workbook `Z:\1. Biomassa & Nutrição Animal\BRUNA - Copia\ANTIGRAVITY\data(51).xlsx` and builds an interactive **executive dashboard** for logistics operations.

- **Metrics**: total plates, plates per operation, unique plates per client, March‑only plates, shared plates, revenue, fleet productivity, plate ranking, growth, top clients.
- **Insights**: automatic anomaly detection (revenue drops, productivity outliers, missing plates).
- **Visuals**: modern Plotly charts embedded in Streamlit, dark theme, smooth hover effects.

## Folder Structure
```
transport_dashboard/
├─ requirements.txt      # Python dependencies
├─ analysis.py           # Data loading & metric calculation
├─ dashboard.py          # Streamlit UI
├─ utils.py              # Helper functions (optional)
└─ README.md (this file)
```

## Quick Start
1. Open a terminal in this folder.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the dashboard:
   ```
   streamlit run dashboard.py
   ```

The app will load the Excel file from the network drive, compute all KPIs, and display them.

## Customisation
- If the Excel sheet has a different name, edit `analysis.SHEET_NAME` in `analysis.py`.
- If column names differ, adjust the mapping dictionary `COLUMN_MAP` in `analysis.py`.
- Change the visual theme by editing `st.set_page_config` in `dashboard.py`.

---
*Created by Antigravity AI*
