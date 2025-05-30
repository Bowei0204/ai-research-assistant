
# 📄 Leveraging KANs for Expedient Training of Multichannel MLPs via
  Preconditioning and Geometric Refinement

- **作者**：Jonas A. Actor, Graham Harper, Ben Southworth, Eric C. Cyr
- **發表日期**：2025-05-23
- **arXiv ID**：2505.18131

---

## 🧠 Abstract（英文）

Multilayer perceptrons (MLPs) are a workhorse machine learning architecture, used in a variety of modern deep learning frameworks. However, recently Kolmogorov-Arnold Networks (KANs) have become increasingly popular due to their success on a range of problems, particularly for scientific machine learning tasks. In this paper, we exploit the relationship between KANs and multichannel MLPs to gain structural insight into how to train MLPs faster. We demonstrate the KAN basis (1) provides geometric localized support, and (2) acts as a preconditioned descent in the ReLU basis, overall resulting in expedited training and improved accuracy. Our results show the equivalence between free-knot spline KAN architectures, and a class of MLPs that are refined geometrically along the channel dimension of each weight tensor. We exploit this structural equivalence to define a hierarchical refinement scheme that dramatically accelerates training of the multi-channel MLP architecture. We show further accuracy improvements can be had by allowing the $1$D locations of the spline knots to be trained simultaneously with the weights. These advances are demonstrated on a range of benchmark examples for regression and scientific machine learning.

## 🌏 Abstract（繁體翻譯）

多層感知器（MLP）是一種主力機器學習體系結構，用於各種現代深度學習框架。但是，最近，Kolmogorov-Arnold Networks（KANS）由於在一系列問題上的成功而變得越來越受歡迎，特別是對於科學機器學習任務。在本文中，我們利用KANS和多通道MLP之間的關係，以獲取如何更快地訓練MLP的結構洞察力。我們證明了KAN基礎（1）提供了幾何局部支持，並且（2）在RELU基礎上充當預處理的下降，總體上導致了加快訓練並提高準確性。我們的結果表明，自由結樣條kan體系結構與一類MLP之間的等效性，這些MLP沿每個重量張量的通道尺寸進行了幾何形式。我們利用這種結構對等度來定義層次結構的精煉方案，該方案大大加速了對多渠道MLP體系結構的訓練。我們可以通過允許$ 1 $ d的位置與重量同時訓練，我們可以顯示進一步的準確性提高。這些進步在用於回歸和科學機器學習的一系列基準示例中得到了證明。

---

## ✅ 優點
- **加速 MLP 訓練:**  論文提出了一種基於 Kolmogorov-Arnold Networks (KANs) 的層次化細化方案，顯著加快了多通道 MLP 架構的訓練速度。
- **提升準確性:**  通過利用 KAN 基礎的幾何局部支撐特性和預條件下降特性，以及允許一維樣條節點位置與權重同時訓練，提升了 MLP 模型的準確性。
- **提供結構性洞察:**  論文揭示了 KANs 與多通道 MLP 之間的結構等價性，提供了關於如何更快訓練 MLP 的結構性見解。
- **適用範圍廣泛:**  論文在迴歸和科學機器學習的基準示例中證明了其方法的有效性。


## ⚠️ 缺點 / 限制
- **僅限於特定類型的 MLP:**  論文的成果可能僅適用於與自由節點樣條 KAN 架構等價的特定類型的多通道 MLP，其適用性可能存在限制。
- **計算成本的潛在增加:**  雖然加速了訓練，但同時訓練節點位置和權重可能會增加單次迭代的計算成本，需要進一步評估其整體效率。
- **可擴展性:**  論文中提出的方法在更大規模的數據集或更複雜的任務上的可擴展性尚不清楚，需要更多實驗驗證。
- **缺乏對 KANs 本身限制的討論:**  論文主要關注 KANs 如何改善 MLP 訓練，但沒有深入探討 KANs 本身可能存在的限制，例如對高維數據的處理能力。

---
（由 AI 技術研究助手自動產生）
