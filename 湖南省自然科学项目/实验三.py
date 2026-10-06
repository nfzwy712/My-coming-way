# -*- coding: utf-8 -*-
"""实验3：扩散步数如何影响原型偏移（各向同性 vs 各向异性）。

场景同实验2：两个高斯类靠得近（中心 ±0.8，std=0.6），每类 5 个支持样本。
本实验扫描不同的扩散步数 T，观察两类方法"原型到真实中心的偏移"随 T 的变化：
  - isotropic    各向同性扩散：偏移迅速增大并饱和（越扩散越污染）
  - anisotropic  各向异性扩散：偏移始终显著更小（跨类刹车在起作用）
"""

import os

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

rng = np.random.default_rng(20260909)

C0 = np.array([-0.8, 0.0])
C1 = np.array([0.8, 0.0])
STD = 0.6


def make_task(n=5):
    s0 = rng.normal(C0, STD, size=(n, 2))
    s1 = rng.normal(C1, STD, size=(n, 2))
    xs = np.vstack([s0, s1])
    ys = np.concatenate([np.zeros(n, int), np.ones(n, int)])
    return xs, ys


def shift(xs, ys):
    pr = np.stack([xs[ys == c].mean(0) for c in (0, 1)])
    d0 = np.linalg.norm(pr[0] - C0)
    d1 = np.linalg.norm(pr[1] - C1)
    return 0.5 * (d0 + d1)


def diffuse(xs, T, dt=0.2, mode="isotropic", K=0.7):
    x = xs.copy().astype(float)
    for _ in range(T):
        d2 = ((x[:, None, :] - x[None, :, :]) ** 2).sum(-1)
        if mode == "isotropic":
            w = np.ones_like(d2)
        else:
            w = np.exp(-d2 / (K * K))
        np.fill_diagonal(w, 0.0)
        w /= w.sum(1, keepdims=True) + 1e-12
        x = x + dt * (w @ x - x)
    return x


def main():
    steps = [0, 5, 10, 20, 40, 80]
    iso_means, an_means = [], []
    print("=" * 58)
    print("实验3：扩散步数 vs 原型偏移（400 次随机任务）")
    print("=" * 58)
    print(f"{'步数T':>6} | {'各向同性偏移':>12} | {'各向异性偏移':>12}")

    for T in steps:
        iso, an = [], []
        for _ in range(400):
            xs, ys = make_task()
            iso.append(shift(diffuse(xs, T, mode="isotropic"), ys))
            an.append(shift(diffuse(xs, T, mode="anisotropic"), ys))
        im, am = np.mean(iso), np.mean(an)
        iso_means.append(im)
        an_means.append(am)
        print(f"{T:6d} | {im:12.4f} | {am:12.4f}")

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(steps, iso_means, "o-", label="各向同性扩散", color="C0")
    ax.plot(steps, an_means, "s-", label="各向异性扩散", color="C1")
    ax.axhline(0.34, ls="--", lw=1, color="gray", alpha=0.7)
    ax.text(0.5, 0.35, "基线采样误差 ≈ 0.34", color="gray", fontsize=9, transform=ax.get_yaxis_transform())
    ax.set_xlabel("扩散步数 T")
    ax.set_ylabel("原型到真实类中心的平均偏移")
    ax.set_title("各向同性扩散越扩散越污染，各向异性扩散显著抑制偏移")
    ax.legend()
    ax.grid(alpha=0.3)
    fig.tight_layout()
    out_png = os.path.join(os.path.dirname(os.path.abspath(__file__)), "experiment3_result.png")
    fig.savefig(out_png, dpi=160)
    print("\n已保存图:", out_png)


if __name__ == "__main__":
    main()
