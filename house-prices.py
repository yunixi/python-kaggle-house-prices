{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "65기_김지윤.ipynb",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/yunixi/python-kaggle-house-prices/blob/main/house-prices.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "3pOSJly9LZHU"
      },
      "source": [
        "# 1. 데이터 수집\n",
        "\n",
        "1) train.csv 파일 읽기\n",
        "\n",
        "2) 전체 데이터 중 내 담당인 칼럼들만 수집하기"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ymB1ep1pJiXd"
      },
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "\n",
        "houseData = pd.read_csv(\"/content/train.csv\")"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 247
        },
        "id": "OyJTnP0zJyfM",
        "outputId": "7f899260-8d32-4d1f-aa67-09e7ab2b41b2"
      },
      "source": [
        "houseData.head(5)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Id</th>\n",
              "      <th>MSSubClass</th>\n",
              "      <th>MSZoning</th>\n",
              "      <th>LotFrontage</th>\n",
              "      <th>LotArea</th>\n",
              "      <th>Street</th>\n",
              "      <th>Alley</th>\n",
              "      <th>LotShape</th>\n",
              "      <th>LandContour</th>\n",
              "      <th>Utilities</th>\n",
              "      <th>LotConfig</th>\n",
              "      <th>LandSlope</th>\n",
              "      <th>Neighborhood</th>\n",
              "      <th>Condition1</th>\n",
              "      <th>Condition2</th>\n",
              "      <th>BldgType</th>\n",
              "      <th>HouseStyle</th>\n",
              "      <th>OverallQual</th>\n",
              "      <th>OverallCond</th>\n",
              "      <th>YearBuilt</th>\n",
              "      <th>YearRemodAdd</th>\n",
              "      <th>RoofStyle</th>\n",
              "      <th>RoofMatl</th>\n",
              "      <th>Exterior1st</th>\n",
              "      <th>Exterior2nd</th>\n",
              "      <th>MasVnrType</th>\n",
              "      <th>MasVnrArea</th>\n",
              "      <th>ExterQual</th>\n",
              "      <th>ExterCond</th>\n",
              "      <th>Foundation</th>\n",
              "      <th>BsmtQual</th>\n",
              "      <th>BsmtCond</th>\n",
              "      <th>BsmtExposure</th>\n",
              "      <th>BsmtFinType1</th>\n",
              "      <th>BsmtFinSF1</th>\n",
              "      <th>BsmtFinType2</th>\n",
              "      <th>BsmtFinSF2</th>\n",
              "      <th>BsmtUnfSF</th>\n",
              "      <th>TotalBsmtSF</th>\n",
              "      <th>Heating</th>\n",
              "      <th>...</th>\n",
              "      <th>CentralAir</th>\n",
              "      <th>Electrical</th>\n",
              "      <th>1stFlrSF</th>\n",
              "      <th>2ndFlrSF</th>\n",
              "      <th>LowQualFinSF</th>\n",
              "      <th>GrLivArea</th>\n",
              "      <th>BsmtFullBath</th>\n",
              "      <th>BsmtHalfBath</th>\n",
              "      <th>FullBath</th>\n",
              "      <th>HalfBath</th>\n",
              "      <th>BedroomAbvGr</th>\n",
              "      <th>KitchenAbvGr</th>\n",
              "      <th>KitchenQual</th>\n",
              "      <th>TotRmsAbvGrd</th>\n",
              "      <th>Functional</th>\n",
              "      <th>Fireplaces</th>\n",
              "      <th>FireplaceQu</th>\n",
              "      <th>GarageType</th>\n",
              "      <th>GarageYrBlt</th>\n",
              "      <th>GarageFinish</th>\n",
              "      <th>GarageCars</th>\n",
              "      <th>GarageArea</th>\n",
              "      <th>GarageQual</th>\n",
              "      <th>GarageCond</th>\n",
              "      <th>PavedDrive</th>\n",
              "      <th>WoodDeckSF</th>\n",
              "      <th>OpenPorchSF</th>\n",
              "      <th>EnclosedPorch</th>\n",
              "      <th>3SsnPorch</th>\n",
              "      <th>ScreenPorch</th>\n",
              "      <th>PoolArea</th>\n",
              "      <th>PoolQC</th>\n",
              "      <th>Fence</th>\n",
              "      <th>MiscFeature</th>\n",
              "      <th>MiscVal</th>\n",
              "      <th>MoSold</th>\n",
              "      <th>YrSold</th>\n",
              "      <th>SaleType</th>\n",
              "      <th>SaleCondition</th>\n",
              "      <th>SalePrice</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>60</td>\n",
              "      <td>RL</td>\n",
              "      <td>65.0</td>\n",
              "      <td>8450</td>\n",
              "      <td>Pave</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Reg</td>\n",
              "      <td>Lvl</td>\n",
              "      <td>AllPub</td>\n",
              "      <td>Inside</td>\n",
              "      <td>Gtl</td>\n",
              "      <td>CollgCr</td>\n",
              "      <td>Norm</td>\n",
              "      <td>Norm</td>\n",
              "      <td>1Fam</td>\n",
              "      <td>2Story</td>\n",
              "      <td>7</td>\n",
              "      <td>5</td>\n",
              "      <td>2003</td>\n",
              "      <td>2003</td>\n",
              "      <td>Gable</td>\n",
              "      <td>CompShg</td>\n",
              "      <td>VinylSd</td>\n",
              "      <td>VinylSd</td>\n",
              "      <td>BrkFace</td>\n",
              "      <td>196.0</td>\n",
              "      <td>Gd</td>\n",
              "      <td>TA</td>\n",
              "      <td>PConc</td>\n",
              "      <td>Gd</td>\n",
              "      <td>TA</td>\n",
              "      <td>No</td>\n",
              "      <td>GLQ</td>\n",
              "      <td>706</td>\n",
              "      <td>Unf</td>\n",
              "      <td>0</td>\n",
              "      <td>150</td>\n",
              "      <td>856</td>\n",
              "      <td>GasA</td>\n",
              "      <td>...</td>\n",
              "      <td>Y</td>\n",
              "      <td>SBrkr</td>\n",
              "      <td>856</td>\n",
              "      <td>854</td>\n",
              "      <td>0</td>\n",
              "      <td>1710</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>1</td>\n",
              "      <td>Gd</td>\n",
              "      <td>8</td>\n",
              "      <td>Typ</td>\n",
              "      <td>0</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Attchd</td>\n",
              "      <td>2003.0</td>\n",
              "      <td>RFn</td>\n",
              "      <td>2</td>\n",
              "      <td>548</td>\n",
              "      <td>TA</td>\n",
              "      <td>TA</td>\n",
              "      <td>Y</td>\n",
              "      <td>0</td>\n",
              "      <td>61</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>2008</td>\n",
              "      <td>WD</td>\n",
              "      <td>Normal</td>\n",
              "      <td>208500</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>20</td>\n",
              "      <td>RL</td>\n",
              "      <td>80.0</td>\n",
              "      <td>9600</td>\n",
              "      <td>Pave</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Reg</td>\n",
              "      <td>Lvl</td>\n",
              "      <td>AllPub</td>\n",
              "      <td>FR2</td>\n",
              "      <td>Gtl</td>\n",
              "      <td>Veenker</td>\n",
              "      <td>Feedr</td>\n",
              "      <td>Norm</td>\n",
              "      <td>1Fam</td>\n",
              "      <td>1Story</td>\n",
              "      <td>6</td>\n",
              "      <td>8</td>\n",
              "      <td>1976</td>\n",
              "      <td>1976</td>\n",
              "      <td>Gable</td>\n",
              "      <td>CompShg</td>\n",
              "      <td>MetalSd</td>\n",
              "      <td>MetalSd</td>\n",
              "      <td>None</td>\n",
              "      <td>0.0</td>\n",
              "      <td>TA</td>\n",
              "      <td>TA</td>\n",
              "      <td>CBlock</td>\n",
              "      <td>Gd</td>\n",
              "      <td>TA</td>\n",
              "      <td>Gd</td>\n",
              "      <td>ALQ</td>\n",
              "      <td>978</td>\n",
              "      <td>Unf</td>\n",
              "      <td>0</td>\n",
              "      <td>284</td>\n",
              "      <td>1262</td>\n",
              "      <td>GasA</td>\n",
              "      <td>...</td>\n",
              "      <td>Y</td>\n",
              "      <td>SBrkr</td>\n",
              "      <td>1262</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1262</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>1</td>\n",
              "      <td>TA</td>\n",
              "      <td>6</td>\n",
              "      <td>Typ</td>\n",
              "      <td>1</td>\n",
              "      <td>TA</td>\n",
              "      <td>Attchd</td>\n",
              "      <td>1976.0</td>\n",
              "      <td>RFn</td>\n",
              "      <td>2</td>\n",
              "      <td>460</td>\n",
              "      <td>TA</td>\n",
              "      <td>TA</td>\n",
              "      <td>Y</td>\n",
              "      <td>298</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>0</td>\n",
              "      <td>5</td>\n",
              "      <td>2007</td>\n",
              "      <td>WD</td>\n",
              "      <td>Normal</td>\n",
              "      <td>181500</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>60</td>\n",
              "      <td>RL</td>\n",
              "      <td>68.0</td>\n",
              "      <td>11250</td>\n",
              "      <td>Pave</td>\n",
              "      <td>NaN</td>\n",
              "      <td>IR1</td>\n",
              "      <td>Lvl</td>\n",
              "      <td>AllPub</td>\n",
              "      <td>Inside</td>\n",
              "      <td>Gtl</td>\n",
              "      <td>CollgCr</td>\n",
              "      <td>Norm</td>\n",
              "      <td>Norm</td>\n",
              "      <td>1Fam</td>\n",
              "      <td>2Story</td>\n",
              "      <td>7</td>\n",
              "      <td>5</td>\n",
              "      <td>2001</td>\n",
              "      <td>2002</td>\n",
              "      <td>Gable</td>\n",
              "      <td>CompShg</td>\n",
              "      <td>VinylSd</td>\n",
              "      <td>VinylSd</td>\n",
              "      <td>BrkFace</td>\n",
              "      <td>162.0</td>\n",
              "      <td>Gd</td>\n",
              "      <td>TA</td>\n",
              "      <td>PConc</td>\n",
              "      <td>Gd</td>\n",
              "      <td>TA</td>\n",
              "      <td>Mn</td>\n",
              "      <td>GLQ</td>\n",
              "      <td>486</td>\n",
              "      <td>Unf</td>\n",
              "      <td>0</td>\n",
              "      <td>434</td>\n",
              "      <td>920</td>\n",
              "      <td>GasA</td>\n",
              "      <td>...</td>\n",
              "      <td>Y</td>\n",
              "      <td>SBrkr</td>\n",
              "      <td>920</td>\n",
              "      <td>866</td>\n",
              "      <td>0</td>\n",
              "      <td>1786</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>1</td>\n",
              "      <td>Gd</td>\n",
              "      <td>6</td>\n",
              "      <td>Typ</td>\n",
              "      <td>1</td>\n",
              "      <td>TA</td>\n",
              "      <td>Attchd</td>\n",
              "      <td>2001.0</td>\n",
              "      <td>RFn</td>\n",
              "      <td>2</td>\n",
              "      <td>608</td>\n",
              "      <td>TA</td>\n",
              "      <td>TA</td>\n",
              "      <td>Y</td>\n",
              "      <td>0</td>\n",
              "      <td>42</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>0</td>\n",
              "      <td>9</td>\n",
              "      <td>2008</td>\n",
              "      <td>WD</td>\n",
              "      <td>Normal</td>\n",
              "      <td>223500</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>70</td>\n",
              "      <td>RL</td>\n",
              "      <td>60.0</td>\n",
              "      <td>9550</td>\n",
              "      <td>Pave</td>\n",
              "      <td>NaN</td>\n",
              "      <td>IR1</td>\n",
              "      <td>Lvl</td>\n",
              "      <td>AllPub</td>\n",
              "      <td>Corner</td>\n",
              "      <td>Gtl</td>\n",
              "      <td>Crawfor</td>\n",
              "      <td>Norm</td>\n",
              "      <td>Norm</td>\n",
              "      <td>1Fam</td>\n",
              "      <td>2Story</td>\n",
              "      <td>7</td>\n",
              "      <td>5</td>\n",
              "      <td>1915</td>\n",
              "      <td>1970</td>\n",
              "      <td>Gable</td>\n",
              "      <td>CompShg</td>\n",
              "      <td>Wd Sdng</td>\n",
              "      <td>Wd Shng</td>\n",
              "      <td>None</td>\n",
              "      <td>0.0</td>\n",
              "      <td>TA</td>\n",
              "      <td>TA</td>\n",
              "      <td>BrkTil</td>\n",
              "      <td>TA</td>\n",
              "      <td>Gd</td>\n",
              "      <td>No</td>\n",
              "      <td>ALQ</td>\n",
              "      <td>216</td>\n",
              "      <td>Unf</td>\n",
              "      <td>0</td>\n",
              "      <td>540</td>\n",
              "      <td>756</td>\n",
              "      <td>GasA</td>\n",
              "      <td>...</td>\n",
              "      <td>Y</td>\n",
              "      <td>SBrkr</td>\n",
              "      <td>961</td>\n",
              "      <td>756</td>\n",
              "      <td>0</td>\n",
              "      <td>1717</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>1</td>\n",
              "      <td>Gd</td>\n",
              "      <td>7</td>\n",
              "      <td>Typ</td>\n",
              "      <td>1</td>\n",
              "      <td>Gd</td>\n",
              "      <td>Detchd</td>\n",
              "      <td>1998.0</td>\n",
              "      <td>Unf</td>\n",
              "      <td>3</td>\n",
              "      <td>642</td>\n",
              "      <td>TA</td>\n",
              "      <td>TA</td>\n",
              "      <td>Y</td>\n",
              "      <td>0</td>\n",
              "      <td>35</td>\n",
              "      <td>272</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>2006</td>\n",
              "      <td>WD</td>\n",
              "      <td>Abnorml</td>\n",
              "      <td>140000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>60</td>\n",
              "      <td>RL</td>\n",
              "      <td>84.0</td>\n",
              "      <td>14260</td>\n",
              "      <td>Pave</td>\n",
              "      <td>NaN</td>\n",
              "      <td>IR1</td>\n",
              "      <td>Lvl</td>\n",
              "      <td>AllPub</td>\n",
              "      <td>FR2</td>\n",
              "      <td>Gtl</td>\n",
              "      <td>NoRidge</td>\n",
              "      <td>Norm</td>\n",
              "      <td>Norm</td>\n",
              "      <td>1Fam</td>\n",
              "      <td>2Story</td>\n",
              "      <td>8</td>\n",
              "      <td>5</td>\n",
              "      <td>2000</td>\n",
              "      <td>2000</td>\n",
              "      <td>Gable</td>\n",
              "      <td>CompShg</td>\n",
              "      <td>VinylSd</td>\n",
              "      <td>VinylSd</td>\n",
              "      <td>BrkFace</td>\n",
              "      <td>350.0</td>\n",
              "      <td>Gd</td>\n",
              "      <td>TA</td>\n",
              "      <td>PConc</td>\n",
              "      <td>Gd</td>\n",
              "      <td>TA</td>\n",
              "      <td>Av</td>\n",
              "      <td>GLQ</td>\n",
              "      <td>655</td>\n",
              "      <td>Unf</td>\n",
              "      <td>0</td>\n",
              "      <td>490</td>\n",
              "      <td>1145</td>\n",
              "      <td>GasA</td>\n",
              "      <td>...</td>\n",
              "      <td>Y</td>\n",
              "      <td>SBrkr</td>\n",
              "      <td>1145</td>\n",
              "      <td>1053</td>\n",
              "      <td>0</td>\n",
              "      <td>2198</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>Gd</td>\n",
              "      <td>9</td>\n",
              "      <td>Typ</td>\n",
              "      <td>1</td>\n",
              "      <td>TA</td>\n",
              "      <td>Attchd</td>\n",
              "      <td>2000.0</td>\n",
              "      <td>RFn</td>\n",
              "      <td>3</td>\n",
              "      <td>836</td>\n",
              "      <td>TA</td>\n",
              "      <td>TA</td>\n",
              "      <td>Y</td>\n",
              "      <td>192</td>\n",
              "      <td>84</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>0</td>\n",
              "      <td>12</td>\n",
              "      <td>2008</td>\n",
              "      <td>WD</td>\n",
              "      <td>Normal</td>\n",
              "      <td>250000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>5 rows × 81 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "   Id  MSSubClass MSZoning  ...  SaleType  SaleCondition SalePrice\n",
              "0   1          60       RL  ...        WD         Normal    208500\n",
              "1   2          20       RL  ...        WD         Normal    181500\n",
              "2   3          60       RL  ...        WD         Normal    223500\n",
              "3   4          70       RL  ...        WD        Abnorml    140000\n",
              "4   5          60       RL  ...        WD         Normal    250000\n",
              "\n",
              "[5 rows x 81 columns]"
            ]
          },
          "metadata": {},
          "execution_count": 2
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 287
        },
        "id": "2TL8ad2GJ4p8",
        "outputId": "f2cd28d8-177f-4201-be45-6b033625243b"
      },
      "source": [
        "#데이터 전처리로 부여한 12개의 칼럼에 대해서 별도의 DataFrame을 myColumn에 생성\n",
        "myColumn = houseData[['2ndFlrSF','LowQualFinSF','GrLivArea','BsmtFullBath','BsmtHalfBath', 'FullBath','HalfBath','KitchenQual','TotRmsAbvGrd','Functional', 'KitchenAbvGr', 'BedroomAbvGr']]\n",
        "\n",
        "#KitchenAbvGr → Kitchen, BedroomAbvGr → Bedroom\n",
        "myColumn.rename(columns = {'KitchenAbvGr':'Kitchen', 'BedroomAbvGr':'Bedroom'}, inplace=True)\n",
        "\n",
        "myColumn.head(5)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/pandas/core/frame.py:4308: SettingWithCopyWarning: \n",
            "A value is trying to be set on a copy of a slice from a DataFrame\n",
            "\n",
            "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
            "  errors=errors,\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>2ndFlrSF</th>\n",
              "      <th>LowQualFinSF</th>\n",
              "      <th>GrLivArea</th>\n",
              "      <th>BsmtFullBath</th>\n",
              "      <th>BsmtHalfBath</th>\n",
              "      <th>FullBath</th>\n",
              "      <th>HalfBath</th>\n",
              "      <th>KitchenQual</th>\n",
              "      <th>TotRmsAbvGrd</th>\n",
              "      <th>Functional</th>\n",
              "      <th>Kitchen</th>\n",
              "      <th>Bedroom</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>854</td>\n",
              "      <td>0</td>\n",
              "      <td>1710</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>Gd</td>\n",
              "      <td>8</td>\n",
              "      <td>Typ</td>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1262</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>TA</td>\n",
              "      <td>6</td>\n",
              "      <td>Typ</td>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>866</td>\n",
              "      <td>0</td>\n",
              "      <td>1786</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>Gd</td>\n",
              "      <td>6</td>\n",
              "      <td>Typ</td>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>756</td>\n",
              "      <td>0</td>\n",
              "      <td>1717</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>Gd</td>\n",
              "      <td>7</td>\n",
              "      <td>Typ</td>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>1053</td>\n",
              "      <td>0</td>\n",
              "      <td>2198</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>Gd</td>\n",
              "      <td>9</td>\n",
              "      <td>Typ</td>\n",
              "      <td>1</td>\n",
              "      <td>4</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   2ndFlrSF  LowQualFinSF  GrLivArea  ...  Functional  Kitchen  Bedroom\n",
              "0       854             0       1710  ...         Typ        1        3\n",
              "1         0             0       1262  ...         Typ        1        3\n",
              "2       866             0       1786  ...         Typ        1        3\n",
              "3       756             0       1717  ...         Typ        1        3\n",
              "4      1053             0       2198  ...         Typ        1        4\n",
              "\n",
              "[5 rows x 12 columns]"
            ]
          },
          "metadata": {},
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "RcHtIZC_LwEP"
      },
      "source": [
        "# 2. 데이터 전처리"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "zpTPxV0kD7j1"
      },
      "source": [
        "## 2-1 데이터 중간값, 평균값, 분산값 등 확인\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "c0VT6xiaD5TV",
        "outputId": "4e5ca6b4-2f12-4f40-ac63-5863e191da33"
      },
      "source": [
        "#myColumn에 대해서 중간값, 평균값, 분산값 구하기\n",
        "\n",
        "#평균값\n",
        "print(myColumn.mean())\n",
        "\n",
        "#분산값\n",
        "print(myColumn.var())\n",
        "\n",
        "#중간값\n",
        "print(myColumn.median())"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2ndFlrSF         346.992466\n",
            "LowQualFinSF       5.844521\n",
            "GrLivArea       1515.463699\n",
            "BsmtFullBath       0.425342\n",
            "BsmtHalfBath       0.057534\n",
            "FullBath           1.565068\n",
            "HalfBath           0.382877\n",
            "TotRmsAbvGrd       6.517808\n",
            "Kitchen            1.046575\n",
            "Bedroom            2.866438\n",
            "dtype: float64\n",
            "2ndFlrSF        190557.075337\n",
            "LowQualFinSF      2364.204048\n",
            "GrLivArea       276129.633363\n",
            "BsmtFullBath         0.269268\n",
            "BsmtHalfBath         0.057003\n",
            "FullBath             0.303508\n",
            "HalfBath             0.252894\n",
            "TotRmsAbvGrd         2.641903\n",
            "Kitchen              0.048549\n",
            "Bedroom              0.665494\n",
            "dtype: float64\n",
            "2ndFlrSF           0.0\n",
            "LowQualFinSF       0.0\n",
            "GrLivArea       1464.0\n",
            "BsmtFullBath       0.0\n",
            "BsmtHalfBath       0.0\n",
            "FullBath           2.0\n",
            "HalfBath           0.0\n",
            "TotRmsAbvGrd       6.0\n",
            "Kitchen            1.0\n",
            "Bedroom            3.0\n",
            "dtype: float64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 78
        },
        "id": "lR6yvbyhGRVm",
        "outputId": "1913e006-95b1-4b04-90e8-02587d1f794f"
      },
      "source": [
        "myColumn.mode()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>2ndFlrSF</th>\n",
              "      <th>LowQualFinSF</th>\n",
              "      <th>GrLivArea</th>\n",
              "      <th>BsmtFullBath</th>\n",
              "      <th>BsmtHalfBath</th>\n",
              "      <th>FullBath</th>\n",
              "      <th>HalfBath</th>\n",
              "      <th>KitchenQual</th>\n",
              "      <th>TotRmsAbvGrd</th>\n",
              "      <th>Functional</th>\n",
              "      <th>Kitchen</th>\n",
              "      <th>Bedroom</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>864</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>TA</td>\n",
              "      <td>6</td>\n",
              "      <td>Typ</td>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   2ndFlrSF  LowQualFinSF  GrLivArea  ...  Functional  Kitchen  Bedroom\n",
              "0         0             0        864  ...         Typ        1        3\n",
              "\n",
              "[1 rows x 12 columns]"
            ]
          },
          "metadata": {},
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 290
        },
        "id": "5s44cbsNrV1f",
        "outputId": "5d9009cc-0404-47b6-a291-1a78afb2aa46"
      },
      "source": [
        "#간단하게 확인하는 방법\n",
        "myColumn.describe()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>2ndFlrSF</th>\n",
              "      <th>LowQualFinSF</th>\n",
              "      <th>GrLivArea</th>\n",
              "      <th>BsmtFullBath</th>\n",
              "      <th>BsmtHalfBath</th>\n",
              "      <th>FullBath</th>\n",
              "      <th>HalfBath</th>\n",
              "      <th>TotRmsAbvGrd</th>\n",
              "      <th>Kitchen</th>\n",
              "      <th>Bedroom</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>1460.000000</td>\n",
              "      <td>1460.000000</td>\n",
              "      <td>1460.000000</td>\n",
              "      <td>1460.000000</td>\n",
              "      <td>1460.000000</td>\n",
              "      <td>1460.000000</td>\n",
              "      <td>1460.000000</td>\n",
              "      <td>1460.000000</td>\n",
              "      <td>1460.000000</td>\n",
              "      <td>1460.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>346.992466</td>\n",
              "      <td>5.844521</td>\n",
              "      <td>1515.463699</td>\n",
              "      <td>0.425342</td>\n",
              "      <td>0.057534</td>\n",
              "      <td>1.565068</td>\n",
              "      <td>0.382877</td>\n",
              "      <td>6.517808</td>\n",
              "      <td>1.046575</td>\n",
              "      <td>2.866438</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>436.528436</td>\n",
              "      <td>48.623081</td>\n",
              "      <td>525.480383</td>\n",
              "      <td>0.518911</td>\n",
              "      <td>0.238753</td>\n",
              "      <td>0.550916</td>\n",
              "      <td>0.502885</td>\n",
              "      <td>1.625393</td>\n",
              "      <td>0.220338</td>\n",
              "      <td>0.815778</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>334.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1129.500000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>5.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>2.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1464.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>6.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>3.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>728.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1776.750000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>7.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>3.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>2065.000000</td>\n",
              "      <td>572.000000</td>\n",
              "      <td>5642.000000</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>14.000000</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>8.000000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "          2ndFlrSF  LowQualFinSF  ...      Kitchen      Bedroom\n",
              "count  1460.000000   1460.000000  ...  1460.000000  1460.000000\n",
              "mean    346.992466      5.844521  ...     1.046575     2.866438\n",
              "std     436.528436     48.623081  ...     0.220338     0.815778\n",
              "min       0.000000      0.000000  ...     0.000000     0.000000\n",
              "25%       0.000000      0.000000  ...     1.000000     2.000000\n",
              "50%       0.000000      0.000000  ...     1.000000     3.000000\n",
              "75%     728.000000      0.000000  ...     1.000000     3.000000\n",
              "max    2065.000000    572.000000  ...     3.000000     8.000000\n",
              "\n",
              "[8 rows x 10 columns]"
            ]
          },
          "metadata": {},
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "kNTqrAEy1EHh"
      },
      "source": [
        "### 참고) WoodDeckSF 데이터 추가로 확인해보기"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 290
        },
        "id": "xgE1ilVU1IQ_",
        "outputId": "7febbe52-7d17-4b70-c146-dae9fcd22f1f"
      },
      "source": [
        "fieldWood = houseData[['WoodDeckSF']]\n",
        "fieldWood.describe()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>WoodDeckSF</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>1460.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>94.244521</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>125.338794</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>168.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>857.000000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "        WoodDeckSF\n",
              "count  1460.000000\n",
              "mean     94.244521\n",
              "std     125.338794\n",
              "min       0.000000\n",
              "25%       0.000000\n",
              "50%       0.000000\n",
              "75%     168.000000\n",
              "max     857.000000"
            ]
          },
          "metadata": {},
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zwAX9G4h3oUh",
        "outputId": "3981dfab-884d-4065-8e60-9a86398cc647"
      },
      "source": [
        "fieldWood['WoodDeckSF'].value_counts(normalize=True)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0      0.521233\n",
              "192    0.026027\n",
              "100    0.024658\n",
              "144    0.022603\n",
              "120    0.021233\n",
              "         ...   \n",
              "269    0.000685\n",
              "265    0.000685\n",
              "263    0.000685\n",
              "260    0.000685\n",
              "215    0.000685\n",
              "Name: WoodDeckSF, Length: 274, dtype: float64"
            ]
          },
          "metadata": {},
          "execution_count": 28
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 316
        },
        "id": "8MvryASo1Sgj",
        "outputId": "c4cf123c-9dec-4ec5-e60e-cee7c7a4f956"
      },
      "source": [
        "fieldWood.hist()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[<matplotlib.axes._subplots.AxesSubplot object at 0x7f2fe5060150>]],\n",
              "      dtype=object)"
            ]
          },
          "metadata": {},
          "execution_count": 16
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "1yB1Uur0L5X8"
      },
      "source": [
        "## 시각화로 데이터 확인하기(Histogram)"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "zu0rqaOeK6FT"
      },
      "source": [
        "import matplotlib.pyplot as plt"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 508
        },
        "id": "lEYMxhYqLGzr",
        "outputId": "0f5ea7ff-9806-483d-ef39-3745329655cc"
      },
      "source": [
        "#전체 칼럼들에 대해서 histogram으로 나타내기\n",
        "myColumn.hist()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[<matplotlib.axes._subplots.AxesSubplot object at 0x7f2fe5003110>,\n",
              "        <matplotlib.axes._subplots.AxesSubplot object at 0x7f2fe55d91d0>,\n",
              "        <matplotlib.axes._subplots.AxesSubplot object at 0x7f2fe4f2d710>],\n",
              "       [<matplotlib.axes._subplots.AxesSubplot object at 0x7f2fe4f5cd90>,\n",
              "        <matplotlib.axes._subplots.AxesSubplot object at 0x7f2fe4f20450>,\n",
              "        <matplotlib.axes._subplots.AxesSubplot object at 0x7f2fe4ed5ad0>],\n",
              "       [<matplotlib.axes._subplots.AxesSubplot object at 0x7f2fe4e97210>,\n",
              "        <matplotlib.axes._subplots.AxesSubplot object at 0x7f2fe4e4c7d0>,\n",
              "        <matplotlib.axes._subplots.AxesSubplot object at 0x7f2fe4e4c810>],\n",
              "       [<matplotlib.axes._subplots.AxesSubplot object at 0x7f2fe4e05f90>,\n",
              "        <matplotlib.axes._subplots.AxesSubplot object at 0x7f2fe4d7bbd0>,\n",
              "        <matplotlib.axes._subplots.AxesSubplot object at 0x7f2fe4d3e290>]],\n",
              "      dtype=object)"
            ]
          },
          "metadata": {},
          "execution_count": 18
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 12 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 316
        },
        "id": "1bDReUWvMFu8",
        "outputId": "99192cd7-d8b2-418c-e6ee-50395611cf51"
      },
      "source": [
        "#특정 칼럼을 histogram으로 나타내기\n",
        "myColumn.hist(column='2ndFlrSF')"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[<matplotlib.axes._subplots.AxesSubplot object at 0x7f2fe4bc2190>]],\n",
              "      dtype=object)"
            ]
          },
          "metadata": {},
          "execution_count": 19
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 296
        },
        "id": "bNF6iGRRBXz1",
        "outputId": "25046ed1-4539-45f8-d797-27f948949c6b"
      },
      "source": [
        "import seaborn as sns\n",
        "\n",
        "sns.countplot(x = myColumn['KitchenQual'])"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f2fd69107d0>"
            ]
          },
          "metadata": {},
          "execution_count": 20
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9SK9fXb8LnWm",
        "outputId": "392fc1dd-4600-4756-f50c-40b59eef70a0"
      },
      "source": [
        "myColumn.info()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 1460 entries, 0 to 1459\n",
            "Data columns (total 12 columns):\n",
            " #   Column        Non-Null Count  Dtype \n",
            "---  ------        --------------  ----- \n",
            " 0   2ndFlrSF      1460 non-null   int64 \n",
            " 1   LowQualFinSF  1460 non-null   int64 \n",
            " 2   GrLivArea     1460 non-null   int64 \n",
            " 3   BsmtFullBath  1460 non-null   int64 \n",
            " 4   BsmtHalfBath  1460 non-null   int64 \n",
            " 5   FullBath      1460 non-null   int64 \n",
            " 6   HalfBath      1460 non-null   int64 \n",
            " 7   KitchenQual   1460 non-null   object\n",
            " 8   TotRmsAbvGrd  1460 non-null   int64 \n",
            " 9   Functional    1460 non-null   object\n",
            " 10  Kitchen       1460 non-null   int64 \n",
            " 11  Bedroom       1460 non-null   int64 \n",
            "dtypes: int64(10), object(2)\n",
            "memory usage: 137.0+ KB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "RhWDCk4dRSNX"
      },
      "source": [
        "# 이상치 탐지 방법"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "jDi4DtasRVJ9"
      },
      "source": [
        "import matplotlib.pyplot as plt\n",
        "import numpy as np\n",
        "from scipy.special import erfc\n",
        "\n",
        "data = myColumn['LowQualFinSF']"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "W2bWvRoMTH3V"
      },
      "source": [
        "## 1. Z-score 방식으로 이상치 탐지\n",
        "Z-score = standard-score\n",
        " - 가우스 분포가 취하고 있다는 가정으로 관측치가 평균에서 벗어난 표준 편차의 수\n",
        " - 참고 URL : https://claryk.tistory.com/5\n",
        "\n",
        "\n",
        "```\n",
        "Z score = ( x - mean ) / std.deviation\n",
        "```\n",
        "![캡처.PNG](data:image/png;base64,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)\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "407Q5SiQRqI-",
        "outputId": "49ec0421-1f79-4c28-d234-7a8761efe283"
      },
      "source": [
        "mean = np.mean(data)\n",
        "std = np.std(data)\n",
        "print('평균 : ', mean, ' / 표준편차 : ', std, sep = '\\n')"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "평균 : \n",
            "5.844520547945206\n",
            " / 표준편차 : \n",
            "48.60642684099989\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FCOnilv_Sq2O",
        "outputId": "21c8b3e4-f153-4679-b53f-3bc209adce44"
      },
      "source": [
        "#Z-score 계산하기\n",
        "threshold = 3\n",
        "outlier = []\n",
        "\n",
        "for i in data:\n",
        "  z = (i-mean) / std\n",
        "  if z> threshold:\n",
        "    outlier.append(i)\n",
        "\n",
        "print('이상치 : ', outlier)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "이상치 :  [360, 513, 234, 528, 572, 392, 371, 390, 420, 473, 156, 515, 360, 232, 481, 514, 397, 479, 205, 384]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 283
        },
        "id": "pWn1El7sVFO_",
        "outputId": "c0f46ff6-1200-4589-fc39-e234d31fb036"
      },
      "source": [
        "data.hist()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f9e1cee1790>"
            ]
          },
          "metadata": {},
          "execution_count": 11
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "I0s5lifUV3Ee"
      },
      "source": [
        "##2. IQR(Interquartile range) 방식\n",
        "- 대표적 이상치 탐지 방법 중 하나\n",
        "- IQR : (Q3 - Q1) 사분위수 상위 75% 지점의 값과 하위 25% 지점의 값 차이\n",
        "- 참고 URL : https://claryk.tistory.com/4"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "udvm2ESWV8rv"
      },
      "source": [
        "def outlier_iqr(data, column): \n",
        "\n",
        "    # lower, upper 글로벌 변수 선언하기     \n",
        "    global lower, upper    \n",
        "    \n",
        "    # 4분위수 기준 지정하기     \n",
        "    q25, q75 = np.quantile(data[column], 0.25), np.quantile(data[column], 0.75)          \n",
        "    \n",
        "    # IQR 계산하기     \n",
        "    iqr = q75 - q25    \n",
        "    \n",
        "    # outlier cutoff 계산하기     \n",
        "    cut_off = iqr * 1.5          \n",
        "    \n",
        "    # lower와 upper bound 값 구하기     \n",
        "    lower, upper = q25 - cut_off, q75 + cut_off     \n",
        "    \n",
        "    print('IQR은',iqr, '이다.')     \n",
        "    print('lower bound 값은', lower, '이다.')     \n",
        "    print('upper bound 값은', upper, '이다.')    \n",
        "    \n",
        "    # 1사 분위와 4사 분위에 속해있는 데이터 각각 저장하기     \n",
        "    data1 = data[data[column] > upper]     \n",
        "    data2 = data[data[column] < lower]    \n",
        "    \n",
        "    # 이상치 총 개수 구하기\n",
        "    return print('총 이상치 개수는', data1.shape[0] + data2.shape[0], '이다.')\n",
        "    "
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6LmbdT-UWDhd",
        "outputId": "afc977fe-fc1c-4425-ab89-824a61ae06fb"
      },
      "source": [
        "data = houseData[['2ndFlrSF']]\n",
        "outlier_iqr(data, '2ndFlrSF')"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "IQR은 728.0 이다.\n",
            "lower bound 값은 -1092.0 이다.\n",
            "upper bound 값은 1820.0 이다.\n",
            "총 이상치 개수는 2 이다.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 322
        },
        "id": "nfOSiVwRZwy8",
        "outputId": "9c9a701e-b28e-4c3f-b500-8a7f18e15a67"
      },
      "source": [
        "sns.distplot(data, kde=True, rug=False)\n",
        "plt.show()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/seaborn/distributions.py:2619: FutureWarning: `distplot` is a deprecated function and will be removed in a future version. Please adapt your code to use either `displot` (a figure-level function with similar flexibility) or `histplot` (an axes-level function for histograms).\n",
            "  warnings.warn(msg, FutureWarning)\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "W7FLh4Gz-se2"
      },
      "source": [
        "테스트\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qneDomr5-teI",
        "outputId": "b629451b-34fb-4d55-bcad-69b0574516f7"
      },
      "source": [
        "testData = houseData[['BsmtFinSF1']]\n",
        "testData.isna().sum()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "BsmtFinSF1    0\n",
              "dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 21
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Iz1u4C-QCLJ9"
      },
      "source": [
        "시각화 참고 URL : https://dining-developer.tistory.com/30"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "lGb0LJmergsB"
      },
      "source": [
        "# 이상치 처리 방법"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ag56MTTtwulF",
        "outputId": "e6ec2a83-e477-455c-e5cb-c8ca004e1e94"
      },
      "source": [
        "mean = np.mean(myColumn['2ndFlrSF'])\n",
        "std = np.std(myColumn['2ndFlrSF'])\n",
        "average = int(np.mean(myColumn['2ndFlrSF']))\n",
        "print(np.mean(myColumn['2ndFlrSF']))\n",
        "threshold = 3\n",
        "\n",
        "def test(x):\n",
        "  if (x - mean) / std > threshold:\n",
        "    print(x)\n",
        "    return 5\n",
        "  else : return x"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "342.76849315068495\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 282
        },
        "id": "3sZSzFsy35jJ",
        "outputId": "41f74b73-4e9f-47a0-b1f3-590ac94b94f9"
      },
      "source": [
        "data1 = myColumn['2ndFlrSF']\n",
        "data1.hist()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f7851c72910>"
            ]
          },
          "metadata": {},
          "execution_count": 70
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 200
        },
        "id": "iiLRewvC4RDQ",
        "outputId": "33eed78b-45f1-4fa6-c1d5-4cf8e379355e"
      },
      "source": [
        "data2 = myColumn[['2ndFlrSF']]\n",
        "data2.head()\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>2ndFlrSF</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>854</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>866</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>756</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>1053</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   2ndFlrSF\n",
              "0       854\n",
              "1         0\n",
              "2       866\n",
              "3       756\n",
              "4      1053"
            ]
          },
          "metadata": {},
          "execution_count": 74
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "HpS29eIB6UC0"
      },
      "source": [
        "def zscoreOutlier(df, col, z):\n",
        "  return df[abs(df[col] - np.mean(df[col]))/np.std(df[col])>z].index"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "KFqR6r9Y7xjk"
      },
      "source": [
        "def test(df, col, z):\n",
        "  return df[(df[col] - np.mean(df[col]))/np.std(df[col])>z].index"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 48
        },
        "id": "XVhzw6ul7FQ8",
        "outputId": "e64acf23-d52f-425b-e71b-4c5d11f82842"
      },
      "source": [
        "data2.loc[test(data2, '2ndFlrSF', 3)]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>2ndFlrSF</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "Empty DataFrame\n",
              "Columns: [2ndFlrSF]\n",
              "Index: []"
            ]
          },
          "metadata": {},
          "execution_count": 83
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 316
        },
        "id": "HZvAqXQp7TZz",
        "outputId": "fdaa4354-4f1c-4169-c7b3-a2726dbf8ac2"
      },
      "source": [
        "data2.hist()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[<matplotlib.axes._subplots.AxesSubplot object at 0x7f7851c41a10>]],\n",
              "      dtype=object)"
            ]
          },
          "metadata": {},
          "execution_count": 78
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 258
        },
        "id": "u6chsQeRzaDc",
        "outputId": "72f2164a-a7e8-4d97-f1ec-dc08bac6b718"
      },
      "source": [
        "\n",
        "myColumn['2ndFlrSF'] = myColumn['2ndFlrSF'].apply(test)\n",
        "\n",
        "testColumn = myColumn[['2ndFlrSF']]\n",
        "testColumn['2ndFlrSF'] = myColumn['2ndFlrSF'].apply(test)\n",
        "\n",
        "t = testColumn.loc[testColumn['2ndFlrSF']==5]\n",
        "\n",
        "t.head(10)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/ipykernel_launcher.py:2: SettingWithCopyWarning: \n",
            "A value is trying to be set on a copy of a slice from a DataFrame.\n",
            "Try using .loc[row_indexer,col_indexer] = value instead\n",
            "\n",
            "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
            "  \n",
            "/usr/local/lib/python3.7/dist-packages/ipykernel_launcher.py:5: SettingWithCopyWarning: \n",
            "A value is trying to be set on a copy of a slice from a DataFrame.\n",
            "Try using .loc[row_indexer,col_indexer] = value instead\n",
            "\n",
            "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
            "  \"\"\"\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>2ndFlrSF</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "Empty DataFrame\n",
              "Columns: [2ndFlrSF]\n",
              "Index: []"
            ]
          },
          "metadata": {},
          "execution_count": 66
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Q9lG-Q5k9acl"
      },
      "source": [
        "다시해보자ㅠ\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 351
        },
        "id": "KGdx6Kgq9cS1",
        "outputId": "fb032a20-83c7-4d73-d101-72d0550e759c"
      },
      "source": [
        "column = myColumn[['LowQualFinSF']]\n",
        "column_order = column.sort_values(by=['LowQualFinSF'], ascending=False)\n",
        "\n",
        "column_order.head(10)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>LowQualFinSF</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>185</th>\n",
              "      <td>572</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>170</th>\n",
              "      <td>528</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>635</th>\n",
              "      <td>515</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1009</th>\n",
              "      <td>514</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>88</th>\n",
              "      <td>513</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>883</th>\n",
              "      <td>481</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1173</th>\n",
              "      <td>479</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>406</th>\n",
              "      <td>473</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>267</th>\n",
              "      <td>420</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1031</th>\n",
              "      <td>397</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "      LowQualFinSF\n",
              "185            572\n",
              "170            528\n",
              "635            515\n",
              "1009           514\n",
              "88             513\n",
              "883            481\n",
              "1173           479\n",
              "406            473\n",
              "267            420\n",
              "1031           397"
            ]
          },
          "metadata": {},
          "execution_count": 99
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "C_5mC7-1AYxT"
      },
      "source": [
        "def getOutlierByZscore(x):\n",
        "  z = (x - mean) / std\n",
        "  if z > 3:\n",
        "    return True;\n",
        "\n",
        "def getOutlierByZscore2(df, col, z):\n",
        "  return df[(df[col] - np.mean(df[col]))/np.std(df[col])>z].index"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 308
        },
        "id": "biyt7eoSE8LN",
        "outputId": "8f2d3510-bff4-44bf-ff0b-9a6d2e1569ee"
      },
      "source": [
        "testData = column_order['LowQualFinSF']\n",
        "s = getOutlierByZscore(testData.item)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "TypeError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-109-107a0fdd6b8c>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0mtestData\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mcolumn_order\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'LowQualFinSF'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0ms\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mgetOutlierByZscore\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtestData\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mitem\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;32m<ipython-input-101-bae2cee1662d>\u001b[0m in \u001b[0;36mgetOutlierByZscore\u001b[0;34m(x)\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0mgetOutlierByZscore\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mx\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m   \u001b[0mz\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0mx\u001b[0m \u001b[0;34m-\u001b[0m \u001b[0mmean\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m/\u001b[0m \u001b[0mstd\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      3\u001b[0m   \u001b[0;32mif\u001b[0m \u001b[0mz\u001b[0m \u001b[0;34m>\u001b[0m \u001b[0;36m3\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m     \u001b[0;32mreturn\u001b[0m \u001b[0;32mTrue\u001b[0m\u001b[0;34m;\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mTypeError\u001b[0m: unsupported operand type(s) for -: 'method' and 'float'"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 168
        },
        "id": "jpw1GTLRCOsj",
        "outputId": "575a2cc1-cdb7-4f77-e6ef-b9df4c671e88"
      },
      "source": [
        "column_order['LowQualFinSF'] = column_order.apply(\n",
        "    lambda x: x['LowQualFinSF'])"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "IndexError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mIndexError\u001b[0m                                Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-104-918628ce1728>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mcolumn_order\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mloc\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mcolumn_order\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'LowQualFinSF'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mgetOutlierByZscore\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcolumn_order\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mvalues\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'LowQualFinSF'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mIndexError\u001b[0m: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 351
        },
        "id": "dwXhNH9e_Ecs",
        "outputId": "81ab7744-202c-4e5f-a441-7193e899b56a"
      },
      "source": [
        "column_order.loc[column_order['LowQualFinSF'] > (column_order['LowQualFinSF'] - 1) ] = 999\n",
        "column_order.head(10)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>LowQualFinSF</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>185</th>\n",
              "      <td>999</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>170</th>\n",
              "      <td>999</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>635</th>\n",
              "      <td>999</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1009</th>\n",
              "      <td>999</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>88</th>\n",
              "      <td>999</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>883</th>\n",
              "      <td>999</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1173</th>\n",
              "      <td>999</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>406</th>\n",
              "      <td>999</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>267</th>\n",
              "      <td>999</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1031</th>\n",
              "      <td>999</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "      LowQualFinSF\n",
              "185            999\n",
              "170            999\n",
              "635            999\n",
              "1009           999\n",
              "88             999\n",
              "883            999\n",
              "1173           999\n",
              "406            999\n",
              "267            999\n",
              "1031           999"
            ]
          },
          "metadata": {},
          "execution_count": 94
        }
      ]
    }
  ]
}