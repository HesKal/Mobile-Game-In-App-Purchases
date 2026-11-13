<div align="center">

# 🎮 Mobile Game Player Spending Segmentation

### Player Intelligence · CDS4003 Data Science Project

<img width="2688" height="1152" alt="player_segmentation_hero" src="https://github.com/user-attachments/assets/3936ddc0-1a28-41b4-8559-cef9934d80bd" />

### Turning player-behaviour data into smarter, more timely engagement

![Predictive Analytics](https://img.shields.io/badge/ANALYTICS-PREDICTIVE%20ANALYTICS-6D28D9?style=for-the-badge)
![Classification](https://img.shields.io/badge/ML%20TASK-MULTI--CLASS%20CLASSIFICATION-0891B2?style=for-the-badge)
![Project Status](https://img.shields.io/badge/STATUS-IN%20PROGRESS-16A34A?style=for-the-badge)


**A group data-science project exploring how mobile-game players can be segmented into Minnows, Dolphins, and Whales to support more relevant player engagement.**

[Project Overview](#about-the-project) · [Dataset](#dataset) · [Workflow](#project-workflow) · [Repository](#repository-structure) · [Progress](#progress)

</div>

---

## About the project
Mobile-game teams need to understand differences in player spending so they can make better-informed decisions about player engagement and monetization. This project studies three spending segments—**Minnow**, **Dolphin**, and **Whale**—using player and gameplay information.

### Business question

> Can player and gameplay characteristics help identify a player's spending segment early enough to support a relevant engagement decision?

**Data-science question:** Can we classify a new player's spending segment—Whale, Dolphin, or Minnow—using demographic profile and early gameplay behaviour?
**Proposed model success measures:** Macro F1-score and per-class recall (especially Whale recall), with a confusion matrix. The business target of a 15% revenue lift is separate and must not be claimed from classification metrics alone.

### Intended business value



## Project status
**Current status: Stages 1–3 in progress.** The team is preparing the business problem, documenting the dataset and its provenance, and reviewing data-quality issues. The proposed objective is under validation. Modeling, final recommendations, and deployment have not yet been completed.



## Project data

The project starts with a Kaggle dataset and documents the team's expansion separately. The additional rows are **synthetic**, not new observations from Kaggle.

| | Dataset | Details |
|---|---|---|
| **01 · Original** | [Open the original CSV](data/01_original_kaggle_data.csv) | The source file reviewed: **3,024 rows · 13 columns**. [View the Kaggle source](https://www.kaggle.com/datasets/pratyushpuri/mobile-game-in-app-purchases-dataset-2025). |
| **02 · Expanded** | [Download the expanded dataset](data/02_expanded_dirty_data.zip) | **250,000 rows · 23 columns**, including generated records and documented data-quality issues for the cleaning exercise. |

The Kaggle listing describes its dataset as synthetic. The original source and the team's added synthetic data are kept distinct throughout the project.


# project-workflow

### 1- Data-quality work
- [02 — Data cleaning](notebooks/02_data_cleaning.ipynb)

### 2-  Feature engineering 


### 3-  Classification model development and comparison 

### 4-  Model evaluation and interpretation 


### 5-  Model evaluation and interpretation 



## Visuals & results

**Results will be added after data cleaning, exploratory analysis, model comparison, and evaluation have been completed.** No model performance or business impact is claimed at this stage.

| Item | Result |
|---|---|
| Final cleaned dataset size | To be reported after cleaning |
| Target definition and prediction time | To be confirmed with instructor |
| Models compared | To be completed |
| Evaluation metrics and results | To be completed |
| Streamlit app | To be deployed |

## Team

| Member | Student ID / GitHub username | Main responsibility |
|---|---|---|
| [Hessa Khalfan] | [H00535166 - [@HesKal](https://github.com/HesKal) ] | [Responsibility] |
| [Nourah Abdulla] | [H00535834 - [@NourahAlghfeli](https://github.com/NourahAlghfeli)] | [Responsibility] |
| [Maryam Ali Bin Hamdah] | [H00535836 - [@MaryamBinHamdah](https://github.com/MaryamBinHamdah)] | [Responsibility] |


## License & attribution

The team's original code is licensed under the [MIT License](LICENSE). The Kaggle dataset and any other third-party materials remain subject to their own license and terms.

<div align="center">

*Built by the CDS4003 project team · Work in progress*

</div>

