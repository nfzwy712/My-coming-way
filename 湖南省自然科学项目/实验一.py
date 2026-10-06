import numpy as np

rng = np.random.default_rng(42)

# 两个高斯类：类0中心(-1.5,0)，类1中心(1.5,0)，标准差0.8（有重叠）
def make_task(shot, n_query=200):
    xs, ys, xq, yq = [], [], [], []
    for c, cx in enumerate([-1.5, 1.5]):
        s = rng.normal((cx, 0.0), 0.8, size=(shot, 2))
        q = rng.normal((cx, 0.0), 0.8, size=(n_query, 2))
        xs.append(s); ys.append(np.full(shot, c, int))
        xq.append(q); yq.append(np.full(n_query, c, int))
    return np.vstack(xs), np.concatenate(ys), np.vstack(xq), np.concatenate(yq)

def accuracy(proto, xq, yq):
    d = ((xq[:, None, :] - proto[None, :, :]) ** 2).sum(-1)
    return (d.argmin(1) == yq).mean()

for shot in [1, 3, 5, 20]:
    accs = []
    for _ in range(500):
        xs, ys, xq, yq = make_task(shot)
        # 每类原型 = 该类支持样本的平均值
        proto = np.stack([xs[ys == 0].mean(0), xs[ys == 1].mean(0)])
        accs.append(accuracy(proto, xq, yq))
    accs = np.array(accs)
    print(f"{shot:2d}-shot: 平均准确率 {accs.mean():.4f}，标准差 {accs.std():.4f}")