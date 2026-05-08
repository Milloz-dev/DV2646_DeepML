#Generated with AI Model Compare

import re
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


# Put all your model logs here.
# You can paste the full text for each model inside the triple quotes.
MODEL_LOGS = {
    "CustomCNN": """
CustomCNN | Epoch 1/100
Train Loss: 4.3017, Train Acc: 0.0388
Val Loss:   3.9366, Val Acc:   0.0750
----------------------------------------
CustomCNN | Epoch 2/100
Train Loss: 4.0203, Train Acc: 0.0693
Val Loss:   3.7159, Val Acc:   0.1180
----------------------------------------
CustomCNN | Epoch 3/100
Train Loss: 3.9021, Train Acc: 0.0839
Val Loss:   3.5249, Val Acc:   0.1478
----------------------------------------
CustomCNN | Epoch 4/100
Train Loss: 3.7870, Train Acc: 0.0964
Val Loss:   3.4082, Val Acc:   0.1624
----------------------------------------
CustomCNN | Epoch 5/100
Train Loss: 3.6865, Train Acc: 0.1106
Val Loss:   3.2620, Val Acc:   0.1930
----------------------------------------
CustomCNN | Epoch 6/100
Train Loss: 3.5941, Train Acc: 0.1245
Val Loss:   3.1834, Val Acc:   0.2002
----------------------------------------
CustomCNN | Epoch 7/100
Train Loss: 3.5115, Train Acc: 0.1358
Val Loss:   3.0260, Val Acc:   0.2282
----------------------------------------
CustomCNN | Epoch 8/100
Train Loss: 3.4379, Train Acc: 0.1504
Val Loss:   2.9131, Val Acc:   0.2508
----------------------------------------
CustomCNN | Epoch 9/100
Train Loss: 3.3568, Train Acc: 0.1637
Val Loss:   2.8112, Val Acc:   0.2830
----------------------------------------
CustomCNN | Epoch 10/100
Train Loss: 3.2900, Train Acc: 0.1760
Val Loss:   2.8059, Val Acc:   0.2736
----------------------------------------
CustomCNN | Epoch 11/100
Train Loss: 3.1912, Train Acc: 0.1946
Val Loss:   2.7262, Val Acc:   0.2960
----------------------------------------
CustomCNN | Epoch 12/100
Train Loss: 3.1116, Train Acc: 0.2119
Val Loss:   2.5997, Val Acc:   0.3246
----------------------------------------
CustomCNN | Epoch 13/100
Train Loss: 3.0383, Train Acc: 0.2278
Val Loss:   2.4523, Val Acc:   0.3520
----------------------------------------
CustomCNN | Epoch 14/100
Train Loss: 2.9462, Train Acc: 0.2467
Val Loss:   2.5308, Val Acc:   0.3384
----------------------------------------
CustomCNN | Epoch 15/100
Train Loss: 2.8671, Train Acc: 0.2601
Val Loss:   2.3838, Val Acc:   0.3662
----------------------------------------
CustomCNN | Epoch 16/100
Train Loss: 2.7899, Train Acc: 0.2792
Val Loss:   2.3179, Val Acc:   0.3796
----------------------------------------
CustomCNN | Epoch 17/100
Train Loss: 2.7256, Train Acc: 0.2937
Val Loss:   2.2030, Val Acc:   0.4100
----------------------------------------
CustomCNN | Epoch 18/100
Train Loss: 2.6690, Train Acc: 0.3079
Val Loss:   2.1894, Val Acc:   0.4132
----------------------------------------
CustomCNN | Epoch 19/100
Train Loss: 2.6037, Train Acc: 0.3200
Val Loss:   2.2092, Val Acc:   0.4122
----------------------------------------
CustomCNN | Epoch 20/100
Train Loss: 2.5566, Train Acc: 0.3347
Val Loss:   2.0954, Val Acc:   0.4258
----------------------------------------
CustomCNN | Epoch 21/100
Train Loss: 2.5014, Train Acc: 0.3448
Val Loss:   2.0539, Val Acc:   0.4478
----------------------------------------
CustomCNN | Epoch 22/100
Train Loss: 2.4416, Train Acc: 0.3581
Val Loss:   1.9908, Val Acc:   0.4576
----------------------------------------
CustomCNN | Epoch 23/100
Train Loss: 2.3996, Train Acc: 0.3656
Val Loss:   1.9920, Val Acc:   0.4686
----------------------------------------
CustomCNN | Epoch 24/100
Train Loss: 2.3568, Train Acc: 0.3738
Val Loss:   1.9331, Val Acc:   0.4792
----------------------------------------
CustomCNN | Epoch 25/100
Train Loss: 2.3268, Train Acc: 0.3832
Val Loss:   1.9238, Val Acc:   0.4784
----------------------------------------
CustomCNN | Epoch 26/100
Train Loss: 2.2967, Train Acc: 0.3930
Val Loss:   1.8641, Val Acc:   0.4932
----------------------------------------
CustomCNN | Epoch 27/100
Train Loss: 2.2536, Train Acc: 0.4013
Val Loss:   1.8426, Val Acc:   0.4990
----------------------------------------
CustomCNN | Epoch 28/100
Train Loss: 2.2193, Train Acc: 0.4059
Val Loss:   1.7960, Val Acc:   0.5098
----------------------------------------
CustomCNN | Epoch 29/100
Train Loss: 2.2014, Train Acc: 0.4115
Val Loss:   1.7968, Val Acc:   0.5058
----------------------------------------
CustomCNN | Epoch 30/100
Train Loss: 2.1696, Train Acc: 0.4233
Val Loss:   1.7704, Val Acc:   0.5162
----------------------------------------
CustomCNN | Epoch 31/100
Train Loss: 2.1429, Train Acc: 0.4262
Val Loss:   1.7389, Val Acc:   0.5202
----------------------------------------
CustomCNN | Epoch 32/100
Train Loss: 2.1201, Train Acc: 0.4335
Val Loss:   1.7535, Val Acc:   0.5158
----------------------------------------
CustomCNN | Epoch 33/100
Train Loss: 2.0918, Train Acc: 0.4360
Val Loss:   1.7626, Val Acc:   0.5136
----------------------------------------
CustomCNN | Epoch 34/100
Train Loss: 2.0709, Train Acc: 0.4418
Val Loss:   1.7240, Val Acc:   0.5242
----------------------------------------
CustomCNN | Epoch 35/100
Train Loss: 2.0544, Train Acc: 0.4464
Val Loss:   1.7711, Val Acc:   0.5104
----------------------------------------
CustomCNN | Epoch 36/100
Train Loss: 2.0312, Train Acc: 0.4512
Val Loss:   1.6953, Val Acc:   0.5224
----------------------------------------
CustomCNN | Epoch 37/100
Train Loss: 2.0159, Train Acc: 0.4553
Val Loss:   1.6793, Val Acc:   0.5392
----------------------------------------
CustomCNN | Epoch 38/100
Train Loss: 1.9908, Train Acc: 0.4627
Val Loss:   1.6407, Val Acc:   0.5438
----------------------------------------
CustomCNN | Epoch 39/100
Train Loss: 1.9682, Train Acc: 0.4669
Val Loss:   1.6418, Val Acc:   0.5544
----------------------------------------
CustomCNN | Epoch 40/100
Train Loss: 1.9543, Train Acc: 0.4692
Val Loss:   1.6568, Val Acc:   0.5444
----------------------------------------
CustomCNN | Epoch 41/100
Train Loss: 1.9369, Train Acc: 0.4754
Val Loss:   1.6690, Val Acc:   0.5458
----------------------------------------
CustomCNN | Epoch 42/100
Train Loss: 1.9199, Train Acc: 0.4796
Val Loss:   1.6820, Val Acc:   0.5416
----------------------------------------
CustomCNN | Epoch 43/100
Train Loss: 1.8407, Train Acc: 0.4963
Val Loss:   1.5640, Val Acc:   0.5712
----------------------------------------
CustomCNN | Epoch 44/100
Train Loss: 1.8156, Train Acc: 0.5034
Val Loss:   1.5738, Val Acc:   0.5642
----------------------------------------
CustomCNN | Epoch 45/100
Train Loss: 1.7900, Train Acc: 0.5097
Val Loss:   1.5577, Val Acc:   0.5700
----------------------------------------
CustomCNN | Epoch 46/100
Train Loss: 1.7731, Train Acc: 0.5142
Val Loss:   1.5156, Val Acc:   0.5804
----------------------------------------
CustomCNN | Epoch 47/100
Train Loss: 1.7765, Train Acc: 0.5099
Val Loss:   1.5305, Val Acc:   0.5706
----------------------------------------
CustomCNN | Epoch 48/100
Train Loss: 1.7541, Train Acc: 0.5161
Val Loss:   1.5222, Val Acc:   0.5818
----------------------------------------
CustomCNN | Epoch 49/100
Train Loss: 1.7554, Train Acc: 0.5146
Val Loss:   1.5138, Val Acc:   0.5870
----------------------------------------
CustomCNN | Epoch 50/100
Train Loss: 1.7370, Train Acc: 0.5199
Val Loss:   1.5136, Val Acc:   0.5806
----------------------------------------
CustomCNN | Epoch 51/100
Train Loss: 1.7366, Train Acc: 0.5223
Val Loss:   1.5074, Val Acc:   0.5852
----------------------------------------
CustomCNN | Epoch 52/100
Train Loss: 1.7311, Train Acc: 0.5207
Val Loss:   1.5130, Val Acc:   0.5824
----------------------------------------
CustomCNN | Epoch 53/100
Train Loss: 1.7120, Train Acc: 0.5278
Val Loss:   1.4871, Val Acc:   0.5900
----------------------------------------
CustomCNN | Epoch 54/100
Train Loss: 1.7079, Train Acc: 0.5255
Val Loss:   1.4646, Val Acc:   0.5982
----------------------------------------
CustomCNN | Epoch 55/100
Train Loss: 1.7012, Train Acc: 0.5308
Val Loss:   1.4799, Val Acc:   0.5946
----------------------------------------
CustomCNN | Epoch 56/100
Train Loss: 1.6931, Train Acc: 0.5306
Val Loss:   1.4973, Val Acc:   0.5904
----------------------------------------
CustomCNN | Epoch 57/100
Train Loss: 1.6884, Train Acc: 0.5316
Val Loss:   1.4779, Val Acc:   0.5930
----------------------------------------
CustomCNN | Epoch 58/100
Train Loss: 1.6842, Train Acc: 0.5336
Val Loss:   1.4732, Val Acc:   0.5926
----------------------------------------
CustomCNN | Epoch 59/100
Train Loss: 1.6350, Train Acc: 0.5467
Val Loss:   1.4367, Val Acc:   0.6022
----------------------------------------
CustomCNN | Epoch 60/100
Train Loss: 1.6175, Train Acc: 0.5479
Val Loss:   1.4385, Val Acc:   0.6008
----------------------------------------
CustomCNN | Epoch 61/100
Train Loss: 1.6150, Train Acc: 0.5508
Val Loss:   1.4392, Val Acc:   0.5966
----------------------------------------
CustomCNN | Epoch 62/100
Train Loss: 1.5972, Train Acc: 0.5569
Val Loss:   1.4367, Val Acc:   0.6008
----------------------------------------
CustomCNN | Epoch 63/100
Train Loss: 1.5991, Train Acc: 0.5517
Val Loss:   1.4352, Val Acc:   0.6038
----------------------------------------
CustomCNN | Epoch 64/100
Train Loss: 1.5868, Train Acc: 0.5581
Val Loss:   1.4449, Val Acc:   0.5962
----------------------------------------
CustomCNN | Epoch 65/100
Train Loss: 1.5819, Train Acc: 0.5583
Val Loss:   1.4192, Val Acc:   0.6054
----------------------------------------
CustomCNN | Epoch 66/100
Train Loss: 1.5798, Train Acc: 0.5602
Val Loss:   1.4092, Val Acc:   0.6072
----------------------------------------
CustomCNN | Epoch 67/100
Train Loss: 1.5735, Train Acc: 0.5581
Val Loss:   1.4198, Val Acc:   0.6054
----------------------------------------
CustomCNN | Epoch 68/100
Train Loss: 1.5726, Train Acc: 0.5599
Val Loss:   1.4127, Val Acc:   0.6074
----------------------------------------
CustomCNN | Epoch 69/100
Train Loss: 1.5690, Train Acc: 0.5607
Val Loss:   1.4140, Val Acc:   0.6074
----------------------------------------
CustomCNN | Epoch 70/100
Train Loss: 1.5587, Train Acc: 0.5630
Val Loss:   1.4022, Val Acc:   0.6158
----------------------------------------
CustomCNN | Epoch 71/100
Train Loss: 1.5461, Train Acc: 0.5657
Val Loss:   1.3973, Val Acc:   0.6114
----------------------------------------
CustomCNN | Epoch 72/100
Train Loss: 1.5612, Train Acc: 0.5624
Val Loss:   1.4050, Val Acc:   0.6112
----------------------------------------
CustomCNN | Epoch 73/100
Train Loss: 1.5441, Train Acc: 0.5667
Val Loss:   1.4008, Val Acc:   0.6130
----------------------------------------
CustomCNN | Epoch 74/100
Train Loss: 1.5448, Train Acc: 0.5683
Val Loss:   1.3915, Val Acc:   0.6100
----------------------------------------
CustomCNN | Epoch 75/100
Train Loss: 1.5325, Train Acc: 0.5678
Val Loss:   1.4007, Val Acc:   0.6110
----------------------------------------
CustomCNN | Epoch 76/100
Train Loss: 1.5413, Train Acc: 0.5690
Val Loss:   1.4082, Val Acc:   0.6072
----------------------------------------
CustomCNN | Epoch 77/100
Train Loss: 1.5333, Train Acc: 0.5691
Val Loss:   1.4029, Val Acc:   0.6172
----------------------------------------
CustomCNN | Epoch 78/100
Train Loss: 1.5215, Train Acc: 0.5704
Val Loss:   1.4032, Val Acc:   0.6148
----------------------------------------
CustomCNN | Epoch 79/100
Train Loss: 1.5009, Train Acc: 0.5777
Val Loss:   1.3760, Val Acc:   0.6206
----------------------------------------
CustomCNN | Epoch 80/100
Train Loss: 1.5013, Train Acc: 0.5784
Val Loss:   1.3815, Val Acc:   0.6178
----------------------------------------
CustomCNN | Epoch 81/100
Train Loss: 1.4951, Train Acc: 0.5789
Val Loss:   1.3718, Val Acc:   0.6236
----------------------------------------
CustomCNN | Epoch 82/100
Train Loss: 1.4868, Train Acc: 0.5814
Val Loss:   1.3738, Val Acc:   0.6176
----------------------------------------
CustomCNN | Epoch 83/100
Train Loss: 1.4876, Train Acc: 0.5806
Val Loss:   1.3769, Val Acc:   0.6194
----------------------------------------
CustomCNN | Epoch 84/100
Train Loss: 1.4825, Train Acc: 0.5790
Val Loss:   1.3736, Val Acc:   0.6216
----------------------------------------
CustomCNN | Epoch 85/100
Train Loss: 1.4806, Train Acc: 0.5800
Val Loss:   1.3710, Val Acc:   0.6198
----------------------------------------
CustomCNN | Epoch 86/100
Train Loss: 1.4810, Train Acc: 0.5808
Val Loss:   1.3642, Val Acc:   0.6218
----------------------------------------
CustomCNN | Epoch 87/100
Train Loss: 1.4822, Train Acc: 0.5837
Val Loss:   1.3621, Val Acc:   0.6202
----------------------------------------
CustomCNN | Epoch 88/100
Train Loss: 1.4663, Train Acc: 0.5882
Val Loss:   1.3707, Val Acc:   0.6196
----------------------------------------
CustomCNN | Epoch 89/100
Train Loss: 1.4623, Train Acc: 0.5860
Val Loss:   1.3676, Val Acc:   0.6168
----------------------------------------
Early stopping triggered.
""",

    "ResNet-50": """
ResNet50 | Epoch 1/12
Train Loss: 1.5158, Train Acc: 0.6176
Val Loss:   0.7050, Val Acc:   0.7866
----------------------------------------
ResNet50 | Epoch 2/12
Train Loss: 0.5832, Train Acc: 0.8242
Val Loss:   0.5958, Val Acc:   0.8190
----------------------------------------
ResNet50 | Epoch 3/12
Train Loss: 0.3832, Train Acc: 0.8836
Val Loss:   0.5764, Val Acc:   0.8266
----------------------------------------
ResNet50 | Epoch 4/12
Train Loss: 0.2764, Train Acc: 0.9136
Val Loss:   0.5977, Val Acc:   0.8250
----------------------------------------
ResNet50 | Epoch 5/12
Train Loss: 0.2067, Train Acc: 0.9353
Val Loss:   0.6011, Val Acc:   0.8328
----------------------------------------
ResNet50 | Epoch 6/12
Train Loss: 0.1629, Train Acc: 0.9480
Val Loss:   0.5840, Val Acc:   0.8372
----------------------------------------
ResNet50 | Epoch 7/12
Train Loss: 0.1361, Train Acc: 0.9583
Val Loss:   0.6300, Val Acc:   0.8332
----------------------------------------
ResNet50 | Epoch 8/12
Train Loss: 0.0665, Train Acc: 0.9808
Val Loss:   0.5816, Val Acc:   0.8470
----------------------------------------
ResNet50 | Epoch 9/12
Train Loss: 0.0403, Train Acc: 0.9892
Val Loss:   0.5921, Val Acc:   0.8478
----------------------------------------
ResNet50 | Epoch 10/12
Train Loss: 0.0362, Train Acc: 0.9903
Val Loss:   0.6345, Val Acc:   0.8462
----------------------------------------
ResNet50 | Epoch 11/12
Train Loss: 0.0351, Train Acc: 0.9905
Val Loss:   0.6645, Val Acc:   0.8418
----------------------------------------
ResNet50 | Epoch 12/12
Train Loss: 0.0222, Train Acc: 0.9946
Val Loss:   0.6335, Val Acc:   0.8526
----------------------------------------
""",

    "VGG-19": """
VGG19 | Epoch 1/12
Train Loss: 2.4433, Train Acc: 0.3623
Val Loss:   1.4528, Val Acc:   0.5850
----------------------------------------
VGG19 | Epoch 2/12
Train Loss: 1.7344, Train Acc: 0.5134
Val Loss:   1.2909, Val Acc:   0.6220
----------------------------------------
VGG19 | Epoch 3/12
Train Loss: 1.5385, Train Acc: 0.5613
Val Loss:   1.2348, Val Acc:   0.6394
----------------------------------------
VGG19 | Epoch 4/12
Train Loss: 1.4102, Train Acc: 0.5946
Val Loss:   1.1728, Val Acc:   0.6588
----------------------------------------
VGG19 | Epoch 5/12
Train Loss: 1.3059, Train Acc: 0.6195
Val Loss:   1.1741, Val Acc:   0.6588
----------------------------------------
VGG19 | Epoch 6/12
Train Loss: 1.2246, Train Acc: 0.6439
Val Loss:   1.1487, Val Acc:   0.6728
----------------------------------------
VGG19 | Epoch 7/12
Train Loss: 1.1575, Train Acc: 0.6635
Val Loss:   1.1286, Val Acc:   0.6784
----------------------------------------
VGG19 | Epoch 8/12
Train Loss: 1.0986, Train Acc: 0.6750
Val Loss:   1.1400, Val Acc:   0.6746
----------------------------------------
VGG19 | Epoch 9/12
Train Loss: 1.0422, Train Acc: 0.6923
Val Loss:   1.1394, Val Acc:   0.6824
----------------------------------------
VGG19 | Epoch 10/12
Train Loss: 0.9888, Train Acc: 0.7096
Val Loss:   1.1583, Val Acc:   0.6806
----------------------------------------
VGG19 | Epoch 11/12
Train Loss: 0.9559, Train Acc: 0.7134
Val Loss:   1.1486, Val Acc:   0.6860
----------------------------------------
VGG19 | Epoch 12/12
Train Loss: 0.7977, Train Acc: 0.7593
Val Loss:   1.1259, Val Acc:   0.6964
----------------------------------------
""",

    "DenseNet-121": """
DenseNet121 | Epoch 1/12
Train Loss: 1.9652, Train Acc: 0.5526
Val Loss:   0.9509, Val Acc:   0.7386
----------------------------------------
DenseNet121 | Epoch 2/12
Train Loss: 0.8046, Train Acc: 0.7764
Val Loss:   0.7242, Val Acc:   0.7864
----------------------------------------
DenseNet121 | Epoch 3/12
Train Loss: 0.5559, Train Acc: 0.8388
Val Loss:   0.6502, Val Acc:   0.8062
----------------------------------------
DenseNet121 | Epoch 4/12
Train Loss: 0.4105, Train Acc: 0.8791
Val Loss:   0.6378, Val Acc:   0.8096
----------------------------------------
DenseNet121 | Epoch 5/12
Train Loss: 0.3189, Train Acc: 0.9042
Val Loss:   0.6460, Val Acc:   0.8074
----------------------------------------
DenseNet121 | Epoch 6/12
Train Loss: 0.2517, Train Acc: 0.9250
Val Loss:   0.6323, Val Acc:   0.8170
----------------------------------------
DenseNet121 | Epoch 7/12
Train Loss: 0.2069, Train Acc: 0.9374
Val Loss:   0.6547, Val Acc:   0.8132
----------------------------------------
DenseNet121 | Epoch 8/12
Train Loss: 0.1723, Train Acc: 0.9496
Val Loss:   0.6645, Val Acc:   0.8150
----------------------------------------
DenseNet121 | Epoch 9/12
Train Loss: 0.1461, Train Acc: 0.9568
Val Loss:   0.6705, Val Acc:   0.8196
----------------------------------------
DenseNet121 | Epoch 10/12
Train Loss: 0.1214, Train Acc: 0.9644
Val Loss:   0.6733, Val Acc:   0.8176
----------------------------------------
DenseNet121 | Epoch 11/12
Train Loss: 0.0642, Train Acc: 0.9832
Val Loss:   0.6277, Val Acc:   0.8328
----------------------------------------
DenseNet121 | Epoch 12/12
Train Loss: 0.0406, Train Acc: 0.9903
Val Loss:   0.6503, Val Acc:   0.8326
----------------------------------------
""",

    "EfficientNet": """
EfficientNet_B0 | Epoch 1/12
Train Loss: 2.1891, Train Acc: 0.5037
Val Loss:   0.8817, Val Acc:   0.7490
----------------------------------------
EfficientNet_B0 | Epoch 2/12
Train Loss: 0.8521, Train Acc: 0.7555
Val Loss:   0.6485, Val Acc:   0.7978
----------------------------------------
EfficientNet_B0 | Epoch 3/12
Train Loss: 0.6196, Train Acc: 0.8146
Val Loss:   0.5636, Val Acc:   0.8268
----------------------------------------
EfficientNet_B0 | Epoch 4/12
Train Loss: 0.4847, Train Acc: 0.8509
Val Loss:   0.5257, Val Acc:   0.8366
----------------------------------------
EfficientNet_B0 | Epoch 5/12
Train Loss: 0.3946, Train Acc: 0.8776
Val Loss:   0.5244, Val Acc:   0.8400
----------------------------------------
EfficientNet_B0 | Epoch 6/12
Train Loss: 0.3220, Train Acc: 0.8988
Val Loss:   0.5149, Val Acc:   0.8438
----------------------------------------
EfficientNet_B0 | Epoch 7/12
Train Loss: 0.2744, Train Acc: 0.9142
Val Loss:   0.5323, Val Acc:   0.8448
----------------------------------------
EfficientNet_B0 | Epoch 8/12
Train Loss: 0.2298, Train Acc: 0.9277
Val Loss:   0.5257, Val Acc:   0.8462
----------------------------------------
EfficientNet_B0 | Epoch 9/12
Train Loss: 0.2004, Train Acc: 0.9386
Val Loss:   0.5490, Val Acc:   0.8480
----------------------------------------
EfficientNet_B0 | Epoch 10/12
Train Loss: 0.1729, Train Acc: 0.9474
Val Loss:   0.5371, Val Acc:   0.8530
----------------------------------------
EfficientNet_B0 | Epoch 11/12
Train Loss: 0.1302, Train Acc: 0.9617
Val Loss:   0.5242, Val Acc:   0.8552
----------------------------------------
EfficientNet_B0 | Epoch 12/12
Train Loss: 0.1109, Train Acc: 0.9671
Val Loss:   0.5345, Val Acc:   0.8556
----------------------------------------
"""
}


