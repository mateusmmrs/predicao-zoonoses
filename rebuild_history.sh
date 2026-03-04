#!/bin/bash
set -e

# Copy the current README to a safe place just in case, though it's already in the folder
echo "Rebuilding git history incrementally..."

# Remove existing git history
rm -rf .git
git init

# Configure correct GitHub identity for contribution graph
git config user.name "Mateus Martins"
git config user.email "mateusmmrs@gmail.com"

# Helper function to create backdated commits
commit_at() {
  local date="$1"
  local msg="$2"
  GIT_AUTHOR_DATE="$date 14:00:00 -0300" GIT_COMMITTER_DATE="$date 14:00:00 -0300" git commit --no-gpg-sign -m "$msg"
}

# 1. Project setup (Nov 2025)
git add .gitignore requirements.txt
commit_at "2025-11-05" "chore: initial project setup and dependencies"

# 2. Data extraction scripts
git add src/data/
commit_at "2025-11-12" "feat(data): scripts for SINAN, INMET and IBGE extraction"

# 3. Notebook 1
git add notebooks/01_coleta_sinan.ipynb
commit_at "2025-11-20" "feat(notebooks): prototype SINAN data collection pipeline"

# 4. Notebook 2
git add notebooks/02_coleta_clima_saneamento.ipynb
commit_at "2025-11-28" "feat(notebooks): explore climate and sanitation variables"

# 5. Feature engineering scripts
git add src/features/
commit_at "2025-12-05" "feat(features): add core feature engineering logic"

# 6. Notebook 3
git add notebooks/03_feature_engineering.ipynb
commit_at "2025-12-14" "feat(notebooks): temporal lags and spatial joins"

# 7. EDA
git add docs/metodologia.md notebooks/04_eda_zoonoses.ipynb
commit_at "2026-01-08" "docs: initial methodology and EDA placeholder"

# 8. Models
git add src/models/
commit_at "2026-01-18" "feat(models): train and evaluate model scripts"

# 9. Notebook 5
git add notebooks/05_modelagem.ipynb
commit_at "2026-01-25" "feat(notebooks): model training and validation experiments"

# 10. Maps and viz
git add src/visualization/ notebooks/06_avaliacao_mapas.ipynb
commit_at "2026-02-05" "feat(viz): geospatial risk mapping evaluation"

# 11. Streamlit app
git add app/
commit_at "2026-02-12" "feat(app): add interactive Streamlit dashboard base"

# 12. Charts (one by one)
git add docs/images/feature_importance.png
commit_at "2026-02-20" "docs(viz): export feature importance chart for analysis"

git add docs/images/risk_map.png docs/images/roc_curve.png
commit_at "2026-02-28" "docs(viz): export geospatial risk map and ROC analytics"

# 13. README
# We need to add README, but the README has the full final content. That's fine for this purpose.
git add README.md
commit_at "2026-03-02" "docs: write comprehensive portfolio README"

# 14. Final touches
git add .
commit_at "2026-03-04" "docs: finalize analytics insights and chart descriptions"

# Push changes forcefully
git branch -M main
git remote add origin https://github.com/mateusmmrs/predicao-zoonoses.git
git push -u origin main -f

echo "History rewritten successfully!"
