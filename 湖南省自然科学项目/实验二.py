# -*- coding: utf-8 -*-
"""实验2：各向同性 vs 各向异性扩散的"跨类污染"机制对照。

场景：两个高斯类靠得近（中心 ±0.8，std=0.6，明显重叠），每类 5 个支持样本。
用"原型到真实类中心的偏移距离"作主指标：
  - baseline      直接取每类均值作原型
  - isotropic     各向同性图扩散(邻居等权)：把两类的样本互相拉，原型向中间偏
  - anisotropic   各向异性扩散(Perona-Malik exp 型)：类内聚拢、跨类自动刹车

预期：原型偏移  anisotropic < baseline < isotropic。
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

rng = np.random.default_rng(20260908)

C0 = np.array([-0.8, 0.0])
C1 = np.array([0.8, 0.0])
STD = 0.6


def make_task(n=5, n_query=300):
    s0 = rng.normal(C0, STD, size=(n, 2))
    s1 = rng.normal(C1, STD, size=(n, 2))
    xs = np.vstack([s0, s1])
    ys = np.concatenate([np.zeros(n, int), np.ones(n, int)])
    q0 = rng.normal(C0, STD, size=(n_query, 2))
    q1 = rng.normal(C1, STD, size=(n_query, 2))
    xq = np.vstack([q0, q1])
    yq = np.concatenate([np.zeros(n_query, int), np.ones(n_query, int)])
    return xs, ys, xq, yq


def prototypes(xs, ys):
    return np.stack([xs[ys == c].mean(0) for c in (0, 1)])


def shift(proto):
    """两类原型到各自真实中心的平均欧氏距离。"""
    d0 = np.linalg.norm(proto[0] - C0)
    d1 = np.linalg.norm(proto[1] - C1)
    return 0.5 * (d0 + d1)


def acc(proto, xq, yq):
    d = ((xq[:, None, :] - proto[None, :, :]) ** 2).sum(-1)
    return (d.argmin(1) == yq).mean()


def diffuse(xs, T=25, dt=0.25, mode="isotropic", K=0.7):
    x = xs.copy().astype(float)
    for _ in range(T):
        d2 = ((x[:, None, :] - x[None, :, :]) ** 2).sum(-1)
        if mode == "isotropic":
            w = np.ones_like(d2)  # 邻居等权：不区分远近/跨类
        else:
            w = np.exp(-d2 / (K * K))  # Perona-Malik：距离大 -> 权重近 0
        np.fill_diagonal(w, 0.0)
        w /= w.sum(1, keepdims=True) + 1e-12
        x = x + dt * (w @ x - x)
    return x


def main():
    print("=" * 62)
    print("实验2：跨类污染机制（两类各5样本、靠得近，400次）")
    print("=" * 62)

    sh = {k: [] for k in ("baseline", "isotropic", "anisotropic")}
    ac = {k: [] for k in ("baseline", "isotropic", "anisotropic")}
    for _ in range(400):
        xs, ys, xq, yq = make_task()
        pb = prototypes(xs, ys)
        xi = diffuse(xs, mode="isotropic")
        xa = diffuse(xs, mode="anisotropic")
        pi = prototypes(xi, ys)
        pa = prototypes(xa, ys)
        sh["baseline"].append(shift(pb))
        sh["isotropic"].append(shift(pi))
        sh["anisotropic"].append(shift(pa))
        ac["baseline"].append(acc(pb, xq, yq))
        ac["isotropic"].append(acc(pi, xq, yq))
        ac["anisotropic"].append(acc(pa, xq, yq))

    print("\n原型到真实类中心的平均偏移(越小越好)：")
    for k in ("baseline", "isotropic", "anisotropic"):
        a = np.array(sh[k])
        print(f"  {k:12s}: {a.mean():.4f} +/- {a.std():.4f}")

    print("\n整体准确率：")
    for k in ("baseline", "isotropic", "anisotropic"):
        a = np.array(ac[k])
        print(f"  {k:12s}: {a.mean():.4f} +/- {a.std():.4f}")

    # 可视化一次任务
    xs, ys, xq, yq = make_task()
    xi = diffuse(xs, mode="isotropic")
    xa = diffuse(xs, mode="anisotropic")
    pb = prototypes(xs, ys)
    pi = prototypes(xi, ys)
    pa = prototypes(xa, ys)

    fig, ax = plt.subplots(1, 3, figsize=(14, 4.4), sharex=True, sharey=True)
    for a, title, ps, pr in zip(
        ax,
        ["无正则(基线)", "各向同性扩散", "各向异性扩散"],
        [xs, xi, xa],
        [pb, pi, pa],
    ):
        a.scatter(xq[yq == 0, 0], xq[yq == 0, 1], s=7, alpha=0.18, c="C0")
        a.scatter(xq[yq == 1, 0], xq[yq == 1, 1], s=7, alpha=0.18, c="C1")
        a.scatter(ps[ys == 0, 0], ps[ys == 0, 1], s=90, marker="s", c="C0", edgecolor="k", label="类0支持")
        a.scatter(ps[ys == 1, 0], ps[ys == 1, 1], s=90, marker="s", c="C1", edgecolor="k", label="类1支持")
        a.scatter(pr[0, 0], pr[0, 1], s=260, marker="*", c="C0", edgecolor="k", label="原型0")
        a.scatter(pr[1, 0], pr[1, 1], s=260, marker="*", c="C1", edgecolor="k", label="原型1")
        a.scatter(C0[0], C0[1], s=120, marker="+", c="k", lw=2)
        a.scatter(C1[0], C1[1], s=120, marker="+", c="k", lw=2)
        a.set_title(title)
        a.set_aspect("equal")
    ax[0].legend(fontsize=7, loc="upper left")
    fig.suptitle("黑十字=真实类中心；各向同性把原型拉向中间，各向异性保持类内聚拢", fontsize=11)
    fig.tight_layout()
    fig.savefig("F:/湖南省自然科学基金基础研究项目/experiment/experiment2_result.png", dpi=160)
    print("\n已保存图: experiment/experiment2_result.png")


if __name__ == "__main__":
    main()
