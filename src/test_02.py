import numpy as np
import matplotlib.pyplot as plt

# 日本語フォントの設定 (macOS用)
plt.rcParams['font.family'] = 'Hiragino Sans'

# ==========================================
# サスペンション用コイルスプリングの応力計算
# ==========================================

# 1. パラメータ設定 (単位: mm, N)
# --------------------------------
d = 12.0          # 素線径 (Wire diameter)
D = 120.0         # コイル平均径 (Mean coil diameter)
Na = 5.0          # 有効巻数 (Number of active coils)
G = 78000.0       # 横弾性係数 (Shear modulus) MPa (鋼の場合)
Load_max = 6000.0 # 想定する最大荷重 (Maximum Load)

# 計算用の荷重配列 (0から最大荷重まで)
P_range = np.linspace(0, Load_max, 100)

# 2. 基本計算
# --------------------------------
c = D / d  # ばね指数 (Spring index)

# ワールの修正係数 (Wahl Correction Factor)
# ばねの内側に生じる応力集中を考慮する係数
K = (4*c - 1) / (4*c - 4) + (0.615 / c)

# バネ定数 k (N/mm)
k = (G * d**4) / (8 * Na * D**3)

# 3. 応力とたわみの計算
# --------------------------------
# たわみ delta (mm) = (8 * P * Na * D^3) / (G * d^4)
deflection = (8 * P_range * Na * D**3) / (G * d**4)

# 最大せん断応力 tau (MPa) = K * (8 * P * D) / (pi * d^3)
shear_stress = K * (8 * P_range * D) / (np.pi * d**3)

# 4. 結果の表示と可視化
# --------------------------------
print(f"--- 計算結果 ---")
print(f"ばね指数 c : {c:.2f}")
print(f"修正係数 K : {K:.2f}")
print(f"ばね定数 k : {k:.2f} N/mm")
print(f"最大荷重時の応力: {np.max(shear_stress):.2f} MPa")

# グラフ描画
fig, ax1 = plt.subplots(figsize=(10, 6))

# 左軸：荷重 vs たわみ
color = 'tab:blue'
ax1.set_xlabel('たわみ (Deflection) [mm]', fontsize=12)
ax1.set_ylabel('荷重 (Load) [N]', color=color, fontsize=12)
ax1.plot(deflection, P_range, color=color, linewidth=2, label='荷重-たわみ曲線')
ax1.tick_params(axis='y', labelcolor=color)
ax1.grid(True, linestyle=':', alpha=0.6)

# 右軸：荷重 vs 応力
ax2 = ax1.twinx()  # x軸を共有
color = 'tab:red'
ax2.set_ylabel('最大せん断応力 (Max Shear Stress) [MPa]', color=color, fontsize=12)
ax2.plot(deflection, shear_stress, color=color, linestyle='--', linewidth=2, label='発生応力')
ax2.tick_params(axis='y', labelcolor=color)

# 降伏応力の目安ライン (例: SUP12 焼入れ焼戻し材で約1100-1200MPa)
yield_limit = 1100
ax2.axhline(y=yield_limit, color='green', linestyle='-.', label='降伏応力目安 (Yield Limit)')

# タイトル
plt.title(f'コイルスプリングの特性と発生応力\n(線径 d={d}mm, コイル径 D={D}mm)', fontsize=14)

# 凡例の整理
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

plt.tight_layout()
output_path = '/Users/juna1013/bin/Report/2025/53_材料工学Ⅱ/images/suspension_stress.png'
plt.savefig(output_path)
print(f"グラフを {output_path} に保存しました。")
# plt.show()