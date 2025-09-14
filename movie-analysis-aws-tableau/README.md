# 🎬 Movie Analysis Using AWS & Tableau

This project analyzes a large movie dataset using cloud technologies provided by **Amazon Web Services (AWS)** and visualizes the insights using **Tableau**.

---

## 📌 Objective

To demonstrate how cloud tools can be used for **data storage, transformation, querying, and visualization** using a real-world dataset of 45,000+ movies from Kaggle.

---

## ⚙️ Tools & Technologies Used

- **AWS S3**: Storage for raw and transformed data.
- **AWS Glue**: Data cleaning and transformation using serverless ETL.
- **AWS IAM**: Role and permission management.
- **AWS Athena**: Serverless querying of transformed data.
- **Tableau**: Data visualization (connected to Athena).
- **PySpark**: Used in Glue scripts for transformations.

---

## 📂 Dataset

The dataset used is from [Kaggle - The Movies Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?select=movies_metadata.csv).  
The primary file used: `movies_metadata.csv`

---

## 🛠️ Methodology

### 1. **Data Acquisition and Storage**
- Dataset stored in **Amazon S3** in the `us-east-1` region.
- Created a folder `/datasets` inside the bucket to hold raw data.

### 2. **Data Transformation**
- Created **IAM Role** with necessary policies.
- Developed a **Glue Job** using PySpark.
- Performed data cleaning, type casting, JSON normalization, and saved output in **Parquet** format.
- Transformed data saved back to **S3** and registered in **AWS Glue Data Catalog**.

### 3. **Data Querying**
- Used **Amazon Athena** to query the Parquet data using standard SQL.
- Results saved to a staging directory in S3.

### 4. **Visualization**
- Connected **Tableau** to Athena using region-specific configuration and secret keys.
- Built interactive dashboards and graphs for insights such as:
  - Revenue trends
  - Average ratings by genre
  - Year-wise release patterns

---

## 📊 Sample Visualizations


- Open **`images`**  
  ➤ images folder contains all the aws related  content in images and visualizations

---



## 🔍 Key Findings

- **Budget vs Revenue trends** show nonlinear growth.
- **Genres like Drama and Action** are most frequent.
- **Release month** significantly affects success metrics.

---

## 🚀 Future Work

- Add **sentiment analysis** from movie reviews.
- Incorporate **machine learning models** for prediction.
- Use **Amazon QuickSight** as an alternative to Tableau.

---

## 🗂️ Project Structure

```bash
C:.
├───data
├───images
└───notebooks
```
---

## 📁 Project Files

- `movie_analysis.ipynb` – PySpark code for transformation.
- `Project.twb` – Tableau workbook.
- `/images` – AWS screenshots for better understanding.

---

## 📚 References

- [Kaggle Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset)
- [AWS Glue Docs](https://docs.aws.amazon.com/glue/)
- [Tableau Docs](https://help.tableau.com/)

---

> This project demonstrates how cloud computing and visualization tools can simplify the process of big data analysis in real-world applications like movie analytics.
