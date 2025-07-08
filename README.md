# 🧙‍♂️ **LIONS MAPPER AI**

*Automatic Navigation on Image Maps using K-Means Clustering*
**Version: Alpha — under active development**

![Python Database X-AI ORM](./assets/lions_mappers.png)

## 📌 Description

**LIONS MAPPER AI** is an **experimental Python tool** that uses **K-Means clustering** (from the [scikit-learn](https://scikit-learn.org/) framework) to trace navigation **paths and routes on image-based maps**, with segmentation based on **RGB color biometrics**.

This alpha version aims to explore how artificial intelligence can interpret static map images to generate logical pathfinding data by analyzing visual patterns through color detection.


## 🚀 Features

* 🧠 K-Means clustering for RGB-based color zone segmentation
* 🗺️ Automatic route generation from segmented image maps
* 📊 Uses the robust and familiar Scikit-Learn framework
* 🔬 Currently in **alpha**: experimental and intended for testing and research
* 🧪 Ideal for computer vision learning, AI-based mapping, and robotics simulations


## 🔧 Requirements

* Python 3.8+
* `scikit-learn`
* `opencv-python`
* `numpy`
* `matplotlib` *(optional, for visualization)*

Install dependencies:

```bash
pip install scikit-learn opencv-python numpy matplotlib
```

---

## 📂 Usage

```bash
python lions_mapper_ai.py path_to_image_map.png [R,G,B]
```

![TERMINAL STATION MAP](./assets/sample_maps.jpg)

This will:

1. Load and analyze the image
2. Apply K-Means clustering on pixel RGB values
3. Highlight and map potential routes

---

## 📸 Example (Coming Soon)

We'll soon include sample map images and visual route outputs.

---

## 📍 Roadmap

* [ ] Add GUI for input/output visualization
* [ ] Improve path accuracy through additional ML filters
* [ ] Expand support for GPS-style coordinate extraction
* [ ] Create dataset and benchmark performance

---

## 👤 Author

* **#Asytrick**
* GitHub: [github.com/@ssmool](https://github.com/ssmool)
* Email: [eusmool@gmail.com](mailto:eusmool@gmail.com)
* Repositorie: [github.com/ssmool/PYAISPINLINE](github.com/ssmool/PYAISPINLINE)
---

## ⚠️ Disclaimer

This is an **experimental prototype**. Use at your own discretion and risk. Contributions and feedback are welcome!
