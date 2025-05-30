# 技術比較表

## A Principled Bayesian Framework for Training Binary and Spiking Neural
  Networks

- **作者**：James A. Walker, Moein Khajehnejad, Adeel Razi
- **發表日期**：2025-05-23
- **arXiv ID**：2505.17962

---

## 🧠 Abstract（英文）

We propose a Bayesian framework for training binary and spiking neural networks that achieves state-of-the-art performance without normalisation layers. Unlike commonly used surrogate gradient methods -- often heuristic and sensitive to hyperparameter choices -- our approach is grounded in a probabilistic model of noisy binary networks, enabling fully end-to-end gradient-based optimisation. We introduce importance-weighted straight-through (IW-ST) estimators, a unified class generalising straight-through and relaxation-based estimators. We characterise the bias-variance trade-off in this family and derive a bias-minimising objective implemented via an auxiliary loss. Building on this, we introduce Spiking Bayesian Neural Networks (SBNNs), a variational inference framework that uses posterior noise to train Binary and Spiking Neural Networks with IW-ST. This Bayesian approach minimises gradient bias, regularises parameters, and introduces dropout-like noise. By linking low-bias conditions, vanishing gradients, and the KL term, we enable training of deep residual networks without normalisation. Experiments on CIFAR-10, DVS Gesture, and SHD show our method matches or exceeds existing approaches without normalisation or hand-tuned gradients.

## 🌏 Abstract（繁體翻譯）

我們提出了一個貝葉斯框架，用於訓練二進制和尖峰神經網絡，該框架在沒有標準化層的情況下實現最先進的性能。與常用的替代梯度方法（通常是啟發式且對超參數選擇敏感）不同，我們的方法基於嘈雜的二進製網絡的概率模型，從而實現了完全基於端到端梯度的優化。我們介紹了重要性加權的直發（IW-ST）估計器，這是一種統一的類別的概括性直通和基於放鬆的估計器。我們表徵了這個家庭中的偏見變化權衡權衡，並通過輔助損失得出了實施的偏見最小目標。在此基礎上，我們引入了尖峰貝葉斯神經網絡（SBNNS），這是一個變異推理框架，使用後噪聲訓練與IW-ST訓練二進制和尖峰神經網絡。這種貝葉斯方法可以最大程度地減少梯度偏差，規範參數並引入類似輟學的噪聲。通過連接低偏置條件，消失的梯度和KL期限，我們可以培訓深層殘留網絡而無需歸一化。在CIFAR-10，DVS手勢和SHD上進行的實驗顯示了我們的方法匹配或超過了沒有標準化或手動梯度的現有方法。

---

## ✅ 優點
- **實現最先進的性能，無需歸一化層:**  這是該方法的主要優勢，克服了許多深度學習模型對歸一化層的依賴。
- **基於概率模型，而非啟發式方法:** 與常用的替代梯度方法不同，該方法基於對帶噪聲二元網絡的概率模型，使得端到端梯度優化成為可能，更具理論基礎。
- **引入統一的IW-ST估計器:**  此估計器泛化了直通估計器和基於鬆弛的估計器，提供了一個更通用的框架。
- **特徵化偏差-方差權衡並最小化偏差:**  通過分析偏差-方差權衡並引入輔助損失函數，減少了梯度估計的偏差。
- **成功應用於二元和脈衝神經網絡 (SBNNs):**  該方法不局限於二元網絡，也成功應用於更複雜的脈衝神經網絡。
- **貝葉斯方法帶來正則化和dropout-like noise:**  貝葉斯方法內在的正則化特性提高了模型的泛化能力，並且引入了類似dropout的噪聲，有助於防止過擬合。
- **在多個數據集上取得了優秀的結果:** 在CIFAR-10, DVS Gesture和SHD數據集上都取得了與現有方法相當或更好的結果。


## ⚠️ 缺點 / 限制
- **計算複雜度:**  貝葉斯方法通常比傳統方法計算複雜度更高，這可能會限制其應用於大型數據集或更複雜的網絡結構。
- **超參數選擇:**  雖然文中提到避免了替代梯度方法中對超參數的敏感性，但該方法本身可能仍然存在需要調整的超參數，只是數量可能較少。
- **可擴展性:**  雖然在文中提到的數據集上取得了成功，但該方法的可擴展性在更大規模的數據集和更複雜的任務上仍需驗證。
- **對先驗分佈的選擇:** 貝葉斯方法的性能高度依賴於先驗分佈的選擇，不恰當的先驗分佈可能會影響模型的性能。
- **缺乏對IW-ST估計器偏差最小化方法的深入解釋:** 摘要中只簡要提到了偏差最小化，缺乏更詳細的理論分析和解釋。

---
（由 AI 技術研究助手自動產生）
- **作者**：James A. Walker, Moein Khajehnejad, Adeel Razi
- **方法摘要**：We propose a Bayesian framework for training binary and spiking neural networks that achieves state-of-the-art performance without normalisation layers. Unlike commonly used surrogate gradient methods -- often heuristic and sensitive to hyperparameter choices -- our approach is grounded in a probabilistic model of noisy binary networks, enabling fully end-to-end gradient-based optimisation. We introduce importance-weighted straight-through (IW-ST) estimators, a unified class generalising straight-through and relaxation-based estimators. We characterise the bias-variance trade-off in this family and derive a bias-minimising objective implemented via an auxiliary loss. Building on this, we introduce Spiking Bayesian Neural Networks (SBNNs), a variational inference framework that uses posterior noise to train Binary and Spiking Neural Networks with IW-ST. This Bayesian approach minimises gradient bias, regularises parameters, and introduces dropout-like noise. By linking low-bias conditions, vanishing gradients, and the KL term, we enable training of deep residual networks without normalisation. Experiments on CIFAR-10, DVS Gesture, and SHD show our method matches or exceeds existing approaches without normalisation or hand-tuned gradients.
- **優點與限制**：

## Leveraging KANs for Expedient Training of Multichannel MLPs via
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
- **作者**：Jonas A. Actor, Graham Harper, Ben Southworth, Eric C. Cyr
- **方法摘要**：Multilayer perceptrons (MLPs) are a workhorse machine learning architecture, used in a variety of modern deep learning frameworks. However, recently Kolmogorov-Arnold Networks (KANs) have become increasingly popular due to their success on a range of problems, particularly for scientific machine learning tasks. In this paper, we exploit the relationship between KANs and multichannel MLPs to gain structural insight into how to train MLPs faster. We demonstrate the KAN basis (1) provides geometric localized support, and (2) acts as a preconditioned descent in the ReLU basis, overall resulting in expedited training and improved accuracy. Our results show the equivalence between free-knot spline KAN architectures, and a class of MLPs that are refined geometrically along the channel dimension of each weight tensor. We exploit this structural equivalence to define a hierarchical refinement scheme that dramatically accelerates training of the multi-channel MLP architecture. We show further accuracy improvements can be had by allowing the $1$D locations of the spline knots to be trained simultaneously with the weights. These advances are demonstrated on a range of benchmark examples for regression and scientific machine learning.
- **優點與限制**：

