# 🧠 Python Neural Network

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/status-active-success?style=for-the-badge)

> **From Scratch to Advanced:** A clear and educational Neural Network implementation built with pure Python and NumPy power, without heavy libraries.

This project is designed to understand the core concepts of Deep Learning such as **Forward Propagation** and **Backpropagation**. It solves the classic **XOR problem** as a demonstration.

---

## 🚀 Features

- **Pure Python & NumPy:** See the core logic without "black box" libraries like TensorFlow or PyTorch.
- **Flexible Structure:** Easily adjust layer sizes (input, hidden, output) with the `NeuralNetwork` class.
- **Backpropagation:** Examine how weights are updated and how the model "learns".
- **XOR Solution:** Test the ability to solve non-linear problems.

---

## 📂 File Structure

```tree
python-neural-network/
├── 📄 main.py          # Example Usage (XOR Problem and Test)
├── 🧠 network.py       # Core Neural Network Class (Logic)
├── 📦 requirements.txt # Project Dependencies (NumPy)
└── 📝 README.md        # Project Documentation
```

---

## 🛠️ Installation

Clone the project to your local machine and install the required dependencies:

```bash
# Clone the repository
git clone git@github.com:shtwon/python-neural-network.git

# Enter the project directory
cd python-neural-network

# Install dependencies
pip install -r requirements.txt
```

---

## 💻 Usage

Run the `main.py` file to train and test the neural network:

```bash
python main.py
```

### Expected Output

After training completes, you will see the loss value decrease and predictions approach the XOR table:

```text
Training...
Predictions after training:
Input: [0 0] - Prediction: 0.0xxx - Expected: 0
Input: [0 1] - Prediction: 0.9xxx - Expected: 1
Input: [1 0] - Prediction: 0.9xxx - Expected: 1
Input: [1 1] - Prediction: 0.0xxx - Expected: 0
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) license.