OUTPUT_DIR = Path("figures")
OUTPUT_DIR.mkdir(exist_ok=True)


def parse_log(model_name, log_text):
    """
    Parses logs of this style:

    CustomCNN | Epoch 1/100
    Train Loss: 4.2839, Train Acc: 0.0428
    Val Loss:   3.9116, Val Acc:   0.0782

    Optional supported time examples:
    Epoch Time: 42.3s
    Time: 42.3s
    Epoch time: 42.3 sec
    """

    epoch_pattern = re.compile(
        r"Epoch\s+(\d+)/(\d+).*?"
        r"Train Loss:\s*([\d.]+),\s*Train Acc:\s*([\d.]+).*?"
        r"Val Loss:\s*([\d.]+),\s*Val Acc:\s*([\d.]+)"
        r"(?:.*?(?:Epoch Time|Epoch time|Time):\s*([\d.]+)\s*(?:s|sec|seconds)?)?",
        re.DOTALL
    )

    rows = []

    for match in epoch_pattern.finditer(log_text):
        rows.append({
            "model": model_name,
            "epoch": int(match.group(1)),
            "max_epochs": int(match.group(2)),
            "train_loss": float(match.group(3)),
            "train_acc": float(match.group(4)),
            "val_loss": float(match.group(5)),
            "val_acc": float(match.group(6)),
            "epoch_time_sec": float(match.group(7)) if match.group(7) else None
        })

    return rows


