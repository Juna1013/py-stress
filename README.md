# py-stress
自動車部品の応力解析シミュレーションプログラム集

## 概要

このリポジトリは、自動車の構造部品における応力計算をPythonで実装したサンプルプログラムを含んでいます。材料工学の基礎的な計算モデルを使用し、軽量化設計やばね特性の理解に役立てることを目的としています。

## プログラム一覧

| ファイル | 説明 |
|----------|------|
| [src/test_01.py](src/test_01.py) | 車体骨格部材（Bピラー）の曲げ応力シミュレーション |
| [src/test_02.py](src/test_02.py) | サスペンション用コイルスプリングの応力計算 |

## ドキュメント

各プログラムの詳細なドキュメントは `docs/` フォルダにあります。

- [docs/test_01.md](docs/test_01.md) - 曲げ応力シミュレーションの詳細
- [docs/test_02.md](docs/test_02.md) - コイルスプリング応力計算の詳細

## 必要環境

- Python 3.x
- NumPy
- Matplotlib

## インストール

```bash
pip install numpy matplotlib
```

## 使用方法

```bash
# 車体骨格部材の曲げ応力シミュレーション
python src/test_01.py

# コイルスプリングの応力計算
python src/test_02.py
```

## ディレクトリ構成

```bash
py-stress/
├── README.md          # このファイル
├── docs/              # ドキュメント
│   ├── test_01.md
│   └── test_02.md
├── images/            # 出力画像
└── src/               # ソースコード
    ├── test_01.py
    └── test_02.py
```
