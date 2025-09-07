
# Ischemic Stroke Risk Prediction (Streamlit App)

A lightweight Streamlit web application that estimates **ischemic stroke risk** from basic clinical and lifestyle features using a different machine learning algorithms e.i RandomForest and LGB ensemble models. I compared dofferent models metrics for superiority.

> ⚠️ **Medical Disclaimer**  
> This tool is for **educational and research purposes only** and **must not** be used for diagnosis or treatment decisions. Always consult qualified clinicians for medical advice.

---

## ✨ Features

- Simple, guided **Streamlit UI** for entering patient attributes.
- Loads a **pre-trained classifier** (serialized with pickle) and returns one of three risk levels: **Low**, **Moderate**, or **High**.
- All inputs are **categorical or discretized**, reducing dependency on raw numeric scales.
- Ready to deploy locally or to Streamlit Community Cloud / any Python hosting that supports Streamlit.

---

## 🗂️ Repository Structure (recommended)

```
.
├── app/
│   └── predictiveAPP.py        # Streamlit app
├── models/
│   └── stk-mod.sav             # Pre-trained model (not tracked by default)
├── notebooks/
│   └── strokegid.ipynb         # Training / exploration (optional)
├── requirements.txt
└── README.md
```

> Place your trained model at `models/stk-mod.sav`. Adjust the path in `predictiveAPP.py` accordingly (see **Configuration** below).

---

## 🚀 Quickstart

### 1) Prerequisites
- Python **3.10+** (recommended)
- pip

### 2) Create & activate a virtual environment
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### 3) Install dependencies
Create a `requirements.txt` (sample below) and install:
```bash
pip install -r requirements.txt
```

**Sample `requirements.txt`:**
```
streamlit>=1.36
numpy>=1.26
scikit-learn==1.3.2   # pin to version used during training for pickle compatibility
```

> Pinning scikit-learn is important because pickle files are **not guaranteed** to be forward/backward compatible across versions.

### 4) Add the trained model
Copy your trained model file to:
```
models/stk-mod.sav
```

### 5) Run the app
```bash
streamlit run app/predictiveAPP.py
```

Open the URL shown in your terminal (usually `http://localhost:8501`).

---

## ⚙️ Configuration

Update the model path in `predictiveAPP.py` to a **relative, repo-friendly** location:

```python
from pathlib import Path
import pickle

MODEL_PATH = Path(__file__).resolve().parents[1] / "models" / "stk-mod.sav"
with open(MODEL_PATH, "rb") as f:
    lomodel = pickle.load(f)
```

> Avoid hard‑coded absolute paths (e.g., `C:/Users/...`) so the app runs on any machine or CI/CD environment.

---

## 🧠 Model & Prediction

- The app loads a pre-trained model from `stk-mod.sav` via `pickle` and calls `.predict()` on a single **row vector** shaped `(1, n_features)`.
- The output class is mapped to one of three messages:
  - `0 → "low risk"`
  - `1 → "moderate risk"`
  - `2 → "high risk"`

If you plan to re-train:
1. Use the notebook in `notebooks/strokegid.ipynb` (or your own pipeline).
2. Export the fitted estimator as `stk-mod.sav` using `pickle` or `joblib`.
3. Keep scikit-learn versions aligned during save/load.

**Security Note:** Only load pickle files **you trust**. Pickle can execute arbitrary code on load.

---

## 🧾 Input Schema (UI Encodings)

The app expects 15 features in the exact order below (encoded as numeric categories from the UI controls).

| # | Feature            | Allowed Values (UI → Encoded) |
|---|--------------------|--------------------------------|
| 1 | Gender             | Male → `1`, Female → `2` |
| 2 | Age bucket         | `0` (20–29), `1` (30–39), `2` (40–59), `3` (60+) |
| 3 | Heart disease      | No → `0`, Yes → `1` |
| 4 | Work type          | Never_work → `0`, Former_worker → `1`, Private → `2`, Public → `3` |
| 5 | Smoking status     | Never_Smoked → `0`, Formerly_smoke → `1`, Stay_around_smokers → `2`, Currently_Smoking → `3` |
| 6 | Systolic (bucket)  | 120–129 → `0`, 130–139 → `0.181818`, 140–149 → `0.363636`, 180 → `1` |
| 7 | Diastolic (bucket) | 120–129 → `0.81818182`, 130–139 → `0.727273`, 140–149 → `0.545455`, 180 → `0.09090909` |
| 8 | Diabetes           | Diabetes → `0`, Type_1 → `1`, Prediabetes → `2`, Type_2 → `3` |
| 9 | Family history     | No → `0`, Yes → `1` |
|10 | Alcohol use        | Never → `0`, Moderate → `1`, Binge → `2`, Heavy → `3` |
|11 | BMI (bucket)       | <18.5 → `0`, 18.5–24.9 → `0.278261`, 25–29.9 → `0.56087`, ≥30 → `1` |
|12 | High cholesterol   | 20 mg/dL → `1.909090909`, <100 mg/dL → `0.454545455`, 100–129 mg/dL → `0.181818182`, ≥130 mg/dL → `0.090909091` |
|13 | Avg glucose level  | 1–4.9% → `0`, 5–5.6% → `0.727273`, 5.7–6.4% → `0.927273`, ≥6.5% → `1` |
|14 | Sleep apnea type   | Never → `0`, Obstructive → `1`, Central → `2`, Mixed/Complex → `3` |
|15 | Other risk         | Vision problem → `0`, Numbness (one side) → `1`, Weakness (one side) → `2`, Paralysis (one side) → `3` |

> Make sure your **training pipeline** uses the exact same encodings and feature order.

---

## 🧪 Reproducibility (Optional)

If you want full training reproducibility:
1. Add a `training` folder with scripts that:
   - Load and clean the dataset
   - Apply the exact bucketing/encodings used in the UI
   - Train the classifier
   - Persist the model to `models/stk-mod.sav`
2. Log versions and random seeds in the notebook.
3. Export evaluation metrics (ROC-AUC, precision/recall, confusion matrix) to `reports/`.

---

## 🛡️ Privacy & Ethics

- Do not log or store personally identifiable information (PII).
- Be explicit about intended use (education/research).
- Include a consent statement if used with real people.
- Clearly communicate model limitations and potential biases.

---

## 🧭 Roadmap

- [ ] Replace magic numbers with config (`yaml/json`), and validate inputs.
- [ ] Add unit tests for mapping logic & model I/O.
- [ ] Support probability outputs and calibrated thresholds.
- [ ] Add CI (linting, tests) and GitHub Actions.
- [ ] Containerize with Docker for consistent deploys.

---

## 🤝 Contributing

Pull requests are welcome! Please open an issue to discuss significant changes.

---

## 📄 License

Specify a license (e.g., MIT, Apache-2.0) to clarify usage and contributions.

---

## 🙏 Acknowledgments

- Open-source community around Streamlit and scikit-learn.
- Any datasets or publications used to build the model (cite here).