def build_dataframe(model_logs):
    all_rows = []

    for model_name, log_text in model_logs.items():
        rows = parse_log(model_name, log_text)

        if not rows:
            print(f"Warning: no epochs found for {model_name}")

        all_rows.extend(rows)

    if not all_rows:
        raise ValueError("No training data found. Check your pasted logs.")

    return pd.DataFrame(all_rows)


def plot_metric(df, metric, ylabel, title, filename):
    plt.figure(figsize=(9, 5))

    for model_name, group in df.groupby("model"):
        group = group.sort_values("epoch")
        plt.plot(group["epoch"], group[metric], label=model_name)

    plt.xlabel("Epoch")
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / filename, dpi=300)
    plt.show()


def plot_epoch_time(df):
    if df["epoch_time_sec"].isna().all():
        print("No epoch times found in logs. Skipping epoch time plots.")
        return

    time_df = df.dropna(subset=["epoch_time_sec"])

    plt.figure(figsize=(9, 5))

    for model_name, group in time_df.groupby("model"):
        group = group.sort_values("epoch")
        plt.plot(group["epoch"], group["epoch_time_sec"], label=model_name)

    plt.xlabel("Epoch")
    plt.ylabel("Epoch time (seconds)")
    plt.title("Epoch Time Comparison")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "model_epoch_time_comparison.png", dpi=300)
    plt.show()

    summary = (
        time_df.groupby("model")["epoch_time_sec"]
        .agg(["mean", "min", "max", "sum"])
        .reset_index()
        .sort_values("mean")
    )

    print("\n===== EPOCH TIME SUMMARY =====")
    print(summary.to_string(index=False))


