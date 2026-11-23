# NovaPlay Player Segment Studio

A Streamlit demo that accepts six player-profile/gameplay inputs and predicts `Minnow`, `Dolphin`, or `Whale` using the project's selected Gini Decision Tree. It includes class scores, global feature importance, a segment-based promotional idea to test, and the team's reported model metrics. It explicitly cautions that segment prediction does not prove campaign revenue impact.

## Files to add to the project repository

Place these files in the repository root (or choose the app folder in Streamlit settings):

- `app.py` — Streamlit interface.
- `model.joblib` — trained preprocessing + Decision Tree pipeline loaded by the app.
- `requirements.txt` — pinned runtime dependencies.

`train_model.py` is included to reproduce `model.joblib` from the team's cleaned CSV. The dataset is not needed by the running app once the model artifact has been committed.

## Rebuild the model artifact

Use Python 3.11 or 3.12 in an environment compatible with `requirements.txt`:

```bash
pip install -r requirements.txt
python train_model.py /path/to/mobile_game_players_eda_features.csv
```

This refits the selected Gini Decision Tree pipeline on all eligible project records after the model-comparison exercise. It uses only the six predictors listed in the report and excludes the target, identifier, direct spending amounts, and generated helper fields.

## Deploy using Streamlit Community Cloud

1. Push `app.py`, `model.joblib`, and `requirements.txt` to the team's GitHub repository.
2. Sign in to Streamlit Community Cloud using the GitHub account that has access to that repository.
3. Choose **Create app** (or **New app**), select the repository, branch (usually `main`), and main file path `app.py`.
4. Choose **Deploy**. The app is public when deployed with public visibility; confirm the intended visibility before sharing the link.

## If the repository does not appear

- Confirm the GitHub account connected to Streamlit is the account that was invited to the team's repository.
- The repository owner should add the deploying account as a repository collaborator (or grant it access through the organization's team). Accept the GitHub invitation.
- If the repository belongs to a GitHub organization, the organization may need to approve Streamlit Community Cloud's GitHub OAuth/app access. Ask the organization owner/admin to review the app's access to organization repositories.
- Refresh or reconnect the GitHub authorization in Streamlit settings after access is granted, then try creating the app again.
- If the team repository is private, ensure the selected GitHub identity has permission to view it and the Streamlit authorization includes that repository.

A classmate who owns the repository can also deploy it from their own Streamlit account and share the app URL with the team. For changes made by another teammate, that person still needs appropriate write permission to push code to the repository.

## User-facing interpretation

The app is an academic demonstration based on generated/expanded project data. Model scores are not calibrated promises of future spending. Promotion ideas are hypotheses for an experiment, not proven recommendations. Any real campaign should be evaluated against a holdout group using incremental in-app-purchase revenue, contribution margin, conversion, and player retention.
