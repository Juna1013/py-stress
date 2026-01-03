import numpy as np
import matplotlib.pyplot as plt

# 日本語フォントの設定 (macOS用)
plt.rcParams['font.family'] = 'Hiragino Sans'

# ==================================================
# 車体骨格部材（Bピラー想定）の曲げ応力シミュレーション
# ==================================================

# 1. 計算モデルの設定 (簡易的な角パイプの3点曲げを想定)
# --------------------------------------------------
L = 1000.0        # 支点間距離 (Span length) mm
W = 100.0         # 断面の幅 (Width) mm
H = 150.0         # 断面の高さ (Height) mm

# 比較する2つの材料の降伏点 (Yield Strength)
sigma_y_mild = 440.0   # 軟鋼・低強度ハイテン (例: 440MPa)
sigma_y_hot  = 1500.0  # ホットスタンプ材 (例: 1500MPa)

# 板厚の設定 (Thickness)
t_mild = 2.0      # 軟鋼の板厚 mm
t_hot  = 1.2      # ホットスタンプ材の板厚 mm (薄肉化)

# 荷重範囲 (Load) N
Force = np.linspace(0, 50000, 100) # 0〜50kN

# 2. 断面性能と応力の計算関数
# --------------------------------------------------
def calculate_stress(force, w, h, t, l):
    # 断面二次モーメント I (中空長方形断面)
    # I = (W*H^3 - (W-2t)*(H-2t)^3) / 12
    outer_I = w * h**3
    inner_I = (w - 2*t) * (h - 2*t)**3
    I = (outer_I - inner_I) / 12
    
    # 最大曲げモーメント M (中央集中荷重)
    # M = F * L / 4
    M = force * l / 4
    
    # 最大曲げ応力 sigma = M * y / I (yは中立軸からの距離 = H/2)
    y = h / 2
    sigma = M * y / I
    return sigma

# それぞれの計算実行
stress_mild = calculate_stress(Force, W, H, t_mild, L)
stress_hot  = calculate_stress(Force, W, H, t_hot, L)

# 3. グラフ描画
# --------------------------------------------------
plt.figure(figsize=(10, 6))

# 軟鋼 (厚い) のプロット
plt.plot(Force/1000, stress_mild, label=f'軟鋼 (厚さ{t_mild}mm) の発生応力', color='blue', linestyle='-')
# 限界線
plt.axhline(y=sigma_y_mild, color='blue', linestyle=':', alpha=0.5, label='軟鋼の降伏点 (440MPa)')

# ホットスタンプ材 (薄い) のプロット
plt.plot(Force/1000, stress_hot, label=f'ホットスタンプ材 (厚さ{t_hot}mm) の発生応力', color='red', linestyle='-')
# 限界線
plt.axhline(y=sigma_y_hot, color='red', linestyle=':', alpha=0.5, label='ホットスタンプ材の降伏点 (1500MPa)')

# グラフ装飾
plt.title('荷重に対する発生応力の比較：軽量化の効果', fontsize=14)
plt.xlabel('負荷荷重 (Load) [kN]', fontsize=12)
plt.ylabel('最大曲げ応力 (Max Bending Stress) [MPa]', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# 注釈
plt.text(5, 600, 
         f'軟鋼(2.0mm)は\n低い荷重で変形開始', 
         color='blue', bbox=dict(facecolor='white', alpha=0.8))

plt.text(30, 1100, 
         f'ホットスタンプ材(1.2mm)は\n薄くても耐えられる\n→ 軽量化成功', 
         color='red', bbox=dict(facecolor='white', alpha=0.8))

plt.tight_layout()
output_path = '/Users/juna1013/bin/Report/2025/53_材料工学Ⅱ/images/body_stress.png'
plt.savefig(output_path)
print(f"グラフを {output_path} に保存しました。")
# plt.show()

# 4. 軽量化率の計算と表示
# --------------------------------------------------
# 単位長さあたりの断面積比較（重量に比例）
area_mild = W*H - (W-2*t_mild)*(H-2*t_mild)
area_hot  = W*H - (W-2*t_hot)*(H-2*t_hot)
weight_reduction = (1 - area_hot/area_mild) * 100

print(f"--- 軽量化の試算結果 ---")
print(f"軟鋼の断面積: {area_mild:.1f} mm2")
print(f"ホットスタンプ材の断面積: {area_hot:.1f} mm2")
print(f"重量削減率: {weight_reduction:.1f}% の軽量化を達成")