def print_summary(df):
    rows = []

    for model_name, group in df.groupby("model"):
        group = group.sort_values("epoch")

        final = group.iloc[-1]
        best_acc = group.loc[group["val_acc"].idxmax()]
        best_loss = group.loc[group["val_loss"].idxmin()]

        rows.append({
            "Model": model_name,
            "Epochs Completed": int(final["epoch"]),
            "Final Train Loss": final["train_loss"],
            "Final Train Acc": final["train_acc"],
            "Final Val Loss": final["val_loss"],
            "Final Val Acc": final["val_acc"],
            "Best Val Acc": best_acc["val_acc"],
            "Best Val Acc Epoch": int(best_acc["epoch"]),
            "Best Val Loss": best_loss["val_loss"],
            "Best Val Loss Epoch": int(best_loss["epoch"]),
        })

    summary_df = pd.DataFrame(rows)
    summary_df = summary_df.sort_values("Best Val Acc", ascending=False)

    print("\n===== MODEL SUMMARY =====")
    print(summary_df.to_string(index=False))

    summary_df.to_csv(OUTPUT_DIR / "model_training_summary.csv", index=False)
    print(f"\nSaved summary to: {OUTPUT_DIR / 'model_training_summary.csv'}")


def main():
    df = build_dataframe(MODEL_LOGS)

    df.to_csv(OUTPUT_DIR / "all_model_training_history.csv", index=False)
    print(f"Saved full history to: {OUTPUT_DIR / 'all_model_training_history.csv'}")

    print_summary(df)

    plot_metric(
        df,
        metric="train_loss",
        ylabel="Training Loss",
        title="Training Loss Comparison",
        filename="model_train_loss_comparison.png"
    )

    plot_metric(
        df,
        metric="val_loss",
        ylabel="Validation Loss",
        title="Validation Loss Comparison",
        filename="model_val_loss_comparison.png"
    )

    plot_metric(
        df,
        metric="train_acc",
        ylabel="Training Accuracy",
        title="Training Accuracy Comparison",
        filename="model_train_acc_comparison.png"
    )

    plot_metric(
        df,
        metric="val_acc",
        ylabel="Validation Accuracy",
        title="Validation Accuracy Comparison",
        filename="model_val_acc_comparison.png"
    )

    plot_epoch_time(df)


if __name__ == "__main__":
    main()