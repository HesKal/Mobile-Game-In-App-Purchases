# Data Dictionary: Mobile Game Player Spending Segmentation

**Project Title:** Mobile Game Player Spending Segmentation (CDS 4003)  
**Dataset Filename:** `02_expanded_dirty_data.csv`  
**Total Records:** 250,000 rows  
**Total Features:** 23 columns  

---

## Overview
This document provides a comprehensive description of all features (columns) included in the expanded and dirty dataset (`02_expanded_dirty_data.csv`). It defines each attribute's data type, business meaning, and expected values prior to and after the data cleaning pipeline.

---

## Column Definitions Table

| No. | Column Name | Data Type (Dirty) | Description / Business Definition | Expected Values / Categories / Range |
| :--- | :--- | :--- | :--- | :--- |
| **1** | `UserID` | String / Object | Unique identification code assigned to each individual player. | Alphanumeric GUID format (e.g., `c9889ab0-...`) |
| **2** | `Age` | Float | The age of the player in years (includes injected negative and extreme outliers). | Numeric range (e.g., 13 to 60+, with intentional dirty outliers like `-5` or `150`) |
| **3** | `Gender` | String / Object | The self reported gender of the player (contains inconsistent text formatting and missing values). | `Male`, `Female`, `Other`, or variations (e.g., `m`, `fem`) |
| **4** | `Country` | String / Object | The country where the player is located (contains typographical errors and missing values). | Country names (e.g., `India`, `USA`, `U.S.A.`, `Switzerland`) |
| **5** | `Device` | String / Object | The mobile platform or operating system used by the player. | `iOS`, `Android` |
| **6** | `GameGenre` | String / Object | The primary category or genre of the mobile game. | `RPG`, `Strategy`, `Puzzle`, `Action RPG`, `Sandbox` |
| **7** | `SessionCount` | Float | Total number of gameplay sessions initiated by the player. | Positive integers (with injected negative outliers like `-10`) |
| **8** | `AverageSessionLength` | String / Object | The average duration of a gameplay session in minutes (includes data type inconsistencies). | Numeric values or contaminated strings (e.g., `15.5`, `"Unknown"`, `"Error"`) |
| **9** | `SpendingSegment` | String / Object | **[Target Variable]** The player monetization tier used for segmentation. | `Whale` (high spender), `Dolphin` (medium spender), `Minnow` (low/non spender) |
| **10** | `InAppPurchaseAmount` | String / Object | Total monetary value spent by the player on in-app purchases (in USD). | Numeric amounts (may include embedded currency symbols like `'$'`) |
| **11** | `FirstPurchaseDaysAfterInstall` | Float | Number of days that passed between account creation and the player's first purchase. | Non-negative numeric value (days) |
| **12** | `PaymentMethod` | String / Object | The primary payment gateway or method utilized for transactions. | `Credit Card`, `PayPal`, `Apple Pay`, `Google Pay`, `Gift Card` |
| **13** | `LastPurchaseDate` | String / Object | The exact date of the player's most recent in-app purchase transaction (mixed date formats). | Dates in various formats (e.g., `DD/MM/YYYY`, `MM-DD-YYYY`) |
| **14** | `AcquisitionChannel` | String / Object | The marketing channel or traffic source through which the player discovered the game. | `Organic`, `Paid Social`, `Search Ads`, `Cross-promotion` |
| **15** | `InstallDate` | String / Object | The date when the game application was first installed on the device. | Date format (may include future date anomalies prior to cleaning) |
| **16** | `ActiveDays30d` | Float | Number of active days logged by the player within a 30-day window. | Range: 0 to 30 |
| **17** | `PlayerLevel30d` | Float | The character or account progression level reached within 30 days. | Positive integer |
| **18** | `AdsWatched30d` | Float | Total number of rewarded or interstitial advertisements watched in 30 days. | Non-negative integer |
| **19** | `SocialActions30d` | Float | Count of social interactions, guild chats, or friend invites performed in 30 days. | Non-negative integer |
| **20** | `GuildMember` | String / Object | Indicator of whether the player is an active member of an in-game guild or clan. | `Yes`, `No` (or boolean equivalent) |
| **21** | `PushNotificationsOptIn` | String / Object | Player consent status for receiving push notifications from the app. | `Yes`, `No` |
| **22** | `PurchaseCount30d` | Float | Total frequency of in-app purchase transactions made within the last 30 days. | Non-negative integer |
| **23** | `WinRate` | Float | The ratio of successful matches or levels won compared to total matches played. | Float value between `0.0` and `1.0` |

---

## Data Quality Notes & Cleaning Rules
- **Missing Values (`NaNs`):** Addressed via median imputation for numerical features and `'Unknown'` labeling for categorical features.
- **Duplicates:** Exactly 2,500 duplicate rows were identified and removed during Stage 3 data cleaning.
- **Outliers:** Negative ages and session counts were corrected using absolute values or bounds filtering.
