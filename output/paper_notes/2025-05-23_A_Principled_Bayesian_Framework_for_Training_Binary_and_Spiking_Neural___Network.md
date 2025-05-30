
# 📄 A Principled Bayesian Framework for Training Binary and Spiking Neural
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
